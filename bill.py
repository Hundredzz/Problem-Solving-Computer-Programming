"""code"""
def main():
    """bill_cal"""
    price = int(input())
    service = price * (10 / 100)
    real_service = max(50, service)
    real_service = min(1000, real_service)
    vat = (price + real_service) * 7 / 100
    print(f"{price + real_service + vat:.2f}")
main()
