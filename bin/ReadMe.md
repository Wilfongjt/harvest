# Harvest

 Create a README file from the comments found in project code.

## Process
### Expected
```
 setup env ...........   + create harvest.env
                         |     + use template when template is available
                         |         + use <<template>> style
                         |
 confirm env .........   + confirm <<HARVEST_INPUT_FOLDER>>
                         + confirm <<HARVEST_OUTPUT_FOLDER>>
                         + confirm <<HARVEST_OUTPUT_FILENAME>>
                         |
 harvest .............   + find all files ending in '.py' or '.env'
                         |   + find all lines that start with '##'
                         |       + convert lines to markdown
                         |
 save README ........... + save compiliation to 'README.md'
                         |
 save env changes ....   + confirm env save
                         +
```
### Actual
1. Setup environment
    1. Load environment variables from harvest.env
    1. Use a template to initialize environment file
    1. Load environment variables into memory
1. Confirm or Change Environment Variables
    1. Collect input folder name when entered by user
    1. Collect output folder name when entered by user
    1. Collect output filename when entered by user
    1. Confirm the saving of ".env"
1. Harvest
    1. Include files ending with ".py", and ".env"
    1. Create output folder when folder does not exist
1. Save
    1. Save README
        1. Save in the same folder as harvest.py
    1. Save harvest.env
        1. Save in the same folder as harvest.py
        1. Preserve user's manual changes
        1. Update changes to existing environment variables

## Environment
* HARVEST_INPUT_FOLDER defines where to get input
* HARVEST_OUTPUT_FOLDER defines where to send output
* HARVEST_OUTPUT_FILENAME defines the name of the output file

## The Field

__Field__

 List of files, folders and subfolders

* Ignore specific files and/or folders (eg ['.DS_Store', '.git', '.gitignore', '.idea']) on evaluation
* List of folders, subfolder and files in a given folder on request

## The Crop

__CropMarkdown__

 Collection of '##' marked comments

* Overide the "#" default character used to identify a single line comment
 collect all the markdwon comments from a string on request
* remove leading spaces for markdown legibility
* replace first occuance of "#" in markdown comment