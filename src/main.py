from pprint import pprint

from src.pipeline.orchestrator import (
    PipelineOrchestrator,
)


def main():

    pipeline = PipelineOrchestrator()

    batch = pipeline.run_batch()

    results = batch["results"]

    analytics = batch["analytics"]

    print()

    print("=" * 60)
    print("PINGSENSE BATCH PROCESSING")
    print("=" * 60)

    print(f"\nProcessed {len(results)} messages.\n")

    print("Sample Results\n")

    pprint(results[:3])

    print("\nAnalytics Summary\n")

    pprint(analytics)

    print("\nOutput Files\n")

    print(batch["output_json"])

    print(batch["output_csv"])


if __name__ == "__main__":
    main()