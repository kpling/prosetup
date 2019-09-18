from rest_framework import serializers

from . import models


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Game
        fields = '__all__'


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Team
        fields = '__all__'


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Player
        fields = '__all__'


class GamePlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.GamePlayer
        fields = '__all__'


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ProductType
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class PlayerProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PlayerProduct
        fields = '__all__'
