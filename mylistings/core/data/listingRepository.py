import os


class ListingRepository(object):
    # Initializer / Instance Attributes

    def __init__(self, where, name, delimiter='\n'):
        self.data = list()

        self.where = where
        self.name = name
        self.delimiter = delimiter

        if not os.path.exists(self.where):
            os.makedirs(self.where)

        self.fileurl = where + '/' + name + '.dat'

        self.reload()

    def reload(self):
        try:
            file = open(self.fileurl, 'r')
            self.data = file.read().split(self.delimiter)
            file.close()
        except FileNotFoundError:
            file = open(self.fileurl, 'x')
            file.close()

    def add(self, value):
        file = open(self.fileurl, 'a')

        if len(self.data) > 0:
            file.write(self.delimiter + value)
        else:
            file.write(value)

        file.close()
        self.data.append(value)
