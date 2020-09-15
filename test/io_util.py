import io

'''
StringIO provides a convenient means of working with text in memory using the file API (read, write. etc.).

ref: https://pymotw.com/2/StringIO/
'''

class StringIO(io.StringIO):
    """
    A "safely" wrapped version
    """

    def __init__(self, value=''):
        value = value.encode('utf8', 'backslashreplace').decode('utf8')
        io.StringIO.__init__(self, value)

    def write(self, msg):
        io.StringIO.write(self, msg.encode('utf8', 'backslashreplace').decode('utf8'))

