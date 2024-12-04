with open("input_files/day04", "r") as f:
    data = f.read()

width = data.find("\n") + 1

xmasses = 0
mas_crosses = 0
for i in range(len(data)):
    runs = [
        data[i:i + 4],
        data[i:i + width * 3 + 1:width],
        data[i:i + width * 3 + 4:width + 1],
        data[i:i + width * 3 - 2:width - 1],
    ]
    falling = data[i:i + width * 2 + 3:width + 1]
    rising = data[i + 2:i + width * 2 + 1:width - 1]

    xmasses += runs.count("XMAS") + runs.count("SAMX")
    mas_crosses += falling in ("MAS", "SAM") and rising in ("MAS", "SAM")

print(xmasses)
print(mas_crosses)
