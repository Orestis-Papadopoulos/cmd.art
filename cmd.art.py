from characters import *

def print_banner(string):
    print('')
    lines = ["" for i in range(5)]

    for char in string:
        for i in range(5):
            try:
                lines[i] += alphanumeric[char][i]
            except KeyError:
                if char == "%": lines[i] += percent[i]
                if char == "[": lines[i] += sq_bracket_open[i]
                if char == "]": lines[i] += sq_bracket_close[i]
                if char == "-": lines[i] += hyphen[i]
                if char == "/": lines[i] += f_slash[i]
                if char == "\\": lines[i] += b_slash[i]
                if char == ".": lines[i] += period[i]
                if char == ",": lines[i] += comma[i]
                if char == "|": lines[i] += pipe[i]
                if char == "(": lines[i] += parentheses_open[i]
                if char == ")": lines[i] += parentheses_close[i]
                if char == "_": lines[i] += underscore[i]
                if char == ":": lines[i] += colon[i]
                if char == " ": lines[i] += space[i]
    for line in lines: print(line)
    print('')

if __name__ == "__main__":
    print_banner("welcome, mr. stark")
