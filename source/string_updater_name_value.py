from source.string_updater import UpdaterString

class NameValue_UpdaterString(UpdaterString):
    ##
    ##__NameValue_UpdaterString__
    ##
    def update(self, key, value):
        ## Update a single name-value pair

        key = str(key).strip()

        temp_content = []
        found = False
        for ln in self.split('\n'):
            if ln.strip().startswith(key):
                found = True
                temp_content.append('{}={}'.format(key, value))
            else:
                temp_content.append(ln)
        if not found:
            # insert at end
            temp_content.append('{}={}'.format(key, value))

        contents = '\n'.join(temp_content)

        return NameValue_UpdaterString(contents)

def main():
    print('TBD NameValue_UpdaterString ')

if __name__ == "__main__":
    # execute as docker
    main()