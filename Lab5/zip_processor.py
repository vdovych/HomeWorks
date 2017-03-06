import os
import shutil
import zipfile
class ZipProcessor:
    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = "unzipped-{}".format(
            zipname[:-4])

    def _full_filename(self, filename):
        '''returns full path to file
        '''
        return os.path.join(self.temp_directory, filename)

    def process_zip(self):
        '''
        processing zip file
        '''
        self.unzip_files()
        self.process_files()
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