# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Website


# @receiver(post_save, sender=User)
# def create_qrcode(sender, instance, created, **kwargs):
#     if created:
#         qrcode = Website.objects.create(user=instance)

