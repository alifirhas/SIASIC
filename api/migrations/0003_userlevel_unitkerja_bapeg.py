# Generated by Django 4.0.1 on 2022-02-05 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_rename_jatahcuti_jeniscuti_formcuti_filepersyaratan'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(max_length=18, null=True)),
                ('Level', models.CharField(choices=[('1', 'Admin'), ('2', 'Atasan'), ('3', 'Pejabat'), ('4', 'Bapeg')], max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UnitKerja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_unit_kerja_id', models.IntegerField()),
                ('atasan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bapeg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_kerja_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.unitkerja')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
