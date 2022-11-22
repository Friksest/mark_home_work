horisontal_line    = '-' * 5
two_vertical_lines = '|   |'


figure = input("what figure to draw? ")

if figure == "line":
  print(horisontal_line)
elif figure == "square":
    for n in (horisontal_line, two_vertical_lines, two_vertical_lines, horisontal_line):
        print(n)
elif figure == "parallel horizontal lines":
    for n in (horisontal_line, horisontal_line):
        print(n)
elif figure == "parallel vertical lines":
    for n in (two_vertical_lines, two_vertical_lines):
        print(n)
else:
  print("CAN'T DRAW SUCH FIGURE!")  