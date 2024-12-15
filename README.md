# selenium-study

Nomad Coder의 selenium 강의 실습을 위한 repo

## 기본 세팅

pipenv를 사용하여 패키지 관리

- python version 3.12 사용

- 설치한 패키지 목록

```bash
pipenv install selenium
pipenv install webdriver-manager
```

- 가상 환경 실행

```bash
pipenv shell
```

## 실습

1. 구글 검색 결과를 스크린샷으로 저장 (`scrap.py`)
   - webdriver-manager를 사용하여 크롬 드라이버 자동 설치
   - `find_element`, `send_keys`, `submit` 메서드를 사용하여 구글 검색 실행
   - `WebDriverWait`와 `EC.presence_of_all_elements_located`를 사용하여 검색 결과가 로드될 때까지 대기
   - `TimeoutException`을 사용하여 검색 결과가 로드되지 않는 경우 예외 처리
   - `find_elements`, `screenshot` 메서드를 사용하여 검색 결과를 스크린샷으로 저장
   - [x] [TO-DO] 해당 code를 class를 사용하여 리팩토링
   - [x] [TO-DO] 검색 결과에서 나오는 최대 페이지 수를 직접 체크하여 모든 페이지에 대해 스크린샷 저장
     - 최대 페이지를 자동으로 체크하지 않고, 사용자에게 최대 페이지 수를 입력받아 스크린샷 저장
     - 실제 결과보다 많은 페이지를 입력받은 경우에 대한 예외 처리를 구현하는 방식으로 처리

## 참고

- [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager)
- [Selenium with Python](https://selenium-python.readthedocs.io/index.html)
