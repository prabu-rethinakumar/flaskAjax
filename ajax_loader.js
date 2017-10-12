/**
 * Created by PXR8053 on 7/13/2017.
 */

function writeOutput(text){
    var obj = JSON.parse(text);
    console.log("obj contains :", obj);
    document.getElementById("backup").innerHTML = obj.message;

}

function HTTPClient(url, asyncCallback) {
    var ajaxRequest = new XMLHttpRequest();
    ajaxRequest.onreadystatechange = function(){
                 if (this.readyState == 4 && this.status == 200){
                        asyncCallback(this.responseText);
                            console.log("Executed the get_process fucntion");
                 }
    };
    ajaxRequest.open("GET", url, true );
    ajaxRequest.send();
}

function get_progress(){
    setInterval(function () {
    HTTPClient('/ajax', writeOutput);
    }, 20000);
}
