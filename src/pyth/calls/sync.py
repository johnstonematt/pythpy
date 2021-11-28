import base64

from solana.rpc.api import Client
from solana.publickey import PublicKey

from pyth.state.oracle import OracleAccount

def load_account_bytes(client: Client, address: PublicKey) -> bytes:
    resp = client.get_account_info(pubkey=address)
    if ('result' not in resp) or ('value' not in resp['result']):
        raise Exception('Cannot load bytes.')
    data = resp['result']['value']['data'][0]
    bytes_data = base64.decodebytes(data.encode('ascii'))
    return bytes_data


def call_oracle_account(client: Client, address: PublicKey) -> OracleAccount:
    bytes_data = load_account_bytes(
        client=client,
        address=address
    )
    oracle_account = OracleAccount.parse(
        bytes_data=bytes_data
    )
    return oracle_account