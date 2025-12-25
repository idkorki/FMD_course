from setup_db import setup_database
from analytics import show_statistics
from export_json import export_to_json
from import_json import import_from_json

while True:
    print("""
=============================
 СИСТЕМА УПРАВЛЕНИЯ ДАННЫМИ
=============================
1 — Создать и заполнить БД
2 — Показать аналитику
3 — Экспорт в JSON
4 — Импорт из JSON
0 — Выход
""")

    choice = input("Выбор: ")

    if choice == "1":
        setup_database()
    elif choice == "2":
        show_statistics()
    elif choice == "3":
        export_to_json()
    elif choice == "4":
        import_from_json()
    elif choice == "0":
        break
    else:
        print("Неверный ввод")
