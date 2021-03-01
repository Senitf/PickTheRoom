# Generated by Django 3.1.5 on 2021-03-01 14:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, choices=[('서울', '서울'), ('경기', '경기'), ('강원', '강원'), ('충남', '충남'), ('충북', '충북'), ('전남', '전남'), ('전북', '전북'), ('제주', '제주')], max_length=5)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('rating', models.FloatField(default=0.0)),
                ('distance', models.CharField(blank=True, max_length=100)),
                ('charge', models.IntegerField(default=0)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('distance_score', models.IntegerField(default=0)),
                ('charge_score', models.IntegerField(default=0)),
                ('rating_score', models.IntegerField(default=0)),
                ('SAW_score', models.FloatField(default=0)),
                ('scrap', models.ManyToManyField(blank=True, related_name='scrap', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['region', '-SAW_score', 'title'],
            },
        ),
    ]
