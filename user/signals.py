from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import Group
from doctor.models import Doctorprofile

@receiver(post_save, sender= User)
def createProfile(sender, instance, created, **kwargs):
    print('Profile signal triggered')
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            name = user.first_name,
            username = user.username,
            email = user.email,
        )

        subject = 'Welcome to Medilab'
        message = 'We are glad you are here!'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )
    else:
        # pass
        # if Group.objects.get(name='doctor') == instance.groups.all()[len(instance.groups.all()) - 1]:
        #     profile = instance.profile
        #     doctor_profile = Doctorprofile.objects.get_or_create(
        #         user = instance
        #     )
        #     # doctor_profile.name = user.first_name
        #     print(doctor_profile[0].name)
        try:
            original_instance = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
            original_instance = None

        if original_instance and not Group.objects.filter(name='doctor', user=original_instance).exists() and Group.objects.filter(name='doctor', user=instance).exists():
            # "doctor" group is being added to the instance's groups
            profile = instance.profile
            doctor_profile, created = Doctorprofile.objects.get_or_create(user=instance)
            # doctor_profile.name = instance.first_name
            print(doctor_profile.name)

    