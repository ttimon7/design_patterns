from dependency_injector.wiring import Provide, inject
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from snaking.app_config import ServiceConfiguration
from snaking.containers import ConfigDependencyContainer, ServiceDependencyContainer
from snaking.controllers import get_routers

config_container = ConfigDependencyContainer()
service_container = ServiceDependencyContainer()


def _set_routers(app: FastAPI) -> None:
    for router in get_routers():
        app.include_router(router)


@inject
def _add_middlewares(
    app: FastAPI,
    config: ServiceConfiguration = Provide[ConfigDependencyContainer.service_config],
) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.api.allow_origins,
        allow_methods=config.api.allow_methods,
        allow_headers=config.api.allow_headers,
    )


def init_app(app: FastAPI) -> None:
    # TODO investigate why manual wiring is required here
    config_container.wire(modules=[__name__])
    _set_routers(app=app)
    _add_middlewares(app=app)


def create_app() -> FastAPI:
    return FastAPI()


app = create_app()
init_app(app=app)
