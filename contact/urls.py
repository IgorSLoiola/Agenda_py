from django.urls import path
from contact import views

urlpatterns = [
    path('<int:id>/', views.Contactid, name='contact'),
    path('', views.index, name='index'),
]