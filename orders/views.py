from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Order, OrderItem, PaymentModel
from .forms import OrderCreateForm, PaymentCreateForm
from cart.cart import Cart
from django.db.models.signals import post_save
from django.dispatch import receiver


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
            return HttpResponseRedirect(reverse("orders:make_payment"))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


def orderId(id):
    orderId.id=id


@receiver(post_save, sender=Order)
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.id:
            orderId(instance.id)


def payment_create(request):
    if request.method == 'POST':
        order=''
        try:
            order = Order.objects.get(id=orderId.id)
        except Order.DoesNotExist:
            order = Order.objects.filter().last()

        PaymentModel.objects.create(order=order, email=request.POST["email"],
                                    card_number=request.POST["card_number"],
                                    card_date=request.POST['card_date'],
                                    card_name=request.POST["card_name"])
        return render(request, 'orders/order/created.html')

    else:
        return render(request, 'orders/order/payment.html')
