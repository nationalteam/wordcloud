import logging
import os

import ckiptagger
import click
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from font import get_default_font

logger = logging.getLogger(__name__)


class WordSegmentation(object):
    def __init__(self, root='./', disable_cuda=False):
        self.root = root
        self.data_dir = os.path.join(self.root, 'data')
        self.disable_cuda = disable_cuda
        self.model = self.load_model()

    def download_model_files(self):
        if not os.path.exists(self.data_dir):
            logger.info('%s not exists', self.data_dir)
            ckiptagger.data_utils.download_data_gdown(self.path)
        else:
            logger.info('%s exists', self.data_dir)

    def load_model(self):
        self.download_model_files()
        return ckiptagger.WS(self.data_dir, disable_cuda=self.disable_cuda)

    def predict(self, *args, **kwargs):
        return self.model(*args, **kwargs)


def load_lines(f):
    with open(f, 'r') as fp:
        for line in fp.readlines():
            yield line.strip()


@click.command()
@click.option('-t', '--text-file', default='default.txt')
@click.option('-o', '--output-file', default='cloud.png')
@click.option('--show', is_flag=True)
def main(text_file, output_file, show):

    # load text file
    lines = list(load_lines(text_file))

    # word segment
    ws = WordSegmentation()
    word_sentence_list = ws.predict(lines)

    words = []
    for word_sentence in word_sentence_list:
        for word in word_sentence:
            words.append(word)

    # plot word cloud
    text = ' '.join(words)
    wc = WordCloud(font_path=get_default_font(),
                   relative_scaling=.75,
                   width=1280,
                   height=720).generate(text)
    if output_file:
        wc.to_file('za_cloud.png')

    if show:
        plt.imshow(wc)
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    main()
