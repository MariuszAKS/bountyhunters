# Generated by Django 4.1.5 on 2023-01-11 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bounties', '0002_rename_id_creator_bounty_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='target_description',
            field=models.TextField(blank=True, default='Jest słaby i wiele zapomniał'),
        ),
    ]
