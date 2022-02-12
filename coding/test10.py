def printTrianger(char, height=5):
    for i in range(1,height+1):
        for j in range(height-i):
            print(' ',end='')
        for j in range(2*i-1):
            print(char,end='')
        print('@',6)
printTrianger('@',6)
printTrianger('#',height=7)
printTrianger(char='*')
def test(a,*books):
    print(books)
    for i in books:
        print(i)
    print(a)
test(5,'疯狂java讲义','疯狂python讲义')