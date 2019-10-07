
def solution(n):
    answer = 0
    stack = []
    # result = [0, ]

    # [x * y for i, x in enumerate(range(1, n + 1)) for j, y in enumerate(range(1, n + 1)) if x < y]

    for x in range(1, (n+2)):
        res = x

        for y in range(1, (n+2)):
            if x >= y:
                continue

            res *= y

            if res <= 10**12:
                if not res in stack:
                    stack.append(res)

    # result = sorted(set(stack))
    result = sorted(stack, reverse=0)

    print(result)
    print("n", n)
    print("size", len(result))
    print("max", max(result))

    n_figure = 0

    # print(sum(1 for _ in str(max(result))))
    for _ in str(max(result)):
        n_figure += 1

    print("n-figure", n_figure)

    answer = result[n - 1]

    return answer


# n = 1
# n = 2
# n = 10
n = 500
print(solution(n))


# def solution(n):
#     answer = 0
#     begin = 1
#     end = 10
#     result = []
#     # result.append(1)
#
#     for i in range(begin, end):
#         mul = i
#         for j in range(i + 1, end + 1):
#             # print(i, j)
#             mul *= j
#             result.append(mul)
#
#         i += 1
#
#     result = sorted(set(result))
#     print(result)
#
#     if len(result) < 10**6 and max(result) < 10**12:
#         # print(result)
#         answer = result[n - 1]
#
#     return answer
