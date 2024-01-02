
import os
from pprint import pprint
#from source.utility_script import UtilityRecorder
#from source.lb_template_markdown import Lb_MarkDownString #LbDocComments
#from source.lb_reader_string import ReaderString
#from source.lb_util import LbUtil
from source.ability.able import Fileable,Folderable
from source.reader_string import ReaderString
from source.farm import Field, CommentMarkdown

# from source.lb_template_saveable import SavableString, Lb_SaveableTemplate

def main():
    ### Harvest comments from python files in this project
    ##* Create documentation for python (.py) files

    from source.lb_util import LbUtil

    ##* output docs to a single project_folder, eg /docs

    output_folder = os.getcwd().split('/')[0:-1]
    output_folder.append('crop')
    output_folder = '/'.join(output_folder)

    print('output', output_folder)

    search_folder = os.getcwd().replace('/bin','')
    file_list = Field(search_folder, '.py').traverse_folder()
    #print('file_list', file_list)
    comments = []
    commentMarkdown = CommentMarkdown(lookfor='##')
    for f in file_list:
        print('file', f)
        commentMarkdown.load(ReaderString(f))

    ##* create output folder when folder does not exist

    Folderable().makedirs(output_folder)
    ##* Finally, Save to file
    ##* overwrite when file exists
    commentMarkdown.save('{}/Readme.md'.format(output_folder))

if __name__ == "__main__":
    # execute as docker
    main()