v1=int(input())
v2=int(input())
t=int(input())
def decorator(func):
    def wrapper():
        func()
        print('s:',((v1+v2)/2)*t)
    return wrapper
@decorator
def fun():
    a=(v2-v1)/t
    print(a)
fun()


