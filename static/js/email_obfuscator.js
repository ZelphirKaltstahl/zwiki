$(document).ready(function() {
	$('.email-address').hover(function() {
			var actual_href = $(this).attr('href').replace('\.spam', '\.com');
			$(this).attr('href', actual_href);
	});
});