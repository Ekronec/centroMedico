# Generated by Django 4.2.6 on 2023-10-26 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centroMedicoApp', '0013_alter_medico_id_user_alter_secretaria_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='id_user',
            field=models.ForeignKey(default=models.PositiveIntegerField(primary_key=True, serialize=False), on_delete=django.db.models.deletion.CASCADE, to='centroMedicoApp.user'),
        ),
        migrations.AlterField(
            model_name='secretaria',
            name='id_user',
            field=models.ForeignKey(default=models.PositiveIntegerField(primary_key=True, serialize=False), on_delete=django.db.models.deletion.CASCADE, to='centroMedicoApp.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_user',
            field=models.PositiveIntegerField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
