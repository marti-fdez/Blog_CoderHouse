# Generated by Django 4.1 on 2022-09-20 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0004_alter_articulo_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='profesion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BlogApp.profesion'),
        ),
    ]