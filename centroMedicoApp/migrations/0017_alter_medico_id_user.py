# Generated by Django 4.2.6 on 2023-10-26 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centroMedicoApp', '0016_alter_user_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='id_user',
            field=models.ForeignKey(default=models.PositiveIntegerField(primary_key=True, serialize=False), on_delete=django.db.models.deletion.CASCADE, to='centroMedicoApp.user'),
        ),
    ]
