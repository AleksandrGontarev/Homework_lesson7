import os

class WorkDirname:

    def __init__(self, dirname: str):

        self.dirname = dirname
        self.files_path = self.creat_dict_file_dir()
        self.sort = self.sort_dictionary()
        self.dictionary = self.write_file_path()
        self.creat_dict_file_dir()

    def creat_dict_file_dir(self):
        list_files = []
        list_path = []
        dict_files_path = dict()
        list_dir = os.listdir(self.dirname)
        for filename in list_dir:
            filepath = os.path.join(self.dirname, filename)
            if os.path.isdir(filepath):
                list_path.append(filename)
            elif os.path.isfile(filepath):
                list_files.append(filename)
        dict_files_path["filenames"] = list_files
        dict_files_path["dirnames"] = list_path
        return dict_files_path

    def sort_dictionary(self, revers_sort: bool = True):
        dict_sort = self.files_path
        for key, value in dict_sort.items():
            dict_sort[key] = sorted(value, reverse=not revers_sort)
        return dict_sort

    def write_file_path(self, string: str = ""):
        dictionary = self.files_path
        if string:
            if string.count("."):
                dictionary["filenames"].append(string)
            else:
                dictionary["dirnames"].append(string)
        return dictionary

    def creat_file_path(self, dir_name: str):
        dictionary = self.files_path
        for value in dictionary["dirnames"]:
            filepath = os.path.join(dir_name, value)
            os.makedirs(filepath, exist_ok=True)
        for value in dictionary["filenames"]:
            filepath = os.path.join(dir_name, value)
            if os.path.isfile(filepath):
                with open(filepath, 'w') as file:
                    file.write(dir_name)


dir_name = "\\Homeworks"

files_folders = WorkDirname(dir_name)
files_folders.files_path = files_folders.creat_dict_file_dir()
files_folders.sort = files_folders.sort_dictionary(False)
files_folders.dictionary = files_folders.write_file_path("qqq")

dir_name_1 = "\\Homework_3"
files_folders.creat_file_path(dir_name_1)










