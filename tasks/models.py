from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ("is_done", "created_at",)
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return f"{self.content} ({self.is_done})"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return self.name
