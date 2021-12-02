# Aprovando e reprovando comentarios com Actions personalizadas
def reprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=False)

def aprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=True)

reprova_comentarios.short_description = 'Reprovar comentários'
aprova_comentarios.short_description = 'Aprovar aprova'
