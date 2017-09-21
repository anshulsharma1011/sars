from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'products'

urlpatterns = [

    url(r'^product/add/$',views.AddProductsView.as_view(),name='add_product'),
    url(r'^product/(?P<pk>[0-9]+)/$',views.UpdateProductsView.as_view(),name='update_product'),
    url(r'^product/(?P<pk>[0-9]+)/delete/$',views.DeleteProductsView.as_view(),name='delete_product'),

    url(r'^$',views.ProductsListView.as_view(),name='products_list'),
    url(r'^view/list/(?P<pk>[0-9]+)$',views.ProductsDetailView.as_view(),name='products_details'),
]

