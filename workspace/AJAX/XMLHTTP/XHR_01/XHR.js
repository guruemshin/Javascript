
var arr=new Array();
var xhr=null;

function startRequest(){
      arr.push("OK");

      // 비동기 기술 ajax 
      xhr=new XMLHttpRequest();                       // 객체 생성
      xhr.open("get", "XHR.txt", true);                   // 요청방식, 서버파일
      xhr.send();                                                     // 서버에 요청 전송
      xhr.onreadystatechange=resultProcess;     // 서버 응답처리 =  콜백함수
}    

function resultProcess(){
   arr.push(xhr.readyState + "," + xhr.status);

   if(xhr.readyState==4 && xhr.status==200){     // 수신완료, 성공
      arr.push(xhr.responseText);
      // alert(arr.join("\n"));

      let disp=document.querySelector("#disp");
      disp.style.color="red";
      disp.innerText=xhr.responseText;
   }
}

/*
   readyState - 서버 상태
   0 : 초기화 되지 않음 
   1 : open() 메소드까지 호출
   2 : send() 메소드까지 호출
   3 : 수신중
   4 : 수신완료

   status
   200 : 성공
   403 :  접근거부
   404 :  페이지 없음
   500 :  서버오류 
 */