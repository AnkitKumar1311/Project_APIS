# Generated by Django 3.1.1 on 2020-09-25 13:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='images/%Y/%m/')),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2020, 9, 25, 19, 23, 34, 54579))),
                ('likes', models.ManyToManyField(related_name='user_likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_foreign', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
