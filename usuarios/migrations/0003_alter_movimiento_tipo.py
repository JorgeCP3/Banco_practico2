# Generated by Django 5.2 on 2025-05-03 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_rename_movimientos_movimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='tipo',
            field=models.CharField(choices=[('ingreso', 'Ingreso'), ('egreso', 'Egreso')], max_length=10),
        ),
    ]
