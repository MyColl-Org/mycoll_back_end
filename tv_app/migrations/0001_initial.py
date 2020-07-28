# Generated by Django 3.0.8 on 2020-07-28 20:14

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
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('season_number', models.IntegerField(verbose_name='Season Number')),
                ('episode_count', models.IntegerField(verbose_name='Episode Count')),
                ('year_first_aired', models.IntegerField(verbose_name='First Aired')),
                ('overview', models.TextField(blank=True, null=True, verbose_name='Overview')),
                ('image_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Image Link')),
                ('tmdb_page_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='TMDb Page Link')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('year_first_aired', models.IntegerField(verbose_name='First Aired')),
                ('overview', models.TextField(blank=True, null=True, verbose_name='Overview')),
                ('image_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Image Link')),
                ('tmdb_page_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='TDMb Page Link')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SeasonCopy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=200, verbose_name='Platform')),
                ('form', models.CharField(max_length=200, verbose_name='Format')),
                ('vod_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='VOD Link')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='copies', to='tv_app.Season')),
            ],
        ),
        migrations.AddField(
            model_name='season',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='season', to='tv_app.Show'),
        ),
    ]
