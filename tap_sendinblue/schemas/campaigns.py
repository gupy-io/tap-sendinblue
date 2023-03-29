from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property("scheduledAt", th.StringType, required=False),
    th.Property("createdAt", th.DateTimeType, required=False),
    th.Property("modifiedAt", th.DateTimeType, required=False),
    th.Property("sentDate", th.DateTimeType, required=False),
    th.Property("shareLink", th.StringType, required=False),
    th.Property("subject", th.StringType, required=False),
    th.Property("statistics",
                th.ObjectType(
                    th.Property("mirrorClick", th.IntegerType),
                    th.Property("remaining", th.IntegerType),
                    th.Property("globalStats",
                                th.ObjectType(
                                    th.Property("uniqueClicks", th.IntegerType),
                                    th.Property("clickers", th.IntegerType),
                                    th.Property("complaints", th.IntegerType),
                                    th.Property("delivered", th.IntegerType),
                                    th.Property("sent", th.IntegerType),
                                    th.Property("softBounces", th.IntegerType),
                                    th.Property("hardBounces", th.IntegerType),
                                    th.Property("uniqueViews", th.IntegerType),
                                    th.Property(
                                        "unsubscriptions", th.IntegerType
                                    ),
                                    th.Property("viewed", th.IntegerType),
                                    th.Property("trackableViews", th.IntegerType),
                                    th.Property(
                                        "trackableViewsRate", th.NumberType
                                    ),
                                    th.Property("estimatedViews", th.IntegerType),
                                )
                                ),
                    th.Property("campaignStats",
                                th.ArrayType(
                                    th.ObjectType(
                                        th.Property("listId", th.IntegerType),
                                        th.Property("uniqueClicks", th.IntegerType),
                                        th.Property("clickers", th.IntegerType),
                                        th.Property("complaints", th.IntegerType),
                                        th.Property("delivered", th.IntegerType),
                                        th.Property("sent", th.IntegerType),
                                        th.Property("softBounces", th.IntegerType),
                                        th.Property("hardBounces", th.IntegerType),
                                        th.Property("uniqueViews", th.IntegerType),
                                        th.Property("trackableViews", th.IntegerType),
                                        th.Property(
                                            "unsubscriptions", th.IntegerType
                                        ),
                                        th.Property("viewed", th.IntegerType),
                                        th.Property("deferred", th.IntegerType),
                                    ),
                                )
                                ),
                ),
                ),
).to_dict()
