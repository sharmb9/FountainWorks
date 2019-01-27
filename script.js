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
}
