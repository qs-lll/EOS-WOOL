import time

import requests

from ServerConfig import *
from eospy import cleos

ce = cleos.Cleos(url=EOS_MAINNET)

def transfer():
    response = ce.transfer(PRIVATEKEY, TRANSFER_FROM, TRANSFER_TO, str(('%.4f ' + SYMBOL) % float(TRANSFER_QUANTITY)),
                TRANSFER_MEMO)
    print(response)

if __name__ == '__main__':
    while(True):
        try:
            transfer()
        except BaseException as e:
            print(e)
        finally:
            time.sleep(1)
