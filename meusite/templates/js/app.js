'use strict'
//Os inimigos e o player serão instanciados aqui
let allEnemies = [];

//Uma classe que cria os inimigos
class Enemy {
    /*constroi as dimensões do inimigo, bem como sua largura e sua altura,
    recebe três argumentos: dimenção de x, dimensão de y e a velocidade de acordo com a criação dos inimigos
    na matriz definida acima*/
    constructor(posX, posY, speed) {
        this.sprite = 'images/enemy-bug.png';
        this.x = posX;
        this.y = posY;
        this.speed = speed;
        this.largura = 50;
        this.altura = 50;
    }
    /*Aqui está presente o método de atualização dos inimigos onde seu SPEED será atualizado
    Também faz com que os inimigos se movam no cenário, recebe o argumento (dt) passado pelo engine.js*/
    update(dt) {
        this.x += this.speed * dt;
        if (this.x > 500) {
            this.x = -100;
        }
    }
    /*Os inimigos são desenhados um a um por meio das dimensões informadas na array allEnemies passadas ao
    método ctx.drawImage dada pela engine.js*/
    render() {
        ctx.drawImage(Resources.get(this.sprite), this.x, this.y);
    }
}

//A criação de três objetos inimigos por meio da class Enemy
allEnemies = [new Enemy(-100, 60, 325), new Enemy(-100, 143, 298), new Enemy(-100, 226, 362)];

//A classe responsável por criar as dimensões, atualização, redenrização e animação do player;
class Player {
    //Aqui são criados as dimensões e é chamado também a imagem do player
    constructor() {
        this.sprite = 'images/char-boy.png';
        this.x = 202;
        this.y = 404;
        this.speed = 2;
        this.largura = 50;
        this.altura = 50;
    }
    /*Método responsável de identificar o comando de direção para animar o player
    de acordo com as instruções passadas pela função document.addEventListener
    a handleInput  recebe um parâmetro direct que define a direção em que o player
    será movido, se o usuário direcionar qualquer tecla direcional do teclado
    o player deve responder habilmente a tal orientação*/
    handleInput(direct) {
        if (direct === 'right' && this.x < 390) {
            this.x += 101;
        }
        if (direct === 'left' && this.x > 10) {
            this.x -= 101;
        }
        if (direct === 'down' && this.y < 400) {
            this.y += 83;
        }
        if (direct === 'up' && this.y > 5) {
            this.y -= 83;
        }
    }
    /*A função colid é de suma importância para o objetivo e a lógica do jogo
    ela detecta a colisão entre inimigos e o player, caso aconteça uma colizão
    o inimigo volta altomaticamente para o seu local de origem*/
    colid(jogador, inimigos) {
        for (let c = 0; c < inimigos.length; c++) {
            if (jogador.x < inimigos[c].x + inimigos[c].largura &&
                jogador.x + jogador.largura > inimigos[c].x &&
                jogador.y < inimigos[c].y + inimigos[c].altura &&
                jogador.y + jogador.altura > inimigos[c].y) {
                jogador.x = 202;
                jogador.y = 404;
                
            }
        }
    }
    /*Aqui é possível identificar quando o player atigi a água, fazendo com que o player
    volte ao seu local de origem*/
    update(jogador, inimigos) {
        if (this.y <= 0) {
            this.x = 202;
            this.y = 404;
        }
        //verificação de colisão a cada atualização 
        this.colid(jogador, inimigos)
    }
    //Desenha o player na tela, e de acordo com as suas coordenadas
    render() {
        ctx.drawImage(Resources.get(this.sprite), this.x, this.y);
    }
}
//Cria um objeto Player por meio da class Player
const player = new Player()

/*Método responsável de colher as infomações quando o usuário preciona as teclas UP, DOWN, REIGHT ou LEFT
e os passa para a função handleInput na classe PLayer.handleInput*/
document.addEventListener('keyup', function (e) {
    var allowedKeys = {
        37: 'left',
        38: 'up',
        39: 'right',
        40: 'down'
    };

    player.handleInput(allowedKeys[e.keyCode]);
});


//links utilizados no projeto:
//============================
//https://developer.mozilla.org/kab/docs/Games/Techniques/2D_collision_detection
//https://www.w3schools.com/graphics/game_canvas.asp
//https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_Breakout_game_pure_JavaScript
//https://stackoverflow.com/questions/17583366/javascript-cannot-read-property-length-of-undefined-when-checking-a-variable/17583387
//============================
//suporte e ajuda:
//Alexandre (Coordenador de Comunidade)*/
