import newed25519 as ed25519
import binascii
spendkey_hex = b'77fadbe52830d30438ff68036374c0e3fb755d0d983743bcbfb6a45962f50a09'
mininero_pub_spend = ed25519.publickey(binascii.unhexlify(spendkey_hex))
print('pub key: ' + str(binascii.hexlify(mininero_pub_spend)))