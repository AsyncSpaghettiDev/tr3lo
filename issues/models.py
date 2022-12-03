from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Issue(models.Model):
    summary = models.CharField(max_length=128)
    description = models.TextField()
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        default=1,
    )
    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,
    )

    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='reporter',
    )

    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='assignee',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
