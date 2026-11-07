// crazytable.ch – Weinkarte. Zeichnet die Regionen aus #wk-data auf eine Weltkarte (Datamaps/d3 v3).
(function () {
  var el = document.getElementById('wk-map');
  var dataEl = document.getElementById('wk-data');
  if (!el || !dataEl || typeof Datamap === 'undefined') return;
  var REGIONS = JSON.parse(dataEl.textContent);
  var css = getComputedStyle(document.documentElement);
  var CYAN = css.getPropertyValue('--cyan').trim() || '#3EAFC8';
  var LAND = '#1A1D1F', LINE = '#2A2E31', GREY = '#55595C';
  var view = 'eu', map, timer;

  function draw() {
    el.innerHTML = '';
    var w = el.clientWidth, h = el.clientHeight;
    map = new Datamap({
      element: el, responsive: false, fills: { defaultFill: LAND },
      setProjection: function () {
        var proj = view === 'eu'
          ? d3.geo.mercator().center([7, 45.2]).scale(Math.min(w, h * 1.6) * 1.45).translate([w / 2, h / 2])
          : d3.geo.equirectangular().center([-10, 15]).scale(w / 6.4).translate([w / 2, h / 2]);
        return { path: d3.geo.path().projection(proj), projection: proj };
      },
      geographyConfig: { borderColor: LINE, borderWidth: 0.6, highlightOnHover: false, popupOnHover: false }
    });
    map.bubbles(REGIONS.map(function (r) {
      return { slug: r.slug, name: r.name, status: r.status, latitude: r.lat, longitude: r.lng,
        radius: r.status === 'TASTED' ? 8 : r.status === 'PLANNED' ? 7 : 5 };
    }), { popupOnHover: false, highlightOnHover: false, borderWidth: 0, fillOpacity: 1 });

    d3.select(el).selectAll('circle.datamaps-bubble')
      .attr('class', function (d) { return 'datamaps-bubble is-' + d.status.toLowerCase(); })
      .attr('tabindex', 0).attr('role', 'link')
      .attr('aria-label', function (d) { return d.name; })
      .style('fill', function (d) { return d.status === 'TASTED' ? CYAN : d.status === 'PLANNED' ? 'transparent' : GREY; })
      .style('stroke', function (d) { return d.status === 'PLANNED' ? CYAN : 'none'; })
      .style('stroke-width', function (d) { return d.status === 'PLANNED' ? 2 : 0; })
      .style('cursor', 'pointer')
      .on('click', function (d) { go(d.slug); })
      .on('keydown', function (d) { var e = d3.event; if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go(d.slug); } })
      .append('title').text(function (d) { return d.name; });
  }

  function go(slug) {
    var t = document.getElementById(slug);
    if (!t) return;
    t.scrollIntoView({ behavior: 'smooth', block: 'start' });
    t.classList.add('is-target');
    setTimeout(function () { t.classList.remove('is-target'); }, 2400);
    if (history.replaceState) history.replaceState(null, '', '#' + slug);
  }

  Array.prototype.forEach.call(document.querySelectorAll('.wk-seg button'), function (b) {
    b.addEventListener('click', function () {
      view = b.getAttribute('data-view');
      Array.prototype.forEach.call(document.querySelectorAll('.wk-seg button'), function (x) {
        x.setAttribute('aria-pressed', x === b ? 'true' : 'false');
      });
      draw();
    });
  });
  window.addEventListener('resize', function () { clearTimeout(timer); timer = setTimeout(draw, 200); });
  draw();
})();
