# Generated by Django 4.2.5 on 2023-10-03 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_registrarform_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrarform',
            name='Id_login',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
