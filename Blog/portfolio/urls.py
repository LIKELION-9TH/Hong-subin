from django.contrib import admin
from django.urls import path
import portfolio.views


urlpatterns =[

    path('portfolio/', portfolio.views.portfolio, name="portfolio"),

]