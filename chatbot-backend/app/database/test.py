import psycopg

try:
    conn = psycopg.connect(
        host="localhost",        # Thay đổi thành 'sales-chatbot-backend-postgres' nếu cần
        port=5432,
        user="postgres",
        password="postgres",
        dbname="chatbot_db"
    )
    print("Kết nối thành công!")
    conn.close()
except Exception as e:
    print(f"Kết nối thất bại: {e}")
