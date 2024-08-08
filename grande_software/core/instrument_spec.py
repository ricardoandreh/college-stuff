from abc import ABC, abstractmethod

from core.enums import Builder, TypeG, Wood


class InstrumentSpec(ABC):
    def __init__(
        self,
        builder: Builder,
        model: str,
        typeg: TypeG,
        back_wood: Wood,
        top_wood: Wood,
    ):
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

    @abstractmethod
    def matches(self, other_spec) -> bool: ...
