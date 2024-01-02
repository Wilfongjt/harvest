# Harvest comments from python files in this project
* Create documentation for python (.py) files
* output docs to a single project_folder, eg /docs
* create output folder when folder does not exist
* Finally, Save to file
* overwrite when file exists
# Abilities

__Appendable__

 Control ablity to append new items to document

* get appendable state on request
* set appendable state on request

__ClassNameable__

 Enable the use of classname for reference

* Get Class Name on request

__Clientable__

 Enable reference to the client folder
* get client folder on request

__Datable__

 Provide a list of name-value pairs for template substitution
* eg [{name: '', value: ''},...]
* retrieve a specific name-value pair on request
* retrieve all name-value pairs on request
* set name-value pairs on request

__Developable__

 Enable reference to the Development folder
* Retrieve the development folder on request

__Failable__

 Enable a fail flag
* provide a "failed" flag
* provide a list of failure mesages
* set failure and add failed message on request
* Provide a hard failure when failed

__Fileable__

 Enable Read from and Write to file for object
* provide folder and filename attributes
* read file contents given a folder and filename
* write contents of object to a file
* contents are inherited from the

__Folderable__

 Allow folder interactions
* change actual folder on request
* track last actual folder when folder is changed
* retrieve the last folder visited on request
* track the last folder on request
* provide a list of files for a given folder
* determine if folder exists on request
* create folders on request

__Mergable__

 Render a template with user provided values

* Merge name-value pairs into a given template string on request

__ProjectNameable__

 Enable reference to the project name
* retrive the GitHub project name from the project_folder

__ProjectFolderable__

 Enable reference to Project folder
* project project_folder ends with the GITHUB project name

__Recordable__


* Record a message
* Retrieve recorded step
* Convert JSON Object to String
* eg {a:1, b:2} to (a, b)

__Resultable__
 seperately keep track of results
* provide dictionary of results
* retrieve specific result on request
* retrieve all results on reauest

__Saveable__

 handle the output folder and filename
* set project_folder and filename from single string
* Set project_folder name on request
* Get project_folder name on request
* Set Filename on request
* Get filename on request

__Taskable__

 Create some legibility for code maintenance
* provide interface for Task
* create
* read
* update
* delete
* validate task inputs
* validate task output

__Workspaceable__
 Enable reference to workspace folder
* retrieve the workspace folder on request

# The Farm

__Field__

 Make a list of files in a folder and its subfolders
* ignore specific files and folder on evaluation
* Make a list of folders and files in a given folder on request
* Collect files via recursion on request

__CommentMarkdown__

 Collection of all markdown comments
* Overide the "#" default character used to identify a single line comment
 collect all the markdwon comments from a string on request
* remove leading spaces for markdown legibility
* replace first occuance of "#" in markdown comment
## String
__ReaderString__
* open a file and read contents into string

## Utility
__LbUtil__
* Copy source project_folder and files on request
* Copy fails when source project_folder doesnt exist ... [x] has test
* Copy fails when destination project_folder is contained in source project_folder ... [x] has test
* dont overwrite destination project_folder when found ... [x] has test
* copy source project_folder, subfolders, and files to destination project_folder when source project_folder is found ... [x] has test
* return LbUtil ... [x] has test
* Create all folders in a given path on request
* create all folders when needed ... [x] has test
* return LbUtil ... [x] has test
* Get the Current Folder Name on request
* remove "_scripts" project_folder name when found
* return str
* Delete file on request
* delete file when project_folder and file are found ... [x] has test
* skip file delete when project_folder and file are NOT found ... [x] has test
* return LbUtil ... [x] has test
* Delete project_folder on request
* remove all files and folders in project_folder ... [x] has test
* return LbUtil ... [x] has test
* Delete all files in a project_folder on request
* Delete all files when files are found in a project_folder ... [x] has test
* return LbUtil ... [x] has test
* Get an LbEnvironment Value by name
* use name to find name in os.environ
* return value when found ... [x] has test
* return "TBD" when not found ... [x] has test
* returns str ... [x] has test
* Calculate the age of a file
* age is system datetime - file datetime ... no test
* age is greater than or equal to zero ... [x] has test
* returns a float  ... [x] has test
* Test if a given project_folder and file exist on request
* file exists when project_folder exists and file exists ... [x] has test
* return bool ... [x] has test
* Test if a given project_folder and file exist on request
* file exists when project_folder exists and file exists ... [x] has test
* return bool ... [x] has test
* Test if a given project_folder exists on request
* project_folder exists when found on drive ... [x] has test
* returns bool ... [x] has test
* Get file extension on request
* return extension/string ... [x] has test
* Get List of File Names on request
* return [] when project_folder is None ... [x] has test
* returns [] when project_folder NOT found ... [x] has test
* returns [] when no files found ... [ ] has test
* return all files when ext = "*" ... [x] has test
* return files when file has specified extention ... [x] has test
* prefix with a project_folder name
* return list of filenames when files found [x] has test
* Get List of Folder Names on request
* return [] when project_folder is None ... [x] has test
* returns [] when project_folder NOT found ... [x] has test
* returns [] when no folders found ... [x] has test
 return list ... [x] has test
__Check for empty file on request__
* empty when project_folder is None
* empty when filename is None
* empty when project_folder not found
* empty when file is not found
* empty when size of file is 0
* file is empty when has no lines ... [ ] has test
* not empty when size of file is NOT 0