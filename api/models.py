import binascii
from os import urandom

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth.models import User


class AuthToken(models.Model):

    key = models.CharField("Key", max_length=40, primary_key=True)
    user = models.OneToOneField(
        User, related_name='Authtoken',
        on_delete=models.CASCADE, verbose_name="Users"
    )
    created = models.DateTimeField("Created", auto_now_add=True)

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(AuthToken, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(urandom(20)).decode()

    def __str__(self):
        return self.key


@receiver(post_save, sender=User)
def save_user_identification(instance, created, **kwargs):
    if created:
        AuthToken.objects.create(user=instance)

