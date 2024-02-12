from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('events_list',views.index, name="event"),
    path('add_events',views.add_events,name="add_events"),
    
   # path('generate_pdf',views.generate_pdf,name="generate_pdf")
]


    