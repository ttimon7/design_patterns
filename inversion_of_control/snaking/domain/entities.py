from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class Environment(Enum):
    """Viable environments."""

    LOCAL = "LOCAL"


class SnakeFamily(Enum):
    """Supported snake families."""

    PYTHON = "PYTHON"
    VIPER = "VIPER"


class SnakeSpecies(Enum): ...


class PythonSpecies(SnakeSpecies):
    """Supported Python species, mixed."""

    A_CHILDRENI = "A. childreni"
    A_MACULOSA = "A. maculosa"
    A_PAPUENSIS = "A. papuensis"
    A_PERTHENSIS = "A. perthensis"


class ViperSpecies(SnakeSpecies):
    A_BILINEATUS = "A. bilineatus"
    A_CONTORTRIX = "A. contortrix"
    A_LATICINCTUS = "A. laticinctus"
    A_PISCIVORUS = "A. piscivorus"
    A_CONANTI = "A. conanti"
    A_RUSSEOLUS = "A. russeolus"
    A_TAYLORI = "A. taylori"


class User(BaseModel):
    """Domain-level user model."""

    id: UUID
    name: str
    family: SnakeFamily
    species: SnakeSpecies
