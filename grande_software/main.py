from core.enums import Builder, Style, TypeG, Wood
from core.guitar import Guitar
from core.guitar_spec import GuitarSpec
from core.inventory import Inventory
from core.mandolin import Mandolin
from core.mandolin_spec import MandolinSpec


def show_instruments(matching_instruments: list[Guitar | Mandolin] | None) -> None:
    if matching_instruments is None:
        print("...\nDesculpe Erin, não temos nada para você\n```")

        return None

    print(f"{'-' * 32}")
    print("Erin, talvez você goste destas: ")
    for i, instrument in enumerate(matching_instruments, 1):
        instrument_spec = instrument.get_spec
        instrument_name = instrument.__class__.__name__
        is_guitar = isinstance(instrument_spec, GuitarSpec)

        print(
            f"\n{i}. {instrument_name}: {instrument.get_serial_number()} {instrument_spec.get_builder().value} {instrument_spec.get_model()} {instrument_spec.get_typeg().value} {instrument_name}:".title(),
            f"\n   - {instrument_spec.get_back_wood().value.capitalize()} na traseira e laterais",
            f"\n   - {instrument_spec.get_top_wood().value.capitalize()} no tampo,",
            f"com {f'{instrument_spec.get_num_strings()} cordas' if is_guitar else f'o estilo {instrument_spec.get_style().value.upper()}'}"
            f"\n   - Ela pode ser sua por apenas US$ {instrument.get_price():.2f}!",
        )
    print(f"{'-' * 32}")


def initialize_inventory(inventory: Inventory) -> None:
    spec1 = GuitarSpec(
        Builder.FENDER,
        "stratocastor",
        TypeG.ELECTRIC,
        Wood.ALDER,
        Wood.ALDER,
        6,
    )

    inventory.add_instrument("V95693", 1499.95, spec1)
    inventory.add_instrument("V99999", 1599.95, spec1)

    spec2 = GuitarSpec(
        Builder.MARTIN,
        "D-18",
        TypeG.ACOUSTIC,
        Wood.MAHOGANY,
        Wood.ADIRONDACK,
        6,
    )

    inventory.add_instrument("122784", 5495.95, spec2)

    spec3 = MandolinSpec(
        Builder.FENDER,
        "stratocastor",
        TypeG.ELECTRIC,
        Wood.ALDER,
        Wood.ALDER,
        Style.F,
    )

    inventory.add_instrument("V95693", 1499.95, spec3)
    inventory.add_instrument("V99999", 1599.95, spec3)

    spec4 = MandolinSpec(
        Builder.MARTIN,
        "D-18",
        TypeG.ACOUSTIC,
        Wood.MAHOGANY,
        Wood.ADIRONDACK,
        Style.A,
    )

    inventory.add_instrument("V22784", 5495.95, spec4)


def main() -> None:
    inventory = Inventory()
    initialize_inventory(inventory)

    ...

    whatErinLikes = GuitarSpec(
        Builder.FENDER,
        "Stratocastor",
        TypeG.ELECTRIC,
        Wood.ALDER,
        Wood.ALDER,
        6,
    )

    matching_instruments = inventory.search(whatErinLikes)
    show_instruments(matching_instruments)

    ...

    whatErinLikes = GuitarSpec(
        Builder.RYAN,
        "Stratocastor",
        TypeG.ACOUSTIC,
        Wood.CEDAR,
        Wood.SITKA,
        6,
    )

    matching_instruments = inventory.search(whatErinLikes)
    show_instruments(matching_instruments)

    ...

    whatErinLikes = MandolinSpec(
        Builder.MARTIN,
        "D-18",
        TypeG.ACOUSTIC,
        Wood.MAHOGANY,
        Wood.ADIRONDACK,
        Style.A,
    )

    matching_instruments = inventory.search(whatErinLikes)
    show_instruments(matching_instruments)

    ...

    whatErinLikes = MandolinSpec(
        Builder.OLSON,
        "D-18",
        TypeG.ELECTRIC,
        Wood.BRAZILIAN_ROSEWOOD,
        Wood.ADIRONDACK,
        Style.F,
    )

    matching_instruments = inventory.search(whatErinLikes)
    show_instruments(matching_instruments)


if __name__ == "__main__":
    main()
