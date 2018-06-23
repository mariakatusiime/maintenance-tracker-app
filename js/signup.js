
function opensignup(){
     document.getElementById('signupcontainer').style.display='block';

    }
function openlogin(){
        
    document.getElementById('logincontainer').style.display='block';
   
       }
   
    function clos(){
     document.getElementById('signupcontainer').style.display='none';
    }
    function closl(){
        document.getElementById('logincontainer').style.display='none';
       }
// Get the modal
var modal = document.getElementById('signupcontainer');


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
        
    }
}

var modallog = document.getElementById('logincontainer');

window.onclick = function(event2){
    if(event2.target == modallog){
        modallog.style.display ="none";
    }
}


