# Generated by Django 2.0.2 on 2018-04-20 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='kpp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
