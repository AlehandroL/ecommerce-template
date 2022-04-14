from django.urls import path

from . import views

app_name = 'stock'

urlpatterns = [
    path('', views.stock_list, name='stock_list'),
    path('<int:int>/', views.stock_detail, name='stock_detail'),
    path('contact/', views.ContactFormView.as_view(), name='contact_form'),
    path('contact/success', views.ContactFormView.as_view(), name='contact_success'),
]
