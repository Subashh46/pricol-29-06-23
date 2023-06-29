from django.db import models
from django.urls import reverse

# Create your models here.


class Machine(models.Model):
    name = models.CharField(max_length=50)
    manufacture_year = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Status(models.Model):
    working_choices = [('Yes', 'Yes'),
                       ('No', 'No')]
    machine = models.ForeignKey(Machine, on_delete=models.SET_NULL, null=True)
    is_working = models.CharField(max_length=3, choices=working_choices)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    document_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        time = str(self.time)[:19]
        name = "{}-{}".format(self.machine, time)
        return name

    def get_absolute_url(self):
        return reverse('home')


