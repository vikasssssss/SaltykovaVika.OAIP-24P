import json

DATA_FILE = 'список.json'
STAT = ["планирование", "в работе", "готов"]
TASK_STAT = ["в процессе", "готов"]

def load_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("проект не найден")
        return []


def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_next_id(data):
    if not data:
        return 1
    return max(item['id'] for item in data) + 1


def show_projects(data):
    print("проекты:")
    if not data:
        print("проектов пока нет")
        return
    for project in data:
        print(f"номер: {project['id']}  название: {project['name']}  статус: {project['status']}")
        print(f"   (задач в проекте: {len(project['tasks'])})")


def create_project(data):
    name = input("введите название нового проекта: ").strip()
    if not name:
        print("название не может быть пустым.")
        return
    new_project = {
        "id": get_next_id(data),
        "name": name,
        "status": "планирование",
        "tasks": []
    }
    data.append(new_project)
    save_data(data)
    print(f"проект '{name}' создан")


def add_task(data):
    if not data:
        print("создайте проект")
        return
    show_projects(data)
    try:
        project_id = int(input(f"количество проектов = {len(data)} \nвведите номер проекта, в который добавить задачу: "))
    except ValueError:
        print("номер должен быть числом")
        return

    project = next((p for p in data if p['id'] == project_id), None)
    if project:
        task_name = input("введите название задачи: ").strip()
        if task_name:
            task_id = len(project['tasks']) + 1
            new_task = {
                "id": task_id,
                "title": task_name,
                "status": "В процессе"
            }
            project['tasks'].append(new_task)
            save_data(data)
            print(f"задача '{task_name}' добавлена в проект")
        else:
            print("название задачи не может быть пустым")
    else:
        print("проект с таким номером не найден")


def show_tasks(data):
    if not data:
        print("нет проектов")
        return
    show_projects(data)
    try:
        project_id = int(input("введите номер проекта для просмотра задач: "))
    except ValueError:
        print("номер должен быть числом")
        return
    project = next((p for p in data if p['id'] == project_id), None)
    if project:
        print(f"задачи проекта: {project['name']} ")
        if project['tasks']:
            for task in project['tasks']:
                status_icon = "[●]" if task["status"] == "Готов" else "[○]"
                print(f"{status_icon} номер: {task['id']} - {task['title']}")
        else:
            print("в этом проекте пока нет задач")
    else:
        print("проект не найден")


def change_status(data):
    if not data:
        print("нет проектов")
        return
    show_projects(data)
    try:
        project_id = int(input("введите номре проекта для изменения статуса: "))
    except ValueError:
        print("номер должен быть числом")
        return
    project = next((p for p in data if p['id'] == project_id), None)
    if project:
        print(f"текущий статус проекта '{project['name']}': {project['status']}")
        print("доступные статусы:")
        for i, status in enumerate(STAT, 1):
            print(f"{i}. {status}")
        try:
            choice = int(input("выберите номер нового статуса: "))
            if 1 <= choice <= len(STAT):
                project['status'] = STAT[choice - 1]
                save_data(data)
                print(f"статус проекта изменен на '{project['status']}'.")
            else:
                print("неверный номер статуса")
        except ValueError:
            print("должно быть число")
    else:
        print("проект не найден")


def change_task_status(data):
    if not data:
        print("нет проектов")
        return
    show_projects(data)
    try:
        project_id = int(input("введите номер проекта: "))
    except ValueError:
        print("номер должен быть числом")
        return
    project = next((p for p in data if p['id'] == project_id), None)
    if project:
        if not project['tasks']:
            print("в этом проекте нет задач")
            return
        print(f"задачи: {project['name']} ")
        for task in project['tasks']:
            status_icon = "[●]" if task["status"] == "Готов" else "[○]"
            print(f"{status_icon} номер: {task['id']} - {task['title']}")
        try:
            task_id = int(input("введите номер задачи для изменения статуса: "))
        except ValueError:
            print("номер должен быть числом")
            return

        task = next((t for t in project['tasks'] if t['id'] == task_id), None)

        if task:
            print(f"текущий статус задачи '{task['title']}': {task['status']}")
            print("доступные статусы:")
            for i, status in enumerate(TASK_STAT, 1):
                print(f"{i}. {status}")

            try:
                choice = int(input("Выберите номер нового статуса: "))
                if 1 <= choice <= len(TASK_STAT):
                    task["status"] = TASK_STAT[choice - 1]
                    save_data(data)
                    print(f"статус задачи изменен на '{task['status']}'.")
                else:
                    print("неверный номер статуса")
            except ValueError:
                print("ввод должен быть числом")
        else:
            print("задача с таким номером не найдена")
    else:
        print("проект не найден")



def main():
    while True:
        print("меню:")
        print("1. показать проекты")
        print("2. создать проект")
        print("3. добавить задачу")
        print("4. показать задачи в проекте")
        print("5. изменить статус проекта")
        print("6. изменить статус задачи")
        print("0. выход")

        choice = input("Выберите действие: ")

        # Загружаем актуальные данные перед каждым действием
        data = load_data()

        if choice == '1':
            show_projects(data)
        elif choice == '2':
            create_project(data)
        elif choice == '3':
            add_task(data)
        elif choice == '4':
            show_tasks(data)
        elif choice == '5':
            change_status(data)
        elif choice == '6':
            change_task_status(data)
        elif choice == '0':
            print("выход из приложения")
            break
        else:
            print("неверный выбор, попробуйте снова")


if __name__ == "__main__":
    main()