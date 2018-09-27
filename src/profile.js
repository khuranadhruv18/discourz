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


$('input[id=base-input]').change(function() {
$('#fake-input').val($(this).val().replace("C:\\fakepath\\", ""));
});

<!--==================Javascript code for custom input type file on button ================-->

$('input[id=main-input]').change(function() {
    console.log($(this).val());
    var mainValue = $(this).val();
    if(mainValue == ""){
        document.getElementById("fake-btn").innerHTML = "Choose File";
    }else{
        document.getElementById("fake-btn").innerHTML = mainValue.replace("C:\\fakepath\\", "");
    }
});

    <!--=========================input type file change on button ends here====================-->

//    ===================== snippet for profile picture change ============================ //

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('.imgCircle')
                    .attr('src', e.target.result)
                    .width(200)
                    .height(200);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

//    =================================== ends here ============================================ //

var checkme = document.getElementById('checker');
var userImage = document.getElementById('image-input');
var userName = document.getElementById('name');
var userPhone = document.getElementById('phone');
var userEmail = document.getElementById('email');
var userPlace = document.getElementById('place');
var UserSend = document.getElementById('submit');
var editPic = document.getElementById('PicUpload');
checkme.onchange = function() {
    UserSend.disabled = !this.checked;
    userImage.disabled = !this.checked;
    userName.disabled = !this.checked;
    userPhone.disabled = !this.checked;
    userEmail.disabled = !this.checked;
    userPlace.disabled = !this.checked;
    editPic.style.display = this.checked ? 'block' : 'none';
};

