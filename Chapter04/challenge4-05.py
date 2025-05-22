def banana(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

b = banana("77.7")
print(b)
