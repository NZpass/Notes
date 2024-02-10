# Информация о проекте
# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список заметок,
# редактировать заметку, удалять заметку.

import os

def create_note():
    note_name = input("Введите название заметки: ")
    note_content = input("Введите текст заметки: ")

    with open(note_name + ".txt", "w") as file:
        file.write(note_content)

    print("Заметка создана!")

def read_notes():
    notes = os.listdir()
    for note in notes:
        if note.endswith(".txt"):
            with open(note, "r") as file:
                print(note[:-4] + ":")
                print(file.read())
                print("-----------------------")

def edit_note():
    note_name = input("Введите имя заметки, которую нужно отредактировать: ")
    if os.path.exists(note_name + ".txt"):
        with open(note_name + ".txt", "w") as file:
            note_content = input("Введите новый текст заметки: ")
            file.write(note_content)
        print("Заметка отредактирована!")
    else:
        print("Заметка не найдена")

def delete_note():
    note_name = input("Введите имя заметки, которую нудно удалить: ")
    if os.path.exists(note_name + ".txt"):
        os.remove(note_name + ".txt")
        print("Заметка удалена!")
    else:
        print("Заметка не найдена")

def main():
    while True:
        print("1. Создать заметку")
        print("2. Показать список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Некорректный ввод, попробуйте еще раз")

if __name__ == "__main__":
    main()