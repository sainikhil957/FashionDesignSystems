
function veripass1() {
    var p = document.getElementById("2").value;
    if (p.length < 6) {
      document.getElementById("span2").innerHTML =
        "password must contain atleast 6 charcters";
    }
  }
  function VerifyPass() {
    var pass = document.getElementById("2").value;
    var verpass = document.getElementById("3").value;
  
    if (pass == verpass) {
    } else {
      document.getElementById("span3").innerHTML = "Password Mismatch";
    }
  }