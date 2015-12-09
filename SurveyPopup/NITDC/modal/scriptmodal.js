function init(){
  window.open('https://ufl.qualtrics.com/SE/?SID=SV_4ZKcfKI49HWLOiF','EFTI Survey','height=400,width=600,top=10000,left=1400');
}

if (!sessionStorage.alreadyClicked) {
    $(document).ready(function() {
        setTimeout(function() {
          $('#myModal').modal('show');
        }, 3000); // milliseconds
        sessionStorage.alreadyClicked = "true";
    });
}


// function caller(){
// 	if (!sessionStorage.alreadyClicked) {
// 	    $(document).ready(function() {
// 	        setTimeout(function() {
// 	          $('#myModal').modal('show');
// 	        }, 3000); // milliseconds
// 	        sessionStorage.alreadyClicked = "true";
// 	    });
// 	}
// }

// if (window.addEventListener){
//     window.addEventListener("load",caller(),false);
// }