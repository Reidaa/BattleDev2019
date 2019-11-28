# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

with open("input2.txt", "r") as file:
    lines = file.read().split("\n")

for i in range(len(lines)):
    lines[i] = int(lines[i])
result = 0
while result * 4 < sum(lines):
    result = result + 1
while result > min(lines):
    result -= 1
total = sum(lines)
throw = total - (4 * result)
# result += 1
print(total - (4 * result))
pass