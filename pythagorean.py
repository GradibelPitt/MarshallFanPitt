import math

def main():
    side_a_str = input("Please enter the length of the first side (a): ")
    side_b_str = input("Please enter the length of the second side (b): ")

    side_a = float(side_a_str)
    side_b = float(side_b_str)


    hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)

    print(f"The hypotenuse is {hypotenuse:.2f}")

if __name__ == "__main__":
    main()
