from django.db import models


class Food(models.Model):

    def __str__(self):
        return self.url

    item_num = models.IntegerField('item number', primary_key=True)
    url = models.CharField('URL', max_length=200, unique=True)
    ingredients = models.CharField('ingredients', max_length=4096, null=False)
    brand = models.CharField('brand', max_length=200, null=True)
    xsm_breed = models.BooleanField('extra small & toy breeds')
    sm_breed = models.BooleanField('small breeds')
    md_breed = models.BooleanField('medium breeds')
    lg_breed = models.BooleanField('large breeds')
    xlg_breed = models.BooleanField('giant breeds')
    food_form = models.CharField('food form', max_length=200, null=True)
    lifestage = models.CharField('lifestage', max_length=200, null=True)
    fda_guidelines = models.BooleanField('adheres to FDA guidelines')


class Diet(models.Model):

    def __str__(self):
        return '{} (item number {})'.format(self.diet, self.item_num.item_num)

    diet = models.CharField('diet', max_length=200)
    item_num = models.ForeignKey(Food, on_delete=models.CASCADE)
