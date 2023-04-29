

numbers = [1.54, 1.93, 2.41, 4.02, 6.71, 11.18, 27.97, 69.93, 349.69]


for i, number in enumerate(numbers):
    try:
        result = numbers[i+1] - numbers[i]
        print(result)
    except IndexError:
        print("DONE!")




0.39
0.48
1.61
2.69
4.47
16.79
41.96
279.76