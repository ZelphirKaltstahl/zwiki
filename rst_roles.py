from docutils import nodes
from docutils.parsers.rst import roles, CustomRole


def wiki_internal_links_role(
    role,
    rawtext,
    text,
    lineno,
    inliner,
    options={},
    content=[]
):
    # try to find the wiki page by using a function from the file reader
    ## imported the file reader
    ## check for wiki page
    ## if it exists
    ### create a link element
    ### return the node and empty list for error messages
    # except the file does not exist, then return an error
    ## inliner.reporter.error(TEXT OF THE ERROR MESSAGE)
    ## return a tuple of no nodes and an error message
    try:
        rfcnum = int(text)
        if rfcnum <= 0:
            raise ValueError
    except ValueError:
        msg = inliner.reporter.error(
            'RFC number must be a number greater than or equal to 1; '
            '"%s" is invalid.' % text, line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]
    # Base URL mainly used by inliner.rfc_reference, so this is correct:
    ref = inliner.document.settings.rfc_base_url + inliner.rfc_url % rfcnum
    set_classes(options)
    node = nodes.reference(rawtext, 'RFC ' + utils.unescape(text), refuri=ref,
                           **options)
    return [node], []



def wiki_internal_links(
    name,
    rawtext,
    text,
    lineno,
    inliner,
    options={},
    content=[]
):
    print('the content of variable text is:', text)
    return_tuple = (

    )

# Set function attributes for customization:
WIKI_INTERNAL_LINKS_ROLE_NAME = 'wikilink'

wiki_internal_links.name = WIKI_INTERNAL_LINKS_ROLE_NAME
# wiki_internal_links.options = {
#     {'class': directives.class_option}'class': 'wiki-internal-link',
#     'pages_directory': 'static/rst/'
# }
# wiki_internal_links.content = []

roles.register_canonical_role(name, wiki_internal_links)
