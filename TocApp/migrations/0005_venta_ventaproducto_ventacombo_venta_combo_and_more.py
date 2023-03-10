# Generated by Django 4.1 on 2022-12-21 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TocApp', '0004_trabajador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('anular', models.BooleanField(default=False)),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='VentaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TocApp.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TocApp.venta')),
            ],
        ),
        migrations.CreateModel(
            name='VentaCombo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TocApp.combo')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TocApp.venta')),
            ],
        ),
        migrations.AddField(
            model_name='venta',
            name='combo',
            field=models.ManyToManyField(through='TocApp.VentaCombo', to='TocApp.combo'),
        ),
        migrations.AddField(
            model_name='venta',
            name='producto',
            field=models.ManyToManyField(through='TocApp.VentaProducto', to='TocApp.producto'),
        ),
        migrations.AddField(
            model_name='venta',
            name='trabajador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TocApp.trabajador'),
        ),
    ]
