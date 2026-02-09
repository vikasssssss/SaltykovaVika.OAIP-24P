import json

def open_base(file_name='каталог_костемитики.json'):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"Записей: {len(data)} "
                  f"База данных: '{file_name}'")
            return data

    except FileNotFoundError:
        empty_db = []
        save_db(empty_db, file_name)
        return empty_db


def save_db(data, file_name='каталог_костемитики.json'):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"{len(data)} записей сохранено в '{file_name}'")
    menu()


def id(data):
    if not data:
        return 1
    true_id = []
    for zapis in data:
        true_id.append(zapis.get('id', 0))
    new_id = max(true_id) + 1
    return new_id



def plus_zapis(data):
    print("Обязательные поля для заполнения:")
    tipe=input('Тип продукта ').strip()
    type_product=[]
    type_product.append(tipe)
    while not tipe:
        print('Это поле обязательное для заполнения, напишите тип продукта')
        tipe = input('Тип продукта').strip()
        type = []
        type.append(tipe)

    life=input('Срок годности ').strip()
    lifee=[]
    lifee.append(life)
    while not life:
        print('Это поле обязательное для заполнения, напишите срок годности')
        life=input('Срок годности ').strip()
        lifee = []
        lifee.append(life)

    color=input('Цвет продукта/ цветовая гамма продукта').strip()
    col=[]
    col.append(color)
    while not color:
        print('Это поле обязательное для заполнения, напишите цвет продукта')
        color=input('Цвет продукта/ цветовая гамма продукта ').strip()
        col = []
        col.append(color)

    new_id=(id(data))
    new_zapis = {
        'id': new_id,
        'Тип продукта': type_product,
        'Срок годности': lifee,
        'Цвет продукта': col
    }


    data.append(new_zapis)

    return data
    menu()

def show_db(data):
    print('Записи в базе данных:')
    if not data:
        print("БД пустая")
        return
    for i in range(len(data)):
        print(data[i])
    menu()


def menu():
    basa= open_base('каталог_костемитики.json')
    print("1.Добавить данные")
    print("2.Показать данные")

    a=int(input("Выбор "))
    if a==1:
        basa=plus_zapis(basa)
        save_db(basa, 'каталог_костемитики.json')

    elif a==2:
        show_db(basa)

    else:
        print("ошибка")


if __name__=="__main__":
    menu()


