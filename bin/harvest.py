
import os
from pprint import pprint

from source.ability.able import Fileable,Folderable, Inputability
from source.reader_string import ReaderString
from source.farm import Field, CommentMarkdown

def main():
    ### Harvest comments from python files in this project
    ##* Create documentation for python (.py) files
    ##* output docs to a single project_folder, eg /docs
    ##* Collect output folder name when entered by user
    default_output_folder = os.getcwd().split('/')[0:-1]
    default_output_folder.append('crop')
    default_output_folder = '/'.join(default_output_folder)
    output_folder = Inputability().get_input('Output folder', default_output_folder, hardstop=True)
    ##* Collect output filename when entered by user
    output_filename = Inputability().get_input('Output file name', 'Readme.md', hardstop=True)
    print('output folder', output_folder)
    print('output filename', output_filename)

    #if 1==1: exit(0)

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
    commentMarkdown.save('{}/{}'.format(output_folder, output_filename))

if __name__ == "__main__":
    # execute as docker
    main()