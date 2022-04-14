from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.template.defaultfilters import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Category, Product


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, active=True)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


class ProductIndexView(generic.ListView):
    template_name = 'store/home.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.products.all()


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'store/products/single.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['category', 'name', 'desc', 'image', 'price']
    template_name = 'store/products/create.html'
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.slug = slugify(form.instance.name)
        form.save()
        return redirect(reverse_lazy('store:product_list'))


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'store/products/delete.html'
    success_url = reverse_lazy('store:product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['category', 'name', 'desc', 'image', 'price', 'active', 'in_stock']
    template_name = 'store/products/update.html'
    
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        form.save()
        return redirect(reverse_lazy('store:product_list'))


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'store/products/list.html'
    raise_exception = True
