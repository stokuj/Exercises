# Write your solution here


def search(products: list, criterion: callable) -> list:
    return list(filter(criterion, products))

def price_under_4_euros(product):
    return product[1] < 4

