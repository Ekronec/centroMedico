# Generated by Django 4.2.6 on 2023-10-26 16:54

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('centroMedicoApp', '0012_alter_medico_id_user_alter_secretaria_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='id_user',
            field=models.ForeignKey(default=django.db.models.fields.IntegerField.get_db_prep_value, on_delete=django.db.models.deletion.CASCADE, to='centroMedicoApp.user'),
        ),
        migrations.AlterField(
            model_name='secretaria',
            name='id_user',
            field=models.ForeignKey(default=django.db.models.fields.IntegerField.get_db_prep_value, on_delete=django.db.models.deletion.CASCADE, to='centroMedicoApp.user'),
        ),
    ]