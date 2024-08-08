from core.guitar import Guitar
from core.guitar_spec import GuitarSpec
from core.instrument import Instrument
from core.mandolin import Mandolin
from core.mandolin_spec import MandolinSpec


class Inventory:
    def __init__(self):
        self.inventory = []

    def add_instrument(
        self, serial_number: str, price: float, spec: GuitarSpec | MandolinSpec
    ) -> None:
        if isinstance(spec, GuitarSpec):
            instrument = Guitar(serial_number, price, spec)
        elif isinstance(spec, MandolinSpec):
            instrument = Mandolin(serial_number, price, spec)

        self.inventory.append(instrument)

    def get_instrument(self, serial_number: str) -> Instrument | None:
        for instrument in self.inventory:
            if instrument.get_serial_number() == serial_number:
                return instrument

        return None

    def search(
        self, search_spec: GuitarSpec | MandolinSpec
    ) -> list[Guitar | Mandolin] | None:
        results = []

        if isinstance(search_spec, GuitarSpec):
            for guitar in self.inventory:
                if isinstance(guitar, Guitar) and guitar.spec.matches(search_spec):
                    results.append(guitar)

        elif isinstance(search_spec, MandolinSpec):
            for mandolin in self.inventory:
                if isinstance(mandolin, Mandolin) and mandolin.spec.matches(
                    search_spec
                ):
                    results.append(mandolin)

        return results or None
