def calculate_discount(price,discount_percentage):
    discount = price*discount_percentage/100

    if discount_percentage > 20:
        final_price = price - discount
        return final_price
    else:
        return price 

price = float(input("Enter the price: "))
discount_percentage = float(input("Enter the discount percentage: "))


print("The final price is: ", calculate_discount(price,discount_percentage))