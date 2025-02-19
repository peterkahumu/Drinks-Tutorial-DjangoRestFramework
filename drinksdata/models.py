from django.db import models

# Create your models here.
class Drinks(models.Model):
    name = models.CharField(max_length=200)
    flavour = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " Flavour: " + self.flavour

    class Meta:
        verbose_name_plural = "Drinks"