from django.db import models

# Create your models here.
markets = [
    ("opensea", "OpenSea"),
    ("nifty_gateway", "Nifty Gateway"),
    ("rarible", "Rarible"),
    ("binance_nft", "Binance NFT"),
    ("superrare", "SuperRare"),
    ("async_art", "Async Art")
]
class MarketPlace(models.Model):
    market = models.CharField(max_length=100, choices=markets, default="opensea")

class ImageLink(models.Model):
    src = models.CharField(max_length=500)
