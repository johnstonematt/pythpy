# Pyth Network

A basic Python framework for reading and decoding data regarding the Pyth network
oracles.

## Install
```
pip3 install pythpy
```
## Setup

```python
import pythpy
from solana.rpc.api import Client

# use a Solana client to get Pyth oracle data
solana_client = Client(
    endpoint='https://api.mainnet-beta.solana.com',
    commitment='confirmed'
)
# public address for the Pyth SOL oracle
sol_oracle_address = 'H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG'
oracle_account_info = pythpy.call_oracle_account(client=solana_client, address=sol_oracle_address)
# view the info
print(oracle_account_info)
```
Output:
```python
{
    "magic": 2712847316,
    "version": 2,
    "oracle_type": 3,
    "size": 1872,
    "price_type": 1,
    "exponent": -8,
    "num_component_prices": 17,
    "num_quoters": 15,
    "last_slot": 109163611,
    "valid_slot": 109163610,
    "twap": {
        "value": 188.081046,
        "fraction": {
            "numerator": 4446404127,
            "denominator": 2364089437
        }
    },
    "twac": {
        "value": 0.10387786,
        "fraction": {
            "numerator": 2455765564,
            "denominator": 2364089437
        }
    },
    "drv1": 1e-08,
    "drv2": 3e-08,
    "product_account_key": "ALP8SdU9oARYVLgLR7LrqMNCYBnhtnQz1cj6bwgwQmgj",
    "next_price_account_key": "11111111111111111111111111111111",
    "previous_slot": 109163609,
    "previous_price": 189.912598,
    "previous_confidence": 0.142106,
    "drv3": 0.0,
    "aggregate": {
        "price": 189.914705,
        "confidence": 0.15314,
        "status": 1,
        "corporate_action": 0,
        "publish_slot": 109163611
    },
    "price_components": [
        {
            "price": 189.922,
            "confidence": 0.074,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163603
        },
        {
            "price": 189.9655,
            "confidence": 0.0695,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163605
        },
        {
            "price": 189.9125,
            "confidence": 0.03348694,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163603
        },
        {
            "price": 189.9125,
            "confidence": 0.03348694,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163603
        },
        {
            "price": 189.801,
            "confidence": 0.0075,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163604
        },
        {
            "price": 189.801,
            "confidence": 0.0075,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163604
        },
        {
            "price": 189.90375,
            "confidence": 0.0875,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163604
        },
        {
            "price": 189.90375,
            "confidence": 0.0875,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163604
        },
        {
            "price": 189.8,
            "confidence": 0.22,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163604
        },
        {
            "price": 189.8,
            "confidence": 0.22,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163604
        },
        {
            "price": 189.94324999,
            "confidence": 0.0945,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163603
        },
        {
            "price": 189.94975,
            "confidence": 0.0945,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163604
        },
        {
            "price": 189.9695,
            "confidence": 0.0915,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163592
        },
        {
            "price": 189.8795,
            "confidence": 0.0915,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163604
        },
        {
            "price": 189.945,
            "confidence": 0.224,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163605
        },
        {
            "price": 189.945,
            "confidence": 0.224,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163605
        },
        {
            "price": 190.00769337,
            "confidence": 0.09500384,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163605
        },
        {
            "price": 190.00769337,
            "confidence": 0.09500384,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163605
        },
        {
            "price": 189.9665,
            "confidence": 0.08199159,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163603
        },
        {
            "price": 189.9665,
            "confidence": 0.08199159,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163603
        },
        {
            "price": 189.9175,
            "confidence": 0.0328868,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163603
        },
        {
            "price": 189.9175,
            "confidence": 0.0328868,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163603
        },
        {
            "price": 189.94345807,
            "confidence": 0.09032811,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163605
        },
        {
            "price": 189.94345807,
            "confidence": 0.09032811,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163605
        },
        {
            "price": 189.94001131,
            "confidence": 0.12145504,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163605
        },
        {
            "price": 189.94001131,
            "confidence": 0.12145504,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163605
        },
        {
            "price": 189.90292767,
            "confidence": 0.08596382,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163603
        },
        {
            "price": 189.90292767,
            "confidence": 0.08596382,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163603
        },
        {
            "price": 189.95925,
            "confidence": 0.32675,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163605
        },
        {
            "price": 189.95925,
            "confidence": 0.32675,
            "status": 1,
            "corporate_action": 0,
            "publish_slot": 109163605
        }
    ]
}
```
