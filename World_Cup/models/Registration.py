from django.db import models


class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    competition_category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def is_valid(self):
        pass
