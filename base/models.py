from django.db import models

# Create your models here.

class Divina_Pagina(models.Model):
    desc = models.CharField(max_length=200000)
    slug = models.CharField(max_length=123)
    doc = models.FileField(null=True,upload_to="divina-pagina-inicio")
    
