# https://6793fdf6.widgets.sphere-engine.com/lp?hash=TWKE0EUuyq
def groupAnagrams(strs):
    if len(strs)==0:
        return [[]]
    for i in range(len(strs)):
        strs[i] = ["".join(sorted(strs[i])),strs[i]]
    
    strs = sorted(strs)

    ans = [[strs[0][1]]]
    for i in range(1,len(strs)):
        if strs[i][0] == strs[i-1][0]:
            ans[-1].append(strs[i][1])
        else:
            ans.append([strs[i][1]])
    
    ans.sort()
    return ans

if __name__ == '__main__':

    for _ in range(int(input())):
        n = int(input())
        arr = input().split()

        print(groupAnagrams(arr))