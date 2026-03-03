import sys

# Расширенный список слов для определения рекламы
ADS_KEYWORDS = [
    'Написать разработчику', 'whatsapp', 'связь с разработчиком', ,
]

def clean_playlist(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")
        return

    cleaned_lines = []
    skip = False

    for line in lines:
        if line.startswith('#EXTINF:'):
            # Приводим строку к нижнему регистру для проверки
            lower_line = line.lower()
            if any(keyword in lower_line for keyword in ADS_KEYWORDS):
                skip = True
                print(f"Пропущен рекламный канал: {line.strip()}")
            else:
                skip = False
                cleaned_lines.append(line)
        elif not line.startswith('#') and not skip:
            cleaned_lines.append(line)
        elif line.startswith('#') and not skip:
            cleaned_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)
    print(f"Обработан {input_file} -> {output_file} (сохранено {len(cleaned_lines)} строк)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python clean_playlist.py <входной> <выходной>")
        sys.exit(1)
    clean_playlist(sys.argv[1], sys.argv[2])
