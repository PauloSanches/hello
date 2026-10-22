# Jogo da Vida - Magnólia

[Voltar ao portfólio — AI/Agent](https://paulosanches.github.io/hello/pt/agent/)

Language: pt-BR

Fonte: https://paulosanches.github.io/hello/pt/portfolio/jogo-da-vida-magnolia/agent/

[English](https://paulosanches.github.io/hello/portfolio/jogo-da-vida-magnolia/case.md) · [Português do Brasil](https://paulosanches.github.io/hello/pt/portfolio/jogo-da-vida-magnolia/case.md) · [Italiano](https://paulosanches.github.io/hello/it/portfolio/jogo-da-vida-magnolia/case.md)

---

Portfolio / Side Quests

Um jogo de tabuleiro interativo baseado em histórias e reflexão.

[![Captura de tela do Jogo da Vida - Magnólia, mostrando o tabuleiro ilustrado na casa final.](https://paulosanches.github.io/hello/assets/side-quest-magnolia.png)](https://paulosanches.github.io/hello/assets/side-quest-magnolia.png)

O tabuleiro ilustrado ao final do jogo. [Ver captura de tela em tamanho original](https://paulosanches.github.io/hello/assets/side-quest-magnolia.png)

## O produto

Jogo da Vida - Magnólia reúne 12 casas ilustradas, histórias de personagens e 10 perguntas para reflexão em um jogo de navegador para computador e celular. Os jogadores controlam o ritmo. Não há pontuação nem formulário de respostas; as perguntas são destinadas à discussão fora da aplicação.

## A experiência

Cada casa conecta uma posição no tabuleiro a uma história. O texto aparece progressivamente, seguido por uma pergunta que mantém a história visível para consulta.

Os jogadores podem avançar, voltar a uma casa anterior, pausar a revelação do texto ou reiniciar o jogo. Avançar para a próxima casa é sempre uma escolha manual.

## Projeto técnico

### Arquitetura em execução

HTML, CSS e SVG definem a interface e o tabuleiro ilustrado. O JavaScript gerencia a casa ativa, o estado da história e da pergunta e as transições no navegador. O GitHub Pages hospeda a aplicação estática; o jogo não exige um backend de aplicação nem um banco de dados.

### Reprodução e navegação

Um controlador dedicado gerencia a tarefa de reprodução atual, o temporizador e os estados de escrita, espera e pausa. Ele usa um intervalo de 24 ms e uma espera de leitura de 3.000 ms antes de apresentar uma pergunta. A apresentação automática aguarda enquanto há texto selecionado, o painel de leitura está com foco de teclado ou ainda há conteúdo não lido abaixo da posição de rolagem.

A navegação cancela tarefas de reprodução pendentes, enquanto verificações do estado de transição impedem movimentos sobrepostos. Pausar ou ocultar a aba suspende o agendamento. O avanço entre as casas do tabuleiro continua manual.

### Layout de leitura e acessibilidade

O texto completo reserva seu espaço no layout antes do início do efeito de escrita, em vez de redimensionar o balão a cada caractere. Uma camada visual separada controla a revelação, enquanto o texto completo permanece disponível para tecnologias assistivas.

A interface oferece navegação por teclado e suporte a prefers-reduced-motion. A história e a pergunta permanecem visíveis juntas.

### Conteúdo e versionamento

O Google Sheets apoiou a edição colaborativa durante a preparação. Após a aprovação editorial, essa dependência foi removida e o conteúdo final foi publicado junto com o código. Isso mantém a narrativa vinculada a uma versão, mas exige uma nova publicação para alterações de conteúdo.

### Testes e publicações

Verificações automatizadas cobrem conteúdo, navegação, imagens e layout, complementadas por validação no navegador em diferentes tamanhos de tela.

Um script de publicação grava o mesmo timestamp UTC na página e em version.json, e adiciona parâmetros de versão derivados de SHA-256 às URLs de JavaScript e CSS. Seu modo de verificação confere a consistência dos timestamps; ele não recalcula os hashes dos arquivos. Os arquivos publicados e o comportamento no navegador são verificados separadamente para confirmar a versão entregue.

### Ferramentas de desenvolvimento

Hermes Agent e Codex apoiaram a implementação e os testes em um MacBook Air M1, com solicitações e revisões pelo Telegram. O ChatGPT gerou as ilustrações dos personagens a partir de fotografias fornecidas; o Hermes preparou e integrou os arquivos. Skills reutilizáveis orientaram design, testes, depuração e revisão. Essas ferramentas pertencem ao fluxo de desenvolvimento, não à execução do jogo.

## Explore o projeto

- [Abrir jogo](https://paulosanches.github.io/magnolia-jogo-da-vida/)
- [Código no GitHub](https://github.com/PauloSanches/magnolia-jogo-da-vida)
- [Ver bastidores](https://paulosanches.github.io/magnolia-jogo-da-vida/backstage/)

Jogo e bastidores em português.
