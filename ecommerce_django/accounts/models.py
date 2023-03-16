from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    name = models.CharField(
        max_length=200,
        null=True,
    )

    email = models.CharField(
        max_length=200,
        null=True,
    )

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, name=instance.username)
