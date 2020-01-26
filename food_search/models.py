from django.db import models


class Food(models.Model):

    def __str__(self):
        return self.url

    item_num = models.IntegerField('item number', primary_key=True)
    url = models.CharField('URL', max_length=200, unique=True)
    name = models.CharField('name', max_length=1000)
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

    def calculate_diets(self):
        diets = Diet.objects.all().filter(item_num=self.item_num)
        diets = ', '.join([d.diet for d in diets])
        if diets == str():
            diets = None
        return diets

    def calculate_breeds(self):
        sizes = list()
        for size, name in [
            (self.xsm_breed, Food._meta.get_field('xsm_breed').verbose_name),
            (self.sm_breed, Food._meta.get_field('sm_breed').verbose_name),
            (self.md_breed, Food._meta.get_field('md_breed').verbose_name),
            (self.lg_breed, Food._meta.get_field('lg_breed').verbose_name),
            (self.xlg_breed, Food._meta.get_field('xlg_breed').verbose_name),
        ]:
            if size == 1:
                sizes.append(name.title())
        sizes = ', '.join(sizes)
        return sizes

    diets = property(calculate_diets)
    breeds = property(calculate_breeds)


class Diet(models.Model):

    def __str__(self):
        return '{} (item number {})'.format(self.diet, self.item_num.item_num)

    diet = models.CharField('diet', max_length=200)
    item_num = models.ForeignKey(Food, on_delete=models.CASCADE)


class ScraperUpdates(models.Model):

    def __str__(self):
        return 'Database last updated on {}'.format(self.date)

    date = models.DateTimeField('last update')
    count = models.IntegerField('food count', null=False)
