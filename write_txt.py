# Write File
# 1. open()
f = open('haedal.txt', 'w') # 'w' : write, 'r' : read, 'a' : append
for i in range(10):
  f.write(f'Hello, Haedal {i}\r\n')
f.close()

# 2. with open()
with open('haedal.txt', 'w') as f:
  f.write('Hello, Haedal!\n')


# 2-1. writelines
with open('haedal.txt', 'w') as f:
  f.writelines(['1\n','2\n','3\n'])

# with: Context Manager

# \를 사용하는 문자 -> 이스케이프 시퀀스(문자)
# \n : 개행 문자
# \t : tab 문자
# \\ : 역슬레시 문자
# \' : 따옴표 문자
# \" : 쌍따옴표 문자