from django.db import models

class Paradigm(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)
    creator = models.CharField(max_length=200)
    created_at = models.DateField()
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name