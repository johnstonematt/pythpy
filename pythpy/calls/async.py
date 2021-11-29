import asyncio
import base64

from solana.rpc.async_api import AsyncClient
from solana.publickey import PublicKey

from pythpy.state.oracle import OracleAccount


async def load_account_bytes(client: AsyncClient, address: PublicKey) -> bytes:
    resp = await client.get_account_info(pubkey=address)
    if ('result' not in resp) or ('value' not in resp['result']):
        raise Exception('Cannot load bytes.')
    data = resp['result']['value']['data'][0]
    bytes_data = base64.decodebytes(data.encode('ascii'))
    return bytes_data


async def call_oracle_account(client: AsyncClient, address: PublicKey) -> OracleAccount:
    bytes_data = await load_account_bytes(
        client=client,
        address=address
    )
    oracle_account = OracleAccount.parse(
        bytes_data=bytes_data
    )
    return oracle_account