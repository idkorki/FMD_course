import json
from db import get_connection

def import_from_json():
    with open("university.json", encoding="utf-8") as f:
        data = json.load(f)

    conn = get_connection()
    cur = conn.cursor()

    for s in data["students"]:
        cur.execute("""
        INSERT INTO students VALUES (%s, %s, %s)
        ON CONFLICT DO NOTHING
        """, tuple(s.values()))

    conn.commit()
    cur.close()
    conn.close()
    print("Импорт из JSON выполнен")
