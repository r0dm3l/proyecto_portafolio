from django.urls import path
from . import views

urlpatterns =[
    path('', views.PortafolioView.as_view(),name="index"),
    path('create/', views.Proyectocreate.as_view(), name="create")
]