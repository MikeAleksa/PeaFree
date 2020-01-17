# Generated by Django 3.0.2 on 2020-01-16 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('item_num', models.IntegerField(primary_key=True, serialize=False, verbose_name='Item Number')),
                ('url', models.CharField(max_length=200, unique=True, verbose_name='URL')),
                ('ingredients', models.CharField(max_length=4096, verbose_name='Ingredients')),
                ('brand', models.CharField(max_length=200, null=True, verbose_name='Brand')),
                ('xsm_breed', models.BooleanField(verbose_name='Extra Small & Toy Breeds')),
                ('sm_breed', models.BooleanField(verbose_name='Small Breeds')),
                ('md_breed', models.BooleanField(verbose_name='Medium Breeds')),
                ('lg_breed', models.BooleanField(verbose_name='Large Breeds')),
                ('xlg_breed', models.BooleanField(verbose_name='Giant Breeds')),
                ('food_form', models.CharField(max_length=200, null=True, verbose_name='Food Form')),
                ('lifestage', models.CharField(max_length=200, null=True, verbose_name='Lifestage')),
                ('fda_guidelines', models.BooleanField(verbose_name='Adheres to FDA Guidelines')),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet', models.CharField(max_length=200, verbose_name='Diet')),
                ('item_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_search.Food')),
            ],
        ),
    ]