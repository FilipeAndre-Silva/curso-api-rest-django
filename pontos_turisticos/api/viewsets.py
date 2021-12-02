from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import PontoTuristico
from pontos_turisticos.api.serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    # Entendendo o mecanismo de autorização
    authentication_classes = (TokenAuthentication, )

    # Autorizando via sistema de permissões do Django
    permission_classes = (DjangoModelPermissions, )

    # Utilizando o SearchFilter
    filter_backends = (SearchFilter, )
    search_fields = ('nome', 'descricao', 'endereco__linha1') # http://127.0.0.1:8000/pontosturisticos/?search=teste

    # Implementando get_queryset
    """def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)"""

    # Alterando o lookup_field padrão do endpoint
    #lookup_field = 'nome'

    # Filtrando por query string
    def get_queryset(self):
        # http://127.0.0.1:8000/pontosturisticos/?id=2&nome=Ponto%202&descricao=teste
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()

        if id:
            queryset = queryset.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome) # Ignora o case sensitive da busca pelo nome
        if descricao:
            queryset = queryset.filter(descricao=descricao)

        return queryset

    # Implementando suas próprias actions personalizadas
    # http://127.0.0.1:8000/pontosturisticos/1/denunciar/
    @action(methods=['get', 'post'], detail=True)
    def denunciar(self, request, pk=None):
        return Response({'Actions Personalizadas': request.data})

    # http://127.0.0.1:8000/pontosturisticos/teste/
    @action(methods=['get'], detail=False)
    def teste(self, request, pk=None):
        return Response({'Actions Personalizadas': request.data})

    # Relacionando objetos com objetos existentes via Action
    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=id)
        ponto.atracoes.set(atracoes)
        ponto.save()
        return HttpResponse('ok')
