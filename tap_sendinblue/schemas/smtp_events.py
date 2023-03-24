from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("email", th.StringType),
    th.Property("date", th.DateTimeType),
    th.Property("subject", th.StringType),
    th.Property("messageId", th.StringType),
    th.Property("event", th.StringType),
    th.Property("tag", th.StringType),
    th.Property("ip", th.StringType),
    th.Property("from", th.StringType),
    th.Property("templateId", th.IntegerType),
).to_dict()
