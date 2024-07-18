from core.guitar import Guitar


class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(
        self, serial_number, price, builder, model, typeg, back_wood, top_wood
    ):
        guitar = Guitar(
            serial_number, price, builder, model, typeg, back_wood, top_wood
        )
        self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar

        return None

    def search_guitar(self, search_guitar):
        results = []

        for guitar in self.guitars:
            if search_guitar.get_builder() != guitar.get_builder():
                continue

            model = search_guitar.get_model().lower()
            if model and model != "" and model != guitar.get_model().lower():
                continue

            if search_guitar.get_typeg() != guitar.get_typeg():
                continue
            if search_guitar.get_back_wood() != guitar.get_back_wood():
                continue
            if search_guitar.get_top_wood() != guitar.get_top_wood():
                continue

            results.append(guitar)

        return results or None
