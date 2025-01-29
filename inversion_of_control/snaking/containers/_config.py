from dependency_injector import containers, providers
from dotenv import load_dotenv

from snaking.app_config import ServiceConfiguration

load_dotenv()


class ConfigDependencyContainer(containers.DeclarativeContainer):
    """Portal Service dependency container."""

    wiring_config = containers.WiringConfiguration(
        modules=[
            "snaking.app",
            "snaking.controllers.routers._match_maker",
        ]
    )

    service_config = providers.Singleton(ServiceConfiguration)
