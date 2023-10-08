from django.db.models import Avg, Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer


# Вывод списка категорий
@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.annotate(products_count=Count('product'))
        data = CategorySerializer(categories, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Вывод одной категории по идентификатору
@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = CategorySerializer(category).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Вывод списка продуктов
@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = ProductSerializer(products, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Вывод одного продукта по идентификатору
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ProductSerializer(product).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Вывод списка отзывов
@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Вывод одного отзыва по идентификатору
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(review).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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