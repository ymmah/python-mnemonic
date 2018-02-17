#!/usr/bin/env python

from __future__ import print_function

import sys
import os
from bip32utils import BIP32Key
from mnemonic import Mnemonic

WORDLIST = os.path.join(os.getcwd(), "mnemonic/wordlist/english.txt")

def assert_wordlist(words):
    ''' Check the given words are contained in the wordlist
    '''
    f = open(WORDLIST, 'r')
    wordlist = set(w.rstrip() for w in f.readlines())
    f.close()
    for w in words:
        if w not in wordlist:
            sys.exit("ERR: %s not in wordlist" % w)


if __name__ == '__main__':
    ''' adapted from generate_vectors.py to convert the xpriv to the passphrase
    '''

    words = sys.argv[1:]
    assert len(words) in [12, 13, 24, 25]

    if len(words) == 12:
        assert_wordlist(words)
        phrase = ' '.join(words)
        passphrase = ""
    elif len(words) == 13:
        assert_wordlist(words[:-1])
        phrase = ' '.join(words[:-1])
        passphrase = words[12]
    elif len(words) == 24:
        assert_wordlist(words)
        phrase = ' '.join(words)
        passphrase = ""
    else:
        assert_wordlist(words[:-1])
        phrase = ' '.join(words[:-1])
        passphrase = words[24]

    print("\nusing phrase: '%s'" % phrase)
    print("using passphrase: '%s'" % passphrase)


    seed = Mnemonic.to_seed(phrase, passphrase=passphrase)
    xpriv = BIP32Key.fromEntropy(seed).ExtendedKey()
    print("\nxpriv: %s" % xpriv)
