import os


class WorkDirname:

    def __init__(self, dirname: str):
        self.dirname = dirname
        self.dict_files_path = self.creat_dict_file_dir()
        self.dictionary = self.sort_dictionary()

    def __repr__(self):
        return f"{self.dict_files_path}"

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

    def sort_dictionary(self, reverse_sort: bool = True):
        for key, value in self.dict_files_path.items():
            self.dict_files_path[key] = sorted(value, reverse=not reverse_sort)
        return self.dict_files_path

    def write_file_path(self, string: str):
        if string.count("."):
            self.dictionary["filenames"].append(string)
        else:
            self.dictionary["dirnames"].append(string)
        return self.dictionary


my_dict = WorkDirname("\\Homeworks")
print(my_dict)
print(my_dict.creat_dict_file_dir())
reverse = False
print(my_dict.sort_dictionary(reverse))
print(my_dict.write_file_path("trs"))