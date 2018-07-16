
function querym(){
    document.getElementById('requestcontainer').style.display='block';
   }
function clos2(){
     document.getElementById('requestcontainer').style.display='none';
    }
    var modal1 = document.getElementById('requestcontainer');


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal1) {
        modal1.style.display = "none";
        
    }
}
