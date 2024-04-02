class BaseModel:
    def __init__(self, base_id: str, created_at: str, updated_at: str):
        self.base_id = base_id
        self.created_at = created_at
        self.updated_at = updated_at
