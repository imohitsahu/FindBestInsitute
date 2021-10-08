var app = angular.module("homepageApp" , []);
app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('((');
  $interpolateProvider.endSymbol('))');
});

app.controller('homepageController' , function($scope , $http){

	$scope.courses = new Array();
	$scope.admitted = new Array();
	$scope.enquiries = new Array();

	$scope.save = function(){
		var name = $scope.cname
		var fees = $scope.cfees

		if(name!=undefined && fees!=undefined ){
			$scope.cname = name.trim();
			url = "save_course?name="+name.trim()+"&fees="+fees
			$http.get(url).then(function(responce){
				data = jQuery.parseJSON(JSON.stringify(responce.data));
				$scope.courses.push(data)
				$scope.cname = ""
				$scope.cfees = ""
			})
		}
	}

	$scope.deleteCourse= function(id , index){
		$http.get('delete_course?id='+id).then(function(responce){
			data = jQuery.parseJSON(JSON.stringify(responce.data));
			if(data == "true"){
				$scope.courses.splice(index , 1)	
			}
			// alert(data)	
		})
	}

	$scope.deleteEnquiry= function(id , index , from){
		// alert(id)
		$http.get('delete_enquiry?id='+id).then(function(responce){
			data = jQuery.parseJSON(JSON.stringify(responce.data));
			if(data == "true"){
				if(from == 'a')
					$scope.admitted.splice(index , 1)	
				else
					$scope.enquiries.splice(index , 1)
			}
			// alert(data)	
		})
	}
	$scope.markAdmitted= function(id , index){
		// alert(id)

		// return ;
		$http.get('mark_admitted?id='+id).then(function(responce){
			data = jQuery.parseJSON(JSON.stringify(responce.data));
			// alert(data)
			if(data == "true"){
				$scope.admitted.push($scope.enquiries[index]);
				$scope.enquiries.splice(index , 1)

			}
			// alert(data)	
		})
	}

	$http.get('get_all_courses').then(function(responce){
		data = jQuery.parseJSON(JSON.stringify(responce.data));
		$scope.courses = data;
		// alert(data)	
	})

	$http.get('get_enquiries').then(function(responce){
		data = jQuery.parseJSON(JSON.stringify(responce.data));
		$scope.enquiries = data;
		// alert(data[0].student.name)
		// alert(data)	
	})
	$http.get('get_admitted').then(function(responce){
		data = jQuery.parseJSON(JSON.stringify(responce.data));
		$scope.admitted = data;
		// alert(data)
		// alert(data[0].student.name)
		// alert(data)	
	})

	
})