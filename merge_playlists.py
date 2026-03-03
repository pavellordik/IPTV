import sys
import glob

def merge_playlists(input_pattern, output_file):
    # Получаем список всех файлов по шаблону (например, *_clean.m3u8)
    files = sorted(glob.glob(input_pattern))
    if not files:
        print(f"Нет файлов по шаблону {input_pattern}")
        return

    with open(output_file, 'w', encoding='utf-8') as out:
        for i, file in enumerate(files):
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                # Для первого файла записываем всё, включая #EXTM3U
                if i == 0:
                    out.writelines(lines)
                else:
                    # Для последующих пропускаем первую строку (#EXTM3U), если она есть
                    if lines and lines[0].startswith('#EXTM3U'):
                        out.writelines(lines[1:])
                    else:
                        out.writelines(lines)
    print(f"Объединённый файл {output_file} создан из {len(files)} файлов.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python merge_playlists.py <входной_шаблон> <выходной_файл>")
        sys.exit(1)
    merge_playlists(sys.argv[1], sys.argv[2])
