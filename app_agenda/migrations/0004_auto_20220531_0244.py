# Generated by Django 2.2.28 on 2022-05-31 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_agenda', '0003_remove_contatos_id_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatos',
            name='id',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]