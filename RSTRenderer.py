from docutils.core import publish_parts
import rst_directive

class RSTRenderer():
    """The RSTRenderer uses docutils to render reStructuredText content."""

    def __init__(self):
        super().__init__()

    def render_string(self, astring):
        astring = '.. sectnum::\n\n' + astring
        # astring = '.. contents:: Table of Contents\n\n' + astring

        return publish_parts(astring, writer_name='html')['html_body']


