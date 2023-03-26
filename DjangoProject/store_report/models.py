from django.db import models

# Create your models here.
class StoreStatus(models.Model):
    store_id= models.IntegerField()
    timestamp= models.DateTimeField()
    status= models.CharField(max_length=10)


class StoreHour(models.Model):
    store_id = models.IntegerField()
    day_of_week = models.IntegerField()
    start_time_local = models.TimeField()
    end_time_local = models.TimeField()
    
class StoreTimezone(models.Model):
    #we have not made a primary key in this and we are referncing a foreighn key from here
    store_id = models.IntegerField()
    timezonee=models.CharField(max_length=50, default='America/Chicago')
    def __str__(self):
        return str(self.store_id)
    
    
class StoreReport(models.Model):
    report_id = models.CharField(max_length=100)
    store_id = models.IntegerField(default=0)
    store_timezone = models.CharField(max_length=64)
    uptime_last_hour = models.DurationField()
    downtime_last_hour = models.DurationField()
    uptime_last_day = models.DurationField()
    downtime_last_day = models.DurationField()
    uptime_last_week = models.DurationField()
    downtime_last_week = models.DurationField()
    
