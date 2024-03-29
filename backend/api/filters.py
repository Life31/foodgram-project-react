import django_filters
from django_filters.rest_framework import filters
from rest_framework.filters import SearchFilter

from recipes.models import Recipe, Tag
from users.models import User


class IngredientSearchFilter(SearchFilter):
    search_param = 'name'


class RecipeFilter(django_filters.FilterSet):
    author = filters.ModelChoiceFilter(
        to_field_name="id", queryset=User.objects.all()
    )
    tags = filters.ModelMultipleChoiceFilter(
        field_name="tags__slug",
        to_field_name="slug",
        queryset=Tag.objects.all(),
    )
    is_favorited = filters.BooleanFilter(
        field_name="favorite__favorite",
        method="filter_favorite_or_shopping_cart",
    )
    is_in_shopping_cart = filters.BooleanFilter(
        field_name="favorite__shopping_cart",
        method="filter_favorite_or_shopping_cart",
    )

    class Meta:
        model = Recipe
        fields = ["author", "tags", "is_favorited", "is_in_shopping_cart"]

    def filter_favorite_or_shopping_cart(self, queryset, name, value):
        if value:
            return queryset.filter(
                favorite__user=self.request.user, **{name: value}
            ).all()

        return queryset.exclude(
            favorite__user=self.request.user, **{name: True}
        ).all()
