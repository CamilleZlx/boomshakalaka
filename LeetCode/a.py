def f(self,n):
    res = 0
    l = str(n)
    for num in l:
        res = res + pow(int(num),2)
    n = res
    self.f()
    print(res)

if __name__ == '__main__':
    f(19)
    