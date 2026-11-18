# Style Lingerie — Site

Site institucional e catálogo da Style Lingerie (Carapicuíba-SP): moda íntima, praia, fitness, modeladores e atendimento para noivas.

- `index.html` — página pronta (HTML/CSS/JS puros, sem dependências). É o que a Vercel publica.
- `fotos/` — fotos dos produtos (`produto-001.jpg` … `produto-125.jpg`).
- `_build/` — scripts que geram o `index.html`:
  - `produtos.py` — nomes e preços
  - `extra.py` — preços antigos (promoção) e categorias
  - `style2.css` / `app2.js` — estilo e carrinho
  - Para regerar: copie a pasta para fora do repositório junto com `site/` e rode `python3 build2.py` (ou edite o `index.html` direto).

Carrinho: o "+" verde soma os produtos e o botão envia o pedido para o WhatsApp (11) 94666-6963.
