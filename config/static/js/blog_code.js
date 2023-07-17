//Javascript para o blog
$(document).ready(function() {

    $('.language-python').parent().attr('class', 'prettyprint');
    $('.language-bash').parent().attr('class', 'prettybash');

    // Cria duas novas <div>
    var novaDivPython = $('<div class="python-command"></div>');
    var novaDivBash = $('<div class="bash-command"></div>');

    // Seleciona o trecho existente que deseja mover
    var trechoExistentePython = $('.texto_postagem pre .language-python').parent();
    var trechoExistenteBash = $('.texto_postagem pre .language-bash').parent();

    // Adiciona a nova div como um elemento pai do trecho existente
    trechoExistentePython.wrap(novaDivPython);
    trechoExistenteBash.wrap(novaDivBash);

    // Insere a nova div após o trecho existente
    var novaDivTypeCodePython = $('<div class="type-code">Python >>></div>');
    var novaDivTypeCodeBash = $('<div class="type-code">Bash >>></div>');
    trechoExistentePython.prepend(novaDivTypeCodePython);
    trechoExistenteBash.prepend(novaDivTypeCodeBash);
});