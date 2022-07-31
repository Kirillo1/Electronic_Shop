from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name="profile",
                                verbose_name="Профиль", on_delete=models.CASCADE)
    addi_info = models.TextField(max_length=3000, verbose_name="Дополнительная информация", null=True, blank=True)


class Meta:
    verbose_name = "Profile"
    verbose_name_plural = "Profiles"


def __str__(self) -> str:
    return f"Profile: {self.user.username}. {self.id}"

