import datetime

class RBTeam:
    def __init__(self, 
                 team_id: int | None = None,
                 name: str | None = None,
                 from_country: str | None = None,
                 compound_id: int | None = None,
                 ):
        self.id = team_id
        self.name = name
        self.from_country = from_country
        self.compound_id = compound_id

    def to_dict(self) -> dict:
        data = {
            'id': self.id,
            'name': self.name,
            'from_country': self.from_country,
            'compound_id': self.compound_id,
        }
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data