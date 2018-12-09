from .loadable import Loadable
from wdframework.exceptions import ComponentException
from wdframework.selector import Selector


class Component(Loadable):
    """
    Base component object class that all component objects should extend.
    """

    def __init__(self, owner: Loadable, container: Selector):
        super().__init__(owner.get_session())

        if container is None:
            raise ComponentException("Container for a component cannot be None")

        if container.get_locator() is None or "":
            raise ComponentException("Container's locator for a component"
                                     "cannot be None or empty")

        self._owner = owner
        self._container = container
