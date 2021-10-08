
"use strict";

// Angular application setup 
var app = angular.module('registrationApp', []);
app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('((');
  $interpolateProvider.endSymbol('))');
});

// creating controller
app.controller('registrationController', function($scope , $http) {
	
	$scope.addresses = Array();


	// when type on address textbox it send request to
	// server and get response then shows the dropdown
	$scope.getAddress = function(who){
		$scope.addresses= Array();
		var value = $('#address').val();

		$scope.addresses= Array();
		if(who=="student"){
			value = $('#student_address').val();
		}
		
		if(value.length==0){
			hidePlaces();
		}
		if(value.length<3){
			return
		}
		$http.get('get_addresses?addr='+value)
		  .then(function(response) {
		  		$scope.addresses= response.data.results
		  		if(who=="student"){
					showStudentPlaces();
					return;
				}
		  		showPlaces();
		});
	}

	// when click on place from drope down
	$scope.selectPlace= function(event , addr , lat , lng , city , state , who){
		var curObj = $(event.target);
		var place = $(curObj).text();
		if(who == 'student'){
			$('#student_address').val(addr);
			$('#student_lat').val(lat);
			$('#student_lng').val(lng);
			$('#student_city').val(city);
			$('#student_state').val(state);
			hideStudentPlaces();
			return;
		}
		$('#address').val(addr)
		$("#lat").val(lat)
		$("#lng").val(lng)
		$("#city").val(city)
		$("#state").val(state)
		// alert(lat)
		// alert(lng)
		hidePlaces();
	}

});


// hide addresses dropdown
function hidePlaces(){
	$('.places').hide();
}

// shows addresses dropdown
function showPlaces(){
	$('.places').show();
}

// hide addresses dropdown
function hideStudentPlaces(){
	$('.student_address').hide();
}

// shows addresses dropdown
function showStudentPlaces(){
	$('.student_address').show();
}


// when document gets ready the it runs
$('document').ready(function(){
		
	hidePlaces();
	hideStudentPlaces();
	position();
	positionForStudent();
})


// when browser resize 
$(window).resize(function(){
	// alert();
	position();
	positionForStudent();
})


// setting the position on the dropdown div according to oaddres text firled
function position(){
	var p = $('#input_group_address').position();
		 $('.places').css('top' , p.top+$('#input_group_address').innerHeight()+20);
		 $('.places').width($('#input_group_address').width());
		// $('#places').position(p)
		// alert(p)
}

// setting the position on the dropdown div according to oaddres text firled
function positionForStudent(){
	var elm = $('#student_address_div');
	var p = $(elm).position();
	$('.student_address').css('top' , p.top + $(elm).innerHeight()+20);
	$('.student_address').width($(elm).width());
}