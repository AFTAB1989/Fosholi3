from django.db import models

from DC.models import District, DC


class Upazilla(models.Model):
    upz_id = models.CharField(primary_key=True, max_length=10, blank=False, unique=True)
    upz_name = models.CharField(max_length=25)
    num_of_union = models.IntegerField()
    num_of_mill = models.IntegerField()
    dist_name = models.ForeignKey(District, on_delete=models.CASCADE)


class UpChairman(models.Model):
    upc_id = models.CharField(primary_key=True, max_length=5, blank=False, unique=True)
    upc_name = models.CharField(max_length=50)
    upc_phone = models.CharField(max_length=15)
    upc_address = models.CharField(max_length=150)
    upc_email = models.EmailField(max_length=50, blank=False, unique=True)
    upc_password = models.CharField(max_length=50)
    upc_nid_no = models.CharField(max_length=25, blank=False, unique=True)
    dc_id = models.ForeignKey(DC, on_delete=models.CASCADE)
