from rest_framework import viewsets

from . import models, serializers


class GameViewSet(viewsets.ModelViewSet):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer


class GamePlayerViewSet(viewsets.ModelViewSet):
    queryset = models.GamePlayer.objects.all()
    serializer_class = serializers.GamePlayerSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ProductType.objects.all()
    serializer_class = serializers.ProductTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class PlayerProductViewSet(viewsets.ModelViewSet):
    queryset = models.PlayerProduct.objects.all()
    serializer_class = serializers.PlayerProductSerializer

