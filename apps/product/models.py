from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

# Create your models here.
class MeasureUnit(BaseModel):
    """Model definition for MeasureUnit."""

    # TODO: Define fields here
    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for MeasureUnit."""
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medidas'

    def __str__(self):
        """Unicode representation of MeasureUnit."""
        return self.description


# Modelo para las categorias
class CategoryProduct(BaseModel):
    """Model definition for CategoryProduct."""
    # TODO: Define fields here
    description = models.CharField('Descripcion', max_length=50, unique=True, null=False, blank=False)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for CategoryProduct."""

        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'

    def __str__(self):
        """Unicode representation of CategoryProduct."""
        return self.description


class Indicador(BaseModel):
    descount_value = models.PositiveSmallIntegerField(default=0)
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
        verbose_name_plural = 'Indicadores'  # Cambiado a 'Indicadores'

    def __str__(self):
        return f'Oferta de la categoría {self.category_product} : {self.descount_value}%'

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



