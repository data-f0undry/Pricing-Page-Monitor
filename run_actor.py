"""Run the Pricing Page Monitor Actor and print the first few results.

    pip install apify-client
    export APIFY_TOKEN=...        # https://console.apify.com/settings/integrations
    python run_actor.py
"""

import os

from apify_client import ApifyClient

ACTOR = "pricing-page-monitor"
INPUT = {
    "urls": [
        "https://www.notion.com/pricing",
        "https://linear.app/pricing"
    ]
}


def main() -> None:
    client = ApifyClient(os.environ["APIFY_TOKEN"])
    run = client.actor(ACTOR).call(run_input=INPUT)
    print("dataset:", run["defaultDatasetId"])

    items = client.dataset(run["defaultDatasetId"]).list_items(limit=5).items
    for item in items:
        print(item)


if __name__ == "__main__":
    main()
