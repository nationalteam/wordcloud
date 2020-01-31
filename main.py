import click
import ckiptagger
import os
import logging

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


@click.command()
@click.argument('sentence')
def main(sentence):

    ws = WordSegmentation()

    sentence_list = [sentence]
    word_sentence_list = ws.predict(sentence_list)

    for word_sentence in word_sentence_list:
        print(word_sentence)


if __name__ == "__main__":
    main()
