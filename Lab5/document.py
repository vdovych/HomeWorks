class CursorOutOfRangeError(Exception):
    pass
class CharDoesNotExistError(Exception):
    pass
class UnnamedFileError(Exception):
    pass
class NotCharError(Exception):
    pass


class Document:
    '''
    Represents text document
    '''
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        '''
        obvious
        '''
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor += 1

    def delete(self):
        '''
        obvious
        '''
        try:
            del self.characters[self.cursor.position]
        except:
            raise CharDoesNotExistError

    def save(self):
        '''
        obvious
        '''
        if not self.filename:
            raise UnnamedFileError
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()

    @property
    def string(self):
        return "".join(self.characters)


class Cursor:
    '''
    Represent cursor in text file
    '''
    def __init__(self, document):
        self.document = document
        self.position = 0
    def forward(self):
        self.position += 1
        if self.position > len(self.document.characters):
            raise CursorOutOfRangeError
    def back(self):
        self.position -= 1
        if self.position < 0:
            raise CursorOutOfRangeError
    def home(self):
        while self.document.characters[
                    self.position-1] != '\n':
            self.position -= 1
            if self.position == 0:
                break

    def end(self):
        while self.position < len(self.document.characters
                                  ) and self.document.characters[
            self.position] != '\n':
            self.position += 1

class Character:
    '''
    Represents a charactes with some style
    '''
    def __init__(self, character,
                 bold=False, italic=False, underline=False):
        if not len(character) == 1:
            raise NotCharError
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.characte
