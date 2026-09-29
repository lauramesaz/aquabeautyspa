(function(){
  var html=document.documentElement;
  function paint(l){
    html.dataset.lang=l; html.lang=l;
    document.querySelectorAll('[data-set]').forEach(function(b){b.classList.toggle('on',b.dataset.set===l)});
  }
  document.querySelectorAll('[data-set]').forEach(function(b){
    b.addEventListener('click',function(){
      paint(b.dataset.set); html.classList.add('lang-chosen');
      try{localStorage.setItem('aqua-lang',b.dataset.set)}catch(e){}
    });
  });
  paint(html.dataset.lang||'es');
  document.querySelectorAll('.links a').forEach(function(a){a.addEventListener('click',function(){document.body.classList.remove('menu-open')})});
})();
(function(){
  var f=document.getElementById('form-contacto'); if(!f) return;
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var d=new FormData(f), en=document.documentElement.dataset.lang==='en';
    var txt=(en?'Hi Aqua! I want to book a consultation.':'¡Hola Aqua! Quiero agendar una valoración.')+
      '\n'+(en?'Name: ':'Nombre: ')+d.get('nombre')+'\n'+(en?'Phone: ':'Teléfono: ')+d.get('tel')+
      '\n'+(en?'Language: ':'Idioma: ')+d.get('idioma')+(d.get('servicio')?'\n'+(en?'Service: ':'Servicio: ')+d.get('servicio'):'');
    if(f.dataset.wa){window.open('https://wa.me/'+f.dataset.wa+'?text='+encodeURIComponent(txt),'_blank');}
    else if(f.dataset.mail){location.href='mailto:'+f.dataset.mail+'?subject=Valoración&body='+encodeURIComponent(txt);}
    else{f.querySelector('.form-pend').hidden=false;return;}
    f.querySelector('.form-ok').hidden=false;
  });
})();
(function(){
  var t=document.querySelector('.g-track');
  document.querySelectorAll('.g-btn').forEach(function(b){
    b.addEventListener('click',function(){t.scrollBy({left:(+b.dataset.dir)*318,behavior:'smooth'})});
  });
  // en celular (sin mouse): la foto se pinta de color al quedar en el centro
  if(window.matchMedia('(hover: none)').matches && 'IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){e.target.classList.toggle('color',e.isIntersecting)})},{rootMargin:'-35% -20% -35% -20%'});
    document.querySelectorAll('.bw').forEach(function(el){io.observe(el)});
  }
})();
