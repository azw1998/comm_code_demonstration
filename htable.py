"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""



def htable(nbuckets):
    """Return a list of nbuckets lists"""
    return [[] for _ in range(nbuckets)]


def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    if type(o) == int:
        return o
    if type(o) == str:
        h = 0
        for c in o:
            h = h*31 + ord(c)
        return h
    return


def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the index of the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """


def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket inicated by key and then append (key,value)
    to that bucket if the (key,valued) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, anything!
    """

    bucket = table[hashcode(key) % len(table)]

    if bucket:
        for association in bucket:
            if association[0] == key:
                bucket.remove(association)
                break
    bucket.append((key, value))

def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    bucket = table[hashcode(key) % len(table)]

    for association in bucket:
        if association[0] == key:
            return association[1]
    return


def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    The output looks like:
        0000->
        0001->
        0002->
        0003->parrt:99
        0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """
    bucket_str_list = []
    for i in range(len(table)):
        bucket_key_values = []
        for association in table[i]:
            if association and association[0] and association[1]:
                bucket_key_values.append(str(association[0]) + ':' + str(association[1]))
        bucket_str_list.append('000' + str(i) + '->' + ', '.join(bucket_key_values))
    return '\n'.join(bucket_str_list) + '\n'


def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    key_values = []

    for bucket in table:
        if bucket:
            for association in bucket:
                key = association[0]
                value = association[1]
                key_values.append(str(key) + ':' + str(value))
    return '{' + ', '.join(key_values) + '}'
