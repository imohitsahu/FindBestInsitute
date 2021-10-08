// Angular application setup 
var app = angular.module('homeApp', []);
app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('((');
  $interpolateProvider.endSymbol('))');
});
//searchbar show only home page using js

// creating controller
var courses ;
app.controller('homeController', function($scope , $http){
	// alert()
	$scope.courses = [12,45,78,89,56,23,533,88];
	$(".only-at-home").attr('hidden' , false);
	// $('.course-container').hide();
	

	// collect courses
	$scope.getAllCourses = function(){
		$http.get("courses_student_home").then(function(responce){
			data = jQuery.parseJSON(JSON.stringify(responce.data));
			$scope.student = data.student
			data.courses.sort(function(a , b){
				d1 = $scope.getDistanceFromLatLonInKm(a.institute.lat , a.institute.lng , $scope.student.lat , $scope.student.lng );
				d2 = $scope.getDistanceFromLatLonInKm(b.institute.lat , b.institute.lng , $scope.student.lat , $scope.student.lng );
				return d1-d2; 
			})
			$scope.courses = data.courses;
			courses  = $scope.courses;
			$('.course-container').fadeIn(1000);
			console.log(data.courses)
			// $('#loading').hide(1000);
			// alert(data)
		})
	}

	$scope.getNumbers = function(n){
		var arr = []
		for (i = 0 ; i < n ; i ++){
			arr.push(i);
		} 
		// alert(arr)
		return arr;
	}

	$scope.toUpper = function(str){
		// alert()
		s =  new String(str)
		return s.toUpperCase();
	}

	$scope.showModel = function(course , color){
		course.color = color;
		$scope.selectedCourse = course;

		$('#infoModel').modal('show')

		$http.get('save_enquiry?courseId='+course.id).then(function(responce){
			// alert(responce.data)
		})
		// alert(course.courseName)
	}

	$scope.getBg = function(index){
		// index = (Math.random()*10).toFixed(0);
		// alert()
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
		mod = index % 11 
		return colors[mod]
		
		
	}



	$scope.getDistanceFromLatLonInKm = function(lat1, lon1, lat2, lon2) {
			// alert(lat1)
			
		  var R = 6371; // Radius of the earth in km
		  var dLat = $scope.deg2rad(lat2-lat1);  // deg2rad below
		  var dLon = $scope.deg2rad(lon2-lon1); 
		  var a = 
		    Math.sin(dLat/2) * Math.sin(dLat/2) +
		    Math.cos($scope.deg2rad(lat1)) * Math.cos($scope.deg2rad(lat2)) * 
		    Math.sin(dLon/2) * Math.sin(dLon/2)
		    ; 
		  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
		  var d = R * c; // Distance in km
		  return d.toFixed(2);
		}

		$scope.deg2rad  = function(deg) {
		  return deg * (Math.PI/180)
		}

	$scope.startAnimation = function(event){
		var curstart = $(event.target);
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
		for(i = 0 ; i< all.length ; i++){
			$(all[i]).removeClass('fa-star-o text-info');
			$(all[i]).addClass('fa-star text-info');
			if(num < i){
				// alert();
				$(all[i]).removeClass('fa-star text-info');
				$(all[i]).addClass('fa-star-o text-info');
			}
		}
	}

	$scope.search = function(event){
		var value = $(event.target).val();

		if(value.trim().length == 0){
			$scope.getAllCourses();
		}

		if(value.length < 3){
			return;
		}
		$('#loading').show(100);
		$http.get('search?q='+value).then(function(responce){
			data = jQuery.parseJSON(JSON.stringify(responce.data));
			
			$scope.student = data.student
			data.courses.sort(function(a , b){
				d1 = $scope.getDistanceFromLatLonInKm(a.institute.lat , a.institute.lng , $scope.student.lat , $scope.student.lng );
				d2 = $scope.getDistanceFromLatLonInKm(b.institute.lat , b.institute.lng , $scope.student.lat , $scope.student.lng );
				return d1-d2; 
			})
			// $('.course-container').hide().fadeIn(500);
			$scope.courses = data.courses;
			console.log(data.courses)
			$('#loading').hide(200);
		})
	}

	$scope.loading = function(){
		$("#loading").show(200)
	}

	/// calling function for strtup
	$scope.getAllCourses();



	$scope.getper = function(v , total){
		// alert(((v/total)*100) + "%")
		return ((v/total)*100) + "%";
	}

	$scope.sort = function(){
		alert();
	}




	// loading
	loading = 0;
	int = setInterval(function(){
		loading = loading + 1;
		if(loading > $(window).width()){
			loading = 0;
		}
	 	$('#loading').width(loading+'px') 
	},5);

	
	
})

