from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import MarketPlace
from .serializers import MarketPlaceSerializer
from rest_framework.response import Response
from selenium import webdriver

# Create your views here.
class SearchMarketPlace(APIView):
    serializer_class = MarketPlaceSerializer
    market = ""

    def post(self, request, format=None):
        serialized_data = self.serializer_class(request.data)
        market = serialized_data.data.get("market")

        options = webdriver.ChromeOptions()
        options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'

        driver = webdriver.Chrome(
        executable_path="D:\\Programming\\Python\\modules\\django\\randomnft\\chromedriver.exe", options=options)
        driver.get("https://opensea.io/assets")

        img_paths = driver.find_elements_by_class_name("Image--image")
        driver.implicitly_wait(6)

        imgs = [img_paths[i].get_attribute('src') for i in range(len(img_paths))]
        imgs_ = []

        for i in imgs:
            if i != None:
                imgs_.append(i)
        driver.close()

        print(imgs_)

        return Response(imgs_)


class ListMarketPlace(generics.ListAPIView):
    queryset = MarketPlace.objects.all()
    serializer_class = MarketPlaceSerializer