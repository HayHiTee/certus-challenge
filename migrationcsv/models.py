from django.db import models
from django.utils import timezone
import datetime


class Findings(models.Model):
    finding_name = models.CharField(max_length=200)
    description = models.TextField()
    solution = models.TextField()
    author = models.TextField(default="Swapnil Deshmukh")
    date_last_edited = models.DateField(default=timezone.now().date())
    website = models.URLField(default='')
    reviwed_by = models.TextField(default="Swapnil Deshmukh")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.date_last_edited = timezone.now().date()
        super().save(force_insert, force_update, using,
                     update_fields)


class CvssScore(models.Model):
    NETWORK = 'N'
    ADJACENT = 'A'
    LOCAL = 'L'
    PHYSICAL = 'P'
    ATTACK_VECTOR_CHOICES = [
        (NETWORK, 'Network'),
        (ADJACENT, 'Adjacent'),
        (PHYSICAL, 'Physical'),
        (LOCAL, 'Local'),
    ]

    NONE = 'N'
    LOW = 'L'
    HIGH = 'H'

    OTHER_CHOICES = [
        (NONE, 'None'),
        (LOW, 'Low'),
        (HIGH, 'High'),
    ]

    overall_base_score = models.CharField(max_length=200)
    attack_vector = models.CharField(max_length=1, choices=ATTACK_VECTOR_CHOICES, default=NETWORK)
    scope = models.BooleanField()
    attack_complexity = models.BooleanField()
    confidentiality = models.CharField(max_length=1, choices=OTHER_CHOICES, default=NONE)
    integrity = models.CharField(max_length=1, choices=OTHER_CHOICES, default=NONE)
    avaiability = models.CharField(max_length=1, choices=OTHER_CHOICES, default=NONE)
    privileges_required = models.CharField(max_length=1, choices=OTHER_CHOICES, default=NONE)
    user_instaction = models.BooleanField()
