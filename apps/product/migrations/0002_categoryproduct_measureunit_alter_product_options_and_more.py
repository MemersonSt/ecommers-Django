# Generated by Django 4.2.7 on 2023-12-06 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'CategoryProduct',
                'verbose_name_plural': 'CategoryProducts',
            },
        ),
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Unidad de Medida',
                'verbose_name_plural': 'Unidades de Medidas',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.AddField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='product',
            name='delete_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de eliminación'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen del producto'),
        ),
        migrations.AddField(
            model_name='product',
            name='modified_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AddField(
            model_name='product',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Description de Producto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre del producto'),
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('descount_value', models.PositiveSmallIntegerField(default=0)),
                ('category_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.categoryproduct', verbose_name='Indicador de oferta')),
            ],
            options={
                'verbose_name': 'Indicador',
                'verbose_name_plural': 'Indicadors',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminación')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Nombre del producto')),
                ('description', models.TextField(verbose_name='Description de Producto')),
                ('image', models.TextField(blank=True, max_length=100, null=True, verbose_name='Imagen del producto')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Product',
                'verbose_name_plural': 'historical Products',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMeasureUnit',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminación')),
                ('description', models.CharField(db_index=True, max_length=50, verbose_name='Descripción')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Unidad de Medida',
                'verbose_name_plural': 'historical Unidades de Medidas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalIndicador',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificación')),
                ('delete_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminación')),
                ('descount_value', models.PositiveSmallIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category_product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='product.categoryproduct', verbose_name='Indicador de oferta')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Indicador',
                'verbose_name_plural': 'historical Indicadors',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='categoryproduct',
            name='measure_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.measureunit', verbose_name='Unidad de medida'),
        ),
    ]
