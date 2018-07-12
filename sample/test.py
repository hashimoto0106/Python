print("Hello world!")

# コンソール入出力
buf = input('Input number : ')
type(buf)
int_a = int(buf)
type(int_a)
print(int_a)

# ファイル入出力
f = open('test.txt', 'r', encoding='utf-8')
for line in f:
    print(line, end='')
f.close()

a = ['aaaaa', 'bbbbbb', 'ccccccccc']
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Hello\n')
    f.writelines(a)
