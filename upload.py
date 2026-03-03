import os
from yadisk import YaDisk

y = YaDisk(token=os.environ['YANDEX_TOKEN'])
target_dir = '/Приложения/teleplaylists'

# Создаём папку, если её нет
if not y.exists(target_dir):
    y.mkdir(target_dir)

# Список всех итоговых файлов (категорийные + отдельные)
files = [
    'Телеканалы.m3u8',
    'Фильмы.m3u8',
    'Сериалы.m3u8',
    '4К.m3u8',
    'Мультфильмы.m3u8',
    'fil_mobai.m3u8',
    'seri_mobai.m3u8',
    'staray_seria.m3u8'
]

for file in files:
    if os.path.exists(file):
        y.upload(file, f'{target_dir}/{file}', overwrite=True)
        print(f'Uploaded {file}')
    else:
        print(f'⚠️ Файл {file} не найден, пропускаем загрузку.')
