from dataclasses import dataclass, field


@dataclass(slots=True)
class PipelineState:

    processed: int = 0

    failed: int = 0

    results: list = field(default_factory=list)