#!/usr/bin/env

MAX_SPLIT_ATTEMPTS = 30

import sha3
import electrum



class Wallet():
    def __init__(self):
        self.language = 'english'

    def calculate_fee(self, fee_per_kb, byte_count, fee_multiplier):
        kB = (bytes + 1023)
        return kB * fee_per_kb * fee_multiplier

    def generate(self, seed):

    def is_deterministic(self):
        # apparently the private viewkey is just the sha3 of the private spend key
        return sha3.sha3_256(self.keys.private.spend).digest() == self.keys.private.view
        

    def get_seed(self):
        '''
        Using the wallet language, determine the electrum-style seed based on the private spend key
        '''

        if !self.is_deterministic():
            print("This is not a deterministic wallet")
            return false

        if !self.language:
            print("seed_language not set")

        return electrum.bytes_to_words(self.keys.private.spend, self.language)