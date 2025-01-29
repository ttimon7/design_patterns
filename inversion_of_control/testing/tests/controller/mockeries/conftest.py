from contextlib import contextmanager
from typing import Any

from fastapi import FastAPI

from snaking.app import config_container, init_app
from testing.tests.controller.mockeries._config import MockedServiceConfiguration  # type: ignore


@contextmanager
def setup_service_with_test_families(app: FastAPI) -> Any:
    with config_container.service_config.override(MockedServiceConfiguration()):
        init_app(app=app)  # the mocked service config has been injected, app can safely be initialized

        yield

        config_container.unwire()
