$(document).ready(function(){

	$('.ir-arriba').click(function(){
		$('body, html').animate({
			scrollTop: '0px'
		}, 300);
	});

	$(window).ready(function(){
		if( $(this).scrollTop() = 0 ){
			$('.ir-arriba').slideUp(300);
		} else {
			$('.ir-arriba').slideDown(300);
		}
	});

});

