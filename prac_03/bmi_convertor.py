
def main():
    weight = float(input("Weight? "))
    height = float(input("Height? "))
    bmi_value = calculate_bmi(weight, height)
    print(bmi_value)

def calculate_bmi(wt, ht):
    return wt / ht / ht


main()