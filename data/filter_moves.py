import re


with open("old_moves.ts", 'r') as f:
    x = re.sub(r"accuracy: [0-7]\d,", "accuracy: 0,", f.read())
    x = re.sub(r"accuracy: [8-9]\d,", "accuracy: 100,", x)
    x = re.sub(r"secondary: {\n\t\t\tchance: [0-9]{2},", "secondary: {\n\t\t\tchance: 0,", x)

with open("moves.ts", 'w') as f:
    f.write(x)
