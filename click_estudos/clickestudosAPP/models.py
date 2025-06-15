from django.db import models
from django.contrib.auth.models import User

class Material(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    arquivo = models.FileField(upload_to='materiais/')
    data_envio = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo