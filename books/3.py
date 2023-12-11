import csv

file_name = 'books.csv'

new_books = [
    {
        'Название': 'Вишневый сад',
        'Автор': 'Чехов',
        'Год издания': 1903
    },
    {
        'Название': 'Старая Изергель',
        'Автор': 'Горький',
        'Год издания': 1895
    },
]

with open(file_name,'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for item in new_books:
        writer.writerow([item['Название'], item['Автор'], item['Год издания']])

print(f'Данные успешно записаны в файл: {file_name}')