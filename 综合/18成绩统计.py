n=int(input())
for i in range(n):
    m=[int(a) for a in input().split()]
    c=len(m)
    m_max=max(m)
    m_min=min(m)
    ave=sum(m)/c
    print(c,m_max,m_min,ave)
