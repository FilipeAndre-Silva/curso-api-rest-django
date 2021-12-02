from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer

    # Utilizando DjangoFilter backend
    # filter_backends = (DjangoFilterBackend,) Caso queria remover o filtro global e usar em uma view especifica
    filter_fields = ('nome', 'descricao')
