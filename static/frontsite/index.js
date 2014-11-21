$(document).ready(function() {
	$('.navbar .fa').hover(
		function() {
			$(this).css("opacity", "0.7");
		},function() {
			$(this).css("opacity", "1.0");
		});
	$('.logo').hover(
		function() {
			$(this).stop().animate(
			  {rotation: 360},
			  {
			    duration: 500,
			    step: function(now, fx) {
			      $(this).css({"transform": "rotate("+now+"deg)"});
			    }
			  }
			);
		},function() {
			$(this).stop().animate(
			  {rotation: -360},
			  {
			    duration: 500,
			    step: function(now, fx) {
			      $(this).css({"transform": "rotate("+now+"deg)"});
			    }
			  }
			);
		});

});

