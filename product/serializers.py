from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Product, Review, Tag, User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Категория с таким именем уже существует.")
        return value

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_category(self, value):
        if not Category.objects.filter(pk=value.pk).exists():
            raise serializers.ValidationError("Указанной категории не существует.")
        return value

    def validate_tags(self, value):
        invalid_tags = [tag for tag in value if not Tag.objects.filter(pk=tag.pk).exists()]
        if invalid_tags:
            raise serializers.ValidationError(f"Следующие теги не существуют: {', '.join([str(tag) for tag in invalid_tags])}")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_product(self, value):
        if not Product.objects.filter(pk=value.pk).exists():
            raise serializers.ValidationError("Указанного продукта не существует.")
        return value

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

    def validate_name(self, value):
        if Tag.objects.filter(name=value).exists():
            raise serializers.ValidationError("Тег с таким именем уже существует.")
        return value