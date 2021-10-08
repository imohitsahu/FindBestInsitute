var app = angular.module("studentProfileApp" , []);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('((');
  $interpolateProvider.endSymbol('))');
});

app.controller('studentProfileController' , function($scope , $http){
	
	// hide show variables
	$scope.showAll = function(show){
		$scope.general_div = show;
		$scope.password_div = show;
		$scope.courses_div = show;
		$scope.institutes_div = show;
		if(!show){
			$(".nav-link").removeClass("active")
		}
	}

	$scope.showAll(false);
	// starting on general tab visible
	$scope.general_div = true;
	$('#generaltab').addClass('active')

	$scope.show = function(event , tab){
		$scope.showAll(false);

		$(event.target).addClass('active')

		if(tab == 'general'){
			$scope.general_div = true;
		}
		else if(tab == 'password'){
			$scope.password_div = true;
		}

		else if(tab == 'courses'){
			$scope.courses_div = true;
		}
		else if(tab == 'institutes'){
			$scope.institutes_div = true;
		}

	}

	$scope.changePassword = function(cp , np , np2){

		var a = $('token').find('input');
		var tokenName = $(a).attr('name');
		var tokenValue = $(a).val();
		if(cp!=undefined && np!=undefined && np2!=undefined ){
			

			$scope.error = false;

			$scope.cpassword = cp.trim();
			$scope.npassword = np.trim();
			$scope.npassword2 = np2.trim();

			if(cp.trim() =='' || np.trim() =='' || np2.trim() =='' ){
				$scope.error = "All Fields Are Required..."
				return ;
			}else if(np.trim()!=np2.trim()){
				$scope.error = "Password Not Matched...";
				return ;
			}


			alert(tokenName)
			alert(tokenValue)
			url = "cpassword="+cp+"&npassword="+np+"&npassword2="+np2;
			$http.get("student_change_password?"+url).then(function(responce){
				if(responce.data != 'ok'){
					$scope.error = responce.data;
				}else{
					$scope.error = "password Changed...";
				}
			});

		}else{
			$scope.error = "All Fields Are Required..."
		}
	}

	$scope.getColor = function(index){
		colors = ['#a5bde5' ,
		 '#8ee2d3' ,
		  '#8ee29e' , 
		  '#bde28e' ,
		   '#e2cf8e' , 
		   '#e2b28e',
		   '#e2938e' ,
		   '#ad99ef' ,
		   '#99c2ef' ,
		    '#64dba4', 
		    '#dbc564']

		    return colors[index]
	}

	$scope.getCourses = function(){
		$http.get('/student_courses').then(function(responce){
			data = jQuery.parseJSON(JSON.stringify(responce.data));
			$scope.courses_institutes = data;
			$scope.applyRating();
		})
	}

	$scope.getCourses();

	$scope.startAnimation = function(event){
		var curstart = $(event.target);
		rating = $(curstart).parent().attr('rating')
		var num = 0;
		if($(curstart).attr('class').includes(' a')){
			num = 0;
		}else if($(curstart).attr('class').includes(' b')){
			num = 1;
		}else if($(curstart).attr('class').includes(' c')){
			num = 2;
		}else if($(curstart).attr('class').includes(' d')){
			num = 3;
		}else if($(curstart).attr('class').includes(' e')){
			num = 4;
		}
		all = $(curstart).parent().children('i');
		// animation rating 
		for(i = 0 ; i< all.length ; i++){
			$(all[i]).removeClass('fa-star-o');
			$(all[i]).addClass('fa-star');
			if(num < i){
				// alert();
				$(all[i]).removeClass('fa-star');
				$(all[i]).addClass('fa-star-o');
			}
		}

		
	}

	$scope.endAnimation = function(event){
		var curstart = $(event.target);
		all = $(curstart).parent().children('i');
		td = $(curstart).parent();
		if($(td).attr('rating')==0){
			$(all).removeClass('fa-star');
			$(all).addClass('fa-star-o');
			return;
		}

		// rating jo phle th vhi vapas kro 
		rat = $(td).attr('rating');
		$(all[i]).removeClass('fa-star-o');
		$(all[i]).removeClass('fa-star');
		for(i = 0 ; i< all.length ; i++){
			
			if(rat <= i){
				// alert();
				$(all[i]).removeClass('fa-star');
				$(all[i]).addClass('fa-star-o');
			}else{
				$(all[i]).addClass('fa-star');
				$(all[i]).removeClass('fa-star-o');
			}
		}
		
	}

	$scope.rate = function(event , courseId){
		// alert(courseId)
		var curstart = $(event.target);
		all = $(curstart).parent().children('i');
		$(all).removeClass('fa-star');
		$(all).addClass('fa-star-o');
		var num = -1;

		if($(curstart).attr('class').includes(' a')){
			num = 0;
		}else if($(curstart).attr('class').includes(' b')){
			num = 1;
		}else if($(curstart).attr('class').includes(' c')){
			num = 2;
		}else if($(curstart).attr('class').includes(' d')){
			num = 3;
		}else if($(curstart).attr('class').includes(' e')){
			num = 4;
		}
		
		
		$(curstart).parent().attr('rating' , num+1)
		
		$http.get('/rate?rate='+(num+1)+'&id='+courseId).then(function(responce){
			// alert(responce.data)
			all = $(curstart).parent().children('i');
			for(i = 0 ; i< all.length ; i++){
				$(all[i]).removeClass('fa-star-o');
				$(all[i]).addClass('fa-star');
				if(num < i){
					$(all[i]).removeClass('fa-star');
					$(all[i]).addClass('fa-star-o');
				}
			}
		})

	}

	// applying rating 

	$scope.applyRating= function(){
		
	}


	/// calling function for strtup
	

	


})