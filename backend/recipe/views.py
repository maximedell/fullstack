from rest_framework import viewsets
from .models import Ingredient, Recipe, NutritionalValueGeneric, Step, NutritionalValue
from rest_framework.response import Response
from rest_framework.decorators import action
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

    @action(detail=False, methods=["get"])
    def empty(self, request):
        # Obtenez une instance vide de l'objet
        instance = self.get_queryset().model()
        # Obtenez le serializer
        serializer = self.get_serializer(instance)
        # Créez un nouvel objet pour stocker les informations du formulaire
        form_info = {}
        for field_name, field_value in serializer.data.items():
            # Obtenez le type de champ
            field_type = type(instance._meta.get_field(field_name)).__name__
            # Si le champ est un ChoiceField, obtenez les options de choix
            choices = (
                instance._meta.get_field(field_name).choices
                if hasattr(instance._meta.get_field(field_name), "choices")
                else None
            )
            if field_type == "ForeignKey":
                choices = [
                    {"value": choice.pk, "display_name": str(choice)}
                    for choice in instance._meta.get_field(
                        field_name
                    ).related_model.objects.all()
                ]
            # Obtenez le verbose_name du champ
            verbose_name = instance._meta.get_field(field_name).verbose_name
            # Ajoutez les informations du champ au form_info
            if verbose_name == "ID":
                continue
            form_info[field_name] = {
                "type": field_type,
                "choices": choices,
                "value": field_value,
                "verbose_name": verbose_name,
            }
        return Response(form_info)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    @action(detail=False, methods=["get"])
    def empty(self, request):
        # Obtenez une instance vide de l'objet
        instance = self.get_queryset().model()
        # Obtenez le serializer
        serializer = self.get_serializer(instance)
        # Créez un nouvel objet pour stocker les informations du formulaire
        form_info = {}
        for field_name, field_value in serializer.data.items():
            # Obtenez le type de champ
            field_type = type(instance._meta.get_field(field_name)).__name__
            # Si le champ est un ChoiceField, obtenez les options de choix
            choices = (
                instance._meta.get_field(field_name).choices
                if hasattr(instance._meta.get_field(field_name), "choices")
                else None
            )
            if field_type == "ForeignKey":
                choices = [
                    {"value": choice.pk, "display_name": str(choice)}
                    for choice in instance._meta.get_field(
                        field_name
                    ).related_model.objects.all()
                ]
            # Obtenez le verbose_name du champ
            verbose_name = instance._meta.get_field(field_name).verbose_name
            # Ajoutez les informations du champ au form_info
            if verbose_name == "ID":
                continue
            form_info[field_name] = {
                "type": field_type,
                "choices": choices,
                "value": field_value,
                "verbose_name": verbose_name,
            }
        return Response(form_info)


class NutritionalValueGenericViewSet(viewsets.ModelViewSet):
    queryset = NutritionalValueGeneric.objects.all()
    serializer_class = NutritionalValueGenericSerializer

    @action(detail=False, methods=["get"])
    def empty(self, request):
        serializer = self.get_serializer()
        return Response(serializer.data)


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

    @action(detail=False, methods=["get"])
    def empty(self, request):
        serializer = self.get_serializer()
        return Response(serializer.data)


class NutritionalValueViewSet(viewsets.ModelViewSet):
    queryset = NutritionalValue.objects.all()
    serializer_class = NutritionalValueSerializer

    @action(detail=False, methods=["get"])
    def empty(self, request):
        serializer = self.get_serializer()
        return Response(serializer.data)
