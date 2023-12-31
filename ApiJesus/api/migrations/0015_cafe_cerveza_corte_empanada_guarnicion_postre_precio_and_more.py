# Generated by Django 4.2.5 on 2023-10-18 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_registrarform_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('Id_cafe', models.AutoField(primary_key=True, serialize=False)),
                ('Americano', models.CharField(db_column='Americano', max_length=100)),
                ('Capuchino', models.CharField(db_column='Capuchino', max_length=100)),
                ('Expreso', models.CharField(db_column='Expreso', max_length=100)),
                ('Nomegustaelcáfe', models.CharField(db_column='No me gusta el cáfe', max_length=100)),
            ],
            options={
                'db_table': 'Cafe',
            },
        ),
        migrations.CreateModel(
            name='Cerveza',
            fields=[
                ('Id_cerveza', models.AutoField(primary_key=True, serialize=False)),
                ('Indio', models.CharField(db_column='Indio', max_length=100)),
                ('Tecate', models.CharField(db_column='Tecate', max_length=100)),
                ('Heineken', models.CharField(db_column='Heineken', max_length=100)),
                ('Notomo', models.CharField(db_column='No tomo', max_length=100)),
            ],
            options={
                'db_table': 'Cerveza',
            },
        ),
        migrations.CreateModel(
            name='Corte',
            fields=[
                ('Id_corte', models.AutoField(primary_key=True, serialize=False)),
                ('Arrachera', models.CharField(db_column='Arrachera', max_length=100)),
                ('Ribeye', models.CharField(db_column='Ribeye', max_length=100)),
                ('Churrasco', models.CharField(db_column='Churrasco', max_length=100)),
                ('Asadodetira', models.CharField(db_column='Asado de tira', max_length=100)),
            ],
            options={
                'db_table': 'Corte',
            },
        ),
        migrations.CreateModel(
            name='Empanada',
            fields=[
                ('Id_empanada', models.AutoField(primary_key=True, serialize=False)),
                ('chistorra', models.CharField(db_column='chistorra', max_length=100)),
                ('queso', models.CharField(db_column='queso', max_length=100)),
                ('eloteconqueso', models.CharField(db_column='elote con queso', max_length=100)),
                ('espinacaconqueso', models.CharField(db_column='espinaca con queso', max_length=100)),
            ],
            options={
                'db_table': 'Empanada',
            },
        ),
        migrations.CreateModel(
            name='Guarnicion',
            fields=[
                ('Id_guarnicion', models.AutoField(primary_key=True, serialize=False)),
                ('Chinchulines', models.CharField(db_column='Chinchulines', max_length=100)),
                ('Mollejas', models.CharField(db_column='Mollejas', max_length=100)),
                ('Chistorra', models.CharField(db_column='Chistorra', max_length=100)),
                ('Chorizoargentino', models.CharField(db_column='Chorizo argentino', max_length=100)),
            ],
            options={
                'db_table': 'Guarnicion',
            },
        ),
        migrations.CreateModel(
            name='Postre',
            fields=[
                ('Id_postre', models.AutoField(primary_key=True, serialize=False)),
                ('Strudeldemanzana', models.CharField(db_column='Strudel de manzana', max_length=100)),
                ('Pastelitodechocolate', models.CharField(db_column='Pastelito de chocolate', max_length=100)),
                ('Duraznoconcremas', models.CharField(db_column='Durazno con cremas', max_length=100)),
                ('Alfajor', models.CharField(db_column='Alfajor', max_length=100)),
            ],
            options={
                'db_table': 'Postre',
            },
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('Id_precio', models.AutoField(primary_key=True, serialize=False)),
                ('precio250', models.CharField(db_column='precio250', max_length=100)),
                ('precio300', models.CharField(db_column='precio300', max_length=100)),
                ('precio350', models.CharField(db_column='precio350', max_length=100)),
                ('precio400', models.CharField(db_column='precio400', max_length=100)),
            ],
            options={
                'db_table': 'Precio',
            },
        ),
        migrations.CreateModel(
            name='Refresco',
            fields=[
                ('Id_refresco', models.AutoField(primary_key=True, serialize=False)),
                ('Pepsi', models.CharField(db_column='Pepsi', max_length=100)),
                ('Mirinda', models.CharField(db_column='Mirinda', max_length=100)),
                ('Manzanita', models.CharField(db_column='Manzanita', max_length=100)),
                ('sevenup', models.CharField(db_column='7up', max_length=100)),
            ],
            options={
                'db_table': 'Refresco',
            },
        ),
        migrations.CreateModel(
            name='SalsaPasta',
            fields=[
                ('Id_salsapasta', models.AutoField(primary_key=True, serialize=False)),
                ('salsaboloñesa', models.CharField(db_column='salsa boloñesa', max_length=100)),
                ('Salsapesto', models.CharField(db_column='Salsa pesto', max_length=100)),
                ('Salsaburro', models.CharField(db_column='Salsa burro', max_length=100)),
                ('Salsaalfredo', models.CharField(db_column='Salsa alfredo', max_length=100)),
            ],
            options={
                'db_table': 'Salsa Pasta',
            },
        ),
    ]
