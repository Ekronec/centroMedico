# Generated by Django 4.2.6 on 2023-11-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centroMedicoApp', '0021_remove_usercentro_rut_usercentro_content_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiasLaborables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_dia', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='medico',
            name='hora_fin_trabajo',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='medico',
            name='hora_inicio_trabajo',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='medico',
            name='dias_laborables',
            field=models.ManyToManyField(null=True, to='centroMedicoApp.diaslaborables'),
        ),
    ]