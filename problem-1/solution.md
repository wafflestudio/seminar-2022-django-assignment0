<!-- TODO -->
# GET

## GET /catfact

고양이에 대한 여러 사실 중 하나를 랜덤으로 불러옴; 성공시 status code 200 반환; 실패시 status code 404 반환.
    {
        "breed": "품종",
        "fact": "고양이에 대한 사실"
    }

## GET /catfact/<str:breed>

특정 품종에 대한 여러 사실 중 하나를 랜덤으로 불러옴; 성공시 status code 200 반환; 실패시 status code 404 반환.
    {
        "breed": <str:breed>,
        "fact": "고양이에 대한 사실"
    }

## GET /catfact/<str:breed>/<int:pk>

특정 품종에 대한 pk번째 사실을 불러옴; 성공시 status code 200 반환; 실패시 status code 404 반환.
    {
        "breed": <str:breed>,
        "fact": "pk번째 사실"
    }


# POST

## POST /catfact

특정 품종에 대한 사실을 추가함; 성공시 status code 201 반환.
    request: {
        "breed": "품종",
        "fact": "특정 품종에 대한 사실"
    }


# PUT

## PUT /catfact/<str:breed>/<int:pk>

breed 품종에 대한 pk번째 사실을 수정함; 성공시 status code 204 반환; 만약 breed 품종의 pk번째 사실을 찾는 것에 실패하는 경우 status code 404 반환.
    request: {
        "fact": "수정할 사실"
    }


# DELETE

## DELETE /catfact/<str:breed>/<int:pk>

breed 품종에 대한 pk번째 사실을 삭제함; 성공시 status code 204 반환; 만약 breed 품종의 pk번째 사실을 찾는 것에 실패하는 경우 status code 404 반환.