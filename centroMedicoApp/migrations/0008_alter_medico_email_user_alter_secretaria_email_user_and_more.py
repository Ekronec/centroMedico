# Generated by Django 4.2.6 on 2023-10-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centroMedicoApp', '0007_alter_especialidad_nom_esp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='email_user',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='secretaria',
            name='email_user',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_user',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
