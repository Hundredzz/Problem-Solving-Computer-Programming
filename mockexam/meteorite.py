"""code"""
def main():
    """function"""
    m_weight = float(input())
    m_sub = int(input())
    safe_weight = float(input())
    time = 0
    old_weiht = 0
    m_count = 0
    old_weiht = m_weight
    while m_weight >= safe_weight:
        m_weight /= m_sub
        time += m_count
        m_count = old_weiht / m_weight
        if not time:
            time += 1
    print(int(time))
main()
