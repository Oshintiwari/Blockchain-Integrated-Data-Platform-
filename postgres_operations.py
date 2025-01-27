import psycopg2
import json

# PostgreSQL Configuration
with open('config/postgres_config.json', 'r') as config_file:
    config = json.load(config_file)

conn = psycopg2.connect(
    host=config["host"],
    database=config["database"],
    user=config["user"],
    password=config["password"]
)

def store_metadata(transaction_id, metadata_hash):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO metadata (transaction_id, metadata_hash) VALUES (%s, %s)", (transaction_id, metadata_hash))
        conn.commit()
        print(f"Metadata stored in PostgreSQL: {transaction_id} -> {metadata_hash}")

def fetch_metadata(transaction_id):
    with conn.cursor() as cur:
        cur.execute("SELECT metadata_hash FROM metadata WHERE transaction_id = %s", (transaction_id,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            raise Exception("No metadata found for the given transaction ID.")
