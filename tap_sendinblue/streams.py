"""Stream type classes for tap-sendinblue."""

from __future__ import annotations


from tap_sendinblue.client import SendInBlueStream
from tap_sendinblue import schemas


class CampaignsStream(SendInBlueStream):
    """Define custom stream."""
    name = "campaigns"
    path = "/emailCampaigns"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "campaigns.[*]"
    schema = schemas.campaigns


class SmtpAggregatedReportStream(SendInBlueStream):
    name = "smtp_report"
    path = "/smtp/statistics/aggregatedReport"
    replication_key = None
    schema = schemas.smtp_report


class SmtpEventsStream(SendInBlueStream):
    name = "smtp_events"
    path = "/smtp/statistics/events"
    replication_key = None
    primary_keys = ["messageId"]
    records_jsonpath = "events.[*]"
    schema = schemas.smtp_events
