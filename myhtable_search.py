# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from htable import *
from words import get_text, words


def myhtable_create_index(files):
        
    index = htable(4011) #create empty htable with 4011 buckets

    for filename in files:
        word_list = set(words(get_text(filename))) 
        for word in word_list:
        #get the file index list which contains the word
            curr_value = htable_get(index, word)
        #if the curr_value exist, we will add the file index into the set
            if curr_value: 
                curr_value.add(files.index(filename)) 
                value = curr_value
            else:
        #if none, we will define a empty set,then add the index into the set
                value = set() 
                value.add(files.index(filename))
        #put the result back to the hash table
            htable_put(index, word, value) 
    return index


def myhtable_index_search(files, index, terms):

    matches = [] #create empty list

    for term in terms:
        term_matches = htable_get(index, term) 
        #if match is empty
        if not matches: 
            matches = term_matches
        #if match is not empty
        else:
            matches = set(matches).intersection(set(term_matches))
    #if matches is empty after checking, return empty list        
    if not matches: 
        return []
    #if matches has common index, return all files in matches
    filenames = [files[match] for match in matches] 
    
    return filenames

