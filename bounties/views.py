from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class CustomRegisterView(FormView):
    template_name = 'bounties/register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        
        if user is not None:
            login(self.request, user)
        
        return super(CustomRegisterView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('')
        return super(CustomRegisterView, self).get(*args, **kwargs)

class CustomLoginView(LoginView):
    template_name = 'bounties/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('')
