$(document).ready(function() {
    $(".category").hover(function(){
        category = $(this).find(".category-drop-btn:hover").attr("category");
        drop_down = $("div[category='"+category+"']")
        drop_down.css("display", "block");
    }, function(){
        $(".category-drop-content").css("display", "none");
    });


      // Quando a página carrega, armazena a cor de fundo original
      $('.category-drop-content a').each(function() {
        $(this).data('original-background-color', $(this).css('background-color'));
      });

    $(".category-drop-content a").hover(function(){
        // Armazena a cor de fundo original em uma variável
        var corOriginal = $(this).data('original-background-color');

        // Define a cor de fundo como "vermelha" durante o hover
        $(this).css('background-color', '#2196f3');
    }, function(){
        // Recupera a cor de fundo original da variável e define-a de volta
        var corOriginal = $(this).data('original-background-color');
        $(this).css('background-color', corOriginal);
    });
});