// function login() {
// 	alert("button pressed");
// 	var user = $('#username').val();
// 	var password = $('#pwd').val();

// 	$.ajax({
// 		type: "GET",
// 		url: "http://dev.weighin.me/api/1/login/",
// 		crossDomain: true,
// 		data: {
// 			username: user,
// 			password: password
// 		},
// 		success: function() {
// 			alert("success");
// 		}
// 	});
// }
            $("login_button").click(function(){
            $.getJSON("http://dev.weighin.me/api/1/login/?username=" + $('#username').val() + "&password=" + $('#pwd').val(),function(result)
            {
            if(result['success'] == "True")
                {
         			alert("Success bitch!");
                }
            else
                {
                    alert("Account not found. Try logging in again");
                }

         });
      });