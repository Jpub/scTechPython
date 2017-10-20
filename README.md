  
# 엔지니어를 위한 파이썬
  
 ![처음 만나는 자바스크립트 표지](http://image.kyobobook.co.kr/images/book/large/777/l9791185890777.jpg)
  
**출판사** 제이펍  
**원출판사** SBクリエイティブ  
**원서명** 確かな力が身につくJavaScript「超」入門(원서 ISBN: 9784797383584)  
**저자명** 가노 스케하루  
**역자명** 김완섭  
**출판일** 2017년 2월 24일  
**페이지** 352쪽  
**시리즈** First Step 시리즈 01  
**ISBN** 979-11-85890-77-7 (93000)  

[### 도서 소개 페이지 바로 가기 ###](http://jpub.tistory.com/)  



_ _ _




이 저장소는 제이펍에서 출간된 아래 서적에 대한 예제 코드를 제공하기 위한 것입니다.

""표지 이미지 및 서지사항""

이 저장소는 주로 이 책에 나온 소스코드와 함께, 지원 웹페이지에 부가 정보를 제공합니다.

깃헙 저장소: https://github.com/pyjbooks/py4science                        
지원 웹페이지: https://pyjbooks.github.io/py4science/

# 소스 코드에 대하여

소스 코드는 이 저장소의 master 브랜치에 있는 "src" 디렉터리에 각 장으로 나뉘어
들어 있습니다. Git을 사용할 수 있는 분은 이 저장소를 클론하시면 됩니다.

Git을 사용하지 않는 분은 이 저장소의 최상위 페이지에서 "Clone or Download"
버튼을 눌러 zip 파일을 다운로드 받으실 수 있습니다.

## 줄바꿈 및 스페이스

이 책에서는 지면 관계상 "줄바꿈"과 "공백"을 의도적으로 적게 사용하였습니다.
그러나 이 저장소에 포함된 소스코드는 PEP8을 준수하여 줄바꿈 및 공백을 사용하고
있습니다.

## import 문 생략

또 소스 코드 앞머리에 오는 import 문 역시 지면 관계상 책에서는 생략된 경우가
있습니다. 이 경우 아래와 같은 import 문이 앞서 나온다는 것을 전제로 하고 있으므로
주의가 필요합니다. 이 저장소에 있는 소스 코드에는 이러한 생략이 없습니다.

  import numpy as np  # NumPy를 np라는 별명으로 임포트
  import scipy as sp  # SciPy를 sp라는 별명으로 임포트
  import pandas as pd  # pandas를 pd라는 별명으로 임포트
  import matplotlib as mpl  # Matplotlib를 mpl이라는 별명으로 임포트
  import matplotlib.pyplot as plt  # Matplotlib.pyplot을 plt라는 별명으로 임포트
  import numexpr as ne  # Numexpr를 ne라는 별명으로 임포트

## Matplotlib에 대한 설정

Matplotlib에 대한 설정은 유저의 환경에 따라 서로 다르므로, 이 책에 실린 플로팅
결과와는 다소 다른 결과를 얻는 경우가 있습니다. 이런 경우에는 책 9.2항을 참고하여
설정을 조정하시면 됩니다.

이 책에서는 다음과 같은 설정을 추천합니다. 책과 다른 결과가 나온다면 아래와 같은
설정을 추가해 주십시오. ("mpl"은 위의 내용과 같이 "matplotlib"의 별명입니다.)

  mpl.rcParams['figure.autolayout'] = True
  mpl.rcParams['font.size'] = 14
  mpl.rcParams['axes.grid'] = True

또, 대화형 모드가 off로 설정된 경우에는 플로팅 결과가 출력되지 않는 경우가 있습니다.
이럴 때는 'plt.ion()'("plt"는 앞서 설명했든 "matplot.pyplot"의 별명) 명령으로
대화형 모드를 활성화시켜 주십시오. 아니면, 플로팅을 마친 후에 'plt.show()'를
실행하여 플로팅 결과를 출력하는 방법도 가능합니다.

## 그 외의 사항

향후 오류가 발견되어서 이 저장소의 소스 코드가 수정되었을 경우가 있습니다.
그 외에도 책에 실린 소스 코드 역시 위에서 생략했던 import 문이 추가되거나
약간의 수정이 있을 수 있습니다.


## 라이선스

이 저장소에 포함된 소스 코드의 라이선스는 "LICENCE.md"에 명시되어 있습니다.
