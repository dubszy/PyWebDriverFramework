from wdframework.session import Session


class Loadable(object):
    """
    Base class that all loadable objects (pages, components, etc) should extend.

    The page object setup of this framework is split into two sections: page
    objects and components. Page objects should represent entire pages (or
    sub-pages of a parent page). Components should represent reusable components
    defined throughout a website or a web application (such as page-level -- not
    browser -- overlays or containers that encapsulate the same fields used in
    multiple places).
    """
    def __init__(self, session: Session):
        self._session = session

    def get_session(self):
        """
        Get the Session associated with this loadable.
        :return:
        """
        return self._session
