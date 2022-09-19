<!-- TODO -->

<head>
    <h1>CatFact 를 CRUD 하는 REST API 설계 </h1>
</head>

<body>
<p>
<h2>GET (조회)</h2>
특정 품종의 catfact를 조회하려면, GET Method를 이용한다. <br>
GET /catfact/bread/'특정 품종 이름' <br>
ex) GET catfact/bread/American_Shorthair <br> 

요청 성공 시 Code 200 return <br>
요청 실패 시에는 Code 404 return</p>
    
<p>
<h2>POST (등록)</h2>
특정 품종의 catfact를 등록하려면, POST Method를 이용한다. <br>
POST /catfact/bread/'특정 품종 이름' <br>
{
    'name' : '특정 품종의 이름',
    'id' : '특정 품종의 id',
    'fact' : '특정 품종에 관한 사실'
    etc...
} <br>

ex) POST /catfact/bread/American_Shorthair

{
    'name' : 'American_Shorthair',
    'id' : 1,
    'fact' : 'grey, white and cute'
} <br>

요청 성공 시 Code 201 return <br>
요청 실패 시에는 Code 400 return</p>

<p>
<h2>PUT (변경)</h2>
특정 품종의 catfact를 변경하려면, PUT Method를 이용한다. <br>
PUT /catfact/bread/'특정 품종 이름' <br>
request: {
    '수정할 항목' : '수정할 내용'
} <br>

ex) PUT /catfact/bread/American_Shorthair
request: {
    'fact' : 'grey, white and lovely'
} <br>

요청 성공 시 Code 200 return (새로운 정보 등록 시에는 POST, 201 return)<br>
요청 실패 시에는 Code 404 return </p>

<p>
<h2>DELETE (삭제)</h2>
특정 품종의 catfact를 삭제하려면, DELETE Method를 이용한다. <br>
DELETE /catfact/bread/'특정 품종 이름' <br>

ex) DELETE /catfact/bread/American_Shorthair

요청 성공 시 Code 201 return <br>
요청 실패 시에는 Code 404 return <br>
(POST 되지 않은 정보를 삭제하는 경우 등..)</p>

<p>
p.s. CRUD을 하기 위한 인증 (Authentication) 에 대해서도 논의할 수 있다..
</p>
</body>