from django.db import models

class TimetableEntry(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly define primary key field
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    time = models.CharField(max_length=20)
    yoga_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.day} - {self.time}: {self.yoga_type}"