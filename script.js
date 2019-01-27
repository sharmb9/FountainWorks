function submitQuery() {
  //alert("Hello Raj!");
  var queryResult = document.getElementById("result").innerHTML;
  //alert(queryResult);

  //Code Block used to Change Color=Red and Text=Not Working

  
   document.getElementById("result").className = "text-red text-uppercase";
   document.getElementById("result").innerHTML = "NOT WORKING";

  //Code Block used to Change Color=Green /text-primary and Text=Working
  //document.getElementById("result").className = "text-primary text-uppercase"
  //document.getElementById("result").innerHTML = "WORKING";

  var request = new XMLHttpRequest();

  request.addEventListener("load", function(evt){
    console.log(evt);
  }, false);

  request.open('GET', 'https://127.0.0.1:5000/', true),
  request.send();

  var xhttp = new XMLHttpRequest();
  
  const xhr = new XMLHttpRequest()
  xhr.onreadystatechange = () => {
    if (xhr.readyState === 4) {
      xhr.status === 200 ? console.log(xhr.responseText) : console.error('error')
    }
  }
  
  xhr.open("GET", "http://127.0.0.1:5000/0002");
  xhr.send();



  //  var hello = request.response;
  //  alert(hello);
}
