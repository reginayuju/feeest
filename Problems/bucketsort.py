data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

def bucketsort(data):
    max_score = 100
    bucket = []
    print("AAA",data)
    print("BBB",bucket)


    for i in range(max_score+1):
        bucket.append(0)
    print("CCC",bucket)
    for score in data:
        print("DDD",bucket)
        print(data,score)
        bucket[score] = bucket[score] + 1
        print(score,bucket)

    index = 0
    for i in range(len(bucket)):
        if bucket[i] != 0:
            for j in range(bucket[i]):
                data[index] = i
                index += 1

bucketsort(data)
print(data)