# Generated by Django 4.1.5 on 2023-07-25 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_rename_bids_auctionlisting_largestbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='DateCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
