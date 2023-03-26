from django.urls import  path
from . import  views


urlpatterns=[
     path('',views.HomePageView),
     path('hello/',views.say_hello),
     path('trigger_report/',views.trigger_report),
     # path('get_report/',views.get_report)
#     path('loading/', views.loading_page, name='loading_page'),
    path('get_report/', views.get_report, name='get_report'),
]