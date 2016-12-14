import electrum
import monerowallet

expected_spend = '77fadbe52830d30438ff68036374c0e3fb755d0d983743bcbfb6a45962f50a09'
expected_view = '6f8cde01cd7fd657c89538815d4a87676762f720f079e522833fd1b55e493f01'

expected_address = '42Cb82LBUhY7g5NGsGmb9FPNXXeK6G9XhRw3rVjYwEL73KBjZkv61h4UeuMuC8sTZQ4AGnqKgdAU6g9MFRF83APMEW2Wb6o'


seed = 'awning ramped obedient frown vaults voice dash sunken talent myriad soggy pumpkins buffet vigilant yields foggy wayside rabbits unplugs sarcasm behind lopped tycoon uttered frown'


wallet = monerowallet.Wallet()
wallet.recover_from_seed(seed)
address = wallet.public_address
