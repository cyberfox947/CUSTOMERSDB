from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256, blank=True)
    phone = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=256, blank=True)
    invoices = models.IntegerField()
    total_collectibles = models.DecimalField(decimal_places=2, max_digits=10)
    notes = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name



