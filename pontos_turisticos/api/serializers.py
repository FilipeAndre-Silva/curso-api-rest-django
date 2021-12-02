from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from atracoes.models import Atracao
from enderecos.models import Endereco
from pontos_turisticos.models import PontoTuristico, DocIdentificacao
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer

# Relacionando objetos com objetos existentes via ID
class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):

    # Incrementando um objeto com NestedRelationships
    atracoes = AtracaoSerializer(many=True, read_only=True)
    endereco = EnderecoSerializer(read_only=True) # Usando o read_only=True o campo não vai ser obrigatório na criação do Ponto Turistico

    # Relacionando objetos com objetos existentes via ID
    doc_identificacao = DocIdentificacaoSerializer()

    # Incluindo informações adicionais com SerializerMethodField e properties
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            'id',
            'nome',
            'descricao',
            'foto',
            'atracoes',
            'comentarios',
            'avaliacoes',
            'endereco',
            'descricao_completa',
            'descricao_completa2',
            'doc_identificacao',
        )
        read_only_fields = ('comentarios', 'avaliacoes', ) # Usando o read_only=True em campos com relacionamento muitos para muitos

    # ManyToMany relationships
    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['entederco']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doc
        ponto.save()

        return ponto

    # Incluindo informações adicionais com SerializerMethodField e properties
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
