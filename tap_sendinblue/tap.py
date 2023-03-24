"""SendInBlue tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_sendinblue import streams


class TapSendInBlue(Tap):
    """SendInBlue tap class."""

    name = "tap-sendinblue"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://api.sendinblue.com/v3",
            description="The url for the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.SendInBlueStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.CampaignsStream(self),
            streams.SmtpAggregatedReportStream(self),
            streams.SmtpEventsStream(self),
        ]


if __name__ == "__main__":
    TapSendInBlue.cli()
