from abc import ABC, abstractmethod
from typing import Optional


class AliasRepository(ABC):
    @abstractmethod
    def get_by_alias(self, alias: str) -> Optional[str]:
        pass

    @abstractmethod
    def add(self, alias: str, long_url: str) -> None:
        pass

    # TODO: Se volete implementate il metodo delete e update

    # @abstractmethod
    # def delete(self, alias: str) -> None:
    #     pass

    # @abstractmethod
    # def update(self, alias: str, long_url: str) -> None:
    #     pass
