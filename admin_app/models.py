from django.db import models

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem_capa = models.ImageField(upload_to='media/imagens_capa/', blank=True, null=True)

    def __str__(self):
        return self.titulo
