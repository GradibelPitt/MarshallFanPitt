INCH_TO_CM = 2.54
CM_TO_INCH = 1 / INCH_TO_CM
YD_TO_M = 0.9144
M_TO_YD = 1 / YD_TO_M
OZ_TO_GM = 28.3495
GM_TO_OZ = 1 / OZ_TO_GM
LB_TO_KG = 0.453592
KG_TO_LB = 1 / LB_TO_KG

def convert_unit(value, unit):

    if unit == "cm":
        return value * CM_TO_INCH, "in"
    elif unit == "in":
        return value * INCH_TO_CM, "cm"
    elif unit == "yd":
        return value * YD_TO_M, "m"
    elif unit == "m":
        return value * M_TO_YD, "yd"
    elif unit == "oz":
        return value * OZ_TO_GM, "g"
    elif unit == "g":
        return value * GM_TO_OZ, "oz"
    elif unit == "lb":
        return value * LB_TO_KG, "kg"
    elif unit == "kg":
        return value * KG_TO_LB, "lb"
    else:
        return None, None 

def main():
    user_input = input("input a distance or a weight amount, must contain a number (with or without decimals) followed by a space
followed by a unit of measurement that can be one of the following: in, cm, yd, m, oz, g,
kg, lb.): ")

    try:
        value_str, unit = user_input.split()
        value = float(value_str) 
    except ValueError:
        print("Invalid input format.")
        return

    converted_value, converted_unit = convert_unit(value, unit)

    if converted_value is not None:
        print(f"{value} {unit} is equal to {converted_value:.4f} {converted_unit}.")
    else:
        print(f"'{unit}' is not a recognized unit.")

if __name__ == "__main__":
    main()
