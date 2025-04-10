def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def compute_total_with_fee(x, y, fee_percent):
    subtotal = add(x, y)
    fee = subtotal * fee_percent / 100
    return subtotal + fee
