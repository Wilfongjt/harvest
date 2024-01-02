#import os
from source.lb_util import LbUtil
from source.ability.able import Fileable,Folderable
##
### The Farm
class Field(list):
    ##
    ##__Field__
    ##
    ## Make a list of files in a folder and its subfolders
    def __init__(self, folder=None, ext='.py'):
        self.folder=folder

        self.ext = ext

    def ignore(self, filename):
        ##* ignore specific files and folder on evaluation
        ignore_list = ['.DS_Store', '.git', '.gitignore', '.idea']

        for x in ignore_list:
            if x in filename:
                return True
        return False

    def get_folder_contents(self, folder):
        ##* Make a list of folders and files in a given folder on request
        files = LbUtil().get_file_list(folder, withpath=True)
        folders = LbUtil().get_folder_list(folder)
        for f in files:
            folders.append(f)

        return folders

    def traverse_folder(self, folder=None):

        ##* Collect files via recursion on request

        if not folder:
            folder = self.folder
        fflist = self.get_folder_contents(folder)
        for ff in fflist:
            if LbUtil().folder_exists(ff):
                if not self.ignore(ff):
                    self.traverse_folder(ff)
            else:
                if not self.ignore(ff):
                    if ff.endswith(self.ext):
                        self.append(ff)
        #pprint(list)
        return self

class CommentMarkdown(list, Fileable):
    ##
    ##__CommentMarkdown__
    ##
    ## Collection of all markdown comments
    def __init__(self, lookfor='##'):
        ##* Overide the "#" default character used to identify a single line comment
        self.lookfor = lookfor

    def load(self, stringvalue):
        ## collect all the markdwon comments from a string on request
        if not stringvalue:
            return
        stringvalue = stringvalue.split('\n')
        for ln in stringvalue:
            ##* remove leading spaces for markdown legibility
            ln = ln.strip()

            if ln.startswith(self.lookfor):
                ##* replace first occuance of "#" in markdown comment
                self.append(ln.replace(self.lookfor, '', 1))

def main():
    assert(Field())
    assert(CommentMarkdown())

if __name__ == "__main__":
    # execute as docker
    main()