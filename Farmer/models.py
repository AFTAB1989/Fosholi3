from django.db import models

from DC.models import District
from UNO.models import Union
from UpChairman.models import Upazilla


class Farmer(models.Model):
    f_id = models.CharField(primary_key=True, max_length=15, blank=False, unique=True)
    f_name = models.CharField(max_length=50)
    f_phone = models.CharField(max_length=15)
    f_address = models.CharField(max_length=250)
    f_email = models.EmailField(max_length=50, blank=False, unique=True)
    f_password = models.CharField(max_length=50, blank=False)
    f_nid_no = models.CharField(max_length=25, blank=False, unique=True)
    f_land_amount = models.IntegerField()
    f_farming_on = models.IntegerField()
    f_land_address = models.CharField(max_length=100)
    union_id = models.ForeignKey(Union, on_delete=models.CASCADE)
    upz_id = models.ForeignKey(Upazilla, on_delete=models.CASCADE)
    dist_name = models.ForeignKey(District, on_delete=models.CASCADE)
    f_total_land_area = models.IntegerField()
