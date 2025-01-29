from uuid import UUID

from pydantic import BaseModel

from snaking.domain.entities import PythonSpecies, SnakeFamily


class UserDto(BaseModel):
    id: UUID
    name: str
    family: SnakeFamily
    species: PythonSpecies
