특정 품종의 catfact를 등록하고 / 수정하고 / 삭제하는 Rest API의 URI / METHOD를 설계해보자

- 가져오기
특정 품종의 facts들을 가져온다. (성공시 status code 200 반환, 실패시 status code 404 반환)
GET /catfact/<<str:breed>>/
...
{
    "breed": "품종",
    "id" : id
    "catfact": "catfact content"
}
...

특정 품종의 id번째 fact를 가져온다. (성공시 status code 200 반환, 실패시 status code 404 반환)
GET /catfact/<<str:breed>>/<<int:id>>/
{
    "breed": "품종",
    "id" : id
    "catfact": "catfact content"
}


- 등록
특정 품종의 fact를 등록한다. (성공시 status code 201 반환)
POST /catfact/
request: { 
    "breed" : "품종",
    "catfact" : "catfact content",
}


- 수정
특정 품종의 id번째 fact를 수정한다. (성공시 status code 204 반환, id번째 fact를 찾지 못하면 status code 404 반환)
PUT /catfact/<<str:breed>>/<<int:id>>/
request: {
    "catfact" : "catfact content"
}


- 삭제
특정 품종의 id번째 fact를 수정한다. (성공시 status code 204 반환, id번째 fact를 찾지 못하면 status code 404 반환)
DELETE /catfact/<<str:breed>>/<<int:id>>/
