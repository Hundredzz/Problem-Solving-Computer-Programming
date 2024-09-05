"""code"""
def storage_check(storage,version):
    """function"""
    price = 0
    if storage == "128 GB":
        pass
    elif storage == "256 GB":
        price = 4000
    elif storage == "512 GB":
        price = 12000
    elif storage == "1 TB" and version in ("iPhone 13 Pro","iPhone 13 Pro Max"):
        price = 20000
    else:
        price = 1
    return price
def main():
    """function"""
    version = input()
    storage = input()
    price = 0
    if version == "iPhone 13 mini":
        price += 25900
    elif version == "iPhone 13":
        price += 29900
    elif version == "iPhone 13 Pro":
        price += 38900
    elif version == "iPhone 13 Pro Max":
        price += 42900
    else:
        price = 1
    price += storage_check(storage,version)
    if int(str(price)[-1]):
        print("Not Available")
    else:
        print(price)
main()
