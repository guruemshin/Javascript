function checkForm(){ 

   let obj=document.querySelector("#member");
   let irum=obj.irum.value;
   let korean=/^[가-힣]+$/;


   if(!korean.test(irum)){
      alert("이름을 입력하세요");
      obj.irum.focus();
      return;
   }
 

 
   if(obj.siteUrl.value==""){
      alert("이동할 사이트를 반드시 선택하세요");
      obj.siteUrl.focus();
      return;
   }
 
   var test=false;
 
   for(let i=0;i<obj.fruit.length;i++){      // i < 4 0123
      if(obj.fruit[i].checked==true){
          // obj.fruit[i].valule;  DB 데이터 값 준다
         test=true;
      }
   }
 
   if(test==false){
      alert("좋아하는 과일 반드시 선택하세요");
      return;
   }
 
   var count=0;
   var str="";
 
   for(let i=0;i<obj.interest.length;i++){
 
      if(obj.interest[i].checked==true){
         str += obj.interest[i].value + ",";    // 경제, 음악
         count++;     // 2
      }
   }
 
    // alert(str);
 
   if(count==0){
      alert("관심사를 반드시 하나이상 체크하세요");
      return;
   }

   obj.submit();
 
}