# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from htable import *
from words import get_text, words


def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """
    index = htable(4011)

    for filename in files:
        word_list = set(words(get_text(filename)))
        for word in word_list:
            curr_value = htable_get(index, word)
            if curr_value:
                curr_value.add(files.index(filename))
                value = curr_value
            else:
                value = set()
                value.add(files.index(filename))
            htable_put(index, word, value)
    return index


def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """

    matches = []

    for term in terms:
        term_matches = htable_get(index, term)
        if not matches:
            matches = term_matches
        else:
            matches = set(matches).intersection(set(term_matches))
    if not matches:
        return []
    filenames = [files[match] for match in matches]
    return filenames

