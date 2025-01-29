from snaking.domain.entities import User


class DbAdapter:
    def get_random_user(self) -> User:
        raise NotImplementedError
