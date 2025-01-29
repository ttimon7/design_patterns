from snaking.controllers.routers._match_maker import get_match_maker_router
from snaking.infrastructure import ApiRouter


def get_routers() -> tuple[ApiRouter, ...]:
    return (get_match_maker_router(),)
