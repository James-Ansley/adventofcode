import re
from math import prod

with open('input_files/day20') as f:
    tiles = dict(re.findall(r'Tile (\d+):\n([.#\n]+)', f.read()))
    tiles = {int(tile_id): [list(line) for line in tile.split()] for tile_id, tile in tiles.items()}


def transformations(tile):
    transformations = [list(tile), list(reversed(tile))]
    transformations += [[list(reversed(line)) for line in t] for t in transformations]
    transformations += [list(list(row) for row in zip(*t[::-1])) for t in transformations]
    return transformations


n = int(len(tiles) ** .5)
row = [tiles.popitem()]
while len(row) < n:
    line_len = len(row)
    right_edge = [line[-1] for line in row[-1][1]]
    for id_, tile in tiles.items():
        for t in transformations(tile):
            left_edge = [line[0] for line in t]
            if right_edge == left_edge:
                row.append((id_, t))
                break
        else:
            continue
        tiles.pop(id_)
        break
    if line_len == len(row):
        row.reverse()
        for _, t in row:
            for line in t:
                line.reverse()

rows = [row]
while len(rows) < n:
    new_row = []
    for _, tile in rows[-1]:
        bottom_edge = tile[-1]
        for id_, next_tile in tiles.items():
            for t in transformations(next_tile):
                top_edge = t[0]
                if bottom_edge == top_edge:
                    new_row.append((id_, t))
                    break
            else:
                continue
            tiles.pop(id_)
            break
    if len(new_row) != n:
        rows.reverse()
        for row in rows:
            for _, t in row:
                t.reverse()
    else:
        rows.append(new_row)

corner_ids = [rows[0][0][0], rows[0][-1][0], rows[-1][0][0], rows[-1][-1][0]]
print(prod(corner_ids))

rows = [[[line[1:-1] for line in tile[1:-1]] for _, tile in row] for row in rows]
rows = [[sum(line, []) for line in zip(*row)] for row in rows]
rows = sum(rows, [])
width = len(rows[0])
transformed_rows = transformations(rows)

monster = '                  # \n#    ##    ##    ###\n #  #  #  #  #  #   '
monster_parts = monster.count('#')
monster_height = monster.count('\n') + 1
monster_width = len(monster) // monster_height
monster = monster.replace(' ', r'[.#]')
monster = monster.replace('\n', f'(?:.|\n){{{width - monster_width + 1}}}')

for map_ in transformed_rows:
    map_ = '\n'.join(''.join(row) for row in map_)
    substrings = (map_[i:i + width * monster_height + 1] for i in range(len(map_) - width * monster_height + 1))
    monsters = sum(bool(re.match(monster, substring)) for substring in substrings)
    if monsters:
        print(map_.count('#') - monster_parts * monsters)
        break
