from django.db import models

# Create your models here.
class HslSertifikat(models.Model):
    file=models.FileField(upload_to="zips/")
    def __str__(self):
        return str(self.file)