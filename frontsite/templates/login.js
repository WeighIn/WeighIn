function login() {
	alert("button pressed");
		var user = 'Andrew';
		var password = '1234567890';
	$.ajax({
		type: 'GET',
		url: "http://dev.weighin.me/api/1/login/",
		crossDomain: true,
		data: {
			username: user,
			password: password
		},
		success: function() {
			alert("success");
		}
	});
}
