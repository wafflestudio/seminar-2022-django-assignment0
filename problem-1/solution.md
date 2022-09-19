<!-- TODO -->
# CATFACT의 특정 품종에 대한 REST API
## 가져오기
### 모든 종들의 목록을 가져오기
- `GET /cat/breeds/`
- breeds를 통해서 모든 종들의 목록을 가져온다. 
- STATUS CODE
    - 정상적으로 가져와지면 : 200

### 특정 품종의 catfact를 가져오기
- `GET /cat/breeds/{id}/fact`
- id로 품종을 구분해서 특정 품종의 fact를 가져온다. 
- STATUS CODE
    - 가져올 품종이 있으면 : 200
    - 가져올 품종이 없으면 : 404
---
## 등록
- `POST /cat/breeds/{id}/fact`
- 특정 품종{id}의 catfact를 등록할 때
```
request: {
    'fact': '등록할 내용',
}
```
- STATUS CODE
    - 등록할 품종이 없었을 때 : 등록하고, 201
    - 등록할 품종에 fact가 없었을 때 : 201
    - 등록할 품종의 fact가 이미 있었을 때 : 409

---
## 수정
- `PUT /cat/breeds/{id}/fact`
- 특정 품종{id}의 catfact를 수정할 때
``` 
request: {
    'fact': '수정할 내용'
}
```
- STATUS CODE
    - 수정할 품종이 없으면 : 404
    - 수정할 품종의 fact가 없으면 : 추가하고 201
    - 수정할 품종의 fact가 있으면 : 201
---
## 삭제
- `DELETE /cat/breeds/{id}/fact`
- 특정 품종{id}의 catfact를 삭제하고 싶을 때
- STATUS CODE
    - 삭제할 품종이 없다면 : 404
    - 삭제할 품종의 fact가 없으면 : 404
    - 삭제할 품종의 fact가 있으면 : 204(fact를 리턴하지는 않음)
---