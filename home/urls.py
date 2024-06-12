from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage),
    path('index.html/',views.homepage),
    path('consultancyproject/about.html/',views.aboutus),
    path('consultancyproject/services.html/',views.services),
    path('consultancyproject/career.html/',views.career),
    path('consultancyproject/signup.html/',views.signup),
    path('consultancyproject/login.html/',views.login),
    path('consultancyproject/contact.html/',views.contactus),
    
    
]