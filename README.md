# Paulo Sanches · Portfólio

Portfólio em português europeu, baseado no CV e no documento de carreira fornecidos em outubro de 2026. HTML, CSS e JavaScript sem dependências de execução, fontes externas ou serviços de backend.

## Desenvolvimento local

Na raiz do repositório:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

O conteúdo está em `index.html`, o estilo em `assets/style.css` e os filtros em `assets/app.js`. Os detalhes dos projetos e a navegação funcionam sem JavaScript. Não há processo de build.

## Publicação no GitHub Pages

Este site é publicado diretamente da branch `main`, sem um workflow de deployment personalizado e sem processamento Jekyll.

1. No GitHub, abrir **Settings → Pages → Build and deployment → Source** e escolher **Deploy from a branch**.
2. Selecionar a branch **main**, a pasta **/ (root)** e guardar.
3. Um push para `main` inicia a publicação. Acompanhar **pages build and deployment** no separador **Actions**.
4. Após uma execução com sucesso, abrir `https://paulosanches.github.io/hello/`.

O ficheiro `.nojekyll` na raiz permite servir o HTML, CSS e JavaScript diretamente. Os caminhos relativos suportam o subdiretório `/hello/`. Não é necessária uma branch chamada `gh-pages`.

Tudo o que for acrescentado à branch pública deve ser apropriado para divulgação. Os anexos originais não estão no repositório.

## Conteúdo e privacidade

Os documentos originais não fazem parte do site. Valores de contratos, custos e métricas internas não foram incluídos na versão pública. Clientes são descritos por setor. O email profissional e o LinkedIn fornecidos no CV são os contactos do site; o telefone foi omitido.

Datas de credenciais representam as datas reportadas nos documentos, não uma validação independente do estado atual. Credenciais internas e reconhecimento estão separados das certificações externas. O ano da certificação AWS Solutions Architect foi omitido por divergência nas fontes.

Antes de acrescentar métricas ou anexar o CV original, rever os dados destinados a divulgação pública.
