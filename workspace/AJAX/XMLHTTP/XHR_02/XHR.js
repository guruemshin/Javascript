var xhr=null;
var arr=new Array();

function startRequest(){
   arr.push("OK");

   xhr=new XMLHttpRequest();
   xhr.open("get", "JSON.txt", true);
   xhr.send();
   xhr.onreadystatechange=resultProcess;
}

function resultProcess(){
   arr.push(xhr.readyState + "," + xhr.status);


   if(xhr.readyState==4 && xhr.status==200){
      let obj=JSON.parse(xhr.responseText);
      arr.push(obj);


      let ul=document.createElement("ul");

      let liName=document.createElement("li");
      liName.innerText=obj.name;

      let liAge=document.createElement("li");
      liAge.innerText=obj.age;

      let liCity=document.createElement("li");
      liCity.innerText=obj.city;

      ul.appendChild(liName);
      ul.appendChild(liAge);
      ul.appendChild(liCity);
      
      let disp=document.querySelector("#disp");
      disp.appendChild(ul);
      
      alert(arr.join("\n"));

   }

}