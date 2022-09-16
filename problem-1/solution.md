# Problem 1

특정 품종의 catfact를 등록, 수정, 삭제하는 REST API를 설계한다.

Method|POST|PUT|DELETE
---|---|---|---
/breeds|품종 등록|405 ERROR|품종 전체 삭제
/breeds/1|405 ERROR|ID ```1``` 품종 수정|ID ```1``` 품종 삭제
/breeds/1/facts|ID ```1``` 품종의 catfact 등록|405 ERROR|ID ```1``` 품종의 catfact 전체 삭제
/breeds/1/facts/1|405 ERROR|ID ```1``` 품종의 ID ```1``` catfact 수정|ID ```1``` 품종의 ID ```1``` catfact 삭제

## 품종 등록

```
POST /breeds
body: {
    "breed": "breed of cat"
}
Content-Type: "application/json"
```

## 특정 품종의 catfact 등록, 수정, 삭제

### 등록

```
POST /breeds/{breed-id}/facts
body: {
    "fact": "cat fact to post"
}
Content-Type: "application/json"
```

### 수정

```
PUT /breeds/{breed-id}/facts/{fact-id}
body: {
    "fact": "new cat fact"
}
Content-Type: "application/json"
```

### 삭제

```
DELETE /breeds/{breed-id}/facts/{fact-id}
```
