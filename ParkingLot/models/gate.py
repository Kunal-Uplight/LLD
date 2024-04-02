from ParkingLot.models.base_model import BaseModel


class Gate(BaseModel):
    def __init__(self, base_id: str, created_at: str, updated_at: str):
        super().__init__(base_id, created_at, updated_at)