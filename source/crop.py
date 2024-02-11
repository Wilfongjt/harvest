#import os
import os
from able import LbUtil, FolderFileable, StringReader, CreatorString
#from source.lb_util import LbUtil
#from source.ability.dep_able import Fileable,Folderable
##
#### The Crop
class CropMarkdown(list, FolderFileable):
    ##
    ##__CropMarkdown__
    ##
    ## Collection of '##' marked comments
    ##
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
        return self

    def toString(self):
        return '\n'.join(self)

def main():

    assert(CropMarkdown() == [])
    contents = StringReader(__file__)
    assert(CropMarkdown().load(contents) != [])
    #print (CropMarkdown().load(contents).toString())

if __name__ == "__main__":
    # execute as docker
    main()