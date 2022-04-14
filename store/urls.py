from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
#    path('', views.product_all, name='product_all'),
    path('', views.ProductIndexView.as_view(), name='product_all'),
    path('tienda/<slug:slug>/', views.category_detail, name='category_detail'),
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('create_product/', views.ProductCreateView.as_view(), name='product_create'),
    path('delete_product/<slug:slug>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('update_product/<slug:slug>/', views.ProductUpdateView.as_view(), name='product_update'),
#    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    
]
