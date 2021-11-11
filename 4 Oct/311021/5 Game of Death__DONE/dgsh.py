class game:
    def death(self,n,k):
        cur = 1
        for index in range(1,n+1):
            cur = (cur + k-1) % index+1
        return cur

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,k = map(int,input().split())
        dd = game()
        print(dd.death(n,k))
