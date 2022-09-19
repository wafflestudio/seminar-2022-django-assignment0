특정 품종의 catfact  등록

POST /catfact
{
  "breed" : "품종",
  "fact" : "팩트"
}

특정 품종의 catfact 수정

PUT /catfact/{id}
{
  "breed" : "수정할 품종",
  "fact" : "수정된 팩트"
}

특정 품종의 catfact 삭제
DELETE /catfact/{id}
{
  "breed" : "삭제할 품종"
}
