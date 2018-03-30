import os


class FileReader():
    """The FileReader reads files from directories and offers convinience
    methods for interacting with the files and directories."""

    def __init__(self):
        super().__init__()

    def get_directories_list(self, path):
        return [
            adir for adir in os.listdir(path)
            if not os.path.isfile(os.path.join(path, adir))
        ]
        # directories = []
        # for (dirpath, dirnames, filenames) in os.walk(path):
        #     directories.extend(dirnames)
        #     break
        # return directories

    def get_files_list(self, path):
        return [
            afile for afile in os.listdir(path)
            if os.path.isfile(os.path.join(path, afile))
        ]
        # files = []
        # for (dirpath, dirnames, filenames) in os.walk(path):
        #     files.extend(filenames)
        #     break
        # return files

    def get_files_and_dirs_list(self, path):
        return [anobj for anobj in os.listdir(path)]

    def file_as_string(self, file_path):
        content = None
        with open(file_path, mode='r') as opened_file:
            content = ''.join(opened_file.readlines())
        return content

    def file_as_list(self, file_path):
        content = None
        with open(file_path, mode='r') as opened_file:
            content = opened_file.readlines()
        return content

    def file_exists(self, file_path):
        dir_path = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        files = self.get_files_list(dir_path)
        return file_name in files
