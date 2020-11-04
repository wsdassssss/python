#Chapter_2
name="xiaoming"
sex="bOy"
msg=f'{name} an {sex}'
print(msg)
print(msg.title())#首字母大写
print(msg.upper())#全部大写
print(msg.lower())#全部小写
print("Languages:\n\tPython\n\tJAVA\n\tC++")#\n 换行  \t TAB

language=" Python  "
print(language.rstrip())#去除尾部空白
print(language.lstrip())#去除头部空白
print(language.strip())#去掉两边空白

#算数运算符
print(4-3)
print(4+3)
print(4*3)
print(4/3)#1.6666666666666666667

print(4**2)#==pow(x,y) 25
print(1+3*4)#14

print(-1.1+0.2)#0.30000000000000004

print(99_200_30)#10020030

x,y,z=-1,0,0
MAX_XX=40#一般把纯大写变量看作是常量
print(MAX_XX)


def chap2(player):
    print(f"Hello {player},would you like to learn some Python today?")
if __name__ == '__main__':
    chap2(name)
    msg="hello ,who \"are you\" "
    print(msg)

