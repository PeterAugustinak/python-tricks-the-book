# good example to use assert in the code
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

# usage
shoes = {'name': "Fancy shoues", 'price': 14900}
price_valid = apply_discount(shoes, 0.25)
print(price_valid)

price_invalid = apply_discount(shoes, 2.0)
print(price_invalid)

# another possible example to use
def do_x():
    pass

def do_y():
    pass

cond = ''

if cond == 'x':
    do_x()
elif cond == 'y':
    do_y()
else:
    assert False, ("This should never happen")

# INCORRECT USAGE for data validation
# if asserts are disabled, then this can cause problems - any user can
# delete, unknown product can be trying to be deleted (DOS attack)
def delete_product(prod_id, user, store):
    assert user.is_admin(), "Must be admin"
    assert store.has_product(), "Unknown product"

    store.get_product(prod_id).delete()
