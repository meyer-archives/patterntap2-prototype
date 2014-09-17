$(document).ready(function(){
	$("#tag-dropdown").hover(
		function(){$("#browse-menu").addClass("menu-visible");},
		function(){$("#browse-menu").removeClass("menu-visible");}
	);
	$("li#profile-menu>ul").hover(
		function(){$("li#profile-menu").addClass("menu-visible");},
		function(){$("li#profile-menu").removeClass("menu-visible");}
	);

	var scrollTimer;
	var scrollDelay = 250;
	$(window).scroll(function(){
		if( scrollTimer ){
			clearTimeout(scrollTimer);
			console.log("Scrolling...");
		} else {
			$(window).trigger('scrollstart');
		}
		scrollTimer = setTimeout(function(){$(window).trigger('scrollstop');scrollTimer=false},scrollDelay);
	}).bind({
		scrollstart: function(){
			$("body").addClass("scrolling");
		},
		scrollstop: function(){
			$("body").removeClass("scrolling");
		}
	});

});
