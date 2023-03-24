from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("requests", th.IntegerType),
    th.Property("delivered", th.IntegerType),
    th.Property("hardBounces", th.IntegerType),
    th.Property("softBounces", th.IntegerType),
    th.Property("clicks", th.IntegerType),
    th.Property("uniqueClicks", th.IntegerType),
    th.Property("opens", th.IntegerType),
    th.Property("uniqueOpens", th.IntegerType),
    th.Property("spamReports", th.IntegerType),
    th.Property("blocked", th.IntegerType),
    th.Property("invalid", th.IntegerType),
    th.Property("unsubscribed", th.IntegerType),
).to_dict()
