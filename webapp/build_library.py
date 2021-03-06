import gzip
import json
import requests

OUTFILES = [
    'card_commander_library.json.gz',
    'card_commander_cardlist.txt'
]


def _get(d, fields):
    return {k: d[k] for k in fields if k in d}


def main():
    url = 'https://mtgjson.com/json/AllSets.json.gz'
    resp = requests.get(url)
    sets = json.loads(gzip.decompress(resp.content).decode('utf8'))

    cards = {}
    SERIE_FIELDS = ['name', 'code']
    CARD_FIELDS = ['name', 'names', 'manaCost', 'type', 'text',
                   'supertypes', 'types', 'subtypes', 'colorIdentity',
                   'power', 'toughness', 'loyalty', 'legalities']
    SKIP_TYPES = {'Vanguard', 'Scheme', 'Conspiracy', 'Phenomenon', 'Plane'}
    for serie in sets.values():
        serie_info = _get(serie, SERIE_FIELDS)
        for card in serie.get('cards'):
            card_types = set(card.get('types', ''))
            if card_types.intersection(SKIP_TYPES):
                continue
            card_info = _get(card, CARD_FIELDS)
            card_info['set'] = serie_info
            cards[card['name']] = card_info

    fname = 'card_commander_library.json.gz'
    json.dump(list(cards.values()), gzip.open(fname, 'wt'))

    fname = 'card_commander_cardlist.txt'
    with open(fname, 'wt') as f:
        f.write('\n'.join(sorted(cards.keys())))

if __name__ == '__main__':
    main()
