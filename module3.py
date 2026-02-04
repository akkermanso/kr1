try:
    v1=int(input())
    v2=int(input())
    t=int(input())
except ValueError:
    print('must be int')
else:
    def decorator(func):
        def wrapper():
            func()
            print('s:',((v1+v2)/2)*t)
        return wrapper
    @decorator
    def fun():
        try:
            a=(v2-v1)/t
            print('a:',a)
        except ZeroDivisionError:
            print('t!=0')
    fun()


