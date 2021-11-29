import json

from typing import List
from construct import Struct, Int64ul, Int32ul, GreedyRange, Container, Int32sl

from solana.publickey import PublicKey

from pyth.layouts import PUBLIC_KEY_LAYOUT
from pyth.state.core import StateCore


class Fraction(StateCore):
    layout = Struct(
        'numerator' / Int64ul,
        'denominator' / Int64ul
    )

    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator

    @classmethod
    def from_container(cls, container: Container):
        fraction = cls(
            numerator=container.numerator,
            denominator=container.denominator
        )
        return fraction

    def parse_precision(self, factor: int):
        pass


    def to_dict(self) -> dict:
        my_dict = {
            'numerator': self.numerator,
            'denominator': self.denominator
        }
        return my_dict


class OracleEma(StateCore):
    layout = Struct(
        'value' / Int64ul,
        'fraction' / Fraction.layout
    )

    def __init__(self, value: int, fraction: Fraction) -> None:
        self.value = value
        self.fraction = fraction

    @classmethod
    def from_container(cls, container: Container):
        oracle_ema = cls(
            value=container.value,
            fraction=Fraction.from_container(container.fraction)
        )
        return oracle_ema

    def parse_precision(self, factor: int):
        obj = self
        obj.value = self.value / factor
        return obj

    def to_dict(self) -> dict:
        my_dict = {
            'value': self.value,
            'fraction': self.fraction.to_dict()
        }
        return my_dict


class PriceInfo(StateCore):
    layout = Struct(
        'price' / Int64ul,
        'confidence' / Int64ul,
        'status' / Int32ul,
        'corporate_action' / Int32ul,
        'publish_slot' / Int64ul
    )

    def __init__(self, price: int, confidence: int, status: int, corporate_action: int, publish_slot: int) -> None:
        self.price = price
        self.confidence = confidence
        self.status = status
        self.corporate_action = corporate_action
        self.publish_slot = publish_slot

    @classmethod
    def from_container(cls, container: Container):
        price_info = cls(
            price=container.price,
            confidence=container.confidence,
            status=container.status,
            corporate_action=container.corporate_action,
            publish_slot=container.publish_slot
        )
        return price_info

    def parse_precision(self, factor: int):
        obj = self
        obj.price = self.price / factor
        obj.confidence = self.confidence / factor
        return obj

    def to_dict(self) -> dict:
        my_dict = {
            'price': self.price,
            'confidence': self.confidence,
            'status': self.status,
            'corporate_action': self.corporate_action,
            'publish_slot': self.publish_slot
        }
        return my_dict


class PriceComponent(StateCore):
    layout = Struct(
        'publisher' / PUBLIC_KEY_LAYOUT,
        'aggregate' / PriceInfo.layout,
        'latest' / PriceInfo.layout
    )

    def __init__(self, publisher: PublicKey, aggregate: PriceInfo, latest: PriceInfo) -> None:
        self.publisher = publisher
        self.aggregate = aggregate
        self.latest = latest

    @classmethod
    def from_container(cls, container: Container):
        price_component = cls(
            publisher=PublicKey(container.publisher),
            aggregate=PriceInfo.from_container(container.aggregate),
            latest=PriceInfo.from_container(container.latest)
        )
        return price_component

    def parse_precision(self, factor: int):
        obj = self
        obj.aggregate = self.aggregate.parse_precision(factor=factor)
        obj.latest = self.latest.parse_precision(factor=factor)
        return obj

    def to_dict(self) -> dict:
        my_dict = {
            'publisher': self.publisher.__str__(),
            'aggregate': self.aggregate.to_dict(),
            'latest': self.latest.to_dict()
        }
        return my_dict


class OracleAccount:
    layout = Struct(
        'magic' / Int32ul,
        'version' / Int32ul,
        'oracle_type' / Int32ul,
        'size' / Int32ul,
        'price_type' / Int32ul,
        'exponent' / Int32sl,
        'num_component_prices' / Int32ul,
        'num_quoters' / Int32ul,
        'last_slot' / Int64ul,
        'valid_slot' / Int64ul,
        'twap' / OracleEma.layout,
        'twac' / OracleEma.layout,
        'drv1' / Int64ul,
        'drv2' / Int64ul,
        'product_account_key' / PUBLIC_KEY_LAYOUT,
        'next_price_account_key' / PUBLIC_KEY_LAYOUT,
        'previous_slot' / Int64ul,
        'previous_price' / Int64ul,
        'previous_confidence' / Int64ul,
        'drv3' / Int64ul,
        'aggregate' / PriceInfo.layout,
        'price_components' / GreedyRange(PriceInfo.layout)
    )

    def __init__(self, magic: int, version: int, oracle_type: int, size: int, price_type: int, exponent: int,
                 num_component_prices: int, num_quoters: int, last_slot: int, valid_slot: int, twap: OracleEma,
                 twac: OracleEma, drv1: int, drv2: int, product_account_key: PublicKey,
                 next_price_account_key: PublicKey, previous_slot: int, previous_price: int, previous_confidence: int,
                 drv3: int, aggregate: PriceInfo, price_components: List[PriceInfo]) -> None:
        self.magic = magic
        self.version = version
        self.oracle_type = oracle_type
        self.size = size
        self.price_type = price_type
        self.exponent = exponent
        self.num_component_prices = num_component_prices
        self.num_quoters = num_quoters
        self.last_slot = last_slot
        self.valid_slot = valid_slot
        self.twap = twap
        self.twac = twac
        self.drv1 = drv1
        self.drv2 = drv2
        self.product_account_key = product_account_key
        self.next_price_account_key = next_price_account_key
        self.previous_slot = previous_slot
        self.previous_price = previous_price
        self.previous_confidence = previous_confidence
        self.drv3 = drv3
        self.aggregate = aggregate
        self.price_components = price_components

    @classmethod
    def from_container(cls, container: Container):
        oracle_account = cls(
            magic=container.magic,
            version=container.version,
            oracle_type=container.oracle_type,
            size=container.size,
            price_type=container.price_type,
            exponent=container.exponent,
            num_component_prices=container.num_component_prices,
            num_quoters=container.num_quoters,
            last_slot=container.last_slot,
            valid_slot=container.valid_slot,
            twap=OracleEma.from_container(container=container.twap),
            twac=OracleEma.from_container(container=container.twac),
            drv1=container.drv1,
            drv2=container.drv2,
            product_account_key=PublicKey(container.product_account_key),
            next_price_account_key=PublicKey(container.next_price_account_key),
            previous_slot=container.previous_slot,
            previous_price=container.previous_price,
            previous_confidence=container.previous_confidence,
            drv3=container.drv3,
            aggregate=PriceInfo.from_container(container=container.aggregate),
            price_components=[PriceInfo.from_container(container=c) for c in container.price_components if c.status == 1]
        )
        return oracle_account

    def parse_precision(self, factor: int):
        obj = self
        obj.twap = self.twap.parse_precision(factor=factor)
        obj.twac = self.twac.parse_precision(factor=factor)
        obj.drv1 = self.drv1 / factor
        obj.drv2 = self.drv2 / factor
        obj.previous_price = self.previous_price / factor
        obj.previous_confidence = self.previous_confidence / factor
        obj.drv3 = self.drv3 / factor
        obj.aggregate = self.aggregate.parse_precision(factor=factor)
        obj.price_components = [pc.parse_precision(factor=factor) for pc in self.price_components]

    def to_dict(self) -> dict:
        my_dict = {
            'magic': self.magic,
            'version': self.version,
            'oracle_type': self.oracle_type,
            'size': self.size,
            'price_type': self.price_type,
            'exponent': self.exponent,
            'num_component_prices': self.num_component_prices,
            'num_quoters': self.num_quoters,
            'last_slot': self.last_slot,
            'valid_slot': self.valid_slot,
            'twap': self.twap.to_dict(),
            'twac': self.twac.to_dict(),
            'drv1': self.drv1,
            'drv2': self.drv2,
            'product_account_key': self.product_account_key.__str__(),
            'next_price_account_key': self.next_price_account_key.__str__(),
            'previous_slot': self.previous_slot,
            'previous_price': self.previous_price,
            'previous_confidence': self.previous_confidence,
            'drv3': self.drv3,
            'aggregate': self.aggregate.to_dict(),
            'price_components': [pc.to_dict() for pc in self.price_components]
        }
        return my_dict

    def __str__(self):
        my_dict = self.to_dict()
        return json.dumps(my_dict, sort_keys=False, indent=4)

    @classmethod
    def parse(cls, bytes_data: bytes):
        container = cls.layout.parse(data=bytes_data)
        obj = cls.from_container(container=container)
        obj.parse_precision(factor= 10 ** (-obj.exponent))
        return obj

    def get_price(self) -> float:
        price = self.aggregate.price
        return price