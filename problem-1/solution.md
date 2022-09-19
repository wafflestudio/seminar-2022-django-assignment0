<!-- TODO -->
<h1>Problem 1</h1>
<h3>(1) 특정 품종의 catfact 등록하기</h3>
request : {"breed" : "sphinx", "fact" : "Sphynx is one of the friendliest companions."}
<p>method : POST</p> 
url : http://aboutcat/facts<hr>
<h3>(2) 특정 품종의 catfact 수정하기</h3>
request : {"breed" : "sphinx", "fact" : "Sphynx is one of the playful companions."}
<p>method : PUT</p>
url : http://aboutcat/facts/cat{breed}
<hr>
<h3>(3) 특정 품종의 catfact 삭제하기</h3>
request : {"breed" : "sphinx"}
<p>method : DELETE</p>
url : http://aboutcat/facts/cat{breed}