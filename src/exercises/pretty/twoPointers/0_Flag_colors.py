
def sortColors(colors:list) -> list:
    if not colors:
        return []
    
    red, white, blue= 0, 0, len(colors) - 1

    while white <= blue:
        if colors[white] == 0:

            if colors[red] != 0:
                colors[red], colors[white] = colors[white], colors[red]
            
            white+=1
            red+=1
        elif colors[white] == 1:
            white += 1

        else:
            if colors[blue] != 2:
                colors[blue], colors[white] = colors[white], colors[blue]

            blue -= 1

    return colors


if __name__ == "__main__":
    colors:list = [1,2,1,0, 1,1,0,0, 2]
    print(colors)
    print(sortColors(colors))