from django.db import models
from django.urls import reverse

# Create your models here.


class TodoModel(models.Model):
    text = models.CharField(max_length=400)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("todo_detail", kwargs={"pk": self.pk})
