# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

with open("input2.txt", "r") as file:
    lines = file.read().split("\n")

lines.pop(0)
for i in range(len(lines)):
    lines[i] = lines[i].split(' ')
values = [int(name[1]) for name in lines]
names = [name[0] for name in lines]
min = min(values)
index = values.index(min)
print(names[index])
pass