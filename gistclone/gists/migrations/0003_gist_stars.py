# Generated by Django 3.2.5 on 2021-07-14 07:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gists', '0002_auto_20210714_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='gist',
            name='stars',
            field=models.ManyToManyField(blank=True, related_name='stars', to=settings.AUTH_USER_MODEL),
        ),
    ]
