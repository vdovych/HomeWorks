import sys
import os
import shutil
import zipfile
from pygame import image
from pygame.transform import scale


class ZipProcessor:
    def __init__(self, zipname, processor):
        self.zipname = zipname
        self.temp_directory = "unzipped-{}".format(
            zipname[:-4])
        self.processor = processor

    def _full_filename(self, filename):
        '''returns full path to file
        '''
        return os.path.join(self.temp_directory, filename)

    def process_zip(self):
        '''
        processing zip file
        '''
        self.unzip_files()
        self.processor.process_files()
        self.zip_files()

    def unzip_files(self):
        '''
        opens zip archive
        '''
        try:
            os.mkdir(self.temp_directory)
        except FileExistsError:
            pass
        zip = zipfile.ZipFile(self.zipname)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()

    def zip_files(self):
        '''
        closes zip archive
        '''
        file = zipfile.ZipFile(self.zipname, 'w')
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(
                filename), filename)
        shutil.rmtree(self.temp_directory)


class ZipReplace(ZipProcessor):
    def __init__(self, search_string,
                 replace_string):
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self, processor):
        '''perform a search and replace on all files
            in the temporary directory'''
        for filename in os.listdir(processor.temp_directory):
            with open(processor._full_filename(filename)) as file:
                contents = file.read()
                contents = contents.replace(
                    self.search_string, self.replace_string)
            with open(
                    processor._full_filename(filename), "w") as file:
                file.write(contents)


if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).process_zip()


class ScaleZip:
    def process_files(self, processor):
        '''Scale each image in the directory to 640x480'''
        for filename in os.listdir(processor.temp_directory):
            im = image.load(processor._full_filename(filename))
            scaled = scale(im, (640, 480))
            image.save(scaled, processor._full_filename(filename))


if __name__ == "__main__":
    ScaleZip(*sys.argv[1:4]).process_zip()
