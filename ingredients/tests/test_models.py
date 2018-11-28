import pytest


from ingredients.models import Category

"""
pytestにDBアクセスさせるにはこの設定が必要
"""
pytestmark = pytest.mark.django_db

class TestCategoryModel:

  def test_category_save(self):
    category = Category.objects.create(name="Category01")

    saved_category = Category.objects.get(pk=category.id)
    assert saved_category.name == "Category01"