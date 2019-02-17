
import tarfile

BASE_PATH = '/Users/ayushshrestha/my_projects/PythonBasics/tar_untar/'


def tar_files():
    tar = tarfile.open(BASE_PATH+'tarred', "w:gz")
    # tar.add(self.backup_delete_dir + '/')
    tar.add(BASE_PATH + '/my_file.txt')
    tar.close()

def untar_files():
    tar = tarfile.open(BASE_PATH+'tarred')
    tar.extractall(path = BASE_PATH)
    tar.close()

if __name__=='__main__':
    untar_files()

