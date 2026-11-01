// crazytable.ch – kleine, ruhige Animationen. Respektiert "Bewegung reduzieren".
(function(){
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.classList.add(reduce ? 'no-motion' : 'motion');
  if (reduce || !('IntersectionObserver' in window)) return;

  // 1) Elemente beim Scrollen einblenden
  var targets = document.querySelectorAll('.reveal, .rules > li, .card, .bottle, .vote, .person, .steps > li, .stat, .tl-row, .agenda > li');
  targets.forEach(function(el, i){ el.classList.add('reveal'); });
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.1 });
  targets.forEach(function(el){ io.observe(el); });

  // 2) Geschwister nacheinander (Stagger) – pro Container
  document.querySelectorAll('.rules, .cards, .bottles, .votes, .people, .steps, .stats, .timeline, .agenda').forEach(function(group){
    Array.prototype.forEach.call(group.children, function(child, i){ child.style.transitionDelay = (i * 90) + 'ms'; });
  });

  // 3) Kennzahlen hochzählen
  document.querySelectorAll('.stat b').forEach(function(el){
    var text = el.textContent.trim();
    var m = text.match(/^(\d+)(.*)$/); if (!m) return;
    var target = parseInt(m[1], 10), suffix = m[2];
    var done = false;
    var obs = new IntersectionObserver(function(entries){
      if (!entries[0].isIntersecting || done) return; done = true; obs.disconnect();
      var start = null, dur = 900;
      function step(ts){ if(!start) start = ts; var p = Math.min((ts-start)/dur, 1); p = 1 - Math.pow(1-p, 3);
        el.textContent = Math.round(target * p) + suffix; if (p < 1) requestAnimationFrame(step); }
      requestAnimationFrame(step);
    }, { threshold: 0.6 });
    obs.observe(el);
  });
})();
