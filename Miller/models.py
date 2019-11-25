from django.db import models

from DC.models import Crop
from Farmer.models import Farmer
from UpChairman.models import UpChairman


class Miller(models.Model):
    m_id = models.CharField(primary_key=True, max_length=5, blank=False, unique=True)
    m_name = models.CharField(max_length=50)
    m_phone = models.CharField(max_length=15)
    m_address = models.CharField(max_length=150)
    m_email = models.EmailField(max_length=50, blank=False, unique=True)
    m_password = models.CharField(max_length=50)
    m_nid_no = models.CharField(max_length=25, blank=False, unique=True)
    m_license_no = models.CharField(max_length=25)
    stock_capacity_detail = models.CharField(max_length=250)
    season_stock_availability = models.CharField(max_length=250)
    upc_id = models.ForeignKey(UpChairman, on_delete=models.CASCADE)


class TradeList(models.Model):
    trade_id = models.CharField(primary_key=True, max_length=5, blank=False, unique=True)
    f_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    m_id = models.ForeignKey(Miller, on_delete=models.CASCADE)
    crop_id = models.ForeignKey(Crop, on_delete=models.CASCADE)
    purchase_amount = models.IntegerField()
    price_per_unit = models.IntegerField()
    date = models.DateField()
