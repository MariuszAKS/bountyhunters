from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Bounty


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


class BountyListView(ListView):
    template_name = 'bounties/bounty_list.html'
    model = Bounty
    context_object_name = 'bounties'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bounties'] = context['bounties'].filter(target_completed=False)
        context['count'] = context['bounties'].count()

        return context

class BountyCreateView(CreateView):
    template_name = 'bounties/bounty_create.html'
    model = Bounty
    fields = '__all__'
    success_url = reverse_lazy('bounties')

class BountyUpdateView(UpdateView):
    template_name = 'bounties/bounty_update.html'
    model = Bounty
    fields = '__all__'
    success_url = reverse_lazy('bounties')

class BountyDeleteView(DeleteView):
    template_name = 'bounties/bounty_delete.html'
    model = Bounty
    fields = '__all__'
    success_url = reverse_lazy('bounties')
