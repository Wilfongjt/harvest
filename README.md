# Purpose Comments Harvest
Create and extract markdown comments.

### The Issues
* Writing code is hard. 
* Writing useful comments is harder. 
* Writing comments that can be understood a month later might be impossible.

### The Challenges
* I hate comments.
* I don't know what to write in a comment.
* I don't want to read the code to figure it out.
* Integrating code and documentation sucks.

### The Strategies
* Keep a comment relative to the code where it appears.
* Develop sentence patterns to give your brain a rest.
* Change from the __descriptive__ style of comment to a __purpose__ written comment. 
* Enhance the comment with markdown markup language

__What is a "Markdown Comment"__

Markdown comments are code comments formated with markdown.
* Markdown comments are written in markdown markup.
* Markdown comments are single line comments.
* Markdown comments are lines that start with double hashes i.e., "##"
* Definition by example,
    ```python
    # not a markdown comment
    
    ## a markdown comment
    ##__a markdown comment__
    ##~~a markdown comment~~
    ### a markdown comment
    #### a markdown comment
    ##* a markdown comment
    ``` 

__The Double Hash__, ##

A markdown comment is a line that starts with a double hash i.e., ##

<hr>

# Styles

| style                  | comment         | markdown      |
|------------------------|-----------------|---------------|
| no-style               | # a comment     |               |
| normal                 | ## a comment    | a comment     |
| A first-level heading  | ### a Title     | # a Title     |
| A second-level heading | #### a Subtitle | ## a Subtitle |
| A bullet               | ##* one         | * one         |
| A break                | ##              |               |              


# Patterns

Patterns are applied styles with meaning.
Knowing what to write is always a challenge. 
Shifting from developer brain to commenter brain is difficult.
Patterns are a useful hack to get you started.

| Pattern     | Code Comment                                  | Markdown                                    | Meaning                                                                                                                                                                                     |
|-------------|-----------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Descriptive | "# some comment"                              |                                             | Business as usual. Sometimes the code is just to complicated to comment in a way that doesn't require the developer to dig-in to the code. A descriptive comment doesnt convert to markdown |
| Normal      | "## Some comment"                             | Some comment                                |                                                                                                                                                                                             |
| Break       | "##"                                          | " "                                         | Breaks are important for legibility, especially when using markdown in your comments.                                                                                                       |                                                                                                                                                                                            |  
| Title       | "### A Title"                                 | "# A Title"                                 |                                                                                                                                                                                             |
| Name        | "##\__Some Name__"                            | "\__Some Name__"                            | Use for class names                                                                                                                                                                         |
| Bullet      | "##* Some Text"                               | "* Some Text "                              |                                                                                                                                                                                             |
| On Request  | "##* Do something on request"                 | "* Do something on request"                 | Locate and define a method or function                                                                                                                                                      |
| When        | "##* Allow something when user clicks button" | "* Allow something when user clicks button" | Locate and describe an implementation of intended feature                                                                                                                                   |


<hr>

## Descriptive vs Purpose Comments
* Descriptive comments describe what the code does. 
* Purpose comments describe what the code is intended to achieve. 

### Example
The actual code

```python
class Mergable():
    ##
    ##__Mergable__
    ## Render a template with user provided values
    def merge(self, template, nv_list):
        ##
        ##* Merge name-value pairs into a given template string on request
        # replace found names with values by iteration 
        for nv in nv_list:
            template = template.replace(nv['name'], nv['value'])

        return template
```
The expected output

>__Mergable__
> 
>Render a template with user provided values
>* Merge name-value pairs into a given template string on request

<hr>

### Bigger Example 

Using the bin/harvest.py script, I've generated [crop/Readme.md](./crop/Readme.md) 

<hr>

### Harvest 
Harvest is a python script to generate a Readme.md file. 

