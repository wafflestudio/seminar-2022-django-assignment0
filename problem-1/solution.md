# 등록
/<고양이 품종>/facts  
POST

<고양이 품종>에 대한 fact를 등록한다.

## Parameters
contents:  
등록하고자 하는 fact에 대한 내용

## Responses
Code 201  
등록을 성공적으로 마쳐 새로운 fact가 생성되었음.  
Code 400  
<고양이 품종>을 찾을 수 없는 경우.  

# 수정
/<고양이 품종>/facts  
PUT

## Parameters
id:  
수정하고자 하는 fact의 번호.  
contents:  
새로 수정한 fact의 내용.  

## Responses
Code 200  
성공적으로 기존의 fact를 수정함.  
Code 404  
<고양이 품종>을 찾을 수 없는 경우, 또는 파라미터에서 수정하고자 하는 fact의 번호가 존재하지 않는 경우.  

# 삭제
/<고양이 품종>/facts  
DELETE  

## Parameters
id:  
삭제하고자 하는 fact의 번호  

## Responses
Code 200  
성공적으로 기존의 fact를 삭제함  
Code 404
<고양이 품종>을 찾을 수 없는 경우, 또는 파라미터에서 삭제하고자 하는 fact의 번호가 존재하지 않는 경우.  
