/**
 * Created by Stepan on 21.08.14.
 */
$(document).ready(function(){
    console.log(123);
        $('.images').slick({
        dots: true,
        infinite: true,
        speed: 500,
        fade: true,
        slide: 'div',
        cssEase: 'linear'
    });
//    $('.images').slick({
//        dots: true,
//        infinite: true,
//        speed: 500,
//        fade: true,
//        slide: '> div',
//        cssEase: 'linear'
//    });
    console.log(1234);
});