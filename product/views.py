from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer

# Вывод списка категорий
@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    data = CategorySerializer(categories, many=True)
    return Response(data.data, status=status.HTTP_200_OK)

# Вывод одной категории по идентификатору
@api_view(['GET'])
def category_detail_api_view(request, pk):
    category = Category.objects.get(pk=pk)
    data = CategorySerializer(category)
    return Response(data.data, status=status.HTTP_200_OK)

# Вывод списка продуктов
@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True)
    return Response(data.data, status=status.HTTP_200_OK)

# Вывод одного продукта по идентификатору
@api_view(['GET'])
def product_detail_api_view(request, pk):
    product = Product.objects.get(pk=pk)
    data = ProductSerializer(product)
    return Response(data.data, status=status.HTTP_200_OK)

# Вывод списка отзывов
@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True)
    return Response(data.data, status=status.HTTP_200_OK)

# Вывод одного отзыва по идентификатору
@api_view(['GET'])
def review_detail_api_view(request, pk):
    review = Review.objects.get(pk=pk)
    data = ReviewSerializer(review)
    return Response(data.data, status=status.HTTP_200_OK)