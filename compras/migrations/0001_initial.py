# Generated by Django 3.1.3 on 2024-06-14 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.TextField()),
                ('Descripcion', models.TextField()),
                ('Stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('total', models.FloatField()),
                ('id_ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.ingrediente')),
            ],
        ),
    ]