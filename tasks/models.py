from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.tag


class Task(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        ordering = ["done", "-created_at"]
