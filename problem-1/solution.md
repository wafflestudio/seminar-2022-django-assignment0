1.등록

```
POST /cats/{breed}/facts
{
    "category" : "category",
    "fact" : "fact"
}
```

EX)
```
POST /cats/abyssinian/facts
{
    "category" : "성격 및 행동",
    "fact" : "나무타기나 물놀이를 좋아하는 등 매우 활발하다."
}
```
```
HTTP/1.1 201 Created
Content-Location: /facts/{id}
{
    "id" : "id",
    "category" : "category",
    "fact" : "fact"
}
```


2.수정
1) PUT 이용
```
PUT /cats/{breed}/facts/{id}
{
    "category" : "modified category",
    "fact" : "modified category"
}
```

EX)
```
PUT /cats/abyssinian/facts/1
{
    "category" : "성격",
    "fact" : "호기심이 많다."
}
```
2. PATCH 이용
```
PATCH /cats/{breed}/facts/{id}
{
    "category" : "modified category"
}
```
EX)
```
PATCH /cats/abyssinian/facts/1
{
    "category" : "행동"
}
```

3.삭제
```
DELETE /cats/{breed}/facts/{id}
```
EX)
```
DELETE /cats/abyssinian/facts/1
```
-> 존재하지 않는 id의 fact를 삭제하려고 한 경우
```
HTTP/1.1 404 Not Found
```