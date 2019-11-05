# 파이썬과 함께 걷기
> 여러 파이썬 프로젝트를 해봅니다

`string_interpolation.py` : 문자열을 사용하는 여러 방법들을 알아봅니다  

1. 옛날 방식
2. `pyformat`
3. `f-string`
```python
# String Interpolation
a = '123'
new_q = f'{a}'

# 1. 옛날 방식
f'%s %s' % ('one', 'two') # => 'one two'

# 2. pyformat
'{} {}'.format('one', 'two') #=> 'one two'

# 3. f-string
a, b = 'one', 'two'
f'{a} {b}' # => 'one two'

# example
name = '홍길동'
eng_name = "Hong Gil dong"

print('안녕하세요, {1}입니다. My name is {0}'.format(name, eng_name))
print(f'안녕하세요, {name}입니다.')
```

`lotto.py` : `random` 이용한 로또 뽑기
```python
import random

numbers = range(1, 46)

lotto = random.sample(numbers, 6)
print(lotto)
print(f'오늘의 행운의 로또는 {sorted(lotto)} 입나다')
```

`write_txt.py` : 파일 입력을 배워봅니다. 하나씩 해봅시다.   
```python
# 하나씩 해봅니다

# Write File
# 1. open()
f = open('mulcam.txt', 'w') # 'w' : write, 'r' : read, 'a' : append
for i in range(10):
  f.write(f'Hello, Mulcam {i}\r\n')
f.close()

# 2. with open()
with open('mulcam.txt', 'w') as f:
  f.write('Hello, Mulcam!\n')

# 2-1. writelines
with open('mulcam.txt', 'w') as f:
  f.writelines(['1\n','2\n','3\n'])

# with: Context Manager

# \를 사용하는 문자 -> 이스케이프 시퀀스(문자)
# \n : 개행 문자
# \t : tab 문자
# \\ : 역슬레시 문자
# \' : 따옴표 문자
# \" : 쌍따옴표 문자
```

`read_txt.py` : 파일 출력을 배워봅니다.  
1. `open files()`
2. `with open()`
```python
# Read File

# 1. open files()
f = open('haedal.txt', 'r')
all_text = f.read()
print(all_text)
f.close()

# 2. with open()
with open('haedal.txt', 'r') as f:
  lines = f.readlines() # List
  for line in lines:
    print(line)
```

`naver_rank.py` : 네이버 실시간 검색어를 긁어옵니다
> 

필요한 라이브러리(`requests`, `bs4`)부터 받습니다
```bash
$ pip3 install requests
```
```bash
$ pip3 install bs4
```

```python
import requests # pip install requests
import bs4 # pip install bs4
import datetime

html = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(html, 'html.parser')

ranks = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k')
now = datetime.datetime.now()

with open('naver_rank.txt', 'w', encoding='utf-8') as f:
  f.write(f'{now} 기준 네이버 검색어 순위\n')
  for i, rank in enumerate(ranks): # [(0, 'a'), (1, 'b'), ...]
    f.write(f'{i+1}. {rank.text}\n')
```