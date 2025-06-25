
import os, json, uuid, datetime, boto3, decimal
dynamodb = boto3.resource('dynamodb')
events_table = dynamodb.Table(os.environ['EVENTS_TABLE'])
bookings_table = dynamodb.Table(os.environ['BOOKINGS_TABLE'])

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        event_id = body.get("eventId")
        user_email = body.get("email")

        if not (event_id and user_email):
            return {"statusCode": 400, "body": json.dumps({"error": "eventId and email are required"})}

        # Ensure event exists
        ev = events_table.get_item(Key={"eventId": event_id}).get("Item")
        if not ev:
            return {"statusCode": 404, "body": json.dumps({"error": "Event not found"})}

        booking = {
            "bookingId": str(uuid.uuid4()),
            "eventId": event_id,
            "email": user_email,
            "bookedAt": datetime.datetime.utcnow().isoformat()
        }
        bookings_table.put_item(Item=booking)
        return {"statusCode": 201, "body": json.dumps(booking)}
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
