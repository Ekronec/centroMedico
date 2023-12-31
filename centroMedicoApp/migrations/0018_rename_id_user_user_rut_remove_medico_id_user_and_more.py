# Generated by Django 4.2.6 on 2023-10-30 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('centroMedicoApp', '0017_alter_medico_id_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id_user',
            new_name='rut',
        ),
        migrations.RemoveField(
            model_name='medico',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='secretaria',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password_user',
        ),
        migrations.AddField(
            model_name='medico',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='centroMedicoApp.user'),
        ),
        migrations.AddField(
            model_name='secretaria',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='centroMedicoApp.user'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_name='custom_users', to='auth.group'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_name='custom_users', to='auth.permission'),
        ),
    ]
