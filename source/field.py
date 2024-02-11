#import os
import os
from pprint import pprint
from able import LbUtil, FolderFileable, StringReader, CreatorString
# The Markdown
##
#### The Field
class Field(list):
    ##
    ##__Field__
    ##
    ## List of files, folders and subfolders
    ##
    def __init__(self, folder=None, ext=['.py']):
        self.folder=folder
        self.ext = ext

    def ignore(self, filename):
        ##* Ignore specific files and/or folders (eg ['.DS_Store', '.git', '.gitignore', '.idea']) on evaluation
        ignore_list = ['.DS_Store', '.git', '.gitignore', '.idea']

        for x in ignore_list:
            if x in filename:
                return True
        return False

    def get_folder_contents(self, folder=None):
        ##* List of folders, subfolder and files in a given folder on request
        if not folder:
            folder = self.folder

        files = LbUtil().get_file_list(folder, withpath=True)
        folders = LbUtil().get_folder_list(folder)
        for f in files:
            folders.append(f)

        return folders

    def traverse(self, folder):
        fflist = self.get_folder_contents(folder)
        for ff in fflist:
            if LbUtil().folder_exists(ff):
                if not self.ignore(ff):
                    self.traverse_folder(folder=ff)
            else:
                if not self.ignore(ff):
                    fn = ff.split('/')[-1]
                    ext =fn.split('.')
                    if len(ext)>1:
                        ext = '.{}'.format(fn.split('.')[-1])
                        if ext in self.ext:
                            self.append(ff)

    def traverse_folder(self, folder=None):
        if not folder:
            folder = self.folder

        self.traverse(folder)

        return self

def main():
    from pprint import pprint

    folder = os.getcwd().replace('/source','')
    #print('folder', folder)
    assert(Field(folder=folder, ext=['.py','.env'])==[])

    assert(Field(folder=folder, ext=['.py','.env']).get_folder_contents()!=[])
    print('---')
    pprint(Field(folder=folder, ext=['.py','.env']).traverse_folder())


if __name__ == "__main__":
    # execute as docker
    main()