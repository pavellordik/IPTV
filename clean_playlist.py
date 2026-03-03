import sys

# Список ключевых слов для рекламы (в нижнем регистре)
ADS_KEYWORDS = [
    'написать разработчику',
    'whatsapp',
    'связь с разработчиком',
    'разработчик',
    'whats',
    'ватсап',
    'макс',
    'max',
    'поддержка',
    'telegram',
    'telergam',
    'чат',
    'подпишись',
    '18+',
    'клубничка'
]

def read_file_with_encoding(file_path):
    """Пытается прочитать файл в разных кодировках."""
    encodings = ['utf-8', 'cp1251', 'latin-1', 'utf-8-sig']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                return f.readlines(), enc
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Не удалось прочитать файл {file_path} ни в одной из кодировок: {encodings}")

def clean_playlist(input_file, output_file):
    try:
        lines, used_encoding = read_file_with_encoding(input_file)
        print(f"Файл {input_file} прочитан в кодировке {used_encoding}")
    except Exception as e:
        print(f"Ошибка чтения файла {input_file}: {e}")
        return

    cleaned_lines = []
    skip = False

    for line in lines:
        if line.startswith('#EXTINF:'):
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
