from django.db import models
import uuid

class Employee(models.Model):
    id_number = models.CharField(max_length=20, unique=True, editable=False)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        if not self.id_number:
            self.id_number = str(uuid.uuid4())[:8].upper()  # short UUID
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
