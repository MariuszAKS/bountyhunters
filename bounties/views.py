from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Bounty, Observe


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
    
    def get_success_url(self):
        return reverse_lazy('bounties')

class CustomLoginView(LoginView):
    template_name = 'bounties/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('bounties')

class UserProfileView(ListView):
    model = Bounty
    context_object_name = 'bounties'
    template_name = 'bounties/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        observes = Observe.objects.all().filter(user_id=self.request.user.id)
        
        context['bounties_created'] = context['bounties'].filter(creator=self.request.user)
        context['bounties_observing'] = []
        for bounty in context['bounties']:
            for relation in observes:
                if relation.bounty_id == bounty.id:
                    context['bounties_observing'].append(bounty)
        context['bounties_completed'] = context['bounties'].filter(hunter=self.request.user.id)

        if self.kwargs['category'] == 'created':
            context['bounties'] = context['bounties_created']
        
        if self.kwargs['category'] == 'observing':
            context['bounties'] = context['bounties_observing']
        
        context['bounties_created_amount'] = context['bounties_created'].count()
        context['bounties_completed_amount'] = context['bounties_completed'].count()

        return context

class UserProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'bounties/user_form.html'

    def get_success_url(self):
        return reverse_lazy('user-profile', kwargs={'pk': self.request.user.id, 'category': 'created'})

class BountyListView(ListView):
    model = Bounty
    context_object_name = 'bounty_list'
    template_name = 'bounties/bounty_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        observe_list = Observe.objects.all().filter(user_id=self.request.user.id)

        context['bounties'] = context['bounty_list'].filter(target_completed=False)
        if self.request.user.is_authenticated:
            context['bounties'] = context['bounties'].exclude(creator=self.request.user)
        context['count'] = context['bounties'].count()
        context['observe_list'] = observe_list

        search_input_name = self.request.GET.get('search-name') or ''
        if search_input_name:
            context['bounties'] = context['bounties'].filter(target_name__icontains=search_input_name)
        
        search_input_reward_lowest = self.request.GET.get('search-reward-lowest') or ''
        search_input_reward_highest = self.request.GET.get('search-reward-highest') or ''
        if search_input_reward_lowest:
            context['bounties'] = context['bounties'].filter(target_reward__gt=search_input_reward_lowest)
        if search_input_reward_highest:
            context['bounties'] = context['bounties'].filter(target_reward__lt=search_input_reward_highest)
        
        for bounty in context['bounties']:
            bounty.observed = any((obs.user_id == self.request.user.id and obs.bounty_id == bounty.id) for obs in context['observe_list'])

        return context

def update_observe(request, *args, **kwargs):
    if request.method == 'POST':
        user_id = request.user.id
        bounty_id = int(request.POST['bounty_id'])

        observe_list = Observe.objects.all().filter(user_id=request.user.id)

        if not any((obs.user_id == user_id and obs.bounty_id == bounty_id) for obs in observe_list):
            observe = Observe.objects.create(user_id=user_id, bounty_id=bounty_id)
            observe.save()
            print('SAVE')
        else:
            Observe.objects.filter(user_id=user_id).filter(bounty_id=bounty_id).delete()
            print('DELETE')
        
        return redirect('/')

class BountyCreateView(CreateView, LoginRequiredMixin):
    model = Bounty
    fields = ['target_name', 'target_reward', 'target_description', 'target_difficulty']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.hunter = 0
        form.instance.observed = False

        form.instance.target_posted_date = timezone.now()
        form.instance.target_completed_date = timezone.now()
        form.instance.completed = False

        return super(BountyCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('user-profile', kwargs={'pk': self.request.user.id, 'category': 'created'})

class BountyUpdateView(UpdateView, LoginRequiredMixin):
    model = Bounty
    fields = ['target_name', 'target_reward', 'target_description', 'target_difficulty', 'target_completed', 'target_completed_date']
    
    def get_success_url(self):
        return reverse_lazy('user-profile', kwargs={'pk': self.request.user.id, 'category': 'created'})

class BountyDeleteView(DeleteView, LoginRequiredMixin):
    model = Bounty
    fields = '__all__'
    
    def get_success_url(self):
        return reverse_lazy('user-profile', kwargs={'pk': self.request.user.id, 'category': 'created'})
