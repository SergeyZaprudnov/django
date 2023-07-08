from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField('media/image/')
    category = models.CharField(max_length=30)
    purchase_price = models.IntegerField(blank=False, null=False)
    date_of_creation = models.DateField(auto_now_add=True)
    last_modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.description}, {self.purchase_price}'

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, unique=True)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ('name',)


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name="user_name")
    email = models.CharField(max_length=100, verbose_name="user_email")
    message = models.CharField(max_length=100, verbose_name="user_message")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
