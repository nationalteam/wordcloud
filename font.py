import os
from tempfile import gettempdir
from urllib.request import urlretrieve

url = r"""https://raw.githubusercontent.com/narumiruna/ZA-Cloud/master/NotoSerifCJKtc-Regular.otf"""


def get_default_font():
    path = os.path.join(gettempdir(), 'NotoSerifCJKtc-Regular.otf')

    if not os.path.exists(path):
        urlretrieve(url, filename=path)

    return path
