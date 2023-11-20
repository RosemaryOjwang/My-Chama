# Generated by Django 4.1.6 on 2023-11-20 03:47

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
            name='Add_Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memberName', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=155)),
                ('thumbnail', models.ImageField(blank=True, upload_to='img')),
                ('occupation', models.TextField(max_length=1000)),
                ('available', models.BooleanField(default=True)),
                ('member_contact', models.DecimalField(decimal_places=0, max_digits=10)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-joined'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'ordering': ['groupName'],
            },
        ),
        migrations.AddIndex(
            model_name='group',
            index=models.Index(fields=['groupName'], name='accounts_gr_groupNa_835a67_idx'),
        ),
        migrations.AddField(
            model_name='add_members',
            name='groupName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='accounts.group'),
        ),
        migrations.AddField(
            model_name='add_members',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_user', to=settings.AUTH_USER_MODEL),
        ),
    ]