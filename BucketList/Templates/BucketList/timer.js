

  setInterval(displayclock,500)
  function displayclock(){
    var time = new Date();
    var datetoday = time.getDate();
    var hrs = time.getHours();
    var min = time.getMinutes();
    var sec = time.getSeconds();

    if (hrs > 12) {
      hrs=hrs-12;
    }
  
    if (hrs == 0){
      hrs = 12;
    }
  
    document.getElementById('clock').innerHTML=  hrs +':'+ min +':'+ sec;
  }
 