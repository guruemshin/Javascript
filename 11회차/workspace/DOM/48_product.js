function sub(){
    // alert("OK");
    let bigPic=document.querySelector("#cup");
    let smallPics=document.querySelectorAll(".small");

    for(let i=0; i<smallPics.length;i++){
        smallPics[i].addEventListener("click",function(){
            // alert(smallPics[i].src); 그림 잘 가져오는지 확인
        bigPic.src=smallPics[i].src;
        });
    }


    let isOpen=false;
    let view=document.querySelector("#view");
    view.addEventListener("click", function(){
        if(isOpen==false){
            let detail=document.querySelector("#detail");
            detail.style.display="block";
            view.innerText="상세설명닫기";
            isOpen=true;
        }else{
            detail.style.display="none";
            view.innerText="상세설명보기";
            isOpen=false;
        }

    });

}