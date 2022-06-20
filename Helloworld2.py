def helloworld_ribbon_vertical(x):
    for i in range(0, x):
        print("H")
        print("  e")
        print("    l")
        print("      l")
        print("        o")
        print("")
        print("        W")
        print("      o")
        print("    r")
        print("  l")
        print("d")
        print("")

string_1 = "H            d    "
string_2 = " e          l     "
string_3 = "  l        r      "
string_4 = "   l      o       "
string_5 = "    o    W        "


text_format = None
while text_format != "vertical" and text_format != "horizontal":
    print("How would you like this to be formatted? ")
    text_format = input(print("Type 'horizontal' or 'vertical'. "))
    print("")

repeat = 0.5
while repeat % 1 != 0:
    print("How many times would you like this to be repeated? ")
    repeat = input(print("Please enter an integer. "))
    print("")
    repeat = float(repeat)
repeat = int(repeat)


if text_format == "vertical":
    print(helloworld_ribbon_vertical(repeat))
    
else:
    print(string_1 * repeat)
    print(string_2 * repeat)
    print(string_3 * repeat)
    print(string_4 * repeat)
    print(string_5 * repeat)
