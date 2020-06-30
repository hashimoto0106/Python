file = open('read.txt', 'r')
text = file.read()
print(text)
file.close()


f = open(''read.txt'')
line = f.readline()
while line:
    line = f.readline()
f.close()


# ファイルをオープンする
test_data = open("test_data", "r")

# 一行ずつ読み込んでは表示する
for line in test_data:
  print line

# ファイルをクローズする
test_data.close()



# ファイルをオープンする
test_data = open("test_data", "r")

# 行ごとにすべて読み込んでリストデータにする
lines = test_data.readlines()

# 一行ずつ表示する
for line in lines:
  print line

# ファイルをクローズする
test_data.close()
