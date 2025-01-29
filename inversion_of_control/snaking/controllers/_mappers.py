from snaking.controllers._dtos import UserDto
from snaking.domain.entities import User


def map_user_domain_to_dto(user: User) -> UserDto:
    return UserDto(**user.model_dump())
