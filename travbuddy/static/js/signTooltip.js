$(function () {
    $('[data-toggle="tooltip"]').tooltip();
    $('.signLangToggler').click(function(){
        $('.signTooltip').toggle();
    });
    $('.highContrastToggler').click(function(){
        $('body').toggleClass('highContrast');
    });
});
