from dataclasses import dataclass


@dataclass(slots=True)
class Media:
    media_id: str
    media_type: str
    file_path: str