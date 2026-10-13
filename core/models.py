from django.db import models
from django.contrib.auth.models import User

class Salary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    month = models.CharField(max_length=20)  # Eg: Jan 2026
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.month} - {self.amount}"

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Rent', 'Rent'),
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Shopping', 'Shopping'),
        ('Other', 'Other'),
    ]
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE, related_name='expenses')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.amount}"

class Saving(models.Model):
    salary = models.OneToOneField(Salary, on_delete=models.CASCADE)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    saved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Saved: {self.saved_amount}"
