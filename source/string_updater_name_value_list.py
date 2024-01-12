from source.string_updater_name_value import NameValue_UpdaterString

class NameValueList_UpdaterString(NameValue_UpdaterString):
    ##
    ##__NameValueList_UpdaterString__
    ##
    def update(self, nv_list):
        ## Update multiple name-value pairs

        contents = self

        for chg in nv_list:

            contents = super().update(chg['name'],chg['value'])

        return NameValue_UpdaterString(contents)


def main():
    print('TBD NameValueList_UpdaterString ')

if __name__ == "__main__":
    # execute as docker
    main()