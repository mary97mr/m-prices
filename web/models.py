from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=240)

class SubCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=240)
    published = models.BooleanField(blank=True, null=True)
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT)

class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=240)
    name = models.CharField("Name", max_length=240)
    badges =  models.JSONField( blank=True, null=True)
    thumbnail =  models.CharField( blank=True, null=True, max_length=300)
    subcategory_id = models.ForeignKey('SubCategory', on_delete=models.PROTECT)
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT)
    is_new = models.BooleanField(blank=True, null=True)
    bunch_selector = models.BooleanField(blank=True, null=True)
    size_format = models.CharField(blank=True, null=True, max_length=240)
    reference_format = models.CharField(blank=True, null=True, max_length=240)
    min_bunch_amount = models.CharField(blank=True, null=True, max_length=240)
    increment_bunch_amount = models.CharField(blank=True, null=True, max_length=240)


class Instances(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)
    iva = models.IntegerField(blank=True, null=True)
    is_pack = models.BooleanField(blank=True, null=True)
    packaging = models.CharField( blank=True, null=True, max_length=240)
    pack_size = models.CharField(blank=True, null=True, max_length=240)

    unit_name = models.CharField(blank=True, null=True, max_length=240)
    unit_size = models.CharField(blank=True, null=True, max_length=240)
    unit_price = models.CharField(blank=True, null=True, max_length=240)
    unit_selector = models.BooleanField(blank=True, null=True)
    total_units = models.CharField(blank=True, null=True, max_length=240)

    approx_size = models.BooleanField(blank=True, null=True)
    drained_weight = models.CharField(blank=True, null=True, max_length=240)

    bulk_price = models.CharField(blank=True, null=True, max_length=240)
    reference_price = models.CharField(blank=True, null=True, max_length=240)
    price_decreased = models.BooleanField(blank=True, null=True)
    published = models.CharField(blank=True, null=True,  max_length=240)
    share_url = models.CharField(blank=True, null=True,  max_length=400)
    selling_method = models.CharField(blank=True, null=True,  max_length=240)
    creation_date_time = models.DateTimeField(auto_now=True)