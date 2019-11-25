from django.db import models


class District(models.Model):
    dist_name = models.CharField(primary_key=True, max_length=50, blank=False, unique=True)
    num_of_upazilla = models.IntegerField()
    num_of_union = models.IntegerField()


class DC(models.Model):
    dc_id = models.CharField(primary_key=True, max_length=5, blank=False, unique=True)
    dc_name = models.CharField(max_length=50)
    dc_phone = models.CharField(max_length=15)
    dc_address = models.CharField(max_length=150)
    dc_email = models.EmailField(max_length=50, blank=False, unique=True)
    dc_password = models.CharField(max_length=50)
    dc_nid_no = models.CharField(max_length=25, blank=False, unique=True)
    dist_name = models.ForeignKey(District, on_delete=models.CASCADE)


class Crop(models.Model):
    crop_id = models.CharField(primary_key=True, max_length=5)
    crop_name = models.CharField(max_length=50)
    crop_type = models.CharField(max_length=50)
