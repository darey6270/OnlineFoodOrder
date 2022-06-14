from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/menu.html',
                  {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'Product/detail.html', {'product': product, 'cart_product_form': cart_product_form})


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class AboutMainWebsite(TemplateView):
    template_name = "main/about.html"


class ContactMainWebsite(TemplateView):
    template_name = "main/contact.html"


class TeamMainWebsite(TemplateView):
    template_name = "main/team.html"


class ClientRemarkWebsite(TemplateView):
    template_name = "main/clientremark.html"


class ServiceWebsite(TemplateView):
    template_name = "main/service.html"


class ServiceWebsite(TemplateView):
    template_name = "main/service.html"


class HomeWebsite(TemplateView):
    template_name = "main/index.html"
