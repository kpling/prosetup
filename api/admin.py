from django.contrib import admin

from . import models

admin.site.register(models.Game)
admin.site.register(models.Team)
admin.site.register(models.Player)
admin.site.register(models.GamePlayer)
admin.site.register(models.ProductType)
admin.site.register(models.Product)
admin.site.register(models.PlayerProduct)
