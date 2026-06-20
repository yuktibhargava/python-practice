def apply_discount(price, discount):
    if not isinstance(price, (int,float)):
        return 'The price should be a number'
    elif not isinstance(discount, (int,float)):
        return 'The discount should be a number'
    elif discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    final_price = price - (price * discount / 100)
    return final_price
print(apply_discount(100, 20)) 
print(apply_discount(50, 10))  