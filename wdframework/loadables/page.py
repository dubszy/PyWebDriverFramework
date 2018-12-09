from .loadable import Loadable
from wdframework.session import Session


class Page(Loadable):
    """
    Base page object class that all page objects should extend.
    """
    def __init__(self, session: Session):
        super().__init__(session)

    def get_comments(self):
        """
        Get all HTML comments on the current page. This is outside of the normal
        flow of Selector because there is no selector for comments.

        The JavaScript in this method is equivalent to:

        var getComments = function(element) {
          var comments = [];
          var nodes = element.childNodes;
          for (var i = 0; i < nodes.length; i++) {
            var node = nodes[i];
            if (node.nodeType === 8) {
              comments.push(node);
            } else {
              comments.push.apply(comments, getComments(node));
            }
          }
          return comments;
        };

        var comments = getComments(document);

        :return: The HTML comments on the current page as a JS object
        """
        return self._session.get_driver_env()\
            .execute_js(False, "let g=function(e){let c=[];let s=e.childNodes;"
                               "for(let i=0;i<s.length;i++){let n=s[i];"
                               "if(n.nodeType===8){c.push(n);}"
                               "else{c.push.apply(c,g(n));}}return c;};"
                               "let c=g(document);")
