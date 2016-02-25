shopping_list = ["banana", "laranja", "maca"]

stock = {
    "banana": 6,
    "maca": 0,
    "laranja": 32,
    "pera": 15
}
    
prices = {
    "banana": 4,
    "maca": 2,
    "laranja": 1.5,
    "pera": 3
}

# Escreva seu codigo abaixo!
def compute_bill(food):
    total = 0
    for var0 in food:
        if stock[var0] > 0:
            total = total + prices[var0]
            stock[var0] = stock[var0] - 1
    return total
    
bag = ["pera","laranja"]
compute_bill(bag)
print stock
