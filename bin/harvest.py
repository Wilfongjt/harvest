
import os
import re
from pprint import pprint
from able import EnvString, FolderFileable, Inputable, ReaderString, CreatorString, UpdaterString
#from source.ability.dep_able import Fileable,Folderable, Inputabile, Saveable
#from source.reader_string import ReaderString
from source.field import Field
from source.crop import CropMarkdown
#from source.string_creator_env import CreatorString_Env
from source.string_template import TemplateString
#from source.string_updater_name_value_list import NameValueList_UpdaterString
import datetime

__version__='1.1.1'
def get_bin_folder():
    return os.getcwd()
def get_default_input_folder():
    return os.getcwd().replace('/bin', '')
def get_default_output_folder():
    return os.getcwd()
def get_template_folder():
    return os.getcwd().replace('/bin','/source/templates')

def main():
    ### Harvest
    ##
    ## Compile "comments" from files in the harvest project
    ##
    ##* Compile comments into a single file
    ##* Load environment variables from harvest.env

    env_folder_filename = '{}/harvest.env'.format(get_bin_folder())

    ##* Use a template to initialize the harvest.env

    template_folder_filename = '{}/harvest.env.tmpl'.format(get_template_folder())
    template_string = TemplateString(ReaderString(template_folder_filename))\
                        .merge('<<HARVEST_INPUT_FOLDER>>',get_default_input_folder())\
                        .merge('<<HARVEST_OUTPUT_FOLDER>>',get_default_output_folder())

    contents = CreatorString(folder_filename=env_folder_filename,
                             default_contents=template_string,
                             overwrite=False, hardfail=False)

    ##* Load environment variables into memory

    env_string = EnvString(env_folder_filename)

    ##* Collect input folder name when entered by user

    os.environ['HARVEST_INPUT_FOLDER'] = Inputable().get_input('HARVEST_INPUT_FOLDER',
                                         os.environ['HARVEST_INPUT_FOLDER'],
                                         hardstop=True)

    ##* Collect output folder name when entered by user

    os.environ['HARVEST_OUTPUT_FOLDER'] = Inputable().get_input('HARVEST_OUTPUT_FOLDER',
                                          os.environ['HARVEST_OUTPUT_FOLDER'],
                                          hardstop=True)

    ##* Collect output filename when entered by user

    os.environ['HARVEST_OUTPUT_FILENAME'] =  Inputable().get_input('HARVEST_OUTPUT_FILENAME',
                                            os.environ['HARVEST_OUTPUT_FILENAME'],
                                            hardstop=True)

    save_env = Inputable().get_input('save env changes',
                                     'N',
                                     hardstop=False)

    # user feedback
    print('HARVEST_INPUT_FOLDER:   ', os.environ['HARVEST_INPUT_FOLDER'])
    print('HARVEST_OUTPUT_FOLDER:  ', os.environ['HARVEST_OUTPUT_FOLDER'])
    print('HARVEST_OUTPUT_FILENAME:',os.environ['HARVEST_OUTPUT_FILENAME'])

    ##* Include files ending with ".py", and ".env"

    file_list = Field(folder=os.environ['HARVEST_INPUT_FOLDER'],
                      ext=['.py', '.env']).traverse_folder()


    file_list = Field(os.environ['HARVEST_INPUT_FOLDER'], ['.py', '.env']).traverse_folder()

    comments = []
    commentMarkdown = CropMarkdown(lookfor='##')
    for f in file_list:
        print('field file', f)
        commentMarkdown.load(ReaderString(f))

    ##* Create output folder when folder does not exist

    os.makedirs(os.environ['HARVEST_OUTPUT_FOLDER'], exist_ok=True)
    ##* Save input, output and filename in the harvest.env file

    output_folderfile = '{}/{}'.format(os.environ['HARVEST_OUTPUT_FOLDER'],  os.environ['HARVEST_OUTPUT_FILENAME'] )
    CreatorString(folder_filename=output_folderfile,
                  default_contents=commentMarkdown.toString(),
                  overwrite=True)

    if save_env.upper() == 'Y':
        ##* Save harvest.env in the same folder as harvest.py

        changelist = [{'name': el, 'value':os.environ[el]}
                      for el in os.environ if el.startswith('HARVEST_')]

        contents = EnvString(env_folder_filename)
        contents = UpdaterString(contents).updates(changelist)
        contents = CreatorString(folder_filename=env_folder_filename, default_contents=contents,overwrite=True)

if __name__ == "__main__":
    # execute as docker
    main()