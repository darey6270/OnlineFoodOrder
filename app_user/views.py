# Create your views here.
from django.shortcuts import render
from app_user.forms import UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView


class user_login(LoginView):
    template_name = 'app_user/sign-in.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('app_activities:admin_home')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_activities:admin_home'))


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            user.save()
            registered = True
            return HttpResponseRedirect(reverse('app_activities:admin_home'))
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'app_user/registration.html',
                  {'form': user_form})
