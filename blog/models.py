from django.db import models

class blog(models.Model):
    Nama = models.CharField(max_length=255)
    Email = models.EmailField(max_length=50)
    Pesan = models.TextField()

    def __str__(self):
        return self.Nama
