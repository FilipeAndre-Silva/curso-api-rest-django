from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from enderecos.api.serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    # Sobrescrevendo a action de GET
    def list(self, request, *args, **kwargs):
        return Response({'Get': 'Personalizado'})

    # Sobrescrevendo a action de POST
    def create(self, request, *args, **kwargs):
        return super(EnderecoViewSet, self).create(request, *args, **kwargs)

    # Sobrescrevendo a action de DELETE
    def destroy(self, request, *args, **kwargs):
        return Response({'Delete Personalizado': request.data})

    # Sobrescrevendo a action de update, partial_update e retrieve
    def retrieve(self, request, *args, **kwargs):
        return Response({'Detail Personalizado': request.data})

    def update(self, request, *args, **kwargs):
        return Response({'Update Personalizado': request.data})

    def partial_update(self, request, *args, **kwargs):
        return Response({'Partial Update Personalizado': request.data})
