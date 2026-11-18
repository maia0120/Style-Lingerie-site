import json,html,urllib.parse
exec(open('produtos.py').read()); exec(open('extra.py').read())
SV=json.load(open('svgs.json'))
WA='5511946666963'
def wa(msg): return f"https://wa.me/{WA}?text="+urllib.parse.quote(msg)
WA_GERAL=wa("Olá! Vim pelo site da Style Lingerie e gostaria de mais informações.")
WA_NOIVA=wa("Olá! Vim pelo site e quero conhecer o atendimento exclusivo para noivas.")
LOJAS=[('ml','Mercado Livre','https://lista.mercadolivre.com.br/_CustId_1108086240','Compra Garantida e entrega para todo o Brasil.'),
       ('shopee','Shopee','https://shopee.com.br/stylelingerieoficiall','Ofertas e cupons direto no app.'),
       ('magalu','Magalu','https://www.magazineluiza.com.br/lojista/stylelingerie','Compre com a segurança do Magalu.')]
SOC=[('WhatsApp',WA_GERAL,SV['wa']),('Instagram','https://www.instagram.com/stylelingerieoficial',SV['ig']),
     ('Facebook','https://www.facebook.com/stylelingeries',SV['fb']),('TikTok Shop','https://www.tiktok.com/@stylelingerieoficial',SV['tt'])]
E=html.escape
def brl(v): return 'R$ '+f'{v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')
ext='target="_blank" rel="noopener noreferrer"'
def card(n):
    _,nome,p=PRODUTOS[n-1]; o=OLD.get(n)
    off=f'<span class="off">-{round((1-p/o)*100)}%</span>' if o and o>p else ''
    old=f'<s>{brl(o)}</s>' if o and o>p else ''
    return (f'<article class="card" data-id="{n}"><div class="ph"><img src="fotos/produto-{n:03d}.jpg" alt="{E(nome)}" loading="lazy" width="148" height="148">{off}'
            f'<button class="add" type="button" aria-label="Adicionar {E(nome)} ao pedido">+</button><span class="qty" hidden></span></div>'
            f'<div class="info"><p class="nm">{E(nome)}</p><p class="pr">{old}<b>{brl(p)}</b></p></div></article>')
def row(ids,label):
    return (f'<div class="row" aria-label="{E(label)}"><button class="arrow prev" type="button" aria-label="Anterior">&#8249;</button>'
            f'<div class="track">{"".join(card(i) for i in ids)}</div><button class="arrow next" type="button" aria-label="Próximo">&#8250;</button></div>')
ofertas=sorted([n for n,_,p in PRODUTOS if OLD.get(n,0)>p],key=lambda n:-(1-PRODUTOS[n-1][2]/OLD[n]))[:16]
CATS=[('lingerie','Lingerie','Renda, conforto e atitude para todos os momentos.'),
      ('praia','Moda Praia','Biquínis e saídas que fazem o verão ser seu.'),
      ('noite','Noite & Pijamas','Camisolas, robes e baby-dolls para noites inesquecíveis.'),
      ('modeladores','Modeladores','Valorize suas curvas com conforto e firmeza.'),
      ('fitness','Fitness','Estilo que acompanha cada treino.')]
by={k:[n for n,nm,_ in PRODUTOS if cat(n,nm)==k] for k,_,_ in CATS}
cat_html=''.join(f'<div class="catblk" id="c-{k}"><div class="cathead"><h3>{t}</h3><p>{d}</p><span>{len(by[k])} peças</span></div>{row(by[k],t)}</div>' for k,t,d in CATS)
chips=''.join(f'<a class="chip" href="#c-{k}">{t}</a>' for k,t,_ in CATS)
loja_cards=''.join(f'<a class="loja {k}" href="{u}" {ext}><span class="lj-top"><span class="lj-dot"></span>Loja oficial</span><span class="lj-name">{n}</span><span class="lj-txt">{t}</span><span class="lj-cta">Comprar {'na' if k=='shopee' else 'no'} {n} <i>→</i></span></a>' for k,n,u,t in LOJAS)
loja_pills=''.join(f'<a class="pill {k}" href="{u}" {ext}><span class="lj-dot"></span>{n}</a>' for k,n,u,_ in LOJAS)
soc_html=''.join(f'<a class="soc" href="{u}" {ext}><span class="soc-ic">{s}</span><span>{n}</span></a>' for n,u,s in SOC)
foot_ic=''.join(f'<a class="foot-ic" href="{u}" {ext} aria-label="{n}">{s}</a>' for n,u,s in SOC)
minp=min(p for _,_,p in PRODUTOS)
DATA=json.dumps({str(n):[nm,p] for n,nm,p in PRODUTOS},ensure_ascii=False)

CSS=open('style2.css').read()
JS=open('app2.js').read().replace('__WA__',WA).replace('__DATA__',DATA)
page=f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Style Lingerie — Moda Íntima, Praia, Fitness e Noivas</title>
<meta name="description" content="Sinta-se poderosa na sua própria pele. Moda íntima, praia, fitness, modeladores e atendimento exclusivo para noivas. Compre no Mercado Livre, Shopee, Magalu ou pelo WhatsApp.">
<link rel="icon" href="logo.png">
<meta property="og:type" content="website">
<meta property="og:url" content="https://style-lingerie-site.vercel.app/">
<meta property="og:site_name" content="Style Lingerie">
<meta property="og:title" content="Style Lingerie — Sinta-se poderosa na sua própria pele">
<meta property="og:description" content="Moda íntima, praia, fitness e noivas. Ofertas exclusivas e compra pelo Mercado Livre, Shopee, Magalu ou WhatsApp.">
<meta property="og:image" content="https://style-lingerie-site.vercel.app/og-image.jpg">
<meta property="og:image:secure_url" content="https://style-lingerie-site.vercel.app/og-image.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Banner da Style Lingerie: Sinta-se poderosa na sua própria pele">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://style-lingerie-site.vercel.app/og-image.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Great+Vibes&family=Jost:wght@300;400;500;600&display=swap">
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="#inicio"><img src="logo.png" alt="Style Lingerie" width="72" height="72"><span>Style Lingerie</span></a>
  <nav><a href="#ofertas">Ofertas</a><a href="#colecao">Coleção</a><a href="#noivas">Noivas</a><a class="nav-cta" href="#lojas">Comprar</a></nav>
</div></header>

<section class="hero" id="inicio">
  <div class="wrap hero-grid">
    <div class="hero-text fade-up">
      <p class="eyebrow">Moda Íntima · Praia · Fitness · Noivas</p>
      <h1>Sinta-se poderosa na sua própria pele.</h1>
      <p class="tagline">A lingerie perfeita para quem dita as regras.</p>
      <div class="ctas">
        <a class="btn btn-gold" href="#lojas">Comprar agora</a>
        <a class="btn btn-ghost" href="#colecao">Ver coleção</a>
      </div>
      <div class="also"><span>Lojas oficiais:</span>{loja_pills}</div>
    </div>
    <div class="hero-photo fade-up delay">
      <img src="hero.jpg" alt="Lingerie Style Lingerie" width="432" height="545">
      <div class="badge"><small>Peças a partir de</small><b>{brl(minp)}</b></div>
    </div>
  </div>
  <svg class="wave" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true"><path fill="currentColor" d="M0 70c240 50 480-40 720-10s480 60 720 0v60H0z"/></svg>
</section>

<div class="marquee" aria-hidden="true"><div class="mq">{"<span>Moda Íntima ✦ Moda Praia ✦ Fitness ✦ Modeladores ✦ Noivas ✦ Pijamas ✦ </span>"*4}</div></div>

<section class="block" id="ofertas">
  <div class="head"><p class="kicker">Por tempo limitado</p><h2 class="script">Ofertas que você não vai deixar passar</h2><p class="lead">Preços especiais em peças selecionadas. Toque no <b class="plus">+</b> para montar seu pedido.</p></div>
  <div class="rows">{row(ofertas,"Ofertas")}</div>
</section>

<section class="block lojas-sec" id="lojas">
  <div class="head"><p class="kicker">Lojas oficiais</p><h2 class="serif">Escolha onde comprar.<br><em>Receba em casa.</em></h2><p class="lead">A Style Lingerie está nas maiores plataformas do Brasil. Compre com segurança, pague do seu jeito e acompanhe a entrega.</p></div>
  <div class="lojas">{loja_cards}</div>
  <a class="wa-line" href="{WA_GERAL}" {ext}>{SV['wa']}Prefere falar com a gente? <b>Compre pelo WhatsApp</b></a>
</section>

<section class="block sobre" id="sobre">
  <div class="sobre-grid">
    <div>
      <p class="kicker">Sobre a Style Lingerie</p>
      <h2 class="script">Feita para você se sentir incrível.</h2>
      <p class="body">A Style Lingerie é uma loja de moda feminina de Carapicuíba-SP que veste a mulher em todos os momentos: da lingerie do dia a dia ao conjunto que faz o coração acelerar, do biquíni de verão ao look do treino.</p>
      <p class="body">Cada peça é escolhida para unir <b>conforto, beleza e atitude</b>. Porque sensualidade não é sobre o tamanho, a idade ou o corpo. É sobre como você se olha no espelho.</p>
      <blockquote>“Lingerie não é sobre ser vista.<br>É sobre como você se sente.”</blockquote>
    </div>
    <div class="pilares">
      <div class="pilar"><b>Moda Íntima</b><span>Renda, conforto e atitude para todos os momentos.</span></div>
      <div class="pilar"><b>Moda Praia</b><span>Biquínis e saídas que fazem o verão ser seu.</span></div>
      <div class="pilar"><b>Fitness</b><span>Estilo que acompanha cada treino.</span></div>
      <div class="pilar"><b>Noivas</b><span>Atendimento exclusivo para o seu grande dia.</span></div>
    </div>
  </div>
  <div class="stats"><div><b>+{len(PRODUTOS)//10*10}</b><span>modelos no catálogo</span></div><div><b>3</b><span>lojas oficiais online</span></div><div><b>1:1</b><span>atendimento no WhatsApp</span></div></div>
</section>

<section class="block colecao" id="colecao">
  <div class="head"><p class="kicker">Coleção completa</p><h2 class="script">Encontre a peça que é a sua cara</h2><p class="lead">Deslize, escolha e toque no <b class="plus">+</b>. Seu pedido vai direto para o nosso WhatsApp.</p></div>
  <div class="chips">{chips}</div>
  {cat_html}
</section>

<section class="cta-band">
  <h2 class="serif">Gostou? <em>Garanta a sua antes que acabe.</em></h2>
  <p>As peças mais desejadas esgotam rápido. Compre agora na sua loja favorita.</p>
  <div class="band-btns">{loja_pills}</div>
</section>

<section class="block noivas" id="noivas">
  <div class="noiva-card">
    <p class="kicker">Atendimento exclusivo</p>
    <h2 class="script">Noivas</h2>
    <p class="body">Do chá de lingerie à lua de mel: montamos com você um enxoval que combina com o seu estilo e com o momento mais especial da sua vida.</p>
    <p class="quote">Você merece se sentir deslumbrante, por dentro e por fora.</p>
    <a class="btn btn-gold" href="{WA_NOIVA}" {ext}>{SV['wa']}Agendar atendimento de noiva</a>
  </div>
</section>

<section class="block redes" id="redes">
  <div class="head"><h2 class="serif small-h">Siga a Style Lingerie</h2><p class="lead">Novidades, lançamentos e bastidores todos os dias.</p></div>
  <div class="socs">{soc_html}</div>
</section>

<footer><div class="foot">
  <div class="foot-brand"><img src="logo.png" alt="" width="48" height="48"><div><p>Style Lingerie</p><p class="small">Carapicuíba-SP · Moda Íntima · Praia · Fitness · Noivas</p></div></div>
  <div class="foot-icons">{foot_ic}</div>
  <div class="contato small"><a href="mailto:oficialstylelingerie@gmail.com">oficialstylelingerie@gmail.com</a><a href="{WA_GERAL}" {ext}>WhatsApp (11) 94666-6963</a><span>© 2026 Style Lingerie</span></div>
</div></footer>

<div class="floatbar" id="buybar"><span>Pronta para se sentir poderosa?</span><a href="#lojas">Comprar agora</a></div>
<div class="floatbar cartbar" id="cartbar" aria-live="polite"><span id="cartsum"></span><button type="button" id="opencart">Ver pedido</button></div>
<div class="sheet-bg" id="sheetbg"></div>
<div class="sheet" id="sheet" role="dialog" aria-modal="true" aria-label="Seu pedido">
  <div class="sheet-h"><h3>Seu pedido</h3><button class="x" type="button" id="closecart" aria-label="Fechar">×</button></div>
  <div class="list" id="cartlist"></div>
  <div class="sheet-f">
    <div class="tot"><span>Total</span><b id="carttotal">R$ 0,00</b></div>
    <a class="send" id="sendwa" href="https://wa.me/{WA}" {ext}>{SV['wa']}Enviar pedido pelo WhatsApp</a>
    <p class="note">Tamanhos, cores e disponibilidade são confirmados pela loja no WhatsApp.</p>
    <div class="sheet-lojas"><span>Prefere comprar numa loja online?</span><div>{loja_pills}</div></div>
    <button class="clear" type="button" id="clearcart">Limpar pedido</button>
  </div>
</div>
<script>{JS}</script>
</body>
</html>'''
open('site/index.html','w').write(page)
print(len(ofertas),{k:len(v) for k,v in by.items()})
