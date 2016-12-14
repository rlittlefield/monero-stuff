# electrum!

SEED_LENGTH = 24

import electrum_english
import math


def find_seed_language(words, has_checksum):
    # only english right now
    language = electrum_english.language
    matched_indices = []
    for word in words:
        if word not in language['words']:
            raise Exception('word not present in language')
        matched_indices.append(language['words'].index(word))
    return language, matched_indices


def words_to_bytes(word_string):
    words = [i.strip() for i in word_string.split(' ') if i]
    word_count = len(words)

    if word_count != SEED_LENGTH / 2 and word_count != SEED_LENGTH and word_count != (SEED_LENGTH + 1):
        raise Exception('seed is not correct length')

    has_checksum = word_count == SEED_LENGTH + 1
    checksum_word = None
    if has_checksum:
        checksum_word = words.pop()

    language, matched_indices = find_seed_language(words, has_checksum)
    word_list_length = language['word_list_length']

    result = b''

    for i in range(0, len(matched_indices), 3):
        indices = matched_indices[i:i+3]
        if len(indices) < 3:
            break
        w1, w2, w3 = indices

        val = w1 + word_list_length * (((word_list_length - w1) + w2) % word_list_length) + \
            word_list_length * word_list_length * (((word_list_length - w2) + w3) % word_list_length)

        if not (val % word_list_length == w1):
            raise Exception("this doesn't work")

        result += val.to_bytes(4, 'little')

    if word_count == SEED_LENGTH / 2:
        result += result

    return result




