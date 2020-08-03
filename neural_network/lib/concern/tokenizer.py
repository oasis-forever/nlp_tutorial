import os
import MeCab

tagger = MeCab.Tagger(os.environ['MECAB_IPADIC_NEOLOGD'])

def tokenize(text):
    node = tagger.parseToNode(text)
    tokens = []
    while node:
        if node.surface != "":
            tokens.append(node.surface)
        node = node.next
    return tokens
