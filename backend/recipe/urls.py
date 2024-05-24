from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    IngredientViewSet,
    RecipeViewSet,
    NutritionalValueGenericViewSet,
    StepViewSet,
    NutritionalValueViewSet,
)

router = DefaultRouter()
router.register(r"ingredients", IngredientViewSet)
router.register(r"recipes", RecipeViewSet)
router.register(r"nutritionalvaluegenerics", NutritionalValueGenericViewSet)
router.register(r"steps", StepViewSet)
router.register(r"nutritionalvalues", NutritionalValueViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
