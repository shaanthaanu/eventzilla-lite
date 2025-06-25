
import os, json, uuid, datetime, boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        item = {
            "eventId": str(uuid.uuid4()),
            "name": body.get("name", "Untitled Event"),
            "date": body.get("date", datetime.date.today().isoformat()),
            "createdAt": datetime.datetime.utcnow().isoformat()
        }
        table.put_item(Item=item)
        return {"statusCode": 201, "body": json.dumps(item)}
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
