from django.db import models


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=200, unique=True, blank=False, null=False, help_text="Game's name")
    short_name = models.CharField(max_length=200, unique=True, blank=True, null=True, help_text="Game's short name")

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False, help_text="Team's name")

    def __str__(self):
        return self.name


class Player(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    alias = models.CharField(max_length=200, unique=True, blank=False, null=False, help_text="Player's alias")
    image = models.CharField(max_length=200, help_text="URL for the player's image")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, help_text="Player's team")

    def __str__(self):
        return self.alias


class GamePlayer(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.game} - {self.player}"


class ProductType(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False, help_text="Type of product")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False, help_text="Product's name")
    amazon = models.CharField(max_length=200, unique=True, blank=False, null=False, help_text="Amazon URL for product")
    image = models.CharField(max_length=200, unique=True, blank=False, null=False, help_text="URL for product image")
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PlayerProduct(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player} - {self.product.type.name}"
