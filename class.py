import os


class WorkDirname:

    def __init__(self, dirname: str):
        self.dirname = dirname
        self.objects = self.creat_dict_file_dir()

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

    def sorted_objects(self, reverse_sort: bool = True):
        dict_sorted_objects = self.objects.copy()
        for key, value in dict_sorted_objects.items():
            dict_sorted_objects[key] = sorted(value, reverse=not reverse_sort)
        return dict_sorted_objects

    def write_objects(self, string: str):
        if string.count("."):
            self.objects["filenames"].append(string)
        else:
            self.objects["dirnames"].append(string)

    def creat_objects(self, dir_name: str):
        for value in self.objects["dirnames"]:
            filepath = os.path.join(dir_name, value)
            os.makedirs(filepath, exist_ok=True)
        for value in self.objects["filenames"]:
            filepath = os.path.join(dir_name, value)
            if os.path.isfile(filepath):
                with open(filepath, 'w') as file:
                    file.write(dir_name)


files_folders = WorkDirname("\\Homeworks")

print(files_folders.objects)

print(files_folders.sorted_objects(False))

files_folders.write_objects("mmm")
print(files_folders.objects)

dir_name = "\\Homework_3"
files_folders.creat_objects(dir_name)
