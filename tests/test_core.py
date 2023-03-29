"""Tests standard tap features using the built-in SDK tests library."""

import datetime
from decouple import config
from singer_sdk.testing import get_tap_test_class

from tap_sendinblue.tap import TapSendInBlue


SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "api_key": config('API_KEY', default="Test"),
}


# Run standard built-in tap tests from the SDK:
TestTapSendInBlue = get_tap_test_class(
    tap_class=TapSendInBlue,
    config=SAMPLE_CONFIG
)
