from uuid import UUID

from dependency_injector.wiring import Provide, inject

from snaking.app_config import ServiceConfiguration
from snaking.containers import ConfigDependencyContainer, ServiceDependencyContainer
from snaking.controllers._dtos import UserDto
from snaking.controllers._mappers import map_user_domain_to_dto
from snaking.domain.entities import SnakeFamily
from snaking.domain.service.match_maker import MatchMakerService
from snaking.infrastructure import ApiRouter


def get_prefix() -> str:
    return "/match"


@inject
def get_match_maker_router(
    # This method must be parameterized by the provider, because the closure it
    # creates prevents dependency injection of encapsulated methods.
    config: ServiceConfiguration = Provide[ConfigDependencyContainer.service_config],
    match_maker_service: MatchMakerService = Provide[ServiceDependencyContainer.match_maker_service],
) -> ApiRouter:
    """Return a router instance configured with endpoints."""
    router = ApiRouter(prefix=get_prefix())

    @router.get("/families", status_code=200)
    async def get_supported_families() -> set[SnakeFamily]:
        """Only these snake families can register."""
        return set(config.match_maker.supported_species.keys())

    @router.get("/mystery", status_code=200)
    async def get_random_match(user_id: UUID) -> UserDto:
        """Return mystery match."""
        user = match_maker_service.get_random_match(user_id=user_id)

        return map_user_domain_to_dto(user=user)

    return router
