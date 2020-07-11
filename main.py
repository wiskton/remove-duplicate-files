import filecmp
import os

total_files = 0
# consultar
dirs = [
    "C:/Users/Willem/Downloads/",
]
# deletar
dir_path2 = "C:/Users/Willem/Downloads/"


def delete_file_equal(file1, file2):
    if file1 != file2 and filecmp.cmp(file1, file2, shallow=False):
        if os.path.exists(file2) and os.path.isfile(file2):
            print("Apagando... ", file2)
            os.remove(file2)
            return True
    return False


if __name__ == "__main__":
    for dir_path in dirs:
        files = os.listdir(dir_path)

        for f in files:
            f_path = os.path.join(dir_path, f)
            if os.path.exists(f_path):
                files2 = os.listdir(dir_path2)

                for f2 in files2:
                    f_path2 = os.path.join(dir_path2, f2)
                    if os.path.exists(f_path2):
                        if delete_file_equal(f_path, f_path2):
                            total_files += 1

    print("total de arquivos apagados", total_files)
