from uuid import uuid4

from snaking.domain.entities import PythonSpecies, SnakeFamily, User
from snaking.domain.persistence.db_adapter import DbAdapter


class MemoryCacheDbAdapter(DbAdapter):
    def get_random_user(self) -> User:
        return User(
            id=uuid4(),
            name="Pretty Python",
            family=SnakeFamily.PYTHON,
            species=PythonSpecies.A_PAPUENSIS,
        )
