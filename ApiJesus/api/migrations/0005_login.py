# Generated by Django 4.2.5 on 2023-10-02 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alumno_has_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('Id_login', models.IntegerField(db_column='Id_login', primary_key=True, serialize=False)),
                ('nombre_us', models.CharField(db_column='nombre_us', max_length=100)),
                ('apellidos_us', models.CharField(db_column='apellidos_us', max_length=100)),
                ('correo_us', models.CharField(db_column='correo_us', max_length=100)),
                ('contraseña', models.CharField(db_column='contraseña_us', max_length=100)),
                ('rep_contra', models.CharField(db_column='rep_contra', max_length=100)),
            ],
        ),
    ]
