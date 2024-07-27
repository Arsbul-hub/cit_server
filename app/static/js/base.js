function open_top_menu() {
    document.getElementById("navigation").style.display = "block";
    document.getElementById("mobile").style.height = "100vh";
    document.getElementById("navigation").style.animation = "base_animation 0.3s forwards";
    document.getElementById("open-navigation").style.display = "none";
    document.getElementById("close-navigation").style.display = "block";
    document.getElementById("close-navigation").style.display = "block";

    document.getElementById("before").style.display = "none";
    document.getElementsByTagName("body")[0].style.backgroundColor = "#404040";
    $(document).bind('scroll',function () { 
            window.scrollTo(0,0); 
        }
    );


}

function close_top_menu() {
    document.getElementById("navigation").style.display = "none";
    document.getElementById("mobile").style.height = "unset";
    document.getElementById("open-navigation").style.display = "block";
    document.getElementById("close-navigation").style.display = "none";
    document.getElementById("before").style.display = "block";
    document.getElementById("after").style.display = "block";
    document.getElementsByTagName("body")[0].style.backgroundColor = "rgb(238, 238, 238)"
    $(document).unbind('scroll');
    // document.getElementsByClassName("navigation")[0].style.visibility = "hidden";
    // document.body.style.overflowY = "auto";

}
