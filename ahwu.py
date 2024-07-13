# list可以混合String, int, float
# index的概念(類似門牌號碼)
# append(為什麼要用append)
# l = []
# for i in range(5):
#     l.append(i)
# print(l)
# a = int(input("請輸入"))
# print(type(a))
# a = 12.333
# print(type(a))

# input()是str的格式，想轉型態必須使用int()包住input()
# list中運用 "+"  "*"會增加list的元素
# find()的使用方式text.find("a")會去尋找text中是否有a這個字串，如若找不到就返回-1，找到的話就返回index值

# split()跟join()必須針對的對象是str
# 生成式寫法用切割的方式來看，前半部分是return的值，後半部分是forloop或是if條件=>生成式產生的都是list
# Slice語法=>[start : stop : step]取index，記得stop會減1，step如果是負數代表倒退

# l = [1, 2, 3]
# # print(1 in l)
# l = ["2a", "1b", "1c"]
# # print("b "not in l)
# l = [1, 2, 1]
# # print(min(l))
# print(l.count(1))
Capitals = dict()

# Fill it with some values
# Capitals['Russia'] = 'Moscow'
# Capitals['Ukraine'] = 'Kiev'
# Capitals['USA'] = 'Washington'
# print(Capitals)

a = zip([1, 2, 3],[4, 5])
print(*a)