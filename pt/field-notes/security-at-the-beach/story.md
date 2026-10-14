# Uma semana na praia. Um incidente de segurança no segundo dia.

[Voltar ao portfólio — AI/Agent](https://paulosanches.github.io/hello/pt/agent/)

Language: pt-BR

Fonte: https://paulosanches.github.io/hello/pt/field-notes/security-at-the-beach/agent/

[English](https://paulosanches.github.io/hello/field-notes/security-at-the-beach/story.md) · [Português do Brasil](https://paulosanches.github.io/hello/pt/field-notes/security-at-the-beach/story.md) · [Italiano](https://paulosanches.github.io/hello/it/field-notes/security-at-the-beach/story.md)

---

SEGURANÇA E LIDERANÇA

Fui trabalhar por uma semana em uma casa de praia, esperando passar mais tempo com a família. No segundo dia, um incidente de segurança em produção mudou os planos.

4 min de leitura

![Vista litorânea pixelada, com palmeiras, praia de areia e água turquesa.](https://paulosanches.github.io/hello/assets/field-notes-beach.png?v=cfb755a41222)

Eu havia acabado de ser promovido a Manager. Entre minhas novas responsabilidades, assumi como Delivery Lead e Solution Architect de um projeto de marketing e CMS para uma das líderes do agronegócio no Brasil.

A solução utilizava Liferay Portal e estava em produção havia três anos. A equipe tinha apenas duas pessoas, não havia registro de problemas relevantes e o cliente estava discutindo a renovação do contrato. Era um projeto pequeno em estrutura, mas importante para a conta.

Com tudo aparentemente sob controle, trabalhar da casa de praia parecia simples. Esperava uma semana normal de trabalho, com mais tempo perto da família.

## Quando a instabilidade virou um incidente de segurança

No segundo dia, identificamos um processo suspeito no servidor de produção. O consumo de memória aumentava, sobrecarregava o ambiente e provocava reinicializações. O que parecia um problema de estabilidade se tornou um incidente de segurança.

Acionamos os protocolos de incidentes da empresa, escalamos o caso e montamos um war room. Minha responsabilidade era coordenar a resposta técnica, organizar as próximas ações e manter o cliente e as lideranças informados sobre o problema e a evolução da solução.

## Encontrar a correção era apenas parte do trabalho

Durante a investigação, encontramos um fator que complicava a resposta. O projeto havia sido desenhado com a edição Community do Liferay na fase de venda. Naquele cenário, não contávamos com o suporte e as correções prontamente disponíveis de que precisávamos para reagir com rapidez.

Identificamos vulnerabilidades conhecidas na versão utilizada, mas não encontramos um pacote de atualização pronto para instalar e corrigir o problema.

Depois de pesquisar em fóruns e abrir chamados com especialistas, descobrimos que a comunidade havia disponibilizado a correção. Havia uma etapa adicional: precisávamos baixar vários gigabytes de arquivos e compilar a aplicação antes de instalar a nova versão no servidor.

Foi aí que a conexão da casa de praia deixou de ser um detalhe. Os downloads e a compilação consumiram duas noites inteiras.

## Mantendo todos informados

Enquanto os downloads avançavam, a pressão aumentava. As lideranças da América Latina acompanhavam o incidente, com atualizações solicitadas várias vezes ao dia.

Eu precisava conduzir duas frentes: ajudar a equipe a chegar à solução e dar clareza aos stakeholders sobre o que sabíamos, o que ainda estava em investigação e quais seriam os próximos passos.

> Precisava deixar claros os próximos passos sem prometer um prazo que ainda não conseguíamos sustentar.

Resolver o problema técnico e comunicar a evolução eram partes da resposta. Ainda havia incertezas, e eu precisava ser transparente sobre elas.

Finalmente compilamos e instalamos a nova versão, corrigimos as vulnerabilidades identificadas e encerramos o incidente.

A praia, quase não aproveitei. Passei boa parte da semana entre reuniões, investigação técnica e noites de trabalho, em um ambiente que não estava preparado para aquela rotina. Foi uma das experiências mais intensas da minha carreira.

## O que ficou comigo

### Manutenção e suporte fazem parte da proposta

O custo de uma solução precisa considerar manutenção, atualizações e suporte. Naquele projeto, a escolha pela edição Community criou uma dificuldade que só ficou evidente quando precisamos responder a uma crise. Se esses recursos são necessários para atender ao cliente, precisam fazer parte da proposta desde o início.

### Liderar é organizar toda a resposta

A correção técnica é apenas parte do trabalho. Também é preciso organizar a resposta, apoiar a equipe e comunicar a evolução com transparência, mesmo quando ainda há perguntas sem resposta.

### Trabalhar de qualquer lugar exige preparação

Poder trabalhar de qualquer lugar também exige pensar nas condições para lidar com o inesperado. A conexão e o ambiente de trabalho importam quando um dia normal vira uma crise.

Eu havia acabado de assumir uma posição de gestão e esperava uma semana tranquila. Acabei vivendo, da casa de praia, uma aula prática sobre responsabilidade, tomada de decisão e liderança sob pressão.

## Mais sobre a parte técnica

Se quiser saber mais sobre os detalhes técnicos desse incidente e acredita que podem ser úteis para você, vou gostar de conversar a respeito.

[Me chame no LinkedIn](https://www.linkedin.com/in/paulosanches)
