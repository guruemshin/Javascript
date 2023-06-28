var xhr=null;
var arr=new Array();

function startRequest(){
    xhr=new XMLHttpRequest();
    xhr.open("get","responseXML.xml",true);
    xhr.send();
    xhr.onreadystatechange=resultProcess;

    }

function resultProcess(){
    if(xhr.redeyState==4 && xhr.status==200){
        arr.push(xhr.responseXML);

        let xmlDoc=xhr.responseXML;
        let studentList=xmlDoc.querySelectorAll("student");
        arr.push(studentList.length);
    alert(arr.join("\n"));
    arr.push(student.length);
        for(let i=0; i<studentList.length; i++){
            let student=studentList[i].childNodes;
            arr.push(student.length);

            for(let j=0; j<student.length; j++){
                if(student[j].nodeType==1){
                    arr.push(student[j].childNodes[0].nodeValue);

                }
            }
        }



    }
}

// workspace\AJAX\XMLHTTP\XML_03\responseXML.xml