# Generated by Django 4.2.1 on 2023-06-17 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medilab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('gallery_image', models.ImageField(blank=True, default='galleries/default.jpg', null=True, upload_to='galleries/')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(blank=True, max_length=200, null=True)),
                ('owner_job', models.CharField(blank=True, max_length=200, null=True)),
                ('owner_image', models.ImageField(blank=True, default='testimonials/user-default.png', null=True, upload_to='testimonials/')),
                ('testi', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
