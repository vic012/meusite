//Javascript para o blog
$('pre').attr('class', 'prettyprint');
$(document).ready(function() {
    // Cria duas novas <div>
    var novaDivPython = $('<div class="python-command"></div>');
    var novaDivBash = $('<div class="bash-command"></div>');
    // Seleciona o trecho existente que deseja mover
    var trechoExistentePython = $('.texto_postagem pre .language-python');
    var trechoExistenteBash = $('.texto_postagem pre .language-bash');
    // Adiciona a nova div como um elemento pai do trecho existente
    trechoExistentePython.wrap(novaDivPython);
    trechoExistenteBash.wrap(novaDivBash);
    // Insere a nova div após o trecho existente
    var novaDivTypeCodePython = $('<div class="type-code">Python >>></div>');
    var novaDivTypeCodeBash = $('<div class="type-code">Linha de comando >>></div>');
    trechoExistentePython.prepend(novaDivTypeCodePython);
    trechoExistenteBash.prepend(novaDivTypeCodeBash);

    //Stiliza o info
    $(".content-info").prepend($("<p class='info-tag'><i class='fa fa-exclamation-triangle' aria-hidden='true'></i>  !!</p>"));
});