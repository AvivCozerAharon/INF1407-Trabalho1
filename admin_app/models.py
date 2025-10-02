from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = CKEditor5Field(config_name="extends", null=True, blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem_capa = models.ImageField(upload_to='imagens_capa/', blank=True, null=True)
    autor_id = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.titulo
