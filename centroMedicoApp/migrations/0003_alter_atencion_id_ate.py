# Generated by Django 4.2.1 on 2023-10-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centroMedicoApp', '0002_alter_atencion_hora_ate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencion',
            name='id_ate',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]