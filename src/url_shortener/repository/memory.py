from .base import AliasRepository

urls_mapping = {}


class InMemory(AliasRepository):
    def get_by_alias(self, alias):
        return urls_mapping.get(alias, None)

    def add(self, alias, long_url):
        urls_mapping[alias] = long_url
