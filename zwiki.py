# python imports
import os

# library imports
from flask import Flask, render_template, url_for, send_from_directory

# project imports
import WikiProcessor

# some definitions
app = Flask(
    __name__,
    template_folder='templates',
    static_url_path='/static'
)
app.debug = True
app.config['IMAGE_FOLDER'] = '/static/img/'

base_dir = os.path.abspath(os.path.dirname(__file__)) + '/'
wiki = WikiProcessor.WikiProcessor(base_dir)

##########
# Routes #
##########
@app.route('/')
@app.route('/index')
def index():
    return wiki.get_index_page()

@app.route('/page/<page>')
def page(page):
    rendered_page = wiki.get_page_by_name(page)
    return rendered_page

# route for images requested by client when visiting wiki pages
# @app.route('/img/<image_path>', methods=['GET'])
# def send_image(image_path):
#     print('trying to image')
#     image_path_in_static = 'img/' + image_path
#     complete_url = url_for('static', filename=image_path_in_static)
#     print(image_path_in_static)
#     print(complete_url)
#     return '<img src="' + complete_url + '" alt="' + complete_url + '">'

#@app.route('/image/<path:filename>', methods=['GET'])
#def image_file(filename):
#    print('trying to serve image')
#    print('app.config[IMAGE_FOLDER]:', app.config['IMAGE_FOLDER'])
#    return send_from_directory(
#        app.config['IMAGE_FOLDER'],
#        filename,
##        as_attachment=True
#    )


# start code
if __name__ == "__main__":
    app.run(host='0.0.0.0')
