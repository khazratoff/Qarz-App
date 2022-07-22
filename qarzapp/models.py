from django.db import models as m
import uuid
# Create your models here.

class QarzModel(m.Model):

    conType=(
        ('ber','Qarz berish'),
        ('ol','Qarz olish'),
    )
    currencyType=(
        ('uzs','UZS'),
        ('usd','USD')
    )
    condition=m.CharField(null=True, max_length=200, choices=conType)
    name=m.CharField(null=True,max_length=200)
    date=m.DateTimeField(auto_now_add=True)
    amount=m.IntegerField(null=True)
    currency=m.CharField(max_length=200, choices=currencyType)
    id=m.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)

    def __str__(self):
        return self.person

    class Meta:
        ordering=['-date']

