import random

print(random.random())#(0,1)----float    大于0且小于1之间的小数

print(random.randint(1,3))  #[1,3]    大于等于1且小于等于3之间的整数

print(random.randrange(1,3)) #[1,3)    大于等于1且小于3之间的整数

print(random.choice([1,'23',[4,5]]))#1或者23或者[4,5]

print(random.sample([1,'23',[4,5]],2))#列表元素任意2个组合

print(random.uniform(1,3))#大于1小于3的小数，如1.927109612082716

item=[1,3,5,7,9]
random.shuffle(item) #打乱item的顺序,相当于"洗牌"
print(item)

# 案例：生成随机验证码
import random

def make_code(size):
    res = ''
    for i in range(size):
        s1=chr(random.randint(65,90))
        s2=str(random.randint(0,9))
        res += random.choice([s1,s2])
    return res

print(make_code(6))  # 6Q6M08

