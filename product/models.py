from django.db import models

# Модель Category (Категория)
class Category(models.Model):
    name = models.CharField(max_length=255)  # Поле для имени категории

    def __str__(self):
        return self.name  # Метод, который возвращает строковое представление объекта Category

# Модель Product (Продукт)
class Product(models.Model):
    title = models.CharField(max_length=255)  # Поле для названия продукта
    description = models.TextField(blank=True, null=True)  # Поле для описания продукта (может быть пустым)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Поле для цены продукта
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Внешний ключ для связи с моделью Category
    is_active = models.BooleanField(default=True)  # Поле для обозначения активности продукта

    def __str__(self):
        return self.title  # Метод, который возвращает строковое представление объекта Product

# Модель Review (Отзыв)
class Review(models.Model):
    text = models.TextField()  # Поле для текста отзыва
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Внешний ключ для связи с моделью Product

    def __str__(self):
        return self.text  # Метод, который возвращает строковое представление объекта Review