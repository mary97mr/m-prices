from rest_framework import serializers
from .models import Product, Category, SubCategory, Instances

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = "__all__"

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory 
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = "__all__"

class InstancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instances 
        fields = "__all__"