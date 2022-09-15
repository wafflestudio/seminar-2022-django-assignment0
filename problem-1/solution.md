<!-- TODO -->
특정 품종의 catfact를 등록하고 / 수정하고 / 삭제하는 Rest API의 URI / METHOD를 설계해보자. 다음 링크 참고

#등록

POST /catfacts/create/
request: {
    "breed": "품종 이름"
    "catfact": "catfact 내용"
}

#수정

PUT /catfacts/1
request: {
    "breed": "수정된 품종 이름"
    "catfact": "수정된 catfact 내용"
}

or

PATCH /catfacts/1
request: {
    "catfact": "수정된 catfact 내용"
}

#삭제

DELETE /catfacts/1
