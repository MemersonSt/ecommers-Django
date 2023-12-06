from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

# Create your models here.
class MeasureUnit(BaseModel): # Modelo para medidas como libras(supongo)
    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medidas'

    def __str__(self):
        return self.description

# Modelo para las categorias
class CategoryProduct(BaseModel):
    description = models.CharField('Descripción', max_length=50, unique=True, null=False, blank=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de medida')

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'CategoryProduct'
        verbose_name_plural = 'CategoryProducts'

    def __str__(self):
        return self.description


class Indicador(BaseModel):
    descount_value = models.PositiveSmallIntegerField(default = 0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de oferta')
    historical = HistoricalRecords()


    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Indicador'
        verbose_name_plural = 'Indicadors'

    def __str__(self):
        return f'Ofertta de la categoria {self.category_product} : {self.descount_value}%'


class Product(BaseModel):
    name = models.CharField('Nombre del producto',max_length=100, unique=True, blank=False, null=False)
    description = models.TextField('Description de Producto', blank=False, null=False)
    image = models.ImageField('Imagen del producto',upload_to='products/', blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name



