from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Pedido:
    cliente: str
    items: list = field(default_factory=list)   # tuplas (nombre, precio, cantidad)
    direccion: str | None = None
    cupon: str | None = None
    notas: str = ""

    @property
    def total(self) -> float:
        return sum(precio * cant for _, precio, cant in self.items)
