from django.http import HttpResponse
import csv
import io
import uuid
import json
from django.db import models
from datetime import datetime, timedelta,time
from django.db.models import F, Sum
from .models import StoreStatus, StoreTimezone

from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import StoreTimezone, StoreHour, StoreStatus
from django.utils import timezone
from dateutil import tz
from django.utils import timezone

def compute_uptime_downtime(store_id):
    # Get the timezone for the store
    store_timezone = StoreTimezone.objects.filter(store_id=store_id).first()
    if store_timezone is None:
        store_timezone = 'America/Chicago'
    else:
        store_timezone = store_timezone.timezonee

    # Get the business hours for the store
    store_business_hours = StoreHour.objects.filter(store_id=store_id)

    if not store_business_hours.exists():
        store_business_hours = {"start_time_local": "09:00:00",
                                "end_time_local": "17:00:00", "timezonee": store_timezone}
    else:
        store_business_hours = {"start_time_local": store_business_hours.first().start_time_local,
                                "end_time_local": store_business_hours.first().end_time_local, "timezonee": store_timezone}

    # Get the store events within the last 24 hours
    # now = timezone.now()
    now = timezone.now() -timezone.timedelta(days=31)
    # now = datetime(2023, 1, 24, 9, 7, 26, 441407)
    yesterday = now - timezone.timedelta(days=7)
    store_events = StoreStatus.objects.filter(
        store_id=store_id, timestamp__range=(yesterday, now)).order_by('timestamp')
    
    print(store_events)
    start_time = timezone.now()
    end_time = timezone.now()
    # Convert business hours to datetime objects 
    if timezone is not None:
        start_time = timezone.now()
        end_time = timezone.now()
        start_time = datetime.strptime(start_time.strftime('%H:%M:%S'), '%H:%M:%S')
        end_time = datetime.strptime(end_time.strftime('%H:%M:%S'), '%H:%M:%S')

    # Convert timezones
    local_timezone = tz.gettz(store_business_hours["timezonee"])
    utc_timezone = tz.gettz('UTC')
    start_time = start_time.replace(
        tzinfo=local_timezone).astimezone(utc_timezone)
    end_time = end_time.replace(tzinfo=local_timezone).astimezone(utc_timezone)

    uptime_duration = timezone.timedelta()
    downtime_duration = timezone.timedelta()

    # Loop through events to compute uptime and downtime
    for i in range(len(store_events)):
        event = store_events[i]
        event_time = event.timestamp

        # Convert event time to UTC
        event_time_utc = event_time.replace(
            tzinfo=local_timezone).astimezone(utc_timezone)

        if event.status == 'active':
            # Check if event occurred during business hours
            if start_time <= event_time_utc <= end_time:
                if i < len(store_events) - 1:
                    next_event = store_events[i + 1]
                    if next_event.status == 'inactive':
                        # Compute uptime duration
                        uptime_duration += next_event.timestamp - event.timestamp
                    else:
                        # No close event found, so assume store is still open
                        uptime_duration += now - event.timestamp
            else:
                # Event occurred outside business hours, so assume store was already closed
                if i < len(store_events) - 1:
                    next_event = store_events[i + 1]
                    if next_event.status == 'inactive':
                        # Compute downtime duration
                        downtime_duration += next_event.timestamp - event.timestamp
                    else:
                        # No close event found, so assume store is still closed
                        downtime_duration += now - event.timestamp

    # Convert durations to seconds
    uptime_seconds = uptime_duration.total_seconds()
    downtime_seconds = downtime_duration.total_seconds()
    # print(uptime_seconds,downtime_seconds)
    return {"uptime": uptime_seconds, "downtime": downtime_seconds}

    
def say_hello(request):
    # return HttpResponse("Hello World!")
    return render(request, template_name="hello.html")


def HomePageView(request):
    # return HttpResponse("Hello World!")
    return render(request, template_name="homepage.html")


def trigger_report(request):
    # Read the data from the database and compute the report
    # ...

    # Return a report ID to the client
    # create a random report_id
    report_id = uuid.uuid4().hex
    return JsonResponse({'report_id': report_id})

def generate_report(report_id):


    # unique_store_ids = StoreTimezone.objects.values('store_id')
    unique_store_ids = StoreTimezone.objects.values_list('store_id', flat=True).distinct()
    print(unique_store_ids)
    ansDic={}
    lst = {}
    j=100
    for store_id in unique_store_ids:
        if(j<0): 
            break
        j-=1
        lDic = compute_uptime_downtime(store_id)
        lDic["Store_id"] = store_id
        # print(lDic)
        lst={**{store_id :lDic},**lst} 
        # print(lst)
    # print(lst)
    return lst


# def generate_report(report_id):
#     unique_store_ids = StoreTimezone.objects.annotate(
#         store_id_int=Cast('store_id', output_field=models.IntegerField())
#     ).values('store_id_int').distinct()
#     lst=[]
#     for store_id in unique_store_ids:
#         lDic=compute_uptime_downtime(store_id)
#         lDic["Store_id"]= store_id
#         lst.append(lDic)
    
#     return lst
        
        


def get_report(request):
    report_id = request.GET.get('report_id')
    result = generate_report(report_id)
    result_json = json.dumps(result)
    return HttpResponse(result_json, content_type='application/json')
# def get_report(request):
#     report_id = request.POST.get('report_id')
#     result = generate_report(report_id)
#     print(result)
#     return HttpResponse(result, content_type='text/html')


# def get_report(request):
#     report_id = request.GET.get('report_id')
#     # print(report_id)
   
#     result=generate_report(report_id)
#     print(result)
#     # return render(request, str(result))
#     return render(request.POST., result.html)
    # return result 
    # return json.dumps(result)
    # return JsonResponse({'report_id': report_id})
# 