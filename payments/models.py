from django.db import models
from users.models import User

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    invoice_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Invoice {self.invoice_id} - {self.user.username}"
