file = open('read.txt', 'r')
text = file.read()
print(text)
file.close()


f = open(''read.txt'')
line = f.readline()
while line:
    line = f.readline()
f.close()


# �t�@�C�����I�[�v������
test_data = open("test_data", "r")

# ��s���ǂݍ���ł͕\������
for line in test_data:
  print line

# �t�@�C�����N���[�Y����
test_data.close()



# �t�@�C�����I�[�v������
test_data = open("test_data", "r")

# �s���Ƃɂ��ׂēǂݍ���Ń��X�g�f�[�^�ɂ���
lines = test_data.readlines()

# ��s���\������
for line in lines:
  print line

# �t�@�C�����N���[�Y����
test_data.close()
