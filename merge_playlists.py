import sys
import os

def merge_files(input_files, output_file):
    with open(output_file, 'w', encoding='utf-8') as out:
        first_file = True
        for fname in input_files:
            if not os.path.exists(fname):
                print(f"⚠️ Предупреждение: файл {fname} не найден, пропускаем.")
                continue
            with open(fname, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if first_file:
                    out.writelines(lines)
                    first_file = False
                else:
                    # Пропускаем первую строку, если это #EXTM3U
                    if lines and lines[0].startswith('#EXTM3U'):
                        out.writelines(lines[1:])
                    else:
                        out.writelines(lines)
            print(f"➕ Добавлен {fname}")
    print(f"✅ Создан {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python merge_categories.py <входной1> <входной2> ... <выходной>")
        sys.exit(1)
    *inputs, output = sys.argv[1:]
    merge_files(inputs, output)
