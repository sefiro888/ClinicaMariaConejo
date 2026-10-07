/* Fisioterapia María Conejo · interacción
   Todo respeta «reducir movimiento» y funciona sin dependencias. */
(() => {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const body = document.body;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const finePointer = matchMedia('(hover: hover) and (pointer: fine)').matches;
  const MC = window.MC || { hours: [], days: [], services: [], areas: {}, phone: '34656643330' };

  /* ── Año ── */
  $$('[data-year]').forEach(el => (el.textContent = new Date().getFullYear()));

  /* ── Horario en vivo ── */
  const fmt = h => `${String(Math.floor(h)).padStart(2, '0')}:${h % 1 ? '30' : '00'}`;
  function openStatus() {
    const now = new Date();
    const day = (now.getDay() + 6) % 7; // 0 = lunes
    const h = now.getHours() + now.getMinutes() / 60;
    const today = MC.hours[day] || [];
    const span = today.find(([a, b]) => h >= a && h < b);
    if (span) return { open: true, text: `Abierto ahora · hasta las ${fmt(span[1])}` };
    const later = today.find(([a]) => h < a);
    if (later) return { open: false, text: `Cerrado · abrimos hoy a las ${fmt(later[0])}` };
    for (let i = 1; i <= 7; i++) {
      const d = (day + i) % 7;
      if ((MC.hours[d] || []).length) {
        const when = i === 1 ? 'mañana' : `el ${MC.days[d].toLowerCase()}`;
        return { open: false, text: `Cerrado · abrimos ${when} a las ${fmt(MC.hours[d][0][0])}` };
      }
    }
    return { open: false, text: 'Consulta nuestro horario' };
  }
  function paintStatus() {
    if (!MC.hours.length) return;
    const st = openStatus();
    $$('[data-open-status]').forEach(el => {
      el.classList.toggle('is-open', st.open);
      el.classList.toggle('is-closed', !st.open);
      const b = el.querySelector('b');
      if (b) b.textContent = st.text;
    });
    const d = (new Date().getDay() + 6) % 7;
    $$('.hours li').forEach(li => li.classList.toggle('is-today', +li.dataset.day === d));
  }
  paintStatus();
  setInterval(paintStatus, 60000);

  /* ── Cabecera, progreso y botones flotantes ── */
  const toTop = $('.to-top');
  const bar = toTop && toTop.querySelector('.tt-bar');
  const floats = $$('.float-wa, .float-ig');
  let ticking = false;
  function onScroll() {
    const y = scrollY;
    body.classList.toggle('is-scrolled', y > 6);
    const max = document.documentElement.scrollHeight - innerHeight;
    if (toTop) {
      toTop.classList.toggle('is-visible', y > 700);
      if (bar) bar.style.strokeDashoffset = 126 - 126 * Math.min(1, y / max);
    }
    floats.forEach(f => f.classList.toggle('is-visible', y > 500));
    ticking = false;
  }
  addEventListener('scroll', () => { if (!ticking) { requestAnimationFrame(onScroll); ticking = true; } }, { passive: true });
  onScroll();
  toTop && toTop.addEventListener('click', () => scrollTo({ top: 0, behavior: reduced ? 'auto' : 'smooth' }));

  /* ── Mega menú ── */
  const drop = $('.nav-drop');
  const header = $('.site-header');
  if (drop) {
    const btn = $('.nav-drop-btn', drop);
    let t;
    const set = open => {
      drop.classList.toggle('is-open', open);
      header.classList.toggle('mega-open', open);
      btn.setAttribute('aria-expanded', String(open));
    };
    if (finePointer) {
      drop.addEventListener('mouseenter', () => { clearTimeout(t); t = setTimeout(() => set(true), 90); });
      drop.addEventListener('mouseleave', () => { clearTimeout(t); t = setTimeout(() => set(false), 220); });
    }
    btn.addEventListener('click', () => set(!drop.classList.contains('is-open')));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') set(false); });
    document.addEventListener('click', e => { if (!drop.contains(e.target)) set(false); });
    drop.addEventListener('focusout', e => { if (!drop.contains(e.relatedTarget)) set(false); });

    const pImg = $('.mega-preview-media img', drop);
    const pTitle = $('[data-mp-title]', drop);
    const pText = $('[data-mp-text]', drop);
    let current = '';
    const preview = a => {
      const src = `assets/images/${a.dataset.preview}.webp`;
      pTitle.textContent = a.dataset.previewTitle;
      pText.textContent = a.dataset.previewText;
      if (src === current) return;
      current = src;
      pImg.classList.add('swap');
      setTimeout(() => { pImg.src = src; pImg.onload = () => pImg.classList.remove('swap'); }, 180);
    };
    $$('[data-preview]', drop).forEach(a => { a.addEventListener('mouseenter', () => preview(a)); a.addEventListener('focus', () => preview(a)); });
  }

  /* ── Menú móvil ── */
  const menu = $('#mobile-menu');
  const toggle = $('.menu-toggle');
  if (menu) {
    const open = state => {
      menu.classList.toggle('is-open', state);
      menu.setAttribute('aria-hidden', String(!state));
      body.classList.toggle('menu-open', state);
      toggle && toggle.setAttribute('aria-expanded', String(state));
      if (state) setTimeout(() => $('.m-close', menu).focus(), 300);
    };
    toggle && toggle.addEventListener('click', () => open(true));
    $$('[data-open-menu]').forEach(b => b.addEventListener('click', () => open(true)));
    $$('[data-close-menu]', menu).forEach(b => b.addEventListener('click', () => open(false)));
    $$('a', menu).forEach(a => a.addEventListener('click', () => open(false)));
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && menu.classList.contains('is-open')) { open(false); toggle && toggle.focus(); } });
    $$('.m-acc', menu).forEach(d => d.addEventListener('toggle', () => { if (d.open) $$('.m-acc', menu).forEach(o => o !== d && (o.open = false)); }));
  }

  /* ── Separar titulares en palabras para animarlas ── */
  function split(el) {
    let i = 0;
    const build = (src, dest) => {
      src.childNodes.forEach(node => {
        if (node.nodeType === 3) {
          node.textContent.split(/(\s+)/).forEach(part => {
            if (!part) return;
            if (/^\s+$/.test(part)) { dest.appendChild(document.createTextNode(' ')); return; }
            const w = document.createElement('span'); w.className = 'w';
            const s = document.createElement('span'); s.style.setProperty('--i', i++); s.textContent = part;
            w.appendChild(s); dest.appendChild(w);
          });
        } else if (node.nodeType === 1) {
          const clone = node.cloneNode(false);
          build(node, clone);
          dest.appendChild(clone);
        }
      });
    };
    const frag = document.createElement('div');
    build(el, frag);
    el.innerHTML = frag.innerHTML;
  }
  if (!reduced) $$('.hs-title, .ph-title').forEach(split);

  /* ── Slider de portada ── */
  const slider = $('[data-slider]');
  if (slider) {
    const slides = $$('.hero-slide', slider);
    const rail = $$('.rail-item', slider);
    const counter = $('[data-current]', slider);
    const DUR = 7000;
    slider.style.setProperty('--dur', DUR + 'ms');
    let cur = 0, timer, paused = false;
    const show = n => {
      cur = (n + slides.length) % slides.length;
      slides.forEach((s, i) => {
        s.classList.toggle('is-current', i === cur);
        s.setAttribute('aria-hidden', String(i !== cur));
        $$('a', s).forEach(a => (a.tabIndex = i === cur ? 0 : -1));
        if (i === cur) { const im = $('img', s); im.loading = 'eager'; }
      });
      rail.forEach((r, i) => {
        r.classList.remove('is-active');
        r.classList.toggle('is-done', i < cur);
      });
      void slider.offsetWidth;
      rail[cur] && rail[cur].classList.add('is-active');
      if (counter) counter.textContent = String(cur + 1).padStart(2, '0');
      // precarga la siguiente imagen
      const next = $('img', slides[(cur + 1) % slides.length]); if (next) next.loading = 'eager';
    };
    const play = () => { clearTimeout(timer); if (reduced || paused) return; timer = setTimeout(() => { show(cur + 1); play(); }, DUR); };
    rail.forEach((r, i) => r.addEventListener('click', () => { show(i); play(); }));
    $('[data-prev]', slider).addEventListener('click', () => { show(cur - 1); play(); });
    $('[data-next]', slider).addEventListener('click', () => { show(cur + 1); play(); });
    const pause = p => { paused = p; slider.classList.toggle('is-paused', p); if (p) clearTimeout(timer); else play(); };
    if (finePointer) { slider.addEventListener('mouseenter', () => pause(true)); slider.addEventListener('mouseleave', () => pause(false)); }
    document.addEventListener('visibilitychange', () => pause(document.hidden));
    let sx = 0, sy = 0;
    slider.addEventListener('touchstart', e => { sx = e.touches[0].clientX; sy = e.touches[0].clientY; }, { passive: true });
    slider.addEventListener('touchend', e => {
      const dx = e.changedTouches[0].clientX - sx, dy = e.changedTouches[0].clientY - sy;
      if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) { show(cur + (dx < 0 ? 1 : -1)); play(); }
    }, { passive: true });
    show(0); play();
  }

  /* ── Aparición al hacer scroll ── */
  const io = 'IntersectionObserver' in window ? new IntersectionObserver(entries => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
  }, { rootMargin: '0px 0px -8% 0px', threshold: .08 }) : null;
  $$('.reveal').forEach(el => io ? io.observe(el) : el.classList.add('is-in'));

  /* ── Contadores ── */
  const countIO = 'IntersectionObserver' in window ? new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (!en.isIntersecting) return;
      const el = en.target; countIO.unobserve(el);
      const end = parseFloat(el.dataset.count), dec = +(el.dataset.decimals || 0);
      if (reduced) { el.textContent = end.toFixed(dec).replace('.', ','); return; }
      const t0 = performance.now(), dur = 1600;
      const step = t => {
        const p = Math.min(1, (t - t0) / dur), v = end * (1 - Math.pow(1 - p, 3));
        el.textContent = v.toFixed(dec).replace('.', ',');
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    });
  }, { threshold: .6 }) : null;
  $$('[data-count]').forEach(el => countIO && countIO.observe(el));

  /* ── Buscador «¿Qué te ocurre?» ── */
  $$('.finder').forEach(f => {
    const chips = $$('[data-finder]', f), panels = $$('[data-finder-panel]', f);
    chips.forEach(c => c.addEventListener('click', () => {
      chips.forEach(x => { x.classList.toggle('is-on', x === c); x.setAttribute('aria-selected', String(x === c)); });
      panels.forEach(p => p.classList.toggle('is-on', p.dataset.finderPanel === c.dataset.finder));
    }));
  });

  /* ── Winback ── */
  const depths = ['92%', '62%', '32%'];
  $$('.winback').forEach(w => {
    const beam = $('.wb-beam', w);
    const tabs = $$('[data-wb]', w), texts = $$('[data-wb-text]', w);
    const set = i => {
      tabs.forEach(t => { const on = t.dataset.wb === String(i); t.classList.toggle('is-on', on); t.setAttribute('aria-selected', String(on)); });
      texts.forEach(t => t.classList.toggle('is-on', t.dataset.wbText === String(i)));
      beam.style.setProperty('--depth', depths[i]);
    };
    tabs.forEach(t => t.addEventListener('click', () => set(+t.dataset.wb)));
    set(0);
  });

  /* ── Carruseles ── */
  $$('[data-carousel]').forEach(track => {
    const wrap = track.closest('.container');
    const step = () => (track.firstElementChild ? track.firstElementChild.getBoundingClientRect().width + 24 : 300);
    const prev = $('[data-car-prev]', wrap), next = $('[data-car-next]', wrap);
    prev && prev.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: 'smooth' }));
    next && next.addEventListener('click', () => {
      const end = track.scrollLeft + track.clientWidth >= track.scrollWidth - 10;
      track.scrollTo({ left: end ? 0 : track.scrollLeft + step(), behavior: 'smooth' });
    });
  });

  /* ── Preguntas: solo una abierta por lista ── */
  $$('.faq-list').forEach(list => {
    const items = $$('details', list);
    items.forEach(d => d.addEventListener('toggle', () => { if (d.open) items.forEach(o => o !== d && (o.open = false)); }));
  });

  /* ── Visor de imágenes ── */
  const lbItems = $$('[data-lightbox]');
  if (lbItems.length) {
    const lb = document.createElement('div');
    lb.className = 'lightbox';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.innerHTML = '<button class="lb-close" aria-label="Cerrar">✕</button><button class="lb-prev" aria-label="Anterior">‹</button><figure style="margin:0"><img alt=""><p></p></figure><button class="lb-next" aria-label="Siguiente">›</button>';
    body.appendChild(lb);
    let idx = 0;
    const show = i => {
      idx = (i + lbItems.length) % lbItems.length;
      const it = lbItems[idx];
      $('img', lb).src = `assets/images/${it.dataset.lightbox}.webp`;
      $('img', lb).alt = it.dataset.caption || '';
      $('p', lb).textContent = it.dataset.caption || '';
    };
    const close = () => { lb.classList.remove('is-open'); body.classList.remove('menu-open'); };
    lbItems.forEach((it, i) => { it.tabIndex = 0; const go = () => { show(i); lb.classList.add('is-open'); body.classList.add('menu-open'); $('.lb-close', lb).focus(); }; it.addEventListener('click', go); it.addEventListener('keydown', e => e.key === 'Enter' && go()); });
    $('.lb-close', lb).addEventListener('click', close);
    $('.lb-prev', lb).addEventListener('click', () => show(idx - 1));
    $('.lb-next', lb).addEventListener('click', () => show(idx + 1));
    lb.addEventListener('click', e => { if (e.target === lb) close(); });
    document.addEventListener('keydown', e => {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
    });
  }

  /* ── Mapa bajo demanda ── */
  $$('[data-load-map]').forEach(b => b.addEventListener('click', () => {
    const box = b.closest('[data-map]');
    const f = document.createElement('iframe');
    f.src = box.dataset.map; f.loading = 'lazy'; f.title = 'Mapa de la clínica'; f.referrerPolicy = 'no-referrer-when-downgrade';
    box.innerHTML = ''; box.appendChild(f);
  }));

  /* ── Reserva guiada por WhatsApp ── */
  $$('[data-booking]').forEach(form => {
    const steps = $$('.bk-step', form);
    const dots = $$('.bk-progress span', form);
    const sel = $('select[name="servicio"]', form);
    const svcField = $('[data-service-field]', form);
    const state = { area: '', service: '', franja: '', modalidad: 'en la clínica' };
    const go = n => {
      steps.forEach((s, i) => s.classList.toggle('is-active', i === n));
      dots.forEach((d, i) => d.classList.toggle('is-on', i <= n));
      update();
    };
    const fill = area => {
      const list = MC.services.filter(s => s.area === area);
      sel.innerHTML = '<option value="">Aún no lo sé, prefiero que me orientéis</option>' + list.map(s => `<option value="${s.slug}">${s.title}</option>`).join('');
      svcField.hidden = !list.length;
    };
    const step1Next = $('[data-step="1"] [data-next]', form);
    const step2Next = $('[data-step="2"] [data-next]', form);
    $$('[data-area]', form).forEach(c => c.addEventListener('click', () => {
      $$('[data-area]', form).forEach(x => x.classList.toggle('is-on', x === c));
      state.area = c.dataset.area; state.service = '';
      fill(state.area);
      step1Next.disabled = false;
      update();
    }));
    sel.addEventListener('change', () => { state.service = sel.value; update(); });
    $$('[data-group]', form).forEach(g => $$('.chip', g).forEach(c => c.addEventListener('click', () => {
      $$('.chip', g).forEach(x => x.classList.toggle('is-on', x === c));
      state[g.dataset.group] = c.dataset.value;
      if (g.dataset.group === 'franja') step2Next.disabled = false;
      update();
    })));
    $$('[data-next]', form).forEach(b => b.addEventListener('click', () => go(steps.findIndex(s => s.classList.contains('is-active')) + 1)));
    $$('[data-prev]', form).forEach(b => b.addEventListener('click', () => go(steps.findIndex(s => s.classList.contains('is-active')) - 1)));
    $$('input, textarea', form).forEach(i => i.addEventListener('input', update));
    form.addEventListener('submit', e => e.preventDefault());

    function message() {
      const name = $('[name="nombre"]', form).value.trim();
      const det = $('[name="detalle"]', form).value.trim();
      const svc = MC.services.find(s => s.slug === state.service);
      let what;
      if (svc) what = `para «${svc.title}»`;
      else if (state.area && MC.areas[state.area]) what = `en ${MC.areas[state.area].toLowerCase()}`;
      else what = 'y que me orientéis sobre el servicio más adecuado';
      let msg = `Hola, María 👋${name ? ` Soy ${name}.` : ''} Me gustaría pedir cita ${what}`;
      if (state.modalidad === 'a domicilio') msg += ' a domicilio';
      msg += '.';
      if (state.franja) msg += ` Me vendría mejor ${state.franja}.`;
      if (det) msg += `\n\n${det}`;
      return msg;
    }
    function update() {
      const msg = message();
      const p = $('[data-preview-msg]', form); if (p) p.textContent = msg;
      const a = $('[data-send]', form); if (a) a.href = `https://wa.me/${MC.phone}?text=${encodeURIComponent(msg)}`;
    }
    // valores predefinidos (páginas de área o de servicio)
    const pa = form.dataset.presetArea, ps = form.dataset.presetService;
    if (pa) { const c = $(`[data-area="${pa}"]`, form); c && c.click(); if (ps) { sel.value = ps; state.service = ps; } }
    update();
  });

  /* ── Subnavegación con seguimiento ── */
  const subLinks = $$('.subnav a:not(.subnav-cta)');
  if (subLinks.length && 'IntersectionObserver' in window) {
    const map = new Map(subLinks.map(a => [a.getAttribute('href').slice(1), a]));
    const spy = new IntersectionObserver(entries => {
      entries.forEach(en => {
        if (en.isIntersecting) {
          subLinks.forEach(a => a.classList.remove('is-active'));
          const a = map.get(en.target.id);
          if (a) {
            a.classList.add('is-active');
            const bar = a.parentElement;
            bar.scrollTo({ left: a.offsetLeft - bar.clientWidth / 2 + a.clientWidth / 2, behavior: 'smooth' });
          }
        }
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    map.forEach((_, id) => { const s = document.getElementById(id); s && spy.observe(s); });
  }

  /* ── Anclas internas con desplazamiento suave (sin scroll-behavior global) ── */
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href*="#"]');
    if (!a) return;
    const url = new URL(a.href, location.href);
    if (url.pathname !== location.pathname || !url.hash || url.hash === '#') return;
    const target = document.getElementById(decodeURIComponent(url.hash.slice(1)));
    if (!target) return;
    e.preventDefault();
    target.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' });
    history.replaceState(null, '', url.hash);
  });

  /* ── Reels: vista previa en bucle solo cuando están en pantalla ── */
  const previews = $$('video[data-autoplay]');
  if (previews.length && 'IntersectionObserver' in window && !reduced) {
    const vio = new IntersectionObserver(entries => {
      entries.forEach(en => {
        const v = en.target;
        if (en.isIntersecting) { v.preload = 'auto'; const p = v.play(); if (p) p.catch(() => {}); }
        else v.pause();
      });
    }, { threshold: .35 });
    previews.forEach(v => vio.observe(v));
  }

  /* ── Visor de reels con sonido ── */
  const modal = $('#reel-modal');
  if (modal) {
    const video = $('video', modal);
    let lastFocus = null;
    const close = () => {
      video.pause();
      video.removeAttribute('src');
      video.load();
      modal.hidden = true;
      body.classList.remove('menu-open');
      lastFocus && lastFocus.focus();
    };
    $$('[data-reel]').forEach(card => card.addEventListener('click', () => {
      lastFocus = card;
      const key = card.dataset.reel;
      video.poster = `assets/video/${key}.webp`;
      video.src = `assets/video/${key}.mp4`;
      $('[data-rm-title]', modal).textContent = card.dataset.title || '';
      $('[data-rm-text]', modal).textContent = card.dataset.text || '';
      $('[data-rm-credit]', modal).textContent = card.dataset.credit || '';
      $('[data-rm-url]', modal).href = card.dataset.url || 'https://www.instagram.com/fisiomariacm/';
      modal.hidden = false;
      body.classList.add('menu-open');
      video.muted = false;
      const p = video.play(); if (p) p.catch(() => {});
      $('.rm-close', modal).focus();
    }));
    $$('[data-close-reel]', modal).forEach(b => b.addEventListener('click', close));
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && !modal.hidden) close(); });
  }

  /* ── Botones magnéticos ── */
  if (!reduced && finePointer) {
    $$('.magnetic').forEach(b => {
      b.addEventListener('mousemove', e => {
        const r = b.getBoundingClientRect();
        b.style.transform = `translate(${(e.clientX - r.left - r.width / 2) * .18}px, ${(e.clientY - r.top - r.height / 2) * .3}px)`;
      });
      b.addEventListener('mouseleave', () => (b.style.transform = ''));
    });
  }

  /* ── Transición suave entre páginas ── */
  if (!reduced) {
    const veil = document.createElement('div'); veil.className = 'page-fade'; body.appendChild(veil);
    document.addEventListener('click', e => {
      const a = e.target.closest('a');
      if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || a.target === '_blank' || a.hasAttribute('download')) return;
      const url = new URL(a.href, location.href);
      if (url.origin !== location.origin || url.pathname === location.pathname || !/\.html$/.test(url.pathname)) return;
      e.preventDefault();
      body.classList.add('is-leaving');
      setTimeout(() => (location.href = a.href), 260);
    });
    addEventListener('pageshow', () => body.classList.remove('is-leaving'));
  }
})();
