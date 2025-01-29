from typing import Any, Generator, Union

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from snaking.app import create_app

Fixture = Union


@pytest.fixture
def app() -> Generator[FastAPI, Any, Any]:
    """App should only be initialized after mocking took place."""
    app = create_app()

    yield app


@pytest.fixture
def client(app: Fixture[FastAPI]) -> Generator[TestClient, Any, Any]:
    yield TestClient(app)
