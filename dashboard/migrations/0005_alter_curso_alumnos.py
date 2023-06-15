# Generated by Django 3.2 on 2023-06-01 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20230531_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='alumnos',
            field=models.ManyToManyField(limit_choices_to={'ciclo': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.ciclo')}, to='dashboard.Alumno'),
        ),
    ]