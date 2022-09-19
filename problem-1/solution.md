<!-- TODO -->
## 등록
```bash
POST /catfact \
request = { \
  "breed": "Abyssinian" \
  "fact": "info" \
} 
```

## 수정
```bash
PUT /catfact/<int:pk> \
request = { \
  "breed": "edited breed" \
  "fact": "edited info" \
} 
```
## 삭제
```bash
DELETE /catfact/<int:pk> 
```
