
# Harvest 
Harvest simplifies the maintenance of documentation.

## Why do this?
Have you ever come back to some code and not have a clue as to what it does or why you wrote it. 
Of course, you can check the documentation but did you remember to update the documentation. 
And where is the code that implements that new feature?

## Get started
1. clone the harvest repo
2. install python 3.9.6
3. install the "able" library, run the scripts/05.install.from.gh.sh
3. run bin/harvest.py
4. accept the defaults when askded for HARVEST_INPUT_FOLDER, HARVEST_OUTPUT_FOLDER, and HARVEST_OUTPUT_FILENAME values
4. type Y to save these values in the harvest.env file
5. the ReadMe.md is generated in the /bin folder

## How it works
1. Markup your files with specialized comments. At a minimum, replace your single line comments "#" with "##"
2. Run the harvest script (bin/harvest.py) and generate a [Readme.md](bin/ReadMe.md) file

### File Markup

```python

# Normally commented lines are ignored by Harvest.
# Double hashed comments are read and appended into a readme.md
# Try adding markdown to your double hash comments 
# Use "## " to add a blank line to your output 
class Mergable():
    ##
    ## __Mergable__
    ## Render a template with user provided values
    def merge(self, template, nv_list):
        ##
        ## * Merge one or more values into a given template on request
        # replace found names with values by iteration 
        for nv in nv_list:
            template = template.replace(nv['name'], nv['value'])

        return template
```
Harvest renders

>__Mergable__
> 
> _Render a template with user provided values_
>
>* Merge one or more values into a given template on request
<hr>



