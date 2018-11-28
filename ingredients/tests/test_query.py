import pytest
from ingredients.schema import Query
from ingredients.models import Category
from graphql.execution.executors.asyncio import AsyncioExecutor

from graphene.types import Schema

@pytest.mark.asyncio
async def test_get_single_category():
  Category.objects.create(name="testCategory01")

  schema = Schema(Query)
  result = await schema.execute(
    """
    query {
    	category(id: 1) {
        name
      }
    }
    """,
    executor=AsyncioExecutor(),
    return_promise=True,
  )

  assert not result.errors
  assert result.data == {
    "category": {
      "name": "testCategory01"
    }
  }
