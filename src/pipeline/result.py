from dataclasses import dataclass

from src.analytics.models import Analytics


@dataclass(slots=True)
class PipelineResult:

    results: list[dict]

    analytics: Analytics

    output_json: str

    output_csv: str