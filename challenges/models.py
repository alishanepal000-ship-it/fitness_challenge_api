from django.db import models
from django.conf import settings


# Create your models here.
class Challenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    goal = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)

    start_date = models.DateField()
    end_date = models.DateField()

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="challenges",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title