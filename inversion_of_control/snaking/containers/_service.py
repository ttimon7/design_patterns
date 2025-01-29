from dependency_injector import containers, providers
from dotenv import load_dotenv

from snaking.infrastructure.persistence._memory_cache import MemoryCacheDbAdapter
from snaking.service.python_match_maker import PythonMatchMakerService

load_dotenv()


class ServiceDependencyContainer(containers.DeclarativeContainer):
    """Dependency container for other than the configs."""

    wiring_config = containers.WiringConfiguration(
        modules=[
            "snaking.controllers.routers._match_maker",
        ]
    )

    db_adapter = providers.Singleton(MemoryCacheDbAdapter)
    match_maker_service = providers.Singleton(PythonMatchMakerService, db_adapter=db_adapter)
