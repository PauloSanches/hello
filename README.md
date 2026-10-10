# Paulo Sanches · Portfólio

Portfólio em português europeu, baseado no CV e no documento de carreira fornecidos em outubro de 2026. HTML, CSS e JavaScript sem dependências de execução, fontes externas ou serviços de backend.

## Desenvolvimento local

Na raiz do repositório:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

O conteúdo está em `index.html`, o estilo em `assets/style.css` e os filtros em `assets/app.js`. Os detalhes dos projetos e a navegação funcionam sem JavaScript. Não há processo de build.

## Publicação no GitHub Pages

1. Enviar os ficheiros para a branch `main` do repositório `PauloSanches/hello`.
2. No GitHub, abrir **Settings → Pages → Build and deployment → Source** e escolher **GitHub Actions**.
3. Em **Actions**, executar **Deploy portfolio to GitHub Pages** (ou fazer um novo push para `main`).
4. Confirmar que o workflow terminou com sucesso. Endereço esperado: `https://paulosanches.github.io/hello/`.

O workflow publica apenas `index.html`, `assets/` e `.nojekyll`. Os caminhos relativos permitem servir o site no subdiretório `/hello/`.

Alternativa sem Actions: em **Settings → Pages**, escolher **Deploy from a branch**, branch `main`, pasta `/ (root)`. Não é necessária uma branch chamada `gh-pages` para usar GitHub Pages.

## Conteúdo e privacidade

Os documentos originais não fazem parte do site. Valores de contratos, custos e métricas internas não foram incluídos na versão pública. Clientes são descritos por setor. O email profissional e o LinkedIn fornecidos no CV são os contactos do site; o telefone foi omitido.

Datas de credenciais representam as datas reportadas nos documentos, não uma validação independente do estado atual. Credenciais internas e reconhecimento estão separados das certificações externas. O ano da certificação AWS Solutions Architect foi omitido por divergência nas fontes.

Antes de acrescentar métricas ou anexar o CV original, rever os dados destinados a divulgação pública.
