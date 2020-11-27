from django.db import models

# Create your models here.


class cities(models.Model):
    cityname = models.CharField(max_length=50)

    def __str__(self):
        return self.cityname

    class Meta:
        verbose_name_plural = "cities1"
