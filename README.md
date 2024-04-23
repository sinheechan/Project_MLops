# Project_MLops

<br/>

<img src="MLops_workflow.png">

<br/><br/>

## Object

이 프로젝트는 Python, SQL 코드를 활용하여 데이터 수집부터 데이터베이스 적재까지의 일련의 과정을 자동화하는 것을 목표로 합니다.

또한 일정 시간마다 데이터를 최신화하여 보다 양질의 데이터를 제공하는 모델을 구축하고 있습니다.

<br/><br/>

## Content

1. Module 소개
2. 데이터 가져오기
3. 데이터 적재

<br/><br/>

### 1. Module 소개

<br/>

- app_starter.py : 서버를 구동하는 메인 모듈입니다. ( __name__ == __main__ )
- api_test.py : 데이터를 요청하고 서버 응답자료를 받아 JSON 반환하고 DataFrame 형태로 처리합니다.
- getdata_from_db.py : watcher모델에서 지정한 시간에 맞춰 감시폴더 내 DB 최신화합니다.
- external_api_test.py : 외부데이터를 문자열로 수집하여 그 값을 반환합니다.

<br/><br/>

### 2. 데이터 가져오기

<br/>

- app_starter.py 실행하면 __name__ == __main__ 실행조건이 충족되어 Flask 애플리케이션에 API를 추가합니다.

  이 코드를 실행함으로써 API의 버전, 제목, 설명 등을 설정할 수 있습니다.

  [URL] http://127.0.0.1:9999/api-docs 

* API 홈페이지 이미지


- tes






















































