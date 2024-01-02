import os
from source.ability.able import Fileable, ClassNameable
#### String
class ReaderString(str, Fileable, ClassNameable):
    ##__ReaderString__
    ##* open a file and read contents into string
    def __init__(self, folder_filename):
        Fileable.__init__(self)

        self.folder = folder_filename.split('/')[0:-1]
        self.filename = folder_filename.split('/')[-1]

    def __new__(cls, folder_filename):
        #print('read', cls.read())
        string_value = ''
        #with open(folder_filename) as f:
        #    string_value = f.read()
        string_value = Fileable().read_file(folder_filename)
        instance = super().__new__(cls, string_value)
        return instance

    #def getClassName(self) -> str:
    #    ##__Get Class Name on request__
    #    ##* returns current class name
    #    return self.__class__.__name__

    def depisAppendable(self):
        # is file intended to be appended
        # use '.append.' in filename to indicate this file should be appended to existing file
        if '.append.' in self.filename:
            return True
        return False

    def show(self):
        print('## {}'.format(self.getClassName()))
        print('file:  ', self.folder)
        print('project_folder:', self.filename)
        print('actual:')
        print('   ', (self.replace('\n', '\n    ')))

        return self

def main():
    print(' ')
    #tmpl_folder_filename = '{}/template/api/env/api/latest/.env.compile.tmpl'.format(os.getcwd())
    tmpl_folder_filename = __file__
    # print('tmpl_folder_filename',tmpl_folder_filename)
    #tmpl_filename = '.env.compile.tmpl'
    tmpl_text = ReaderString(tmpl_folder_filename)
    assert ('<<WS_ORGANIZATION>>' in tmpl_text)
    # tmpl_text.show()

    tmpl_folder_filename = '{}/template/api/platform/heroku/api/latest/.env.compile.tmpl'.format(os.getcwd().replace('/bin','/source'))
    # print('tmpl_folder_filename', tmpl_folder_filename)
    actual = ReaderString(tmpl_folder_filename)
    # print('tmpl_text', actual)
    # print('isAppend', actual.isAppendable())
    assert (actual.isAppendable() == True)


if __name__ == "__main__":
    # execute as docker
    main()