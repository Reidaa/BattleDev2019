# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/

index = 2
with open("input{}.txt".format(index), "r") as file:
    lines = file.read().split("\n")
with open("output{}.txt".format(index)) as file:
    output = file.read().split("\n")
    output = output[0].split(' ')

result = []
error = "pas possible"
for i in range(len(lines)):
    lines[i] = lines[i].split(' ')
nb_cable = int(lines[0][0])
nb_requete = int(lines[0][1])
cables = [i for i in range(1, nb_cable + 1)]
lines.pop(0)
debuts = [int(name[0]) for name in lines]
fins = [int(name[1]) for name in lines]
for t in range(max(fins)):
    for debut in debuts:
        if debut == t:
            if nb_cable == 0:
                print(error)
                break
            nb_cable -= 1
            result.append(cables.pop(-1))
    for fin in fins:
        if fin == t:
            nb_cable += 1
            cables.append(result[-1])

pass

output = ""
for i in range(len(result) - 1):
    output += str(result[i]) + " "
output += str(result[-1])
print(output)

# def print_res(rez: list):
#     output = ""
#     for i in range(len(rez) - 1):
#         output += str(rez[i]) + " "
#     output += str(rez[-1])
#     print(output)
