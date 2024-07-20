from core.enums import Builder, TypeG, Wood


class GuitarSpec:
    def __init__(self, builder, model, typeg, back_wood, top_wood):
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.back_wood = back_wood
        self.top_wood = top_wood

    def get_builder(self) -> Builder:
        return self.builder

    def get_model(self) -> str:
        return self.model

    def get_typeg(self) -> TypeG:
        return self.typeg

    def get_back_wood(self) -> Wood:
        return self.back_wood

    def get_top_wood(self) -> Wood:
        return self.top_wood
