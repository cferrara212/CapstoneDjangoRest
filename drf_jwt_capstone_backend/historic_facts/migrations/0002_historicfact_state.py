# Generated by Django 3.2.8 on 2021-12-02 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historic_facts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicfact',
            name='state',
            field=models.CharField(default='', max_length=50),
        ),
    ]