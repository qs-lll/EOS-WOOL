import os


EOS_MAINNET = os.getenv('EOS_MAINNET', 'http://127.0.0.1:8888')
SYMBOL = os.getenv('SYMBOL', 'SYS')

# BANK_CONFIG
TRANSFER_TO = os.getenv("TRANSFER_TO", 'eosmaxiodice')
TRANSFER_FROM = os.getenv("TRANSFER_FROM", '')
TRANSFER_QUANTITY = os.getenv("TRANSFER_QUANTITY", '1')
TRANSFER_MEMO = os.getenv("TRANSFER_MEMO", '1-96-omgomgwtfwtf-8BUE5Y')

TRANSFER = os.getenv('TRANSFER', 'transfer')
CONTRACT = os.getenv('CONTRACT', 'eosio.token')
# 所有的账号都使用同一个pk
PRIVATEKEY = os.getenv('PRIVATEKEY', '')
