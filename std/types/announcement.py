from dataclasses import dataclass

from lib.std.types.sized_bytes import bytes32
from lib.std.util.hash import std_hash


@dataclass(frozen=True)
class Announcement:
    parent_coin_info: bytes32
    message: bytes

    def name(self) -> bytes32:
        return std_hash(bytes(self.parent_coin_info + self.message))
