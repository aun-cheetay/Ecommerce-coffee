from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PackSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackSize
        fields = '__all__'


class CoffeePodFlavourSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeePodFlavour
        fields = '__all__'


class CoffeeMachineProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = CoffeeMachineProduct
        fields = '__all__'

class CoffeePodProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    flavor = CoffeePodFlavourSerializer()
    pack_size = PackSizeSerializer()

    class Meta:
        model = CoffeePodProduct
        fields = '__all__'