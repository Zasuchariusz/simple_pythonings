import os
import collections


SearchResult = collections.namedtuple('SearchResult', 'file, line, text')


def main():
    print_header()
    folder = get_folder()

    if not folder:
        print("We can't search in that location")
        return

    text = get_text()

    if not text:
        print("We can't search for nothing")
        return

    matches = search_folder(folder, text)

    match_count = 0
    for match in matches:
        match_count += 1
        print_match(match)

    print('Total of {:,} matches'.format(match_count))


def print_header():
    print('--------------------------------')
    print('---------FILE SEARCHER----------')
    print('--------------------------------')
    print()


def get_folder():
    folder = input("What folder do you want to search in? ")
    if not folder or not folder.strip() or not os.path.isdir(folder):
        return None
    else:
        return os.path.abspath(folder)


def get_text():
    return input("What text are you searching for [single phrase]? ").lower()


def search_folder(folder, text):

    items = os.listdir(folder)

    for item in items:

        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folder(full_item, text)
        else:
            yield from search_file(full_item, text)


def search_file(file, text):

    with open(file, 'r', encoding='utf-8') as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(text) >= 0:
                yield SearchResult(line=line_num, file=file, text=line)


def print_match(match):
    print('-----------MATCH------------')
    print('file ' + match.file)
    print('line {}'.format(match.line))
    print('text ' + match.text.strip())
    print()


if __name__ == '__main__':
    main()
