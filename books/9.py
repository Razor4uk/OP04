import csv as dio

new_file_name = input(f'Введите имя нового файла: ')
new_file_name += '.csv'


with open(new_file_name, 'w', newline='', encoding='utf-8') as file:
    books_data = [
        {'Название': 'Тараб Бульба', 'Автор': 'Гоголь', 'Год издания': 1835},
        {'Название': 'Руслан и Людмила', 'Автор': 'Пушкин', 'Год издания': 1820},
    ]

    writer = dio.writer(file)
    for item in books_data:
        writer.writerow([item['Название'], item['Автор'], item['Год издания']])

with open(new_file_name, newline='', encoding='utf-8') as file:
    reader = dio.reader(file)

    for item in reader:
        print(item[0], item[1], item[2])