$(document).ready(function(){
    $(".tab1 .single-bottom").hide();
    $(".tab2 .single-bottom").hide();
    $(".tab3 .single-bottom").hide();
    $(".tab4 .single-bottom").hide();
    $(".tab5 .single-bottom").hide();
    $(".tab6 .single-bottom").hide();
    $(".tab7 .single-bottom").hide();
    $(".tab8 .single-bottom").hide();
    $(".tab9 .single-bottom").hide();
    $(".tab10 .single-bottom").hide();

    $(".tab1 ul").click(function(){
        $(".tab1 .single-bottom").slideToggle(300);
    })
    $(".tab2 ul").click(function(){
        $(".tab2 .single-bottom").slideToggle(300);
    })
    $(".tab3 ul").click(function(){
        $(".tab3 .single-bottom").slideToggle(300);
    })
    $(".tab4 ul").click(function(){
        $(".tab4 .single-bottom").slideToggle(300);
    })
    $(".tab5 ul").click(function(){
        $(".tab5 .single-bottom").slideToggle(300);
    })
    $(".tab6 ul").click(function(){
        $(".tab6 .single-bottom").slideToggle(300);
    })
    $(".tab7 ul").click(function(){
        $(".tab7 .single-bottom").slideToggle(300);
    })
    $(".tab8 ul").click(function(){
        $(".tab8 .single-bottom").slideToggle(300);
    })
    $(".tab9 ul").click(function(){
        $(".tab9 .single-bottom").slideToggle(300);
    })
    $(".tab10 ul").click(function(){
        $(".tab10 .single-bottom").slideToggle(300);
    })
});

$(window).load(function() {
      $('.flexslider').flexslider({
        animation: "slide",
        controlNav: "thumbnails"
      });
    });

$(function () {
      $("#slider").responsiveSlides({
      	auto: true,
      	nav: true,
      	speed: 2500,
        namespace: "callbacks",
        pager: false,
      });
    });
