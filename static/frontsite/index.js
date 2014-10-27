$(document).ready(function() {
	$('ul>li').hover(
		function() {
			$(this).addClass('hover');
		},
		function() {
			$(this).removeClass('hover');
		}

	});
});
