

  function ValidateForm() {
    var date=document.forms["addItem"]["deadline"].value;
    var deadline=new Date(date);
    var deadlinedate=deadline.getDate(date);    
    var today=new Date();
    today.setHours(0,0,0,0);
    var x = document.forms["addItem"]["content"].value;
    var z = document.forms["addItem"]["member"].value;
    if (x == "" ) {
        alert("Work field must be filled out");
        return false;
    }
    if(today >= deadline){
        alert("Deadline should be set to a date greater than today!");
        return false;
    }
}
