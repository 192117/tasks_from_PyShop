from django.db import models
from django.db.models import Q
import json

class Product(models.Model):
    categories = models.ManyToManyField(Category,
                                        related_name='products',
                                        blank=True, verbose_name=u"категории")
    related_products = models.ManyToManyField('Product',
                                              blank=True,
                                              verbose_name="связанные продукты")

    sku = models.CharField(u'артикул', max_length=128, validators=[validators.check_bad_symbols], unique=True)

    price = models.DecimalField(u'цена', max_digits=12, decimal_places=4)

    slug = models.SlugField(u'slug', max_length=80, db_index=True, unique=True)

    name = models.CharField(u'название', max_length=128)
    title = models.CharField(u'заголовок страницы (<title>)', max_length=256, blank=True)
    description = models.TextField(u'описание', blank=True)

def live_search(request):
    ''' Return JSON objects. '''
    q = request.GET.get("q", "")
    if q:
        items = Product.objects.filter(
            Q(sku__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)).values()
        result = [item for item in items]
    else:
        result = []
    return json.dumps(result) # It's true if 'Product' doesn't have a date or time in the fields.