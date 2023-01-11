from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers


class Bounty(models.Model):

    DIFFICULTY_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    
    target_name = models.CharField(max_length=100, default='Bezimienny')
    target_reward = models.IntegerField(default=100)
    target_description = models.TextField(blank=True, default='Jest słaby i wiele zapomniał')
    target_difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=1)
    
    target_posted_date = models.DateTimeField(auto_now_add=True)
    target_completed_date = models.DateTimeField(null=True, blank=True)
    target_completed = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.title
    
    class Meta:
        default_related_name = 'bounties'
        ordering = ['target_posted_date']
