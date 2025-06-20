from kafka import KafkaConsumer, KafkaProducer
import json

used_id = set()
consumer = KafkaConsumer('ecommerce_cdc.public.orders', bootstrap_servers='localhost:9092')
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

for msg in consumer:
    raw_data = json.loads(msg.value)
    if raw_data['after.id'] in used_id:
        print(f"Duplicate order ID found: {raw_data['after.id']}")
        error_data = {
            "error_type": "DuplicateOrderID",
            "error_message": f"Duplicate order ID found: {raw_data['after.id']}",
            "original_data": raw_data
        }
        producer.send("ecommerce_cdc.public.orders.error", value=error_data)
        continue
    used_id.add(raw_data['after.id'])