#!/usr/bin/env

MAX_SPLIT_ATTEMPTS = 30

import sha3
import electrum
import random
import newmininero as mininero # it would be nice to use mainstream ed25519 and b58 libraries instead
import binascii
import things
import hashlib

config = {
    'coinUnitPlaces': 12,
    'coinSymbol': 'XMR',
    'coinName': 'Monero',
    'coinUriPrefix': 'monero:',
    'addressPrefix': b'12',
    'version': 18
}

def swap32(x):
    swappedbytes = [bytes([i]) for i in x[::-1]]
    return b''.join(swappedbytes)


class Wallet():
    def __init__(self):
        self.language = 'english'


    def calculate_fee(self, fee_per_kb, byte_count, fee_multiplier):
        kB = (bytes + 1023)
        return kB * fee_per_kb * fee_multiplier


    def generate_keys(self, recovery_bytes=None):
        if not recovery_bytes:
            recovery_bytes = random.SystemRandom().getrandbits(256)
        sec = things.sc_reduce32(recovery_bytes)
        pub = mininero.publicFromSecret(sec)
        return sec, pub

    def recover_from_seed(self, seed):
        seedbytes = electrum.words_to_bytes(seed)
        self.recover_from_bytes(seedbytes)

    def _set_public_address(self):
        prefix = b'\x12'
        pubspend = self.spendkeys[1]
        pubview = self.viewkeys[1]
        buf = prefix + pubspend + pubview
        bufhex = binascii.hexlify(buf)
        h = sha3.keccak_256(buf).hexdigest().encode('ascii')
        checksum = h[0:8]
        bufhex += checksum
        self.public_address = things.b58encode(bufhex)
        print(self.public_address)
        return self.public_address

    def recover_from_bytes(self, recovery_bytes):
        spendkeys = self.generate_keys(recovery_bytes)
        newbytes = sha3.keccak_256(recovery_bytes).digest()
        viewkeys = self.generate_keys(newbytes)

        self.spendkeys = spendkeys
        self.viewkeys = viewkeys
        self._set_public_address()


    def is_deterministic(self):
        # apparently the private viewkey is just the sha3 of the private spend key
        return sha3.keccak_256(self.keys.private.spend).digest() == self.keys['private_view']


    def get_seed(self):
        '''
        Using the wallet language, determine the electrum-style seed based on the private spend key
        '''

        if not self.is_deterministic():
            print("This is not a deterministic wallet")
            return false

        if not self.language:
            print("seed_language not set")

        return electrum.bytes_to_words(self.keys.private.spend, self.language)