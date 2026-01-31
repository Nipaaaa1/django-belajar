from django.db import models


class Person(models.Model):
    name = models.CharField()
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.age}"

class PriorityChoices(models.IntegerChoices):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Todo(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=200)
    done = models.BooleanField()
    datetime = models.DateField(null=True, blank=True)
    priority = models.IntegerField(choices=PriorityChoices.choices)

    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="todos", blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.title}"
