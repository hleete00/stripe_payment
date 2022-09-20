from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price_in_cents = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "$" + str("{:.2f}".format(self.price_in_cents / 100))
