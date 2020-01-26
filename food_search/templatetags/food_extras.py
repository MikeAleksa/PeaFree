import re

from django import template

register = template.Library()

vitamins_pattern = re.compile(
    "(mineral|vitamin|zinc|supplement|calcium|phosphorus|potassium|sodium|" +
    "magnesium|sulfer|sulfur|iron|iodine|selenium|copper|salt|chloride|" +
    "choline|lysine|taurine)", flags=re.I
)
bad_ingredients_pattern = re.compile("(pea |peas| pea |chickpea|peanut|bean|lentil|potato|seed|soy)", flags=re.I)


@register.filter(name='highlight_bad')
def bad_ingredients(ingredients):
    # find "main ingredients" - all ingredients before appearance of first vitamin or mineral
    ingredients = str(ingredients)
    main_ingredients = vitamins_pattern.split(ingredients, maxsplit=1)[0]
    rest_ingredients = ''.join(vitamins_pattern.split(ingredients, maxsplit=1)[1:])
    highlighted = bad_ingredients_pattern.sub('<span class="highlight">\\1</span>', main_ingredients)
    return highlighted + rest_ingredients
