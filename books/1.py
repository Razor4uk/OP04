import csv


books_list = [
    {
        'Название': 'Война и мир',
        'Автор': 'Толстой',
        'Год издания': 1869
    },
    {
        'Название': 'Капитанская дочка',
        'Автор': 'Пушки',
        'Год издания': 1836
    },
    {
        'Название': 'Волки и овцы',
        'Автор': 'Крылов',
        'Год издания': 1833
    },
]

file_name = 'books.csv'

with open(file_name, 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['Название', 'Автор', 'Год издания']
    writer = csv.DictWriter(file, fieldnames)

    writer.writeheader()
    for item in books_list:
        writer.writerow(item)

print(f'Создан новый файл: {file_name}')