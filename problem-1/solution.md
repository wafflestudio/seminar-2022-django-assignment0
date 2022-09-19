<!-- TODO -->
1) 등록 <br>
   URI: /catfact/<br>
   METHOD: POST <br>
   - pk는 각 고양이의 품종을 구별할 id
   - 요청시에 등록할 품종의 이름과 catfact의 항목들에 대한 정보를 담아서 보내야 할 것.
2) 수정 <br>
   URI: /catfact/<int:pk> <br>
   METHOD: PUT <br>
   - pk는 각 고양이의 품종을 구별할 id
   - 요청시에 수정사항(품종이름, 수정할 catfact의 항목들 등)을 함께 보내야 함
3) 삭제 <br>
   URI: /catfact/<int:pk> <br>
   METHOD: DELETE
   - pk는 각 고양이의 품종을 구별할 id