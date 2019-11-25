from django.db import models

from DC.models import Crop
from Farmer.models import Farmer


class FieldAgent(models.Model):
    fa_id = models.CharField(primary_key=True, max_length=5, blank=False, unique=True)
    fa_name = models.CharField(max_length=50)
    fa_phone = models.CharField(max_length=15)
    fa_address = models.CharField(max_length=250)
    fa_email = models.EmailField(max_length=50, blank=False, unique=True)
    fa_password = models.CharField(max_length=50)
    fa_nid_no = models.CharField(max_length=25, blank=False, unique=True)
    fa_farmer_under_obs = models.IntegerField()


class SeasonReport(models.Model):
    season_id = models.CharField(primary_key=True, max_length=5, blank=False)
    season_name = models.CharField(max_length=50)
    f_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop_id = models.ForeignKey(Crop, on_delete=models.CASCADE)
    field_size = models.CharField(max_length=5)
    estimated_crop = models.IntegerField()
    estimated_cost = models.FloatField()
