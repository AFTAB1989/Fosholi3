from django.contrib import admin

from .models import FieldAgent, SeasonReport, SeasonalServey

admin.site.register(FieldAgent)
admin.site.register(SeasonReport)
admin.site.register(SeasonalServey)
