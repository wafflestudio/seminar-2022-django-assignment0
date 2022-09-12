(1) 특정 품종 등록

POST /catfact \
request {\
    "breed" : "cat",\
    "catfact" : "Cats have 30 vertebrae (humans have 33 vertebrae during early development; 26 after the sacral and coccygeal regions fuse)", \
}

(2) 특정 품종 수정

GET /catfact/4 \
request {\
    "breed" : "cat",\
    "catfact" : "Cats have 30 vertebrae (humans have 33 vertebrae during early development; 26 after the sacral and coccygeal regions fuse)",\
    "length" : 122, \
    "number" : 4 \
}

POST /catfact/4 \
request {\
    "breed" : "cat",\
    "catfact" : "Cats dislike citrus scent.", \
    "length" : 26, \
    "number" : 4 \
}

(3) 특정 품종 삭제

DELETE /catfact/4 \
request {\
    "number" : 4 \
}