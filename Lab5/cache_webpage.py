from urllib.request import urlopen
import time
class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None
        self._last_refresh = 0

    @property
    def content(self):
        if not self._content or time.time() - self._last_refresh > 24*3600:
            print("Retrieving New Page...")
            try:
                self._content = urlopen(self.url).read()
            except:
                raise ValueError('Unable to open page')
            self._last_refresh = time.time()
        return self._content

    def refresh(self):
        print("Refreshing...")
        self._content = urlopen(self.url).read()