from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import user_passes_test,login_required
from django.views.generic import View,ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView
from .models import Product
# Create your views here.

@method_decorator(user_passes_test(lambda u:u.is_superuser),name='dispatch')
class AddProductsView(CreateView):
    template_name = 'products/add_products.html'
    model = Product
    fields = ['name','base_quantity','quantity_unit','rate','photo']

@method_decorator(user_passes_test(lambda u:u.is_superuser),name='dispatch')
class UpdateProductsView(UpdateView):
    model = Product
    template_name = 'products/add_products.html'
    fields = ['name','base_quantity','quantity_unit','rate','photo']

@method_decorator(user_passes_test(lambda u:u.is_superuser),name='dispatch')
class DeleteProductsView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:products_list')

class ProductsListView(ListView):
    template_name = 'products/products_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

class ProductsDetailView(DetailView):
    template_name = 'products/products_details.html'
    model = Product
    context_object_name = 'product'
