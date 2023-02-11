from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Specialist(models.Model):
    """Specialist model."""
    specialist = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Имя специалиста'
    )