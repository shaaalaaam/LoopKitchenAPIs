import csv
import pytz
import datetime
from django.core.management.base import BaseCommand
from store_report.models import StoreTimezone, StoreHour, StoreStatus


def load_data():
    with open('storesStatus.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # to skip the header row
        for row in reader:
            store_id = int(row[0])
            timezone_str = row[1]
            store = StoreTimezone(store_id=store_id, timezone_str=timezone_str)
            store.save()
    with open('store_hours.csv','r') as f:
        reader=csv.reader(f)
        next(reader)
        for row in reader: 
            store_id= int(row[0])
            day_of_week = int(row[1])
            start_time_local= datetime.datetime.strptime(row[2],'%H:%M:%S').time()
            end_time_local= datetime.datetime.strptime(row[3],'%H:%M:%S').time()
            store= StoreTimezone.objects.get(store_id=store_id)
            store_hour= StoreHour(store=store,day_of_week=day_of_week,start_time_local=start_time_local, end_time_local=end_time_local)
            store_hour.save()
    
    with open('store_status.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            store_id = int(row[0])
            timestamp_utc = datetime.datetime.strptime(
                row[1], '%Y-%m-%d %H:%M:%S')
            status = row[2]
            store = StoreTimezone.objects.get(store_id=store_id)
            store_status = StoreStatus(store=store, timestamp_utc=timestamp_utc,status=status)
            store_status.save()

load_data()







# class Command(BaseCommand):
#     help = 'Loads data from the CSV files'
    # def handle( self,*args, **kwargs):
        # load storesTimeZones
        # with open('storesStatus.csv','r' ) as f:
        #     reader=csv.reader(f)
        #     next(reader) # to skip the header row
        #     for row in reader:
        #         store_id = int(row[0])
        #         timezone_str= row[1]
        #         store = StoreTimezone(store_id=store_id, timezone_str= timezone_str)
        #         store.save()
                
        # with open('store_hours.csv','r') as f:
        #     reader=csv.reader(f)
        #     next(reader)
        #     for row in reader: 
        #         store_id= int(row[0])
        #         day_of_week = int(row[1])
        #         start_time_local= datetime.datetime.strptime(row[2],'%H:%M:%S').time()
        #         end_time_local= datetime.datetime.strptime(row[3],'%H:%M:%S').time()
        #         store= StoreTimezone.objects.get(store_id=store_id)
        #         store_hour= StoreHour(store=store,day_of_week=day_of_week,start_time_local=start_time_local, end_time_local=end_time_local)
        #         store_hour.save()
        
        #     with open('store_status.csv', 'r') as f:
        #         reader = csv.reader(f)
        #         next(reader)  # Skip the header row
        #         for row in reader:
        #             store_id = int(row[0])
        #             timestamp_utc = datetime.datetime.strptime(
        #                 row[1], '%Y-%m-%d %H:%M:%S')
        #             status = row[2]
        #             store = StoreTimezone.objects.get(store_id=store_id)
        #             store_status = StoreStatus(store=store, timestamp_utc=timestamp_utc,status=status)
        #             store_status.save()
                