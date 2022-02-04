from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import MarketPlace, ImageLink
from .serializers import MarketPlaceSerializer, ImageLinkSerializer
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
        driver.implicitly_wait(15)

        imgs = [img_paths[i].get_attribute('src') for i in range(len(img_paths))]

        for i in imgs:
            if i != None:
                image_link = ImageLink(src=i)
                image_link.save()
                print(i)

        driver.close()

        return Response({"msg": "POST success"}, status=status.HTTP_201_CREATED)


class ListImageLinks(generics.ListAPIView):
    queryset = ImageLink.objects.all()
    serializer_class = ImageLinkSerializer
