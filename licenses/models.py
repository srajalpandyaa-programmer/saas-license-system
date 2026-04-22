from django.db import models
from users.models import User

class License(models.Model):
    key = models.CharField(max_length=100, unique=True)
    product_name = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    expiry_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product_name} - {self.key}"
