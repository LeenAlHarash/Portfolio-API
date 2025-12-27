class Project(BaseModel):
    id: int
    name: str
    type: str
    tech: List[str]
    description: str
