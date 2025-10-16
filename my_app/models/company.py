from django.db import models
from my_app.models.base_model import BaseModel

class Company(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=5, unique=True, null=True, blank=True)
    strength = models.IntegerField(default=0)
    website_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
