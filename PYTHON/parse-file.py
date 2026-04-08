import os
import csv

DIRECTORY = '/home/user/CODE/templates'
TARGET_STR = 'старый_текст'  # ДОЛЖЕН БЫТЬ ЗАДАН
NEW_STR = 'новый_текст'  # ДОЛЖЕН БЫТЬ ЗАДАН

LOG_CSV_FILE = "/home/user/DOCS/update_header_report.csv"
LOG_HEADERS = ['file_path', 'status', 'text_error']


def init_log_file(file_path, headers):
    """Создаёт файл лога с заголовками"""
    with open(file_path, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)


def write_log(file_path, log_data):
    """Записывает строку в лог"""
    with open(file_path, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        row = [log_data.get(h, '') for h in LOG_HEADERS]
        writer.writerow(row)


def read_and_change_file(file_path, target_str, new_str):
    """Ищет и заменяет текст в файле"""
    log_data = {h: '' for h in LOG_HEADERS}
    log_data['file_path'] = file_path

    try:
        with open(file_path, "r", encoding='utf-8') as f:
            content = f.read()

        if target_str in content:
            new_content = content.replace(target_str, new_str)
            with open(file_path, "w", encoding='utf-8') as f:
                f.write(new_content)
            log_data['status'] = 'OK'
        else:
            log_data['status'] = 'NOT_FOUND'

    except Exception as e:
        log_data['text_error'] = str(e)
        log_data['status'] = 'ERROR'

    write_log(LOG_CSV_FILE, log_data)  # Исправлен путь к лог-файлу


def get_files(directory):
    """Получает список файлов в директории"""
    files = []
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isfile(full_path):
            files.append(full_path)
    return files


def init(directory):
    """Основная функция"""
    init_log_file(LOG_CSV_FILE, LOG_HEADERS)
    files = get_files(directory)
    for file_path in files:
        read_and_change_file(file_path, TARGET_STR, NEW_STR)


if __name__ == "__main__":
    # Установите значения для замены!
    TARGET_STR = 'что_заменять'
    NEW_STR = 'на_что_заменять'
    init(DIRECTORY)