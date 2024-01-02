# Purpose Comments Harvest
Create and extract markdown comments.

### The Issues
* Writing coding is hard. 
* Writing useful comments is harder. 
* Writing comments that can be understood a month later might be impossible.

### The Challenges
* I hate comments.
* I don't know what to write in a comment.
* Read the code to figure it out.
* Integrating code and documentation sucks.

### The Strategies
* Keep a comment relative to the code where it appears.
* Develop sentence patterns to give your brain a rest.
* Change from the __descriptive__ style of comment to a __purpose__ based comment. 

## Descriptive vs Purpose Comments
* Descriptive comments describe what the code does. 
* Purpose comments describe what the code is intended to achieve. 

## Keep It Simple
## One Thing
__What are Markdown Comments__
Nothing special. 

### Technical vs Purpose based comments 

Markdown comments are normal single line comments with an extra hash '#'

```python
# Ignore normal comments
### Title text
## Plain text 
##__Bold test__
##* Bullet
```

__The Double Hash__ 

Identify the markdown comments with the double hash '##'
In your code, identify markdown comments with  


```python
# Ignore normal comments
### Title text
## Plain text 
##__Bold test__
##* Bullet
```
# Title text
Plain test
__Bold test__
* Bullet

Add an extra line before "Bullet"
```python
# Ignore normal comments

## Plain text 
## 
##__Bold test__
##* Bullet
```
Plain test

__Bold test__
* Bullet



Function comments
```python

class Mergable():
    ##
    ##__Mergable__
    ##* 
    def merge(self, template, nv_list):
        ##* Merge given list of name-value pairs into a given template

        for nv in nv_list:
            template = template.replace(nv['name'], nv['value'])

        return template


```
```
# 
cd harvest/bin/
python harvest
```
# Patterns
Knowing what to write is always a challenge. 
Shifting from developer brain to commenter brain is difficult.
Patterns are a useful hack to get you started.
1. the Normal pattern
1. the Markdown pattern 
2. the Script pattern
3. the Function pattern
4. the Class pattern

### Normal Pattern
Business as usual. 
Sometimes the code is just to complicated to comment in a way that doesn't require the developer to dig-in to the code.

```python
# normal comment 
```
### Identity Pattern
Identify a Markdown comment in your code. 

```python
# normal comments are still useful but are ignored during extraction

## Identify a Markdown comment with an extra hash before a normal comment
```
### Break Pattern

```python
##
```

### Title Pattern

```python
### Title Pattern
```

### Name Pattern

```python
##__Some Name__
```

### On Request Pattern

```python
##* Do something on request
```

### When Pattern
when
```python
##* Allow something when user clicks button 
```

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

__Mergable__

Render a template with user provided values
* Merge name-value pairs into a given template string on request



### Harvest 
