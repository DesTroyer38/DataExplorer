print("Привет, я запустился!")
import pandas as pd

df = pd.read_csv('data/data.csv')
print(df.head())
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

# Загружаем данные
df = pd.read_csv('data/data.csv')

def show_info():
    print("\n--- Основная информация о датафрейме ---")
    print(df.info())
    print("\n--- Первые 5 строк ---")
    print(df.head())
    print("\n--- Статистика по числовым значениям ---")
    print(df.describe())

def filter_data():
    age_limit = int(input("Показать всех старше возраста: "))
    filtered = df[df['age'] > age_limit]
    print(f"\n--- Люди старше {age_limit} лет ---")
    print(filtered)

def show_stats():
    max_age = df['age'].max()
    min_age = df['age'].min()
    print(f"\nСамый старший возраст: {max_age}")
    print(f"Самый младший возраст: {min_age}")

def add_person():
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    global df
    df = pd.concat([df, pd.DataFrame([{'name': name, 'age': age}])], ignore_index=True)
    print(f"\nДобавлен: {name}, {age} лет")
    print(df)

def save_data():
    filename = input("Введите имя файла для сохранения (например, data/new_data.csv): ")
    df.to_csv(filename, index=False)
    print(f"Данные сохранены в {filename}")

def plot_ages():
    plt.figure(figsize=(6,4))
    plt.bar(df['name'], df['age'])
    plt.title('Возраст людей')
    plt.xlabel('Имя')
    plt.ylabel('Возраст')
    plt.show()

def menu():
    while True:
        print("\n=== DataExplorer Меню ===")
        print("1. Показать базовую информацию")
        print("2. Фильтрация — показать старше заданного возраста")
        print("3. Статистика (максимум/минимум)")
        print("4. Добавить человека")
        print("5. Сохранить изменения в CSV")
        print("6. Построить график возрастов")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            show_info()
        elif choice == '2':
            filter_data()
        elif choice == '3':
            show_stats()
        elif choice == '4':
            add_person()
        elif choice == '5':
            save_data()
        elif choice == '6':
            plot_ages()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор, повторите.")

if __name__ == '__main__':
    menu()