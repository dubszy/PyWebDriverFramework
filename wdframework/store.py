from .exceptions import StoreException


class Store:

    def __init__(self):
        self.__internal_store = {}

    def get(self, key: str):
        if key is None or key is "":
            raise StoreException("Key cannot be None or empty")
        self.__internal_store.get(key)

    def put(self, key: str, item: object):
        if key is None or key is "":
            raise StoreException("Key cannot be None or empty")
        if item is None:
            raise StoreException("Item cannot be None")
        if self.get(key) is not None:
            raise StoreException("Key already set in this Store")
        self.__internal_store[key] = item

    # TODO: Add interpolation method
