from uuid import UUID

from snaking.domain.entities import User
from snaking.domain.persistence.db_adapter import DbAdapter
from snaking.domain.service.match_maker import MatchMakerService


class PythonMatchMakerService(MatchMakerService):
    """Python-specific match maker implementation."""

    def __init__(self, db_adapter: DbAdapter) -> None:
        self.db_adapter = db_adapter

    def get_random_match(self, user_id: UUID) -> User:  # noqa: ARG002
        return self.db_adapter.get_random_user()
