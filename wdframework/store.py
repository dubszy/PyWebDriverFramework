from .exceptions import StoreException


class Store:
    """
    Base class for storing data from test runs (or storing data to pass to tests). It is recommended that you subclass
    this to fit your needs.
    """
    def __init__(self):
        self.__internal_store = {}

    def get(self, key: str):
        """
        Get a value from this Store.

        :param key: The key for the value to get

        :return: The value identified by the key

        :exception StoreException: If the key is None or empty
        """
        if key is None or key is "":
            raise StoreException("Key cannot be None or empty")
        return self.__internal_store.get(key)

    def put(self, key: str, item: object):
        """
        Put a key-value pair in this Store (if the key isn't already set).

        :param key: The key
        :param item: The value

        :exception StoreException: If the key is None or empty, the item is None, or the key is already set in this
        store
        """
        if key is None or key is "":
            raise StoreException("Key cannot be None or empty")
        if item is None:
            raise StoreException("Item cannot be None")
        if self.get(key) is not None:
            raise StoreException("Key already set in this Store")
        self.__internal_store[key] = item

    # TODO: Add interpolation method
