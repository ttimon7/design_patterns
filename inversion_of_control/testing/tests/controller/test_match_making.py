import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from testing.conftest import Fixture
from testing.tests.controller.mockeries.conftest import setup_service_with_test_families
from testing.tests.controller.mockeries.consts import TEST_SNAKE_FAMILIES


@pytest.mark.asyncio
async def test_only_configured_families_are_returned(app: Fixture[FastAPI], client: Fixture[TestClient]) -> None:
    with setup_service_with_test_families(app=app):
        response = client.get("http://localhost:8000/match/families")

        families = set(response.json())

        assert {family.name for family in TEST_SNAKE_FAMILIES.keys()} == families
