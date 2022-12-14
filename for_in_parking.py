PARKING_PLACES = 7
FREE_PLACE     = 3 

print('#' * PARKING_PLACES * 5)

for place_index in range(1, PARKING_PLACES + 1):
    if place_index == FREE_PLACE:
        print("|   |", end="")
        continue
    print("| X |", end="")

print("\n","#"*PARKING_PLACES*5, sep="")


"""
sep - используется для указания знака разделителя.
По умолчанию использует \n, но \n добавляет красную строку/абзац/пробел перед новой строкой.
sep="" - меняет элемент по умолчанию на "без каких либо знаков".
В нашем случае мы принудительно перенесли корретку на новую строку, 
но "пробел" убрали командой/параметром/фитчей  sep = "".

"""