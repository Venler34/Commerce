# Generated by Django 4.1.5 on 2023-07-21 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.CharField(blank=True, max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='AuctionListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(default='No Name', max_length=64)),
                ('ItemDescription', models.CharField(default='No Description', max_length=600)),
                ('DateCreated', models.DateTimeField()),
                ('Bids', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction', to='auctions.bid')),
                ('Comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction', to='auctions.comment')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='Auctions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='auctions.auctionlisting'),
        ),
        migrations.AddField(
            model_name='user',
            name='Bids',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to='auctions.bid'),
        ),
    ]
