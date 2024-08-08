from abc import ABC

from core.guitar_spec import GuitarSpec
from core.mandolin_spec import MandolinSpec


class Instrument(ABC):
    def __init__(
        self, serial_number: str, price: float, spec: GuitarSpec | MandolinSpec
    ):
        self.serial_number = serial_number
        self.price = price
        self.spec = spec

    def get_serial_number(self) -> str:
        return self.serial_number

    def get_price(self) -> float:
        return self.price

    def set_price(self, price: float) -> None:
        self.price = price

    @property
    def get_spec(self) -> GuitarSpec | MandolinSpec:
        return self.spec
