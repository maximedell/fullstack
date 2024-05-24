from rest_framework import serializers

from .models import (
    Recipe,
    Ingredient,
    Category,
    NutritionalValue,
    Step,
    NutritionalValueGeneric,
)


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class NutritionalValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionalValue
        fields = "__all__"


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = "__all__"


class NutritionalValueGenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionalValueGeneric
        fields = "__all__"
