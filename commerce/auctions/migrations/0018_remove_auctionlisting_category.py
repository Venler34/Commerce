# Generated by Django 4.1.5 on 2023-08-01 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_category_alter_auctionlisting_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='category',
        ),
    ]
