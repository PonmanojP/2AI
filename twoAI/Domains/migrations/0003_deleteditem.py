# Generated by Django 4.2.1 on 2024-02-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Domains', '0002_rename_link_bigdata_link_1_rename_link_cloud_link_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
            ],
        ),
    ]
