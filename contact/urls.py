from django.urls import path
from contact import views

#app_name = 'contact'

urlpatterns = [
    #contact
    path('contact/<int:id>/detail/', views.contact, name='contact'),
    #CRUD contato
    path('contact/create/', views.create, name='create'),
    path('contact/<int:id>/update/', views.update, name='update'),
    path('contact/<int:id>/delete/', views.delete, name='delete'),

    #CRUD user
    path('user/register/',views.register ,name='register'),
    path('user/login/',views.login ,name='login'),
    path('user/logoff/',views.logoff ,name='logoff'),
    path('user/updateuser/',views.updateuser ,name='updateuser'),

    #search
    path('search/',views.search ,name='search'),

    #index
    path('', views.index, name='index'),
]