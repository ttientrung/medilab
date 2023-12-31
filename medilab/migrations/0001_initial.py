# Generated by Django 4.2.1 on 2023-06-16 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('short_intro', models.CharField(blank=True, max_length=2000, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, default='department/default.jpg', null=True, upload_to='departments/')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('short_intro', models.CharField(blank=True, max_length=2000, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, default='doctors/user-default.png', null=True, upload_to='doctors/')),
                ('social_twitter', models.CharField(blank=True, max_length=2000, null=True)),
                ('social_facebook', models.CharField(blank=True, max_length=2000, null=True)),
                ('social_instagram', models.CharField(blank=True, max_length=2000, null=True)),
                ('social_linkedin', models.CharField(blank=True, max_length=2000, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='medilab.department')),
            ],
        ),
    ]
