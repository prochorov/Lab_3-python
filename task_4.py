import chardet


def detect_encoding(file):
    with open(file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
    return result['encoding']


def read_file(file, encoding):
    with open(file, 'r', encoding=encoding) as f:
        content = f.read()
    return content


def main():
    files = ['text-1.txt', 'text-2.txt', 'text-3.txt', 'text-4.txt']
    for file in files:
        encoding = detect_encoding(file)
        content = read_file(file, encoding)
        if content.startswith('Привет'):
            print(f'File {file} is encoded in {encoding} and its content is:')
            print(content)


if __name__ == '__main__':
    main()
