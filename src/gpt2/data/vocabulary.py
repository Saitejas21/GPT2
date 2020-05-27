
class Vocabulary(object):
    """Vocabulary class for mapping tokens to indices.

    Arguments:
        vocab (str): Vocabulary file path.
        bos_token (str): Begin-of-sentence token name.
        eos_token (str): End-of-sentence token name.
        pad_token (str): Pad token name.
    """
    def __init__(self,
                 vocab: str,
                 bos_token: str = '<s>',
                 eos_token: str = '</s>',
                 pad_token: str = '<pad>'):
        self.bos_token = bos_token
        self.eos_token = eos_token
        self.pad_token = pad_token

        # Create vocabulary dictionary which maps from subwords to indices.
        with open(vocab, 'r', encoding='utf-8') as fp:
            self.vocab = {word: i for i, word in enumerate(fp.read().split())}

    def __getitem__(self, token: str) -> int:
        return self.vocab[token]

    @property
    def bos_idx(self):
        return self[self.bos_token]

    @property
    def eos_idx(self):
        return self[self.eos_token]

    @property
    def pad_idx(self):
        return self[self.pad_token]