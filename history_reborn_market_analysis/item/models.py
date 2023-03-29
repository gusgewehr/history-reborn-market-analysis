""" Models that manages items"""

from django.db import models
from django.utils import timezone


class Item(models.Model):
    """ This class create a bd relation that is used 
    to describe which itens the user wants to track """
    ro_id = models.BigIntegerField()
    coin = models.ForeignKey("Item", on_delete=models.DO_NOTHING)
    price = models.IntegerField()
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(blank=True, null=True, editable=False)
    track = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()          
        self.modified = timezone.now()

        oldItem = ItemHist(
                coin = self.coin,
                price = self.price,
                date = timezone. now()
            )
        
        oldItem.save()
        return super(Item, self).save(*args, **kwargs)


class ItemHist(models.Model):
    ro_id = models.BigIntegerField()
    coin = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.IntegerField
    date = models.DateTimeField(blank=True, editable=False)