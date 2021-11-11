def findLuckyNumber(input_arr):
    for i in range(len(input_arr)):
        for j in range(len(input_arr)):
            ans = 0
            if(input_arr[i] == input_arr[j]):
                ans = input_arr[i]
            if(ans <= 0):
                return -1
            else:
                return ans

if __name__ == "__main__":
    num_elems = int(input())
    input_arr = []
    for index in range(num_elems):
        input_arr.append(int(input()))
