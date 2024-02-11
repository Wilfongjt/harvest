### Harvest
##
## Create a README file from the comments found in project code.
##
import os

from able import EnvString, \
                 Inputable, \
                 StringReader, \
                 StringWriter, \
                 UpdaterString, \
                 TemplateString

from source.field import Field
from source.crop import CropMarkdown
#### Process
##### Expected
##```
## setup env ...........   + create harvest.env
##                         |     + use template when template is available
##                         |         + use <<template>> style
##                         |
## confirm env .........   + confirm <<HARVEST_INPUT_FOLDER>>
##                         + confirm <<HARVEST_OUTPUT_FOLDER>>
##                         + confirm <<HARVEST_OUTPUT_FILENAME>>
##                         |
## harvest .............   + find all files ending in '.py' or '.env'
##                         |   + find all lines that start with '##'
##                         |       + convert lines to markdown
##                         |
## save README ........... + save compiliation to 'README.md'
##                         |
## save env changes ....   + confirm env save
##                         +
##```

def get_bin_folder():
    return os.getcwd()
def get_default_input_folder():
    return os.getcwd().replace('/bin', '')
def get_default_output_folder():
    return os.getcwd()
def get_template_folder():
    return os.getcwd().replace('/bin','/source/templates')

def main():
    ##### Actual
    ##1. Setup environment
    ##    1. Load environment variables from harvest.env

    env_folder_filename = '{}/harvest.env'.format(get_bin_folder())

    ##    1. Use a template to initialize environment file

    template_folder_filename = '{}/harvest.env.tmpl'.format(get_template_folder())

    ##    1. Load environment variables into memory

    env_string = EnvString(StringReader(env_folder_filename)
                           or
                           TemplateString(StringReader(template_folder_filename)) \
                           .merge('<<HARVEST_INPUT_FOLDER>>', get_default_input_folder()) \
                           .merge('<<HARVEST_OUTPUT_FOLDER>>', get_default_output_folder())
                           )

    # save changes to environment variables

    # StringWriter(env_folder_filename, env_string)
    ##1. Confirm or Change Environment Variables
    ##    1. Collect input folder name when entered by user

    os.environ['HARVEST_INPUT_FOLDER'] = Inputable().get_input('HARVEST_INPUT_FOLDER',
                                         os.environ['HARVEST_INPUT_FOLDER'],
                                         hardstop=True)

    ##    1. Collect output folder name when entered by user

    os.environ['HARVEST_OUTPUT_FOLDER'] = Inputable().get_input('HARVEST_OUTPUT_FOLDER',
                                          os.environ['HARVEST_OUTPUT_FOLDER'],
                                          hardstop=True)

    ##    1. Collect output filename when entered by user

    os.environ['HARVEST_OUTPUT_FILENAME'] =  Inputable().get_input('HARVEST_OUTPUT_FILENAME',
                                            os.environ['HARVEST_OUTPUT_FILENAME'],
                                            hardstop=True)
    ##    1. Confirm the saving of ".env"
    save_env = Inputable().get_input('save env changes',
                                     'N',
                                     hardstop=False)

    # user feedback
    print('HARVEST_INPUT_FOLDER:   ', os.environ['HARVEST_INPUT_FOLDER'])
    print('HARVEST_OUTPUT_FOLDER:  ', os.environ['HARVEST_OUTPUT_FOLDER'])
    print('HARVEST_OUTPUT_FILENAME:',os.environ['HARVEST_OUTPUT_FILENAME'])
    ##1. Harvest
    ##    1. Include files ending with ".py", and ".env"

    file_list = Field(folder=os.environ['HARVEST_INPUT_FOLDER'],
                      ext=['.py', '.env']).traverse_folder()

    file_list = Field(os.environ['HARVEST_INPUT_FOLDER'], ['.py', '.env']).traverse_folder()

    comments = []
    commentMarkdown = CropMarkdown(lookfor='##')
    for f in file_list:
        print('field file', f)
        commentMarkdown.load(StringReader(f))

    ##    1. Create output folder when folder does not exist

    os.makedirs(os.environ['HARVEST_OUTPUT_FOLDER'], exist_ok=True)
    ##1. Save

    output_folderfile = '{}/{}'.format(os.environ['HARVEST_OUTPUT_FOLDER'],  os.environ['HARVEST_OUTPUT_FILENAME'] )
    ##    1. Save README
    ##        1. Save in the same folder as harvest.py

    StringWriter(folder_filename=output_folderfile,
                 content_string=commentMarkdown.toString())

    if save_env.upper() == 'Y':
        ##    1. Save harvest.env
        ##        1. Save in the same folder as harvest.py

        changelist = [{'name': el, 'value':os.environ[el]}
                      for el in os.environ if el.startswith('HARVEST_')]
        # load user's original env custom and other
        ##        1. Preserve user's manual changes
        contents = EnvString(StringReader(env_folder_filename))
        #print('changelist',changelist)
        ##        1. Update changes to existing environment variables
        contents = UpdaterString(contents).updates('\n'.join(changelist))
        StringWriter(folder_filename=env_folder_filename,
                     content_string=contents)
        #contents = CreatorString(folder_filename=env_folder_filename, default_contents=contents,overwrite=True)

if __name__ == "__main__":
    # execute as docker
    main()