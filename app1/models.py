from django.db import models


class Maqola(models.Model):
    sarlavha = models.CharField(max_length=80)
    sana = models.DateField()
    mavzu = models.CharField(max_length=80)
    matn = models.TextField()
    muallif = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.sarlavha} ({self.muallif})"

