"""code"""
def check_ping(ping_wip):
    """ping"""
    ping_wip = ping_wip[::-1]
    ip = ""
    num = 0
    for i in ping_wip:
        if not num:
            if i.isnumeric() or i in (":","."):
                num = 1
                ip += i
        elif i.isnumeric() or i in (":","."):
            ip += i
        else:
            break
    ip = ip[::-1]
    return ip
def main():
    """function"""
    _ = input()
    _ = input()
    pas = 0
    low = 2000000000000000000
    avg = 0
    high = 0
    ping_wip = input()
    for _ in range(4):
        rp1 = input()
        if rp1.count("Reply"):
            pas += 1
            if rp1.count("<"):
                low = 0
            else:
                num = int(rp1[rp1.find("time")+5:rp1.rfind("ms")])
                if num < low:
                    low = num
                if num > high:
                    high = num
                avg += num
    ping_wip = ping_wip[:ping_wip.find("with")-1]
    ip = check_ping(ping_wip)
    print(f"Ping statistics for {ip}:")
    print(f"    Packets: Sent = 4, Received = {pas}, Lost = {4 - pas} ({100-(pas*25)}% loss),")
    if pas:
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {low}ms, Maximum = {high}ms, Average = {avg//pas}ms")
main()
