from django.contrib import admin

from .models import (FavoriteRecipe, Ingredient, IngredientsInRecipes, Recipe,
                     RecipesTags, Tag)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "slug",
        "name",
        "color",
    )
    list_display_links = (
        "pk",
        "slug",
    )
    list_editable = ("name",)
    search_fields = (
        "slug",
        "name",
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "measurement_unit")
    list_display_links = (
        "pk",
        "name",
    )
    list_editable = ("measurement_unit",)
    search_fields = ("name",)
    

class IngredientInRecipeInline(admin.TabularInline):
    model = IngredientsInRecipes
    raw_id_fields = ("recipe",)
    min_num = 1
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientInRecipeInline,
    ]
    search_fields = (
        "author",
        "name",
    )


@admin.register(FavoriteRecipe)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "recipe",
        "shopping_cart",
        "favorite",
    )


@admin.register(RecipesTags)
class RecipesTags(admin.ModelAdmin):
    autocomplete_fields = (
        "recipe",
        "tag",
    )
    search_fields = (
        "recipe__name",
        "tag__name",
    )
