# -*- coding: utf-8 -*-
"""
    The Pygments reStructuredText directive
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This fragment is a Docutils_ 0.5 directive that renders source code
    (to HTML only, currently) via Pygments.

    To use it, adjust the options below and copy the code into a module
    that you import on initialization.  The code then automatically
    registers a ``sourcecode`` directive that you can use instead of
    normal code blocks like this::

        .. sourcecode:: python

            My code goes here.

    If you want to have different code styles, e.g. one with line numbers
    and one without, add formatters with their names in the VARIANTS dict
    below.  You can invoke them instead of the DEFAULT one by using a
    directive option::

        .. sourcecode:: python
            :linenos:

            My code goes here.

    Look at the `directive documentation`_ to get all the gory details.

    .. _Docutils: http://docutils.sf.net/
    .. _directive documentation:
       http://docutils.sourceforge.net/docs/howto/rst-directives.html

    :copyright: Copyright 2006-2015 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from docutils import nodes
from docutils.parsers.rst import directives, Directive

from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer

from pygments.formatters import HtmlFormatter


class Pygments(Directive):
    """ Source code syntax hightlighting.
    """
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        try:
            if self.arguments[1] == 'linenos':
                linenos = 'table'
            else:
                linenos = False
        except IndexError as exc:
            linenos = False

        try:
            lexer = get_lexer_by_name(self.arguments[0])
        except ValueError:
            # no lexer found - use the text one instead of an exception
            lexer = TextLexer()

        formatter = HtmlFormatter(
            noclasses = False,
            cssclass = 'codehilite',
            linenos = linenos,
            linenospecial = 5,
            lineanchors = 'lineno',
            anchorlinenos = True
        )

        # parse the code, which shall be highlighted
        parsed = highlight(u'\n'.join(self.content), lexer, formatter)

        return [nodes.raw('', parsed, format='html')]

directives.register_directive('sourcecode', Pygments)

