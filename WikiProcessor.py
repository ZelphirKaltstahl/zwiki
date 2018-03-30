from flask import render_template

import FileReader
import Link
import RSTRenderer

class WikiProcessor():
    """The WikiProcessor generates wiki contents from available files."""

    def __init__(self, base_dir):
        super().__init__()

        self.file_reader = FileReader.FileReader()
        self.rst_renderer = RSTRenderer.RSTRenderer()

        self.base_dir = base_dir
        self.static_dir = base_dir + 'static/'
        self.pages_dir = base_dir + 'static/rst/'

    def get_index_page(self, filter=None):
        file_names = self.file_reader.get_files_list(self.pages_dir)
        file_names.sort()

        labels = [
            self.file_name_to_link_label(file_name)
            for file_name in file_names
        ]
        targets = [
            self.file_name_to_link_target(file_name)
            for file_name in file_names
        ]

        links = [
            Link.Link(labels[ind], targets[ind])
            for ind in range(len(file_names))
        ]

        return render_template('index.j2', links=links)

    def get_page_by_name(self, page):
        page_rst_content = self.file_reader.file_as_string(
            self.pages_dir + page + '.rst'
        )
        page_html = self.rst_renderer.render_string(page_rst_content)
        return render_template('page.j2', page_content = page_html)

    def file_name_to_link_label(self, file_name):
        return file_name.replace('_', ' / ')[:-4]

    def file_name_to_link_target(self, file_name):
        return '/page/' + file_name[:-4]
