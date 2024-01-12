#### The Shed
##
## Maintain the "harvest.env" file
class UpdaterString(str):
    ##
    ##__UpdaterString__
    ##
    def update(self, key, new_line):
        ## Replace line containing key with a new line
        ##* eg "A big dog" -> "A big cat"
        key = str(key).strip()

        temp_content = []
        found = False
        for ln in self.split('\n'):
            if key in ln:
                found = True
                temp_content.append(new_line)
            else:
                temp_content.append(ln)
        if not found:
            # insert at end
            temp_content.append(new_line)

        contents = '\n'.join(temp_content)

        return UpdaterString(contents)

## Extentions


def main():
    str_value = '''
    #
    # Environment
    
    '''.replace('  ','') # remove leading spaces
    expected_value = '''
        #
        # File system

        '''.replace('  ', '')  # remove leading spaces

    contents = UpdaterString(str_value)
    contents = UpdaterString(contents).update('Environment', '# File system')
    print('contents', contents)
    assert(contents == expected_value)

if __name__ == "__main__":
    # execute as docker
    main()