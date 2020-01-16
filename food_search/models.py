from django.db import models


# Create your models here.
class Food(models.Model):

    def __str__(self):
        return self.url

    item_num = models.IntegerField('Item Number', primary_key=True)
    url = models.CharField('URL', max_length=200, unique=True)
    ingredients = models.CharField('Ingredients', max_length=4096, null=False)
    brand = models.CharField('Brand', max_length=200, null=True)
    xsm_breed = models.BooleanField('Extra Small & Toy Breeds')
    sm_breed = models.BooleanField('Small Breeds')
    md_breed = models.BooleanField('Medium Breeds')
    lg_breed = models.BooleanField('Large Breeds')
    xlg_breed = models.BooleanField('Giant Breeds')
    food_form = models.CharField('Food Form', max_length=200, null=True)
    lifestage = models.CharField('Lifestage', max_length=200, null=True)
    fda_guidelines = models.BooleanField('Adheres to FDA Guidelines')


class Diet(models.Model):

    def __str__(self):
        return '{} (item number {})'.format(self.diet, self.item_num.item_num)

    diet = models.CharField('Diet', max_length=200)
    item_num = models.ForeignKey(Food, on_delete=models.CASCADE)
