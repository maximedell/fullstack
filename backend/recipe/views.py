from rest_framework import viewsets
from .models import Ingredient, Recipe, NutritionalValueGeneric, Step, NutritionalValue
from .serializers import (
    IngredientSerializer,
    RecipeSerializer,
    NutritionalValueGenericSerializer,
    StepSerializer,
    NutritionalValueSerializer,
)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class NutritionalValueGenericViewSet(viewsets.ModelViewSet):
    queryset = NutritionalValueGeneric.objects.all()
    serializer_class = NutritionalValueGenericSerializer


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class NutritionalValueViewSet(viewsets.ModelViewSet):
    queryset = NutritionalValue.objects.all()
    serializer_class = NutritionalValueSerializer
