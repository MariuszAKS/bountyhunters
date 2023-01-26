# Generated by Django 4.1.5 on 2023-01-26 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Observe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('bounty_id', models.IntegerField()),
            ],
            options={
                'ordering': ['user_id'],
                'default_related_name': 'observes',
            },
        ),
        migrations.CreateModel(
            name='Bounty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observed', models.BooleanField()),
                ('target_name', models.CharField(default='Bezimienny', max_length=100)),
                ('target_photo', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/')),
                ('target_reward', models.IntegerField(default=100)),
                ('target_description', models.TextField(blank=True, default='Jest słaby i wiele zapomniał', max_length=375)),
                ('target_difficulty', models.IntegerField(choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')], default=1)),
                ('target_posted_date', models.DateField(auto_now_add=True)),
                ('target_completed_date', models.DateField(blank=True, null=True)),
                ('target_completed', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creators', to=settings.AUTH_USER_MODEL)),
                ('hunter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hunters', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['target_posted_date'],
                'default_related_name': 'bounties',
            },
        ),
    ]