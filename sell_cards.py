from pyperclip import copy


def extract_cards(filename) -> dict:
    cards = {}
    with open(filename, 'r') as f:
        for line in f:
            content = line.split(' | ')
            if content[1] in cards:
                cards[content[1]].append(content[0])
            else:
                cards[content[1]] = [content[0]]
    return cards


def remove_duplicates(cards) -> str:
    rm = []

    for k, v in cards.items():
        # rm.extend(map(int, v[1:]))
        rm.extend(v[1:])

    # rm = sorted(rm)
    rm = ', '.join(rm)

    return f'-card sell {rm}'


if __name__ == '__main__':
    cards = extract_cards('cards.txt')
    # print(remove_duplicates(cards))
    copy(remove_duplicates(cards))
    print('command copied to clipboard')
