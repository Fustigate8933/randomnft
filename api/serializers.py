from rest_framework import serializers
from .models import MarketPlace, ImageLink

class MarketPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketPlace
        fields = "__all__"

class ImageLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageLink
        fields = "__all__"