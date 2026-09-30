def main():
    arr = [64, 34, 25, 12 ,22, 11, 90]
    for i in range(0, len(arr)):  
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j]=temp

    print(arr)
    print(*(arr))
    for n in range(len(arr)):
        print(arr[n] , end=" ")

 


if __name__ == "__main__":
    main()
