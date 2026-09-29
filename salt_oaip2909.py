import sqlite3


def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            group_name TEXT NOT NULL,
            grade INTEGER NOT NULL,
            age INTEGER
        )
    ''')

    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        initial_data = [
            ('Макан', 'ИСП-423т', 5, 25),
            ('Настя', 'ИСП-324п', 4, 18),
            ('Леха', 'ИСП-126', 3, 19),

        ]
        cursor.executemany('''
            INSERT INTO students (name, group_name, grade, age) 
            VALUES (?, ?, ?, ?)
        ''', initial_data)
        conn.commit()

    return conn, cursor


def show_all(cursor):

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\nСписок всех студентов")
    for s in students:
        print(f"ID: {s[0]}  ФИО: {s[1]}  Группа: {s[2]}  Оценка: {s[3]}  Возраст: {s[4]}")



def add_student(conn, cursor):

    print("\nДобавление нового студента")
    name = input("Введите ФИО: ")
    group_name = input("Введите название группы: ")

    try:
        grade = int(input("Введите оценку: "))
        age = int(input("Введите возраст: "))
    except ValueError:
        print("Ошибка: оценка и возраст должны быть числами!")
        return

    cursor.execute('''
        INSERT INTO students (name, group_name, grade, age) 
        VALUES (?, ?, ?, ?)
    ''', (name, group_name, grade, age))
    conn.commit()
    print("Студент успешно добавлен!\n")


def search_by_group(cursor):

    group = input("\nВведите название группы для поиска: ")
    cursor.execute("SELECT * FROM students WHERE group_name = ?", (group,))
    students = cursor.fetchall()

    print(f"\nСтуденты группы {group}")
    if not students:
        print("Студентов в такой группе не найдено.")
    else:
        for s in students:
            print(f"ID: {s[0]} ФИО: {s[1]} Оценка: {s[3]} Возраст: {s[4]}")



def search_by_grade(cursor):

    try:
        grade = int(input("\nВведите оценку для поиска: "))
    except ValueError:
        print("Ошибка: оценка должна быть числом!")
        return

    cursor.execute("SELECT * FROM students WHERE grade = ?", (grade,))
    students = cursor.fetchall()

    print(f"\nСтуденты с оценкой {grade} ")
    if not students:
        print("Студентов с такой оценкой не найдено.")
    else:
        for s in students:
            print(f"ID: {s[0]} ФИО: {s[1]}  Группа: {s[2]}  Возраст: {s[4]}")


def update_grade(conn, cursor):

    print("\n Изменение оценки ")
    try:
        student_id = int(input("Введите ID студента: "))
        new_grade = int(input("Введите новую оценку: "))
    except ValueError:
        print("Ошибка: ID и оценка должны быть числами!")
        return

    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id))
    conn.commit()

    if cursor.rowcount > 0:
        print("Оценка успешно изменена!\n")
    else:
        print("Студент с таким ID не найден.\n")


def delete_student(conn, cursor):

    print("\nУдаление студента")
    try:
        student_id = int(input("Введите ID студента для удаления: "))
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Студент успешно удален. Оставшиеся студенты:")
        show_all(cursor)
    else:
        print("Студент с таким ID не найден.\n")


def show_average_grade(cursor):

    cursor.execute("SELECT AVG(grade) FROM students")
    avg_grade = cursor.fetchone()[0]

    if avg_grade is not None:
        print(f"\n*** Дополнительное задание ***")
        print(f"Средняя оценка всех студентов: {avg_grade:.2f}\n")
    else:
        print("\nБаза данных пуста, невозможно вычислить средний балл.\n")


def main():
    conn, cursor = init_db()

    while True:
        print("УЧЁТ СТУДЕНТОВ")
        print("1. Показать всех студентов")
        print("2. Добавить студента")
        print("3. Найти студентов по группе")
        print("4. Найти студентов по оценке")
        print("5. Изменить оценку")
        print("6. Удалить студента")
        print("7. [Доп] Показать средний балл")
        print("0. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            show_all(cursor)
        elif choice == '2':
            add_student(conn, cursor)
        elif choice == '3':
            search_by_group(cursor)
        elif choice == '4':
            search_by_grade(cursor)
        elif choice == '5':
            update_grade(conn, cursor)
        elif choice == '6':
            delete_student(conn, cursor)
        elif choice == '7':
            show_average_grade(cursor)
        elif choice == '0':
            print("Сохранение данных и выход")
            break
        else:
            print("Неверный ввод, попробуйте снова.\n")

    conn.close()


if __name__ == "__main__":
    main()