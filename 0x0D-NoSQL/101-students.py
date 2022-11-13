#!/usr/bin/env python3
"""
function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    function
    """

    return mongo_collection.aggregate(
        [
            {
                "$project": {
                    "_id": "$_id",
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
            },
            {
                "$sort": {
                    "averageScore": -1
                }
            }
        ]
