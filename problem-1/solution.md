특정 품종의 catfact 등록, 수정, 삭제 API
---
### 1. catfact 등록하기
- URL : /catfact/
- METHOD : POST
```
request = {
    "cat-breed": "siamese",
    "fact" : "Siamese cats are an ancient cat breed and have lived side-by-side with humans for hundreds of years."
}
```

### 2. catfact 수정하기
- URL : /catfact/<fact-id>
- METHOD : POST
```
request = {
    "fact-id" : 1
    "edited-cat-breed" : "siamese",
    "edited-fact" : "They are so cute."
}
```

### 3. 삭제
- URL : /catfact/<fact-id>
- METHOD : DELETE
```
request = {
    "fact-id" : 1
}
```