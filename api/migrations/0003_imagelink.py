# Generated by Django 3.2.6 on 2022-02-04 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_marketplaces_marketplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=500)),
            ],
        ),
    ]