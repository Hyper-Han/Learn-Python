number = input("请输入你的编号：")
seat = number[0]
west=['A','B','C']
east=['D','E','F']
if seat in west:
    print("西门")
if seat in east:
    print("东门")
