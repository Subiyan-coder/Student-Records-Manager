import pymysql
import os
from dotenv import load_dotenv

# Load your Aiven credentials from .env
load_dotenv()

print("Connecting to Aiven Cloud...")
conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=int(os.getenv("DB_PORT"))
)

try:
    with conn.cursor() as cursor:
        print("Upgrading 'cgpa' column to hold percentages...")
        # DECIMAL(5,2) allows numbers up to 999.99
        cursor.execute("ALTER TABLE students MODIFY COLUMN cgpa DECIMAL(5, 2);")
        
        print("Upgrading 'institute_name' column for longer names...")
        # VARCHAR(255) allows up to 255 characters
        cursor.execute("ALTER TABLE students MODIFY COLUMN institute_name VARCHAR(255);")
        
    conn.commit()
    print("✅ Success! Database columns upgraded.")
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    conn.close()
    print("Connection securely closed.")