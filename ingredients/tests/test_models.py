import pytest


from ingredients.models import Category, Ingredient

"""
pytestにDBアクセスさせるにはこの設定が必要
"""
pytestmark = pytest.mark.django_db

class TestCategoryModel:


  def test_category_save(self):
    category = Category.objects.create(name="Category01")

    saved_category = Category.objects.get(pk=category.id)
    assert saved_category.name == "Category01"

class TestIngredientModel:

  def test_ingredient_save(self):
    category = Category.objects.create(name="Category01")
    ingredient = Ingredient.objects.create(
      name="Ingredient01",
      notes="TestNotes",
      category=category
    )

    saved_ingredient = Ingredient.objects.get(pk=ingredient.id)
    assert saved_ingredient.name == "Ingredient01"