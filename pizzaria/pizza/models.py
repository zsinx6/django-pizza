from django.db import models


class Pizza(models.Model):
    flavor = models.CharField(max_length=128)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    ingredients = models.TextField()

    def __unicode__(self):
        return self.flavor

    def __repr__(self):
        return unicode(self)
