# 1. 등록
## 1) 특정 품종 등록
```
POST /breeds
request: {
    "breed": "Norwegian forest cat"
}
```
## 2) 특정 품종의 fact 등록
```
POST /breeds/{breedid}/facts
request: {
    "fact": "These cats are intelligent and alert, 
            and they love human connection and affection."   
}
```

# 2. 수정
## 1) 특정 품종 수정
```
# PUT 사용, 전체 데이터 수정, 전송하지 않은 데이터 삭제
PUT /breeds/{breedid}
request: {
    "breed": "Norwegian forest"
}

# PATCH사용, 부분 데이터 수정, 전송하지 않은 데이터 미삭제
PATCH /breeds/{breedid}
request: {
    "breed": "Norwegian forest"
}
```
## 2) 특정 품종의 fact 수정
```
# PUT 사용
PUT /breeds/{breedid}/facts/{factid}
request: {
    "fact": "When they do meow, their high-pitched meows 
            sound almost like chirps."
}

# PATCH사용
PATCH /breeds/{breedid}/facts/{factid}
request: {
    "fact": "When they do meow, their high-pitched meows 
            sound almost like chirps."
}
```

# 3. 삭제
## 1) 특정 품종 삭제
```
DELETE /breeds/{breedid}
```

## 2) 특정 품종의 fact 삭제
```
DELETE /breeds/{breedid}/facts/{factid}
```
