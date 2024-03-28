print("Welcome to our calculator where you can find the exact price for the construction of your window by giving some measures.")
print("Enter window width (in meters):")
widthInput = input()
width = float(widthInput)
print("Enter window height (in meters):")
heightInput = input()
height = float(heightInput)
woodLength = 2 * (width + height) * 3.28
glassArea = 2 * (width * height)
print("The length of the wood needed is " + str(woodLength) + " feet.")
print("The area of the glass needed is " + str(glassArea) + " square metres.")
while True:
    try:
        height = float(input("Enter the height of window (between 0.5 and 3 meters): "))
        if 0.5 <= height <= 3:
            break
        else:
            print("Please enter a valid height between 0.5 and 3 meters.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for height.")

while True:
    try:
        width = float(input("Enter the width of window (between 0.5 and 3 meters): "))
        if 0.5 <= width <= 3:
            break
        else:
            print("Please enter a valid width between 0.5 and 3 meters.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for width.")

wood_price_per_foot = float(input("Enter the price of wood per foot ($): "))
glass_price_per_sq_meter = float(input("Enter the price of glass per square meter ($): "))

window_area = height * width

wood_cost = wood_price_per_foot * (2 * height + 2 * width)

glass_cost = glass_price_per_sq_meter * window_area

total_cost = wood_cost + glass_cost
hst = total_cost * 0.13
total_cost_with_hst = total_cost + hst

print(f"The window is {height:.1f} meters high and {width:.1f} meters wide.")
print(f"The cost of the wood is ${wood_cost:.2f}.")
print(f"The cost of the glass is ${glass_cost:.2f}.")
print(f"The total cost of the window (including HST) is ${total_cost_with_hst:.2f}.")