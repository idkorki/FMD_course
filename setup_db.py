from db import get_connection

def setup_database():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        studentid SERIAL PRIMARY KEY,
        fullname TEXT NOT NULL,
        studentgroup TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS teachers (
        teacherid SERIAL PRIMARY KEY,
        teachername TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS courses (
        courseid SERIAL PRIMARY KEY,
        coursename TEXT NOT NULL,
        teacherid INT REFERENCES teachers(teacherid)
    );

    CREATE TABLE IF NOT EXISTS grades (
        studentid INT REFERENCES students(studentid),
        courseid INT REFERENCES courses(courseid),
        grade INT CHECK (grade BETWEEN 1 AND 5),
        PRIMARY KEY (studentid, courseid)
    );
    """)

    cur.execute("""
    INSERT INTO students (fullname, studentgroup) VALUES
    ('Иванов Илья', 'ИКБО-11'),
    ('Петрова Мария', 'ИКБО-11'),
    ('Сидоров Кирилл', 'ИКБО-12')
    ON CONFLICT DO NOTHING;
    """)

    cur.execute("""
    INSERT INTO teachers (teachername) VALUES
    ('Смирнов А.П.'),
    ('Кузнецова О.Н.')
    ON CONFLICT DO NOTHING;
    """)

    cur.execute("""
    INSERT INTO courses (coursename, teacherid) VALUES
    ('Базы данных', 1),
    ('Программирование', 2)
    ON CONFLICT DO NOTHING;
    """)

    cur.execute("""
    INSERT INTO grades VALUES
    (1, 1, 5),
    (1, 2, 5),
    (2, 1, 4)
    ON CONFLICT DO NOTHING;
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("База данных создана и заполнена")

if __name__ == "__main__":
    setup_database()
