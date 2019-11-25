from django.db import models


class Farmer(models.Model):
    f_id = models.CharField(primary_key=True, max_length=5, blank=False, unique=True)
    f_name = models.CharField(max_length=50)
    f_phone = models.CharField(max_length=15)
    f_address = models.CharField(max_length=250)
    f_email = models.EmailField(max_length=50, blank=False, unique=True)
    f_password = models.CharField(max_length=50, blank=False)
    f_nid_no = models.CharField(max_length=25, blank=False, unique=True)
    f_land_amount = models.IntegerField()
    f_farming_on = models.IntegerField()
