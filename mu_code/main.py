y = ""


def std():
    for i in range(len(x)):
        if x[i] >= "0" and x[i] <= "9":
            y = y + x[i]
        else:
            y = "0"
    return


print(std("1234"))
