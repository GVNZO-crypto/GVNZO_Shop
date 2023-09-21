from django.db.models import Avg, Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer

# Вывод списка категорий
@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.annotate(products_count=Count('product'))
    data = CategorySerializer(categories, many=True).data
    return Response(data, status=status.HTTP_200_OK)


# Вывод одной категории по идентификатору
@api_view(['GET'])
def category_detail_api_view(request, pk):
    category = Category.objects.get(pk=pk)
    data = CategorySerializer(category).data
    return Response(data, status=status.HTTP_200_OK)

# Вывод списка продуктов
@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data, status=status.HTTP_200_OK)

# Вывод одного продукта по идентификатору
@api_view(['GET'])
def product_detail_api_view(request, pk):
    product = Product.objects.get(pk=pk)
    data = ProductSerializer(product).data
    return Response(data, status=status.HTTP_200_OK)

# Вывод списка отзывов
@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data, status=status.HTTP_200_OK)

# Вывод одного отзыва по идентификатору
@api_view(['GET'])
def review_detail_api_view(request, pk):
    review = Review.objects.get(pk=pk)
    data = ReviewSerializer(review).data
    return Response(data, status=status.HTTP_200_OK)

# Вывод списка товаров с отзывами и средним баллом отзывов
@api_view(['GET'])
def products_with_reviews(request):
    products = Product.objects.all()
    products_data = []
    for product in products:
        reviews = Review.objects.filter(product=product)
        average_rating = reviews.aggregate(Avg('stars'))['stars__avg']
        product_data = ProductSerializer(product).data
        product_data['average_rating'] = average_rating
        review_data = ReviewSerializer(reviews, many=True).data
        product_data['reviews'] = review_data
        products_data.append(product_data)
    return Response(products_data, status=status.HTTP_200_OK)