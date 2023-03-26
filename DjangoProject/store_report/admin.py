from django.contrib import admin

# Register your models here.
from .models import StoreStatus,StoreHour, StoreTimezone



admin.site.register(StoreStatus)
admin.site.register(StoreHour)
admin.site.register(StoreTimezone)