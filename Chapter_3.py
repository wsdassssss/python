#Chapter 3 列表 []
#Author:Mimo431
#Date:2020-11-03
stu=['xiaoming','xiaobai','xiaohong','aimong','honglai','fssss']
print(stu)#输出所有元素
print(stu[1])#xiaobai
print(stu[2])
print(stu[-1])#访问最后一个元素

msg=f"hello,my name is  {stu[2]}"#在字符串中使用元素
print(msg)

stu[1]="mimo" #修改元素
print(stu[1])

stu.append("xiaolv")#添加元素
print(stu)

#数组中间插入元素
stu.insert(2,"xiaohei")#第三个位置插入元素
print(stu)

#列表删除元素
del stu[2]
print(stu)

#删除最后一个元素，但还要使用元素,删除第i+1个
i=1
print("*****")
stu_del=stu.pop(i)
print(stu)
print(stu_del)

#根据value来删除对应元素,remove只能删除第一个
print("*******")
print(stu)
stu.remove("xiaolv")
print(stu)

#排序
print("******")
stu.sort()#根据首字符大小写，ASCII？
print(stu)

stu.sort(reverse=True)#逆向排序
print(stu)

#临时排序
print("********")
print(stu)
print(sorted(stu))
print(stu)

#反转元素
print("*******")
print(stu)
stu.reverse()
print(stu)
print(stu)

#列表长度
print("********")
print(stu)
print(len(stu))

