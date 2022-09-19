<!-- TODO -->
#등록
POST /catfact
request = {
  "breed": "Abyssinian"
  "fact": "info"
}

#수정
PUT /catfact/<int:pk>
request = {
  "breed": "edited breed"
  "fact": "edited info"
}

#삭제
DELETE /catfact/<int:pk>
