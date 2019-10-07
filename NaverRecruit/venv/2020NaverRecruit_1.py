
# Test Case
record = [
    "RECEIVE abcd@naver.com",
    "RECEIVE zzkn@naver.com",
    "RECEIVE aabkn@naver.com",
    "DELETE",
    "DELETE",
    "RECEIVE qwerty@naver.com",
    "SAVE",
    "SAVE",
    "RECEIVE QwerTY@naver.com",
    "DELETE",
    "SAVE",
    "DELETE"
]

tmp_stack = []
result = []

for i in range(len(record)):
    record[i] = record[i].split()
    print(record[i])

    cmd = record[i][0]
    # print(cmd)

    if cmd == "RECEIVE":
        tmp_stack.append(record[i][1])
        print("tmp", tmp_stack)

    # print("tmp", tmp_stack)

    elif cmd == "DELETE":
        if len(tmp_stack) != 0:
            del tmp_stack[-1]

        else:
            # break
            continue

        print("-- after continue --; 임시보관함에 저장된 메일이 있다는 뜻 ")

    elif cmd == "SAVE":
        result += tmp_stack
        tmp_stack = []

print("tmp", tmp_stack)
print("final", result)

'''
record = [
    "RECEIVE abcd@naver.com",
    "RECEIVE zzkn@naver.com",
    "DELETE",
    "RECEIVE qwerty@naver.com",
    "SAVE",
    "RECEIVE QwerTY@naver.com"
]

record = [
    "RECEIVE abcd@naver.com",
    "RECEIVE zzkn@naver.com",
    "DELETE",
    "RECEIVE qwerty@naver.com",
    "SAVE",
    "SAVE",
    "DELETE",
    "RECEIVE QwerTY@naver.com",
    "SAVE"
]
'''
