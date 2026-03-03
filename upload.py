import os
from yadisk import YaDisk

y = YaDisk(token=os.environ['YANDEX_TOKEN'])
target_dir = '/Приложения/teleplaylists'

# Создаём все папки по пути, если их нет
y.makedirs(target_dir, exist_ok=True)

files = [
    '10_clean.m3u8', '11_clean.m3u8', '2_clean.m3u8', '20TV_clean.m3u8',
    '3_clean.m3u8', '4_clean.m3u8', '5_clean.m3u8', '6_clean.m3u8',
    '7_clean.m3u8', '8_clean.m3u8', '9_clean.m3u8', 'fil_mobai_clean.m3u8',
    'seri_mobai_clean.m3u8', 'staray_seria_clean.m3u8'
]

for file in files:
    if os.path.exists(file):
        y.upload(file, f'{target_dir}/{file}', overwrite=True)
        print(f'Uploaded {file}')
