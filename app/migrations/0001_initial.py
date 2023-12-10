# Generated by Django 4.2.7 on 2023-12-10 20:56

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.CharField(blank=True, max_length=50, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=300)),
                ('rating', models.IntegerField()),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.profile')),
                ('disliked', models.ManyToManyField(related_name='quest_profiles_disliked', to='app.profile')),
                ('liked', models.ManyToManyField(related_name='quest_profiles_liked', to='app.profile')),
                ('tags', models.ManyToManyField(to='app.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=300)),
                ('rating', models.IntegerField()),
                ('creation_date', models.DateTimeField()),
                ('correct', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.profile')),
                ('disliked', models.ManyToManyField(related_name='answ_profiles_disliked', to='app.profile')),
                ('liked', models.ManyToManyField(related_name='answ_profiles_liked', to='app.profile')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.question')),
                ('tags', models.ManyToManyField(to='app.tag')),
            ],
        ),
    ]