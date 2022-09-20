
> 등록

- **POST**

/breeds : 품종 등록

```
POST /breeds

body: {"breed": {품종}}
```

/facts : 해당 품종의 fact 등록

```
POST /facts

body: {"fact1": {fact1},
       "fact2": {fact2}...}
```


> 수정

- **PUT**

/breeds/{breed-id} : 해당 품종 전체 수정
```
PUT /breeds/{breed-id}

body: {"breed": {품종}}
```

/facts/{facts-id} : 해당 품종의 fact 전체 수정
```
PUT /facts/{facts-id}

body: {"fact": {fact}}
```

- **PATCH**

/breeds/{breed-id} : 해당 품종 일부 수정
```
PATCH /breeds

body: {"breed": {품종}}
```
/facts/{fact-id}: 해당 품종의 fact 일부 수정
```
PATCH /facts/{fact-id}

body: {"fact": {fact}}
```

>삭제

- **DELETE**

/breeds : 품종 전체 삭제

/breeds/{breed-id} : 해당 품종 삭제

/facts : fact 삭제

/facts/{fact-id} : 특정 fact 삭제
```
DELETE /breeds...
```



성공적인 request의 경우 200번대 status code를, 잘못된 request는 400번대 status code를 return함.

