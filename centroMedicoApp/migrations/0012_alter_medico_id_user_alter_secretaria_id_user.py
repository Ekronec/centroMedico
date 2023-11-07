# Generated by Django 4.2.6 on 2023-10-26 16:53

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('centroMedicoApp', '0011_rename_email_user_user_id_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='id_user',
            field=models.ForeignKey(default=django.db.models.fields.Field.value_from_object, on_delete=django.db.models.deletion.CASCADE, to='centroMedicoApp.user'),
        ),
        migrations.AlterField(
            model_name='secretaria',
            name='id_user',
            field=models.ForeignKey(default=django.db.models.fields.Field.value_from_object, on_delete=django.db.models.deletion.CASCADE, to='centroMedicoApp.user'),
        ),
    ]