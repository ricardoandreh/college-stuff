from core.inventory import Inventory
from core.guitar_spec import GuitarSpec
from core.enums import Builder, TypeG, Wood


def main():
    inventory = Inventory()

    inventory.add_guitar(
        "V95693",
        1499.95,
        GuitarSpec(
            Builder.FENDER.value,
            "Stratocastor",
            TypeG.ELETRIC.value,
            Wood.ALDER.value,
            Wood.ALDER.value,
        ),
    )

    inventory.add_guitar(
        "V55206",
        1329.79,
        GuitarSpec(
            Builder.FENDER.value,
            "Telecaster",
            TypeG.ELETRIC.value,
            Wood.CEDAR.value,
            Wood.MAPLE.value,
        ),
    )

    inventory.add_guitar(
        "V95393",
        1195.49,
        GuitarSpec(
            Builder.FENDER.value,
            "Stratocastor",
            TypeG.ELETRIC.value,
            Wood.ALDER.value,
            Wood.ALDER.value,
        ),
    )

    whatErinLikes = GuitarSpec(
        Builder.FENDER.value,
        "Stratocastor",
        TypeG.ELETRIC.value,
        Wood.ALDER.value,
        Wood.ALDER.value,
    )

    guitars = inventory.search_guitar(whatErinLikes)

    if guitars is None:
        print("Desculpe Erin, não temos nada para você :(")

        return None

    print(f"Erin, talvez você goste desta{'s' if len(guitars) > 1 else ''}:")

    for i, guitar in enumerate(guitars):
        print(
            f"\n{i+1}. {guitar.get_spec().get_builder()} {guitar.get_spec().get_model()} {guitar.get_spec().get_typeg()} guitar:".title()
        )
        print(
            f"   {guitar.get_spec().get_back_wood().capitalize()} na traseira e laterais e {guitar.get_spec().get_top_wood().capitalize()} no tampo."
        )
        print(f"   Ela pode ser sua por apenas US$ {guitar.get_price()}!")


if __name__ == "__main__":
    main()
