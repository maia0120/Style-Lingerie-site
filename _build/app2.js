(function(){
var WA="__WA__";
var P=__DATA__;
var cart={};
try{cart=JSON.parse(localStorage.getItem("styleCart")||"{}")||{};}catch(e){cart={};}
function brl(v){return v.toLocaleString("pt-BR",{style:"currency",currency:"BRL"});}
function save(){try{localStorage.setItem("styleCart",JSON.stringify(cart));}catch(e){}}
function ids(){return Object.keys(cart).filter(function(k){return cart[k]>0&&P[k];});}
function code(k){return ("00"+k).slice(-3);}
var heroPassed=false;
function bars(n){
  document.getElementById("cartbar").classList.toggle("show",n>0);
  document.getElementById("buybar").classList.toggle("show",n===0&&heroPassed);
}
function render(){
  var list=ids(),n=0,t=0;
  list.forEach(function(k){n+=cart[k];t+=cart[k]*P[k][1];});
  document.querySelectorAll(".card").forEach(function(c){
    var q=cart[c.dataset.id]||0,b=c.querySelector(".qty");
    b.hidden=!q;b.textContent=q;
  });
  document.getElementById("cartsum").innerHTML=n?("<b>"+n+(n>1?" itens":" item")+"</b> · "+brl(t)):"";
  document.getElementById("carttotal").textContent=brl(t);
  var h="";
  list.forEach(function(k){
    h+='<div class="it"><img src="fotos/produto-'+code(k)+'.jpg" alt=""><div class="t">'+P[k][0]+'<span>'+brl(P[k][1])+'</span></div>'+
       '<div class="stp"><button type="button" data-m="'+k+'" aria-label="Diminuir">−</button><b>'+cart[k]+'</b><button type="button" class="p" data-p="'+k+'" aria-label="Aumentar">+</button></div></div>';
  });
  document.getElementById("cartlist").innerHTML=h||'<p class="note" style="padding:1.5rem 0">Seu pedido está vazio.</p>';
  var msg="Olá! Vim pelo site da Style Lingerie e quero fazer este pedido:\n\n";
  list.forEach(function(k){msg+="• "+cart[k]+"x "+P[k][0]+" (cód. "+code(k)+") — "+brl(P[k][1]*cart[k])+"\n";});
  msg+="\nTotal: "+brl(t)+"\n\nPode me confirmar tamanhos e disponibilidade?";
  document.getElementById("sendwa").href="https://wa.me/"+WA+"?text="+encodeURIComponent(msg);
  bars(n);
  if(!n)closeS();
  save();
}
function add(k,d){cart[k]=Math.max(0,(cart[k]||0)+d);if(!cart[k])delete cart[k];render();}
document.querySelectorAll(".add").forEach(function(b){
  b.addEventListener("click",function(){add(b.closest(".card").dataset.id,1);});
});
document.getElementById("cartlist").addEventListener("click",function(e){
  var b=e.target.closest("button");if(!b)return;
  if(b.dataset.p)add(b.dataset.p,1);if(b.dataset.m)add(b.dataset.m,-1);
});
function openS(){document.getElementById("sheet").classList.add("open");document.getElementById("sheetbg").classList.add("open");}
function closeS(){document.getElementById("sheet").classList.remove("open");document.getElementById("sheetbg").classList.remove("open");}
document.getElementById("opencart").addEventListener("click",openS);
document.getElementById("closecart").addEventListener("click",closeS);
document.getElementById("sheetbg").addEventListener("click",closeS);
document.getElementById("clearcart").addEventListener("click",function(){cart={};render();});
/* barra "comprar agora": aparece depois do banner e some na seção das lojas */
var hero=document.getElementById("inicio"),lojas=document.getElementById("lojas"),heroOut=false,lojasIn=false;
function upd(){heroPassed=heroOut&&!lojasIn;bars(ids().reduce(function(s,k){return s+cart[k];},0));}
if("IntersectionObserver" in window){
  new IntersectionObserver(function(e){heroOut=!e[0].isIntersecting;upd();}).observe(hero);
  new IntersectionObserver(function(e){lojasIn=e[0].isIntersecting;upd();},{threshold:.15}).observe(lojas);
}
/* setas dos carrosséis */
document.querySelectorAll(".row").forEach(function(row){
  var t=row.querySelector(".track");
  function step(){var c=t.querySelector(".card");return c?(c.getBoundingClientRect().width+parseFloat(getComputedStyle(t).columnGap||0))*2:300;}
  row.querySelector(".next").addEventListener("click",function(){
    if(t.scrollLeft+t.clientWidth>=t.scrollWidth-5)t.scrollTo({left:0});else t.scrollBy({left:step()});
  });
  row.querySelector(".prev").addEventListener("click",function(){
    if(t.scrollLeft<=5)t.scrollTo({left:t.scrollWidth});else t.scrollBy({left:-step()});
  });
});
render();
})();
