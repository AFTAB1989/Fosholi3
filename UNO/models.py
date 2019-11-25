from django.db import models

from UpChairman.models import Upazilla, UpChairman


class Union(models.Model):
    union_id = models.CharField(primary_key=True, max_length=5, blank=False, unique=True)
    union_name = models.CharField(max_length=25)
    num_of_farmer = models.IntegerField()
    farmable_land = models.IntegerField()
    upz_id = models.ForeignKey(Upazilla, on_delete=models.CASCADE)


class UNO(models.Model):
    uno_id = models.CharField(primary_key=True, max_length=5, blank=False, unique=True)
    uno_name = models.CharField(max_length=50)
    uno_phone = models.CharField(max_length=15)
    uno_address = models.CharField(max_length=150)
    uno_email = models.EmailField(max_length=50, blank=False, unique=True)
    uno_password = models.CharField(max_length=50)
    uno_nid_no = models.CharField(max_length=25, blank=False, unique=True)
    upc_id = models.ForeignKey(UpChairman, on_delete=models.CASCADE)
