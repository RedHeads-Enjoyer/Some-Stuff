import os
import sys
import chardet

std_lib = sys.modules.keys()

unique_libs = set()

def process_file(file_path):
    encoding = None
    with open(file_path, 'rb') as f:
        data = f.read()
        encoding = chardet.detect(data)['encoding']
    with open(file_path, "r", encoding=encoding) as f:
        code = f.read()
        for line in code.split("\n"):
            line = line.strip()
            if line.startswith("import") or line.startswith("from"):
                tokens = line.split()
                if len(tokens) > 1:
                    lib_name = tokens[1]
                    if "." in lib_name:
                        lib_name = lib_name.split(".")[0]
                    unique_libs.add(lib_name)

def process_directory(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(dirpath, filename)
                process_file(file_path)

def write_to_file(libs, filename):
    with open(filename, "w") as f:
        for lib in libs:
            if lib != 'main' or lib != '':
                f.write(lib + "\n")

blocknote_dir = os.path.join(os.path.dirname(__file__), "blocknote-master")
result_file = os.path.join(os.path.dirname(__file__), "requirements.txt")

process_directory(blocknote_dir)
unique_libs = [lib for lib in unique_libs if lib not in std_lib]
write_to_file(unique_libs, result_file)
