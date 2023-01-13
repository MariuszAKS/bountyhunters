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
            return redirect('bounties')
        return super(CustomRegisterView, self).get(*args, **kwargs)

class CustomLoginView(LoginView):
    template_name = 'bounties/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('bounties')


class BountyListView(ListView):
    model = Bounty
    context_object_name = 'bounties'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bounties'] = context['bounties'].filter(target_completed=False)
        context['count'] = context['bounties'].count()

        search_input_name = self.request.GET.get('search-name') or ''
        if search_input_name:
            context['bounties'] = context['bounties'].filter(target_name__icontains=search_input_name)
        
        search_input_reward_lowest = self.request.GET.get('search-reward-lowest') or ''
        search_input_reward_highest = self.request.GET.get('search-reward-highest') or ''
        if search_input_reward_lowest:
            context['bounties'] = context['bounties'].filter(target_reward__gt=search_input_reward_lowest)
        if search_input_reward_highest:
            context['bounties'] = context['bounties'].filter(target_reward__lt=search_input_reward_highest)
        
        # search_input_difficulties = self.request.GET.getlist('search-difficulty')
        # print(search_input_difficulties)
        search_input_difficulty_1 = self.request.GET.get('search-difficulty-1')
        search_input_difficulty_2 = self.request.GET.get('search-difficulty-2')
        search_input_difficulty_3 = self.request.GET.get('search-difficulty-3')
        search_input_difficulty_4 = self.request.GET.get('search-difficulty-4')
        search_input_difficulty_5 = self.request.GET.get('search-difficulty-5')

        context['search_input_name'] = search_input_name
        context['search_input_reward_lowest'] = search_input_reward_lowest
        context['search_input_reward_highest'] = search_input_reward_highest
        context['search_input_difficulty_1'] = search_input_difficulty_1
        context['search_input_difficulty_2'] = search_input_difficulty_2
        context['search_input_difficulty_3'] = search_input_difficulty_3
        context['search_input_difficulty_4'] = search_input_difficulty_4
        context['search_input_difficulty_5'] = search_input_difficulty_5

        print(search_input_difficulty_1)
        print(search_input_difficulty_2)
        print(search_input_difficulty_3)
        print(search_input_difficulty_4)
        print(search_input_difficulty_5)

        return context

class BountyCreateView(CreateView):
    model = Bounty
    fields = '__all__'
    success_url = reverse_lazy('bounties')

class BountyUpdateView(UpdateView):
    model = Bounty
    fields = '__all__'
    success_url = reverse_lazy('bounties')

class BountyDeleteView(DeleteView):
    model = Bounty
    fields = '__all__'
    success_url = reverse_lazy('bounties')
