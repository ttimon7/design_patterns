from snaking.app_config import ApiServiceConfig, MatchMakerConfig, ServiceConfiguration
from snaking.domain.entities import Environment, SnakeFamily, SnakeSpecies
from testing.tests.controller.mockeries.consts import TEST_SNAKE_FAMILIES


class MockedMatchMakerConfig(MatchMakerConfig):
    supported_species: dict[SnakeFamily, set[SnakeSpecies]] = TEST_SNAKE_FAMILIES


class MockedServiceConfiguration(ServiceConfiguration):
    environment: Environment = Environment.LOCAL
    api: ApiServiceConfig = ApiServiceConfig()
    match_maker: MatchMakerConfig = MockedMatchMakerConfig()
