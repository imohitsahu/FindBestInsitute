$(document).ready(function(){
	$('#forgotPasswordbutton').click(function(){
		$('#passwordModal').modal('show')
	})

	$('.newpassworddiv').hide(500)
	$('#passError').hide()
});

function changePassword(){

	var npassword = $('input[name="forpasswordreenter"]').val()
	var npassword2 = $('input[name="forpassword"]').val()
	var otp = $('input[name="otp"]').val(); 
	if(npassword == npassword2 ){
		var xhttp = new XMLHttpRequest();
		  xhttp.onreadystatechange = function() {
		    if (this.readyState == 4 && this.status == 200) {
		    	if(this.responseText == "true"){
		    		$('#passwordModal').modal('hide')
		    	}else{
		    		alert(this.responseText);
		    	}
		    }
		  };
		xhttp.open("GET", "/change_password_otp?otp="+otp+"&npassword="+npassword, true);
		xhttp.send();
	}else{
		$('#passError').html("password Not Matched..")
		$('#passError').show()	;
	}
	
}



function sendOtp(){
	var email = $('input[name="passwordresetemail"]').val()
	var xhttp = new XMLHttpRequest();
	  xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	    	if(this.responseText != "false"){
	    		$('.sendotpdiv').hide()
				$('.newpassworddiv').show()
	    	}else{
	    		alert("Email incorrect")
	    	}
	    }
	  };
	  xhttp.open("GET", "/sendOtp?email="+email, true);
	  xhttp.send();
}