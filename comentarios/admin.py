from django.contrib import admin
from .models import Comentario
from .actions import reprova_comentarios, aprova_comentarios

# Aprovando e reprovando comentarios com Actions personalizadas
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'aprovado']
    actions = [reprova_comentarios, aprova_comentarios]


admin.site.register(Comentario, ComentarioAdmin)
