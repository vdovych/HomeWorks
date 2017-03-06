from document import *

doc = Document()
try:
    doc.save()
except UnnamedFileError:
    pass
doc.filename = 'doc'
doc.insert('a')
try:
    doc.delete()
except CharDoesNotExistError:
    pass
