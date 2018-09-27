



$(document).ready(function(){
	resizeContent();

    $(window).resize(function() {
        resizeContent();
    });
});

	
function resizeContent() {
	var width = $(window).width();
	var sidebarWidth = $('#mySidenav').width();
	$('.content').css('width', (width - sidebarWidth) + 'px');

	var height = $(window).height();
	
	$('.right-header-contentChat').css('height', (height - 206) + 'px');
}

function toggleNav2() {
	var width = $(window).width();
	var x = $('#mySidenav');
	var elements = $('.sidebar-text');
	var content = $('.content');


	if (x.width() !== 160) {
		x.css('width', '160px');
		elements.css('color', '#818181');
		content.css('left', '160px');
		content.css('width', (width - 160) + 'px');
	}
	else {
		x.css('width', '45px');
		elements.css('color', '#111');
		content.css('left', '45px');
		content.css('width', (width - 45) + 'px');
	}
}
