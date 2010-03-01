"""
Automatically load the wordmap, if available.
"""

import cPickle
from common.file import myopen
import sys
from os.path import join

from rundir import rundir

def _wordmap_filename(language):
    import common.hyperparameters, common.options
    HYPERPARAMETERS = common.hyperparameters.read("language-model")
    return join(rundir(), "idmap.%s.include_unknown=%s.pkl.gz" % (language, HYPERPARAMETERS["INCLUDE_UNKNOWN_WORD"]))

_wordmap = {}
def wordmap(language):
    """
    Read the wordmap for a particular language.
    """
    if language not in _wordmap:
        _wordmap[language] = cPickle.load(myopen(_wordmap_filename(language)))
        _wordmap[language].str = _wordmap[language].key
    return _wordmap[language]

def write(wordmap, language):
    """
    Write the word ID map, passed as a parameter.
    """
    print >> sys.stderr, "Writing word map with %d words to %s..." % (wordmap.len, _wordmap_filename(language))
    cPickle.dump(wordmap, myopen(_wordmap_filename(language), "w"))
