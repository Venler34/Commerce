# Generated by Django 4.1.5 on 2023-07-23 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_auctionlisting_user_auctions_user_bids'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='Category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='ImageURL',
            field=models.CharField(max_length=100, null=True),
        ),
    ]