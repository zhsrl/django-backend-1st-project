from typing import Text
from unicodedata import name
from django.db import models
from django.forms import BooleanField, CharField, FloatField, IntegerField


class Product(models.Model):

    Phones = "PHONES"
    Laptops = "LAPTOPS"
    TV = "TV"
    PC = "PC"

    CATEGORIES = (
        (Phones, "phones"),
        (Laptops, "laptops"),
        (TV, "tv"),
        (PC, "pc")
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    decription = models.TextField()
    category = models.CharField(
        choices=CATEGORIES, max_length=9, default=Phones)
    count = models.IntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'decription': self.decription
        }


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
