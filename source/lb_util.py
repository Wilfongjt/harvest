
import os
from os.path import isfile, join
from os import listdir
import shutil
import time
import re

from source.nv_pair import NVPair

from source.lb_exceptions import BadFolderNameException, \
                                 FolderNotFoundException, \
                                 FolderAlreadyExistsException, \
                                 SubfolderCopyException
##
#### Utility
class LbUtil():
    ##__LbUtil__
    def hello_world(self):
        print("I am LbUtil!")

    def ch_dir(self, folder):
        os.chdir(folder)
        return self

    def copy_folder(self, src_folder, dst_folder, dirs_exist_ok=True):
        ##* Copy source project_folder and files on request
        ##* Copy fails when source project_folder doesnt exist ... [x] has test
        if not self.folder_exists(src_folder):
            raise FolderNotFoundException('Source project_folder {}'.format(src_folder))
        ##* Copy fails when destination project_folder is contained in source project_folder ... [x] has test
        if src_folder in dst_folder:
            raise SubfolderCopyException('Source project_folder {} contains {}'.format(src_folder,dst_folder))
        ##* dont overwrite destination project_folder when found ... [x] has test
        #if self.folder_exists(dst_folder):
        #    raise FolderAlreadyExistsException('Destination project_folder already exists "{}"'.format(dst_folder))
        ##* copy source project_folder, subfolders, and files to destination project_folder when source project_folder is found ... [x] has test
        shutil.copytree(src_folder,
                        dst_folder,
                        dirs_exist_ok=dirs_exist_ok)
        ##* return LbUtil ... [x] has test
        return self

    def create_empty_file(self, folder, filename):
        f = open('{}/{}'.format(folder,filename), "w")
        f.close()
        return self

    def create_folder(self, folder):
        ##* Create all folders in a given path on request
        # No trailing / in project_folder
        # path = project_folder
        if not folder:
            raise BadFolderNameException('BadFolderName {}'.format(folder))
        ##* create all folders when needed ... [x] has test
        p = ''
        for sub in folder.split('/'):
            if len(sub) > 0:
                p += '/{}'.format(sub)
                # print('check project_folder ', p)
                if not os.path.exists(p):
                    # print('create project_folder ', p)
                    os.mkdir('{}/'.format(p))
        ##* return LbUtil ... [x] has test
        return self
    def current_directory(self):
        ##* Get the Current Folder Name on request
        ##* remove "_scripts" project_folder name when found
        ##* return str
        return os.getcwd().replace('/_scripts', '')

    def delete_file(self, folder, file_name):
        ##* Delete file on request
        if self.file_exists(folder, file_name):
            ##* delete file when project_folder and file are found ... [x] has test
            os.remove("{}/{}".format(folder, file_name))

        ##* skip file delete when project_folder and file are NOT found ... [x] has test

        ##* return LbUtil ... [x] has test
        return self

    def delete_folder(self, folder):
        ##* Delete project_folder on request
        # Note: You can only remove empty folders.

        ##* remove all files and folders in project_folder ... [x] has test
        if self.folder_exists(folder):
            shutil.rmtree(folder)

        ##* return LbUtil ... [x] has test
        return self

    def delete_folder_files(self, folder, ext):
        ##* Delete all files in a project_folder on request
        # ext = 'custom'
        ##* Delete all files when files are found in a project_folder ... [x] has test
        self.deleted_file_list = self.get_file_list(folder, ext)
        for filename in self.deleted_file_list:
            self.delete_file(folder, filename)
        ##* return LbUtil ... [x] has test
        return self

    def get_env_value(self, KEY_NAME, default='TBD'):
        ##* Get an LbEnvironment Value by name
        ##* use name to find name in os.environ

        rc = default
        if KEY_NAME in os.environ:
            ##* return value when found ... [x] has test
            rc = os.environ[KEY_NAME]
        ##* return "TBD" when not found ... [x] has test
        ##* returns str ... [x] has test
        return rc

    def file_age(self, folder, filename):
        ##* Calculate the age of a file
        ##* age is system datetime - file datetime ... no test
        ##* age is greater than or equal to zero ... [x] has test
        x = os.stat('/bin')
        result = (time.time() - x.st_mtime)
        # print("The age of the given file is: ", result)
        ##* returns a float  ... [x] has test
        return result

    def folderfile_exists(self, folder_filename):
        ##* Test if a given project_folder and file exist on request

        ##* file exists when project_folder exists and file exists ... [x] has test
        exists = os.path.isfile(folder_filename)

        ##* return bool ... [x] has test
        return exists
    def file_exists(self, folder, filename):
        ##* Test if a given project_folder and file exist on request

        ##* file exists when project_folder exists and file exists ... [x] has test
        exists = os.path.isfile('{}/{}'.format(folder, filename))

        ##* return bool ... [x] has test
        return exists

    def folder_exists(self, folder):
        ##* Test if a given project_folder exists on request
        ##* project_folder exists when found on drive ... [x] has test
        exists = os.path.isdir('{}'.format(folder))
        ##* returns bool ... [x] has test
        return exists

    def get_file_extension(self, filename):
        ##* Get file extension on request
        ext = filename.split('.')[-1]
        ##* return extension/string ... [x] has test
        return ext

    def get_file_list(self, path, ext=None, withpath=False):
        ##* Get List of File Names on request
        onlyfiles = []

        ##* return [] when project_folder is None ... [x] has test
        if not path:
            return []

        ##* returns [] when project_folder NOT found ... [x] has test
        if not self.folder_exists(path):
            return []
        # get list of files
        lst = listdir(path)
        ##* returns [] when no files found ... [ ] has test

        if lst == []:
            return []
        ##* return all files when ext = "*" ... [x] has test
        onlyfiles = [f for f in lst if isfile(join(path, f))]

        ##* return files when file has specified extention ... [x] has test
        if ext != None and ext != '*':
            onlyfiles = [f for f in onlyfiles if f.startswith(ext) or f.endswith(ext)]
        onlyfiles =  [fn for fn in onlyfiles if '.DS_Store' not in fn]
        ##* prefix with a project_folder name
        if withpath:
            onlyfiles = ['{}/{}'.format(path, fn) for fn in onlyfiles]

        ##* return list of filenames when files found [x] has test
        return onlyfiles

    def get_folder_list(self, path):
        ##* Get List of Folder Names on request

        onlyfolders = []
        ##* return [] when project_folder is None ... [x] has test
        if not path:
            return []

        ##* returns [] when project_folder NOT found ... [x] has test
        if not self.folder_exists(path):
            return []

        # get list of folders and files
        lst = listdir(path)

        ##* returns [] when no folders found ... [x] has test
        if lst == []:
            return []

        onlyfolders = ['{}/{}'.format(path, f) for f in lst if not isfile(join(path, f))]

        ## return list ... [x] has test
        return [fn for fn in onlyfolders]

    def is_empty(self, folder, filename):
        ##__Check for empty file on request__
        ##* empty when project_folder is None
        #print('is_empty 1')
        if not folder:
            return True
        #print('is_empty 2')

        ##* empty when filename is None
        if not filename:
            return True
        #print('is_empty 3')

        ##* empty when project_folder not found
        exists = os.path.isdir('{}'.format(folder))
        if not exists:
            return True
        #print('is_empty 4')

        ##* empty when file is not found
        exists = os.path.isfile('{}/{}'.format(folder, filename))
        if not exists:
            print('not found', '{}/{}'.format(folder, filename))
            return True
        #print('is_empty 5',"{}/{}".format(project_folder, filename))

        ##* empty when size of file is 0
        if os.stat("{}/{}".format(folder, filename)).st_size == 0:
            ##* file is empty when has no lines ... [ ] has test
            #self.addStep('empty')
            return True
        #print('is_empty out')

        ##* not empty when size of file is NOT 0
        return False

    def inn(self, search_pattern, list1):
        rc = False

        for element in list1:
            m1 = re.match(search_pattern, element)
            if m1 and m1.span()[1] == len(element):
                rc = True
        return rc

    def replace(self, search_pattern, replaceStr, list1):
        # replace element with replaceStr when search_pattern is found list
        rc = []
        i = 0
        # compare all elements in list to pattern
        for element in list1:
            m1 = re.match(search_pattern, element)
            if m1 and m1.span()[1] == len(element):
                # when pattern matches replace element with replaceStr
                rc.append(replaceStr)
            else:

                rc.append(element)
            i += 1
        return rc

    def replace(self, search_pattern, replaceStr, list1):
        # replace element with replaceStr when search_pattern is found list
        rc = []
        i = 0
        # compare all elements in list to pattern
        for element in list1:
            m1 = re.match(search_pattern, element)
            if m1 and m1.span()[1] == len(element):
                # when pattern matches replace element with replaceStr
                rc.append(replaceStr)
            else:

                rc.append(element)
            i += 1
        return rc


    def synchronize(self, A, B):
        # merges to strings together
        #print(' ')
        #print('Sync ({}) and ({})'.format(self.replace('\n', '.'), B.replace('\n', '.')))
        A = A.strip('\n').split('\n')
        B = B.strip('\n').split('\n')

        # print('  A: ', A)
        # print('  B: ', B)

        pattern = '^(<<>>)=(.+)'
        AB = []
        # put all A first in list
        AB = [a for a in A]
        # print('AB',AB)

        for b in B:
            # print('----')
            b = NVPair(b)
            #print(' ')
            for a in A:
                a = NVPair(a)
                pttrn = pattern.replace('<<>>', a.getName())

                # if a.isNV and b.isNV and a.equivelent(pttrn, b):

                # not a and not b ok
                #   if '' not in AB: append('') ok

                # a and b
                #   if a not in AB: append(a)
                #   if b not in AB: append(b)

                # not a and b
                #   if '' not in AB: append('')
                #   if b not in AB: append(b)

                # a and not b
                #   if a not in AB: append(a)

                if not a and not b:
                    if a not in AB:
                        AB.append(a)
                    # print('  1.1  a: ({}) b: ({}) AB: {}'.format(a.ljust(10), b.ljust(10), AB))
                elif a and b:
                    if a not in AB:
                        if not LbUtil().inn(pttrn,
                                        AB):  # dont overwrite with A only B ...# Allow the first element found in A ... avoid overwrite of element that was just added
                            AB.append(a)

                        # print('  2.1    a: ({}) b: ({}) AB: {}'.format(a.ljust(10), b.ljust(10), AB))
                    if b not in AB:
                        pttrn = pattern.replace('<<>>', b.getName())
                        if LbUtil().inn(pttrn, AB):  # overwrite with B never A
                            AB = LbUtil().replace(pttrn, b, AB)
                            # print('  2.1.1  a: ({}) b: ({}) AB: {}'.format(a.ljust(10), b.ljust(10), AB))

                        if b not in AB:
                            AB.append(b)
                            # print('  2.1.2  a: ({}) b: ({}) AB: {}'.format(a.ljust(10), b.ljust(10), AB))

                elif not a and b:
                    if a not in AB:
                        AB.append(a)
                        # print('  3.1    a: ({}) b: ({}) AB: {}'.format(a.ljust(10), b.ljust(10), AB))
                    if b not in AB:
                        AB.append(b)
                        # print('  3.2    a: ({}) b: ({}) AB: {}'.format(a.ljust(10), b.ljust(10), AB))
                elif a and not b:
                    if a not in AB:
                        AB.append(a)
                        # print('  3.3    a: ({}) b: ({}) AB: {}'.format(a.ljust(10), b.ljust(10), AB))
                else:
                    # print('  4     not a and not b', not a and not b)
                    # print('  4    a: ({}) b: ({}) AB: {}'.format(a.ljust(10), b.ljust(10), AB))
                    raise Exception('Unhandled line case a: ({}) b: ({})'.format(a, b))

        # remove all the ''
        AB = [a for a in AB if a != '']

        # add '' when empty
        if not AB:
            # print('add')
            AB.append('')

        return '\n'.join(AB)

def mainTestSynchonize():
    actual = LbUtil()
    # assert (actual.synchronize('''''') == '''''')
    assert (actual.synchronize('''''', '''''') == '''''')
    assert (actual.synchronize('''''', '''\n''') == '''''')
    assert (actual.synchronize('''''', '''# abc''') == '''# abc''')
    assert (actual.synchronize('''''', '''A=a''') == '''A=a''')
    assert (actual.synchronize('''\n''', '''''') == '''''')
    assert (actual.synchronize('''\n''', '''\n''') == '''''')
    assert (actual.synchronize('''# A''', '''''') == '''# A''')
    assert (actual.synchronize('''# A''', '''\n''') == '''# A''')
    assert (actual.synchronize('''# A''', '''# A''') == '''# A''')
    assert (actual.synchronize('''# A''', '''A=a''') == '''# A\nA=a''')
    assert (actual.synchronize('''# A''', '''# A\nA=a''') == '''# A\nA=a''')
    assert (actual.synchronize('''# A''', '''# A\nA=a\nB=b''') == '''# A\nA=a\nB=b''')
    assert (actual.synchronize('''# A''', '''A=a''') == '''# A\nA=a''')
    assert (actual.synchronize('''# A''', '''A=a\nB=b''') == '''# A\nA=a\nB=b''')

    expected = '''# A\nA=a\n# B\nB=b'''  # '''\n# A\nA=a\n# B\nB=b\n'''
    assert (actual.synchronize('''''', '''\n# A\nA=a\n# B\nB=b\n''') == expected)
    # print('actual: {} \nexpect: {}'.format(TemplateString('''\n''', '''# A\nA=a\n# B\nB=b\n''')).replace('\n','.') , '''\n# A\nA=a\n# B\nB=b\n'''.replace('\n','.')))
    assert (actual.synchronize('''\n''', '''# A\nA=a\n# B\nB=b\n''') == expected)
    assert (actual.synchronize('''\n# A''', '''\nA=a\n# B\nB=b\n''') == expected)
    assert (actual.synchronize('''\n# A\n''', '''A=a\n# B\nB=b\n''') == expected)
    assert (actual.synchronize('''\n# A\nA=a''', '''\n# B\nB=b\n''') == expected)
    assert (actual.synchronize('''\n# A\nA=a\n''', '''# B\nB=b\n''') == expected)
    assert (actual.synchronize('''\n# A\nA=a\n# B''', '''\nB=b\n''') == expected)
    assert (actual.synchronize('''\n# A\nA=a\n# B\n''', '''B=b\n''') == expected)
    assert (actual.synchronize('''\n# A\nA=a\n# B\nB=b''', '''\n''') == expected)
    assert (actual.synchronize('''\n# A\nA=a\n# B\nB=b\n''', '''''') == expected)
    assert (actual.synchronize('''\n# A\nA=a\n# B\nB=b\n''', '''\n# A\nA=a\n# B\nB=b\n''') == expected)

    # dev changes file

    expected = '''# A\nA=b'''
    # print('actual: {} \nexpect: {}'.format(TemplateString('''\n# A\nA=a''', '''\nA=b\n''')).replace('\n','.') , expected.replace('\n','.')))
    assert (actual.synchronize('''\n# A\nA=a''', '''\nA=b''') == expected)

    expected = '''# A\nA=b\nB=b'''
    assert (actual.synchronize('''\n# A\nA=a''', '''\nA=b\nB=b''') == expected)


def main():
    print('lb_util')
    folder = '/'.join(str(__file__).split('/')[0:-1])
    filename = str(__file__).split('/')[-1]
    # Lb_MarkDownString().setFolder(project_folder).setFilename(filename).open().save()
    print('file_exists', LbUtil().file_exists(folder, filename))
    # print('file_exists', LbUtil().file_exists(project_folder, '0.env'))
    print('util.get_folder_list', LbUtil().get_file_list(os.getcwd()))
    print('util.get_folder_list', LbUtil().get_file_list(os.getcwd(),withpath=True))


    # INN
    actual = LbUtil()
    pattern = '^(A)=(.+)'

    assert (not actual.inn('^(X)=(.+)', []))
    assert (not actual.inn('^(X)=(.+)', ['# A']))
    assert (actual.inn('^(A)=(.+)', ['A=a']))
    assert (actual.inn('^(A)=(.+)', ['A=a', 'B=b','C=c']))
    assert (actual.inn('^(A)=(.+)', ['B=b','A=a', 'C=c']))
    assert (actual.inn('^(A)=(.+)', ['B=b', 'C=c','A=a']))

    #assert (actual.inn('^(A)=(.+)', ['# A', 'A=a']))
    #assert (actual.inn('^(A)=(.+)', ['# A', 'A=a']))

    mainTestSynchonize()

def main_document():
    from dep.pylyttlebit.lb_doc_comments import LbDocComments
    print('lb_util')
    folder = '/'.join(str(__file__).split('/')[0:-1])
    filename = str(__file__).split('/')[-1]
    LbDocComments().setFolder(folder).setFilename(filename).open().save()


if __name__ == "__main__":
    # execute as docker
    main()