from faker import Faker
import random
import json
from datetime import datetime, timedelta

fake = Faker()

def generate_data():
    data = {
        "_id": fake.uuid4(),
        "_index": fake.word(),
        "_score": str(random.uniform(0, 1)),
        "_source": {
            "@timestamp": str(fake.date_time_between(start_date="-1y", end_date="now")),
            "@version": str(fake.random_int(1, 5)),
            "cartId": fake.uuid4(),
            "cluster_name": fake.random_element(["Production-Cluster", "AnalyticsCluster", "ResearchCluster", "Main-Cluster", "ProjectA-Cluster"]),
            "countryCd": fake.country_code(),
            "dealerId": fake.uuid4(),
            "environment": fake.word(),
            "errorCode": fake.random_int(100, 999),
            "level": fake.random_element(["INFO", "ERROR", "DEBUG", "SOLVED"]),
            "level_value": fake.random_int(1, 5),
            "logger_name": fake.word(),
            "message": fake.random_element(["Payment Failure", "Card Decline", "Unauthorized: Access denied", "400 Bad Request"]),
            "productCode": fake.uuid4(),
            "productType": fake.word(),
            "projectName": fake.word(),
            "projectVersion": fake.random_int(1, 3),
            "referer": fake.url(),
            "spanId": fake.uuid4(),
            "thread_name": fake.word(),
            "traceId": fake.uuid4(),
        },
        "_version": fake.random_int(1, 3),
        "fields": {
            "@timestamp": [str(fake.date_time_between(start_date="-1y", end_date="now"))],
            "kubernetes.annotations.kubectl.kubernetes.io/restartedAt": [str(fake.date_time_between(start_date="-1y", end_date="now"))],
        },
        "highlight": {
            "message": [fake.random_element(["Payment Failure", "Card Decline", "Unauthorized: Access denied", "400 Bad Request"])]
        }
    }
    return data

records = [generate_data() for i in range(100)]

with open('generated_data.json', 'w') as json_file:
    json.dump(records, json_file, indent=2)

print("Data generated successfully.")