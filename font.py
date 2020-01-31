import os
from tempfile import gettempdir
from urllib.request import urlretrieve


def get_default_font():
    url = r"""https://raw.githubusercontent.com/powerline/fonts/master/SourceCodePro/Source%20Code%20Pro%20for%20Powerline.otf"""

    path = os.path.join(gettempdir(), 'source_code_pro_for_powerline.otf')

    if not os.path.exists(path):
        urlretrieve(url, filename=path)

    return path
