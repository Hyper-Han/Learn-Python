rank={'普通会员':0.95,'银会员':0.90,'金会员':0.85}
goods={'商品一':100,'商品二':200,'商品三':300}
x,y,z=input().split()
m=rank[x]*goods[y]*int(z)
print(m)
