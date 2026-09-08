import pandas as pd

print(pd.__version__)

# pandas : 데이터 입출력, 탐색, 정제, 변환, 집계, 분석... -> 편하게 가능
# Series클래스
# DataFrame클래스

# pandas.py
# class Series: 1차원 배열 + 메서드
# class DataFrame: 2차원 배열 + 메서드

s1 = pd.Series([1,3,5], index= [10,20,30]) # Series클래스의 생성자 (함수) 호출 
print(type(s1))
print(s1)

# ii(인티지 인덱스) : 위치값 
# li(레이블 인덱스) : 자주 사용