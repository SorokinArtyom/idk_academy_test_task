import datetime

class RBMatch:
    def __init__(self, 
                 match_id: int | None = None,
                 first_team_id: int | None = None,
                 second_team_id: int | None = None,
                 time_match: datetime.date | None = None,
                 result_first: int | None = None,
                 result_second: int | None = None
                 ):
        self.id = match_id
        self.first_team_id = first_team_id
        self.second_team_id = second_team_id
        self.time_match = time_match
        self.result_first = result_first
        self.result_second = result_second

    def to_dict(self) -> dict:
        data = {
            'id': self.id,
            'first_team_id': self.first_team_id,
            'second_team_id': self.second_team_id,
            'time_match': self.time_match,
            'result_first': self.result_first,
            'result_second': self.result_second
        }
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data