# Harvest

 Compile "comments" from files in the harvest project

* Compile comments into a single file
* Load environment variables from harvest.env
* Use a template to initialize the harvest.env
* Load environment variables into memory
* Collect input folder name when entered by user
* Collect output folder name when entered by user
* Collect output filename when entered by user
* Include files ending with ".py", and ".env"
* Create output folder when folder does not exist
* Save input, output and filename in the harvest.env file
* Save harvest.env in the same folder as harvest.py

## Environment
* HARVEST_INPUT_FOLDER defines where to get input
* HARVEST_OUTPUT_FOLDER defines where to send output
* HARVEST_OUTPUT_FILENAME defines the name of the output file

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