from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ProductModelForm, CategoryModelForm
from FoodOrdering.models import Category, Product
from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from django.shortcuts import get_object_or_404, render, redirect
from orders.models import Order,PaymentModel


# from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'app_activities/menu.html',
                  {'category': category, 'categories': categories, 'products': products})


def transaction_list(request):
    orders = Order.objects.all()
    return render(request, 'app_activities/transaction.html', {'orders': orders})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'app_activities/food_info_detail.html', {'product': product})


class FoodInfoDetailView(DetailView):
    model = ProductModelForm
    context_object_name = 'food'
    template_name = 'app_activities/food_info_detail.html'


class FoodInfoUpdateView(UpdateView):
    model = Product
    fields = ['name', 'image', 'description', 'price']
    template_name = 'app_activities/food_info_update.html'

    def get_success_url(self):
        return reverse_lazy('app_activities:admin_product_list')

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.category = self.object.category
        fm.available = True
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class FoodInfoDeleteView(DeleteView):
    model = Product
    context_object_name = 'food'
    template_name = 'app_activities/food_info_delete.html'

    def get_success_url(self):
        return reverse_lazy('app_activities:admin_product_list')

class PaymentDeleteView(DeleteView):
    model =Order
    context_object_name = 'payment'
    template_name = 'app_activities/delete_transaction.html'

    def get_success_url(self):
        return reverse_lazy('app_activities:admin_transaction')


class AdminAboutPage(TemplateView):
    template_name = "app_activities/about.html"


class AdminServicePage(TemplateView):
    template_name = "app_activities/service.html"
