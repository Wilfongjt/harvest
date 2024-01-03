import os
import sys
from source.lb_util import LbUtil
### Abilities

class Appendable():
    ##__Appendable__
    ##
    ## Provide the abilty to append new lines to a document
    ##
    def __init__(self):
        #print('appendable init')
        self.appendable=False

    def isAppendable(self):
        ##* get appendable state on request
        return self.appendable
    def setAppendable(self, tf):
        ##* set appendable state on request
        ##
        self.appendable=tf
        return self


class ClassNameable():
    ##__ClassNameable__
    ##
    ## Enable the use of classname for reference
    ##
    def getClassName(self):
        ##* Get Class Name on request
        ##
        return self.__class__.__name__

class Clientable():
    ##__Clientable__
    ##
    ## Enable reference to the client folder
    def __init__(self, project_folder=None):
        self.project_folder = project_folder

    def getClientFolder(self):
        ##* get client folder on request
        ws = '/'.join(self.project_folder.split('/')[0:-2])
        return ws

class Datable():
    ##
    ##__Datable__
    ##
    ## Provide a list of name-value pairs for template substitution
    def __init__(self):
        ##* eg [{name: '', value: ''},...]
        self.data = [] #None

    def getData(self, key=None):
        ##* retrieve a specific name-value pair on request
        if key:
            for d in self.data:
                if key == d['name']:
                    return d['value']

        ##* retrieve all name-value pairs on request
        return self.data

    def setData(self, nv_list):
        ##* set name-value pairs on request
        self.data = nv_list
        return self

class Developable():
    ##
    ##__Developable__
    ##
    ## Enable reference to the Development folder
    def __init__(self, project_folder=None):
        self.project_folder = project_folder

    def getDevelopFolder(self):
        ##* Retrieve the development folder on request
        ws = '/'.join(self.project_folder.split('/')[0:-3])
        return ws

class Failable():
    ##
    ##__Failable__
    ##
    ## Enable a fail flag
    def __init__(self):
        ##* provide a "failed" flag
        self.failed=False
        ##* provide a list of failure mesages
        self.fail_msg=[]

    def setFail(self, tf, msg=None):
        ##* set failure and add failed message on request
        self.failed=tf
        self.fail_msg.append(msg.replace('\n',' '))
        return self

    def on_fail_exit(self):
        ##* Provide a hard failure when failed
        if self.failed:
            sys.exit(1)

        return self

class Fileable():
    ##
    ##__Fileable__
    ##
    ## Enable Read from and Write to file for object
    def __init__(self):
        ##* provide folder and filename attributes
        self.folder=None
        self.filename=None
    def read_file(self, folder_filename):
        ##* read file contents given a folder and filename
        with open(folder_filename) as f:
            string_value = f.read()
        return string_value
    def save(self, folder_filename):
        ##* write contents of object to a file
        ##* contents are inherited from the
        with open(folder_filename, 'w') as f:
            f.write('\n'.join(self))
        return self

class Folderable():
    ##
    ##__Folderable__
    ##
    ## Allow folder interactions
    def __init__(self):
        self.lastdir=os.getcwd()
    def ch_dir(self, folder):
        ##* change actual folder on request
        ##* track last actual folder when folder is changed
        self.set_last_dir()
        os.chdir(folder)
        return self
    def get_last_dir(self):
        ##* retrieve the last folder visited on request
        return self.lastdir
    def set_last_dir(self):
        ##* track the last folder on request
        self.lastdir=os.getcwd()
        return self
    def get_file_list(self, folder):
        ##* provide a list of files for a given folder
        rc = LbUtil().get_file_list(folder)
        return rc
    def folder_exists(self, folder):
        ##* determine if folder exists on request
        exists = os.path.isdir('{}'.format(folder))
        return exists
    def makedirs(self, folder):
        ##* create folders on request
        os.makedirs(folder, exist_ok=True)
        return self

class Inputability():
    ##
    ##__Inputability__
    ## Enable input from user
    ##
    def get_input(self, msg, default, hardstop=True):
        ##* Prompt user for input
        ##* Show current value or default
        rc = '{} [{}] : '.format(msg, default)
        rc = input(rc)
        ##* Provide a default input value when user presses return
        if not rc:
            rc = default
        ##* Cause a hard stop when user types 'n','N','x','X','q' or 'Q'
        if rc in ['n','N','x','X','q','Q','TBD']:
            if hardstop:
                print('stopping...Stopped')
                exit(0)

        return rc
class Mergable():
    ##
    ##__Mergable__
    ##
    ## Render a template with user provided values
    def merge(self, template, nv_list):
        ##
        ##* Merge name-value pairs into a given template string on request
        # replace found names with values by iteration
        for nv in nv_list:
            template = template.replace(nv['name'], nv['value'])

        return template

class ProjectNameable():
    ##
    ##__ProjectNameable__
    ##
    ## Enable reference to the project name
    def __init__(self, project_folder=None):
        # project
        self.project_folder = project_folder

    def getProjectName(self):

        ##* retrive the GitHub project name from the project_folder
        return self.project_folder.split('/')[-1]

# ProjectFolderable
class ProjectFolderable():
    ##
    ##__ProjectFolderable__
    ##
    ## Enable reference to Project folder
    def __init__(self, project_folder=None):
        # project
        self.project_folder = project_folder
    def getProjectFolder(self):
        return self.project_folder
    def setProjectFolder(self, project_folder):
        ##* project project_folder ends with the GITHUB project name
        self.project_folder=project_folder
        return self
class Recordable():
    ##
    ##__Recordable__
    ##
    ##
    def __init__(self):
        self.recording = {}
    def addStep(self, msg, arrow='->'):
        ##* Record a message

        if 'step_list' not in self.recording:
            self.recording['step_list'] = []

        if len(self.recording['step_list']) == 0:
            msg = '[*] -> {}'.format(msg)
            self.recording['step_list'].append({'msg': msg, 'count': 1})
        else:
            msg = '{} {}'.format(arrow, msg)
            if msg == self.recording['step_list'][-1]['msg']:
                self.recording['step_list'][-1]['count'] += 1
            else:
                self.recording['step_list'].append({'msg': msg, 'count': 1})

        return self

    def getSteps(self):
        ##* Retrieve recorded step
        rc = ''
        if 'step_list' not in self.recording:
            self.recording['step_list'] = []

        for s in self.recording['step_list']:
            if s['count'] == 1:
                rc += '{}'.format(s['msg'])
            else:
                rc += '{} ({})'.format(s['msg'],s['count'])

        return rc

    def formulate(self, form, title=None):
        ##* Convert JSON Object to String
        ##* eg {a:1, b:2} to (a, b)
        keys = []
        for key in form:
            keys.append(key)
        if title:
            return '({}({}))'.format(title, ','.join(keys))

        return '({})'.format(','.join(keys))


    def set_(self, key, value):
        if 'state' not in self.recording:
            self.recording['state'] = {}

        self.recording['state'][key] = value
        return self

    def get_(self, key=None):
        rc = None
        if 'state' not in self.recording:
            self.recording['state'] = {}

        if not key:
            rc = self.recording['state']
        elif key in self.recording['state']:
            rc = self.recording['state'][key]

        return rc

    def showSteps(self):
        print(self.getSteps())
        return self

#class Runable():
#    def run(self):
#        return self

class Resultable():
    ##
    ##__Resultable__
    ## seperately keep track of results
    def __init__(self):
        ##* provide dictionary of results
        self.results = {}

    def getResult(self, key=None):
        ##* retrieve specific result on request
        if key:
            return self.results[key]
        ##* retrieve all results on reauest
        return self.results

    def setResult(self, key, value):
        self.results[key]=value
        return self

class Savable():
    ##
    ##__Saveable__
    ##
    ## handle the output folder and filename
    def __init__(self):
        self.folder = None
        self.filename = None

    def getFolderFile(self):
        rc = None
        if not self.getFolder() and not self.getFilename():
            rc = None
        elif not self.getFolder() and self.getFilename():
            return self.getFilename()
        elif self.getFolder() and not self.getFilename():
            return self.getFolder()

        return '{}/{}'.format(self.getFolder(), self.getFilename())

    def setFolderFile(self, folder_filename):
        ##* set project_folder and filename from single string
        self.folder = '/'.join(folder_filename.split('/')[0:-1])
        self.filename = folder_filename.split('/')[-1]
        return self

    def setFolder(self, name, create=False):
        ##* Set project_folder name on request

        if create:
            LbUtil().create_folder(name)
        self.folder=name
        return self

    def getFolder(self):
        ##* Get project_folder name on request
        return self.folder

    def setFilename(self, name):
        ##* Set Filename on request
        self.filename=name

        return self

    def getFilename(self):
        ##* Get filename on request
        return self.filename
class Taskable():
    ##
    ##__Taskable__
    ##
    ## Create some legibility for code maintenance
    ##* provide interface for Task
    def __init__(self):
        self.fail=False
        self.msg=[]
        self.result=None

    def create(self):
        ##* create
        # print('create1')
        return self

    def read(self):
        ##* read
        # print('read1')
        return self

    def update(self):
        ##* update
        # print('update1')
        return self

    def delete(self):
        ##* delete
        # print('delete1')
        return self
    def validateInput(self):
        ##* validate task inputs
        return self

    def validateOutput(self):
        ##* validate task output
        return self

class Workspaceable():
    ##
    ##__Workspaceable__
    ## Enable reference to workspace folder
    def __init__(self, project_folder=None):
        self.project_folder = project_folder

    def getWorkspaceFolder(self):
        ##* retrieve the workspace folder on request
        ws = '/'.join(self.project_folder.split('/')[0:-1])
        return ws

    #def create_workspace(self):
    #    if not LbUtil().folder_exists(self.getWorkspaceFolder()):
    #        os.makedirs(self.getWorkspaceFolder())
    #    return self

# -------
def test_Appendable():
    # print('appendable')
    assert(not Appendable().isAppendable())
    assert(Appendable().setAppendable(True).isAppendable())

def test_ClassNameable():
    assert(ClassNameable())
    assert(ClassNameable().getClassName() == 'ClassNameable')

def test_Clientable(project_folder, client_name):
    assert(Clientable(project_folder))
    print('clientfolder',Clientable(project_folder).getClientFolder())

def test_Datable():
    #print('datable',Datable())

    dA = {'name': 'A', 'value': 'a'}
    dB = {'name': 'B', 'value': 'b'}
    dC = {'name': 'C', 'value': 'c'}
    lst = [dA, dB, dC]

    assert(Datable().getData() == [])
    assert(Datable().setData([]).getData()==[])
    assert(Datable().setData(lst).getData()==lst)
    assert(Datable().setData(lst).getData('A')==dA['value'])
    assert(Datable().setData(lst).getData('B')==dB['value'])
    assert(Datable().setData(lst).getData('C')==dC['value'])

def test_Developable(project_folder):
    assert(Developable())

def test_ExtendedClass():
    #print('testExtendedClass')
    import os
    folder_expected = '{}/Development/temp-org/temp-ws'.format(os.environ['HOME'])
    filename_expected = 'sample.txt'
    folderfile_expected = '{}/{}'.format(folder_expected, filename_expected)

    # test return types
    class Example(Taskable, Savable, Appendable, Datable, Mergable, ClassNameable, Recordable):
        def __init__(self):
            Taskable.__init__(self)
            Savable.__init__(self)
            Appendable.__init__(self)
            Datable.__init__(self)
            Recordable.__init__(self)
            #print('appendable',self.appendable)
    # Savable
    assert(type(Example().setFolderFile(folderfile_expected)) is Example)
    assert(type(Example().setFolder(folder_expected)) is Example)
    assert(type(Example().setFilename(filename_expected)) is Example)
    assert(Example().setFolderFile(folderfile_expected).getFolder()==folder_expected)
    assert(Example().setFolderFile(folderfile_expected).getFilename()==filename_expected)
    assert(Example().setFolderFile(folderfile_expected).getFolderFile()==folderfile_expected)
    # Appendable
    assert(not Example().isAppendable())
    assert(Example().setAppendable(True).isAppendable())
    # Datable
    dA = {'name': 'A', 'value': 'a'}
    dB = {'name': 'B', 'value': 'b'}
    dC = {'name': 'C', 'value': 'c'}
    lst = [dA, dB, dC]
    assert (Example().getData() == [])
    assert (Example().setData([]).getData() == [])
    assert (Example().setData(lst).getData() == lst)
    assert (Example().setData(lst).getData('A') == dA['value'])
    assert (Example().setData(lst).getData('B') == dB['value'])
    assert (Example().setData(lst).getData('C') == dC['value'])
    # Mergable
    nv_list = [{'name': '<<A>>', 'value': 'a'}]
    assert (Example().merge_('abc <<A>>', nv_list) == 'abc a')
    # ClassNameable
    assert (Example().getClassName() == 'Example')
    assert (Example().addStep('A is a').getSteps()=='[*] -> A is a')
    # Taskable
    assert (type(Example().create()) is Example)
    assert (type(Example().read()) is Example)
    assert (type(Example().update()) is Example)
    assert (type(Example().delete()) is Example)

def test_Failable():
    assert(Failable())

def test_Foldable():
    assert(Folderable())

def test_Mergable():
    nv_list = [{'name': '<<A>>', 'value':'a'}]
    assert (Mergable())
    assert (Mergable().merge_('abc <<A>>', nv_list) == 'abc a')

def test_Projectable(project_folder, twidth):

    #project_name = 'py_test'
    #organization = 'temp-org'
    #username_gh = 'wilfongjt'
    #project_folder = '{}/Development/{}/temp-ws/{}'.format(os.environ['HOME'], organization, project_name)
    #workspace_folder = '/'.join(project_folder.split('/')[0:-1])

    # project folder is the same as the clone folder
    print('test ProjectFolderable: ')
    print('project_folder: '.rjust(twidth), end='')

    #project_folder='{}/Development/temp-org/temp-ws'.format(os.environ['HOME'])
    assert (ProjectFolderable())
    assert (ProjectFolderable(project_folder=project_folder).getProjectFolder() == project_folder)
    print(ProjectFolderable(project_folder=project_folder).getProjectFolder())

def test_ProjectNameable(project_folder, project_name,twidth):
    print('project_name: '.rjust(twidth), end='')
    assert (ProjectNameable(project_folder=project_folder).getProjectName() == project_name)
    print(ProjectNameable(project_folder=project_folder).getProjectName())

def test_Recordable():
    assert(Recordable())
    assert(Recordable().addStep('A is a').getSteps()=='[*] -> A is a')

def test_Resultable():
    actual = Resultable()
    assert (actual)
    assert (actual.setResult('key1', 'value1').getResult()=={'key1': 'value1'})
    assert (actual.setResult('key2', 'value2').getResult()=={'key1': 'value1', 'key2': 'value2'})
    assert (actual.setResult('key3', []).getResult()=={'key1': 'value1', 'key2': 'value2', 'key3': []})

def test_Savable():

    import os
    folder_expected = '{}/Development/temp-org/temp-ws'.format(os.environ['HOME'])
    filename_expected = 'sample.txt'
    folderfile_expected = '{}/{}'.format(folder_expected, filename_expected)

    # print('Savable 1')

    assert(Savable().setFolderFile(folderfile_expected).getFolder()==folder_expected)
    assert(Savable().setFolderFile(folderfile_expected).getFilename()==filename_expected)
    assert(Savable().setFolderFile(folderfile_expected).getFolderFile()==folderfile_expected)

    assert(Savable().setFolder(folder_expected).getFolder()==folder_expected)
    assert(Savable().setFolder(folder_expected).getFilename()==None)
    assert(Savable().setFolder(folder_expected).getFolderFile()==folder_expected)

    assert(Savable().setFilename(filename_expected).getFolder()==None)
    assert(Savable().setFilename(filename_expected).getFilename()==filename_expected)
    assert(Savable().setFilename(filename_expected).getFolderFile()==filename_expected)

def test_Taskable():
    assert (Taskable())
    assert (Taskable().create())
    assert (Taskable().read())
    assert (Taskable().update())
    assert (Taskable().delete())
    assert (Taskable().validateInput())
    assert (Taskable().validateOutput())

def test_Workspaceable(project_folder, workspace_folder,twidth):
    print('workspace_folder: '.rjust(twidth), end='')
    assert (Workspaceable(project_folder=project_folder).getWorkspaceFolder() == workspace_folder)
    print(Workspaceable(project_folder=project_folder).getWorkspaceFolder())

def main():
    twidth = 25
    project_name = 'py_test'
    client_name = 'temp-org'
    username_gh = 'wilfongjt'
    project_folder = '{}/Development/{}/temp-ws/{}'.format(os.environ['HOME'], client_name, project_name)
    workspace_folder = '/'.join(project_folder.split('/')[0:-1])
    #--------
    test_Appendable()
    test_ClassNameable()

    test_Clientable(project_folder, client_name)
    test_Datable()

    test_Developable(project_folder)

    test_ExtendedClass()

    test_Failable()
    test_Foldable()

    test_Mergable()

    test_Projectable(project_folder,twidth)
    test_ProjectNameable(project_folder,project_name,twidth)

    test_Recordable()
    test_Resultable()
    test_Savable()

    test_Taskable()
    test_Workspaceable(project_folder, workspace_folder,twidth)


if __name__ == "__main__":
    # execute as docker
    main()