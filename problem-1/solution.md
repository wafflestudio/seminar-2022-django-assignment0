<!-- TODO -->

<h3>base url</h3>
https://catfact.ninza

<h3>특정 품종의 고양이를 추가할 때</h3>
<h4>POST /breeds</h4>
request: {<br>
    "breed": "breed-info"<br>
    "country": "country-info"<br>
    "origin": "origin-info"<br>
    "coat": "coat-info"<br>
    "pattern": "pattern-info"<br>
}
<br>

<h3>특정 품종의 catfact를 등록할 때</h3>
<h4>POST /breeds/{specific-breed}/facts</h4>
request: {<br>
    "fact": "fact-info"<br>
}
<br>
<h3>특정 품종의 catfact를 수정할 때</h3>
<h4>PUT /breeds/{specific-breed}/facts/{fact-id}</h4>
request: {<br>
    "fact": "new-fact-info"<br>
}
<br>
<h3>특정 품종의 catfact를 삭제할 때</h3>
<h4>DELETE /breeds/{specific-breed}/facts/{fact-id}</h4>
