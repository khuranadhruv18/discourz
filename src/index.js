
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


function toggleNav() {
	var x = document.getElementById("mySidenav").style.width;
	var elements = document.querySelectorAll('.sidebar-text');
	var content = document.querySelectorAll('.content');

	if (x !== "160px") {
		document.getElementById("mySidenav").style.width = "160px";
		for(var i=0; i<elements.length; i++) {
    		elements[i].style.color = "#818181";
		}
		content[0].style.left = "160px"; 
	}
	else {
		document.getElementById("mySidenav").style.width = "45px";
		for(var i=0; i<elements.length; i++) {
    		elements[i].style.color = "#111";
		}
		content[0].style.left = "45px";
		
	}
    
}
