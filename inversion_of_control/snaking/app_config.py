from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from snaking.domain.entities import Environment, PythonSpecies, SnakeFamily


class BaseConfiguration(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="",  # Environment variable prefix to load.
        case_sensitive=False,
        env_nested_delimiter="__",
        env_file=".env",
        env_file_encoding="utf-8",
    )


class ApiServiceConfig(BaseConfiguration):
    allow_origins: set[str] = {"http://localhost:3000"}
    allow_methods: set[str] = {"GET"}
    allow_headers: set[str] = {"*"}


class MatchMakerConfig(BaseConfiguration):
    supported_species: dict[SnakeFamily, set[PythonSpecies]] = Field(default_factory=dict)


class ServiceConfiguration(BaseConfiguration):
    environment: Environment = Environment.LOCAL
    api: ApiServiceConfig = ApiServiceConfig()
    match_maker: MatchMakerConfig = MatchMakerConfig()
