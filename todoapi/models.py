from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Q

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=False, null=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=256)
    created_on = models.DateField(auto_now_add=True, blank=True, null=False)
    due_date = models.DateField(blank = False,null=False)

    check_choices = (
        ('Done','Done'),
        ('Not Done','Not Done'),
    )

    completed = models.CharField(max_length=10, choices = check_choices, default='Not Done')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_on"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(created_on__lte=F('due_date')),
                name='correct_datetime'
            ),
        ]

    def __str__(self):
        return self.title + ", created by: " + self.user.username