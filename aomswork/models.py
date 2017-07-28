from django.db import models


# Model Produk
class Product(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    product_name = models.CharField(max_length=200)
    product_desc = models.CharField(max_length=2000)
    colors = models.ManyToManyField('Color', through='ProductColor')

    class Meta:
        ordering  = ('-create_date',)

    def __str__(self):
        return str(self.id) + ' ' + self.product_name + ': ' + self.product_desc

class Color(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    color_name = models.CharField(max_length=200)

    class Meta:
        ordering = ('-color_name',)

    def __str__(self):
        return str(self.id) + ' ' + self.color_name        

class ProductColor(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
    color = models.ForeignKey(
        'Color',
        on_delete=models.CASCADE,
    )

# Model Order
class Order(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    orderdetails = models.ManyToManyField('OrderDetail', related_name='+')

    class Meta:
        ordering  = ('-create_date',)

class OrderDetail(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
    )
    product_color = models.ForeignKey(
        'ProductColor',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering  = ('-create_date',)

# Model Stock
class Stock(models.Model):
    product_color = models.ForeignKey(
        'ProductColor',
        on_delete=models.CASCADE,
    )
    ammount = models.IntegerField()
