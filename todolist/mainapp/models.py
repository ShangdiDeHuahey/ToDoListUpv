from django.db import models

# Create your models here.
class Todo(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(blank=True)
    Deadline = models.DateTimeField(blank=False)
    Completed = models.BooleanField(default=False)
    Worker = models.TextField(blank=True)
    def __str__(self):
        return self.Title