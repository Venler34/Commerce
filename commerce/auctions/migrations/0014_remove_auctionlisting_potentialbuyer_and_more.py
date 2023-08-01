# Generated by Django 4.1.5 on 2023-08-01 17:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='potentialBuyer',
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='potentialBuyers',
            field=models.ManyToManyField(related_name='watchList', to=settings.AUTH_USER_MODEL),
        ),
    ]