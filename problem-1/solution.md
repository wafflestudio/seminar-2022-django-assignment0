
> 등록

- **POST**

/breeds : 품종 등록

```
POST /breeds

body: {"breed": {품종}}
```

/breeds/{breed-id}/facts : 해당 품종의 fact 등록

```
POST /breeds/{breed-id}/facts

body: {"fact1": {fact1},
       "fact2": {fact2}...}
```


> 수정

- **PUT**

/breeds/{breed-id} : 해당 품종 전체 수정
```
PUT /breeds

body: {"breed": {품종}}
```

/breeds/{breed-id}/facts : 해당 품종의 fact 전체 수정
```
PUT /breeds/{breed-id}/facts

body: {"fact1": {fact1},
       "fact2": {fact2}...}
```

- **PATCH**

/breeds/{breed-id} : 해당 품종 일부 수정
```
PATCH /breeds

body: {"breed": {품종}}
```
/breeds/{breed-id}/facts: 해당 품종의 fact 일부 수정
```
PATCH /breeds/{breed-id}/facts

body: {"fact2": {fact2}}
```

>삭제

- **DELETE**

/breeds : 품종 전체 삭제

/breeds/{breed-id} : 해당 품종 삭제

/breeds/{breed-id}/facts : 해당 품종 fact 삭제

```
DELETE /breeds...
```



성공적인 request의 경우 200번대 status code를, 잘못된 request는 400번대 status code를 return함.

