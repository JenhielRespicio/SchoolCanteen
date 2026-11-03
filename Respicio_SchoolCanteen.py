total_sales = 0
met_target = 0
below_target = 0

food_items = int(input("Enter number of food items: "))

for i in range(1, food_items + 1):
    sale = int(input(f"Enter sales for Item {i}: " ))
    total_sales += sale

    if sale >= 500:
        met_target = met_target + 1
    elif sale < 500:
        below_target = below_target + 1

def calculate_average(total_sales, food_items):
    average_sales = total_sales / food_items
    return average_sales

average = calculate_average(total_sales, food_items)

def display_result():
    print("CANTEEN SALES REPORT")
    print(f"Average Sales: PHP {average:.2f} | Meeting Target: {met_target} | Below Target: {below_target}")

display_result()