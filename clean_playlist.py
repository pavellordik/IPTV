import sys

ADS_KEYWORDS = ['реклама', 'advert', 'promo', 'shop', 'tvclub', 'телебар', 'казино', 'еротика']

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
            if any(keyword in line.lower() for keyword in ADS_KEYWORDS):
                skip = True
            else:
                skip = False
                cleaned_lines.append(line)
        elif not line.startswith('#') and not skip:
            cleaned_lines.append(line)
        elif line.startswith('#') and not skip:
            cleaned_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)
    print(f"Обработан {input_file} -> {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python clean_playlist.py <входной> <выходной>")
        sys.exit(1)
    clean_playlist(sys.argv[1], sys.argv[2])
