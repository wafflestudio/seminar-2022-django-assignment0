<!-- TODO -->
새 품종을 등록
POST /catfact
request: {
    "breed": ""
}
response: 
- 등록 성공시: HTTP/1.1 201 Created {
    "breed_id" : 1,
    "breed" : ""
}
- 이미 존재하는 품종: HTTP/1.1 409 Conflict {
    "breed" : "",
    "message" : "breed already exist"
}
- 이외: HTTP/1.1 400 Bad Request {
    "message" : "error message"
}


특정 품종을 삭제
DELETE /catfact
request: {
    "breed" : ""
}
response: 
- 삭제 성공시: HTTP/1.1 204 No Content {}
- 존재하지 않는 품종: HTTP/1.1 404 Not Found {
    "breed" : "",
    "message" : "breed not exist"
}
- 이외: HTTP/1.1 400 Bad Request {
    "message" : "error message"
}

특정 품종의 catfact 등록
POST /catfact/<str:breed>
request: {
    "fact" : ""
}
response:
- 등록 성공시 HTTP/1.1 201 Created {
    "id" : 1,
    "breed" : "", 
    "fact" : ""
}
- 존재하지 않는 품종: HTTP/1.1 404 Not Found {
    "breed" : "",
    "message" : "breed not exist"
}
- 이외: HTTP/1.1 400 Bad Request {
    "message" : "error message"
}

특정 품종의 catfact 삭제
DELETE /catfact/<str:breed>/<int:id>
request: {}
response: 
- 삭제 성공시: HTTP/1.1 204 No Content {}
- 존재하지 않는 id/bread: HTTP/1.1 404 Not Found {
    "id" : 1,
    "breed" : "",
    "message" : "id/bread not exist"
}
- 이외: HTTP/1.1 400 Bad Request {
    "message" : "error message"
}

특정 품종의 catfact 수정
PUT /catfact/<str:breed>/<int:id>
request: {
    "fact" : ""
}
response: 
- 수정 성공시: HTTP/1.1 200 OK {
    "id" : 1,
    "breed" : "", 
    "fact" : ""
}
- 존재하지 않는 id/bread: HTTP/1.1 404 Not Found {
    "id" : 1,
    "breed" : "",
    "message" : "id/bread  not exist"
}
- 이외: HTTP/1.1 400 Bad Request {
    "message" : "error message"
}

특정 품종의 catfact 중 하나를 랜덤으로 불러옴
GET /catfact/<str:breed>
request : {}
response: 
- 불러오는 데 성공: HTTP/1.1 200 OK {
    "id" : 1,
    "breed" : "", 
    "fact" : ""
}
- 존재하지 않는 breed: HTTP/1.1 404 Not Found {
    "breed" : "",
    "message" : "bread not exist"
} 
- 그 breed의 fact가 한 개도 없음: HTTP/1.1 404 Not Found {
    "message" : "no fact exist"
} 
- 이외: HTTP/1.1 400 Bad Request {
    "message" : "error message"
}

catfact 중 하나를 랜덤으로 불러옴
GET /catfact
request : {}
response: 
- 불러오는 데 성공: HTTP/1.1 200 OK {
    "id" : 1,
    "breed" : "", 
    "fact" : ""
}
- breed가 한 개도 없음: HTTP/1.1 404 Not Found {
    "message" : "no bread exist"
} 
- 이외: HTTP/1.1 400 Bad Request {
    "message" : "error message"
}

특정 품종의 catfact를 모두 불러옴
GET /catfacts/<str:breed>
request : {}
response : 
- 불러오는 데 성공: HTTP/1.1 200 OK {
    "breed" : "",
    "content" : [
        {
            "id" : 1,
            "fact" : ""
        }, 
        {
            "id" : 2,
            "fact" : ""
        }
    ]
}
- 존재하지 않는 breed: HTTP/1.1 404 Not Found {
    "breed" : "",
    "message" : "bread not exist"
} 
- 이외: HTTP/1.1 400 Bad Request {
    "message" : "error message"
}

모든 품종의 catfact를 모두 불러옴
GET /catfacts/
request : {}
response : 
- 불러오는 데 성공: HTTP/1.1 200 OK {
    [
        {
            "breed" : "",
            "content" : [
                {
                    "id" : 1,
                    "fact" : ""
                }, 
                {
                    "id" : 2,
                    "fact" : ""
                }
            ]
        }, 
        {
            "breed" : "",
            "content" : [
                {
                    "id" : 1,
                    "fact" : ""
                }, 
                {
                    "id" : 2,
                    "fact" : ""
                }
            ]
        }
    ]
}
- breed가 하나도 없음 : HTTP/1.1 404 Not Found {
    "message" : "no bread exist"
} 
- 이외: HTTP/1.1 400 Bad Request {
    "message" : "error message"
}
