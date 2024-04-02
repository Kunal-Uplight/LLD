from typing import List
from ParkingLot.models.base_model import BaseModel
from ParkingLot.models.parking_floor import ParkingFloor
from ParkingLot.models.display_board import DisplayBoard
from ParkingLot.models.gate import Gate


class ParkingLot(BaseModel):
    def __init__(self, name: str, address: str, parking_floors: List[ParkingFloor], display_board: DisplayBoard,
                 entry_gates: List[Gate], exit_gates: List[Gate], base_id: str, created_at: str, updated_at: str):
        super().__init__(base_id, created_at, updated_at)
        self.name = name
        self.address = address
        self.parking_floors = parking_floors
        self.display_board = display_board
        self.entry_gates = entry_gates
        self.exit_gates = exit_gates
