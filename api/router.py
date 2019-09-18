from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)

router.register('games', views.GameViewSet)
router.register('teams', views.TeamViewSet)
router.register('players', views.PlayerViewSet)
router.register('game_players', views.GamePlayerViewSet)
router.register('product_types', views.ProductTypeViewSet)
router.register('products', views.ProductViewSet)
router.register('player_products', views.PlayerProductViewSet)
