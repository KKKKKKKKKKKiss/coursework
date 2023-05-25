from django.db import models


class Comp (models.Model):

    name = models.CharField(max_length=15, verbose_name="Номер предмета")

    class Meta:
        verbose_name = "Номер предмета"
        verbose_name_plural = "Номер предмета"

    def __str__(self):
        return self.name