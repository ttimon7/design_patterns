from abc import ABC
from uuid import UUID

from snaking.domain.entities import User


class MatchMakerService(ABC):
    """Interface definition for implementing match making services."""

    def get_random_match(self, user_id: UUID) -> User:
        raise NotImplementedError
