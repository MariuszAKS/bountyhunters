from django import forms
from django.contrib.auth.models import User
from django.db import models


class Bounty(models.Model):

    DIFFICULTY_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    hunter = models.IntegerField(default=0)
    observed = models.BooleanField(default=False)
    
    target_name = models.CharField(max_length=100, default='Bezimienny')
    target_reward = models.IntegerField(default=100)
    target_description = models.TextField(max_length=375, blank=True, default='Jest słaby i wiele zapomniał', )
    target_difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=1)
    
    target_posted_date = models.DateField(auto_now_add=True)
    target_completed_date = models.DateField(null=True, blank=True)
    target_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.target_name
    
    class Meta:
        default_related_name = 'bounties'
        ordering = ['target_posted_date']

class Observe(models.Model):
    user_id = models.IntegerField()
    bounty_id = models.IntegerField()

    def __str__(self):
        return "User " + str(self.user_id) + " observing bounty " + str(self.bounty_id)
    
    class Meta:
        default_related_name = 'observes'
        ordering = ['user_id']
