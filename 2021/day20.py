from itertools import product


def pad(image, value=0):
    sides = [value] * 3
    tops = [[value] * (len(image[0]) + 6)] * 3
    image = [*tops,
             *[[*sides, *line, *sides] for line in image],
             *tops]
    return image


def enhance(img, pad_value=0):
    img = pad(img, pad_value)
    height, width = len(img), len(img[0])
    res = [[0] * width for _ in range(height)]
    for i, j in product(range(height - 2), range(width - 2)):
        bits = [img[i1][j1] for i1 in range(i, i + 3) for j1 in range(j, j + 3)]
        index = int(''.join(map(str, bits)), 2)
        res[i + 1][j + 1] = enhancement[index]
    return [line[2:-2] for line in res[2:-2]]


with open('input_files/day20') as f:
    enhancement, img = f.read().split('\n\n')
    enhancement = [1 if x == '#' else 0 for x in enhancement]
    img = [[1 if x == '#' else 0 for x in line] for line in img.split()]

enhanced = enhance(enhance(img), pad_value=1)
print(sum(char for line in enhanced for char in line))

enhanced = img
for i in range(50):
    enhanced = enhance(enhanced, i % 2)
print(sum(char for line in enhanced for char in line))
