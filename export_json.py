import json
from db import get_connection

def export_to_json():
    conn = get_connection()
    cur = conn.cursor()

    data = {}

    for table in ["students", "teachers", "courses", "grades"]:
        cur.execute(f"SELECT * FROM {table}")
        columns = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        data[table] = [dict(zip(columns, row)) for row in rows]

    with open("university.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    cur.close()
    conn.close()
    print("Данные экспортированы в university.json")
