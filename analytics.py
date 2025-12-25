from db import get_connection

def show_statistics():
    conn = get_connection()
    cur = conn.cursor()

    print("\nСредний балл по студентам:")
    cur.execute("""
        SELECT s.fullname, AVG(g.grade)
        FROM students s
        JOIN grades g ON s.studentid = g.studentid
        GROUP BY s.fullname
    """)
    for row in cur.fetchall():
        print(f"{row[0]} — {row[1]:.2f}")

    print("\nСредний балл по курсам:")
    cur.execute("""
        SELECT c.coursename, AVG(g.grade)
        FROM courses c
        JOIN grades g ON c.courseid = g.courseid
        GROUP BY c.coursename
    """)
    for row in cur.fetchall():
        print(f"{row[0]} — {row[1]:.2f}")

    cur.close()
    conn.close()
