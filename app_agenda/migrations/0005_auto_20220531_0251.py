# Generated by Django 2.2.28 on 2022-05-31 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_agenda', '0004_auto_20220531_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatos',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]