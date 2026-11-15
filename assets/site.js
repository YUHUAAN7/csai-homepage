/* CSAI 사이트 공통 동작: 모바일 메뉴, 메인 슬라이드, 목록 필터, 주소 복사, 사이트 검색, 문의 양식 */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };

  /* 모바일 메뉴 */
  var burger = $("#burger"), mnav = $("#mnav");
  if (burger && mnav) {
    burger.addEventListener("click", function () {
      var open = mnav.hidden;
      mnav.hidden = !open;
      burger.setAttribute("aria-expanded", String(open));
    });
    mnav.addEventListener("click", function (e) {
      if (e.target.closest("a")) { mnav.hidden = true; burger.setAttribute("aria-expanded", "false"); }
    });
  }

  /* 메인 비주얼 슬라이드: 자동으로 넘어가고, 화살표로도 넘길 수 있다 */
  var slides = $$(".slide");
  if (slides.length > 1) {
    var cur = 0, no = $("#slideNo"), bar = $(".hero-bar i");
    var show = function (i) {
      cur = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle("on", k === cur); });
      if (no) no.textContent = ("0" + (cur + 1)).slice(-2) + " / " + ("0" + slides.length).slice(-2);
      if (bar) { bar.style.width = (100 / slides.length) + "%"; bar.style.left = (100 / slides.length * cur) + "%"; }
    };
    /* 6초마다 자동으로 넘긴다. 화살표를 누르면 그 자리에서 다시 6초를 센다. 다른 탭을 보는 동안에는 넘기지 않는다 */
    var timer = null;
    var play = function () { if (timer) clearInterval(timer); timer = setInterval(function () { if (!document.hidden) show(cur + 1); }, 6000); };
    $$("[data-slide]").forEach(function (b) {
      b.addEventListener("click", function () { show(cur + (b.dataset.slide === "next" ? 1 : -1)); play(); });
    });
    show(0); play();
  }

  /* 하위 메뉴 탭: 현재 보고 있는 구역 표시 */
  var tabs = $$("#subnav a");
  if (tabs.length && "IntersectionObserver" in window) {
    var byId = {};
    tabs.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (en.isIntersecting) {
          tabs.forEach(function (a) { a.classList.remove("on"); });
          var a = byId[en.target.id];
          if (a) {
            a.classList.add("on");
            /* 탭 줄만 가로로 움직인다. scrollIntoView 는 페이지 전체를 위로 끌어올려 스크롤을 막으므로 쓰지 않는다. */
            var box = a.parentNode;
            while (box && box.id !== "subnav" && box.scrollWidth <= box.clientWidth) box = box.parentNode;
            if (box && box.scrollWidth > box.clientWidth) {
              var r = a.getBoundingClientRect(), bx = box.getBoundingClientRect();
              box.scrollLeft += (r.left + r.width / 2) - (bx.left + bx.width / 2);
            }
          }
        }
      });
    }, { rootMargin: "-30% 0px -60% 0px" });
    Object.keys(byId).forEach(function (id) { var el = document.getElementById(id); if (el) io.observe(el); });
  }

  /* 목록 필터 */
  $$("[data-f]").forEach(function (b) {
    b.addEventListener("click", function () {
      var f = b.dataset.f;
      $$("[data-f]").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
      $$("#articles li").forEach(function (li) { li.hidden = !(f === "all" || li.dataset.t === f); });
    });
  });

  /* 복사 버튼 */
  function selectNode(n) { var r = document.createRange(); r.selectNodeContents(n); var s = getSelection(); s.removeAllRanges(); s.addRange(r); }
  $$("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var n = $(b.dataset.copy); if (!n) return;
      var t = n.textContent, done = function () { b.textContent = b.dataset.done || "OK"; };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(done, function () { selectNode(n); });
      else selectNode(n);
    });
  });

  /* 사이트 검색: 색인 파일은 처음 열 때 한 번만 불러온다 */
  var sov = $("#sov"), sq = $("#sq"), sres = $("#sres"), loaded = false, lastFocus = null;
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function render() {
    var q = sq.value.trim().toLowerCase(), idx = window.CSAI_SEARCH || [];
    if (!q) { sres.innerHTML = '<li class="msg">' + esc(sres.dataset.hint) + "</li>"; return; }
    var words = q.split(/\s+/);
    var hits = idx.filter(function (d) {
      var hay = (d.t + " " + d.s + " " + d.c).toLowerCase();
      return words.every(function (w) { return hay.indexOf(w) > -1; });
    }).slice(0, 30);
    sres.innerHTML = hits.length ? hits.map(function (d) {
      return '<li><a href="' + esc(d.u) + '"><span class="c">' + esc(d.c) + "</span><b>" + esc(d.t) + "</b><small>" + esc(d.s) + "</small></a></li>";
    }).join("") : '<li class="msg">' + esc(sres.dataset.empty) + "</li>";
  }
  function openSearch() {
    lastFocus = document.activeElement;
    sov.hidden = false; sq.focus(); render();
    if (!loaded) {
      loaded = true;
      var s = document.createElement("script");
      s.src = sq.dataset.idx; s.onload = render; document.head.appendChild(s);
    }
  }
  function closeSearch() { sov.hidden = true; if (lastFocus && lastFocus.focus) lastFocus.focus(); }
  if (sov) {
    $$("[data-search-open]").forEach(function (b) { b.addEventListener("click", openSearch); });
    $$("[data-search-close]").forEach(function (b) { b.addEventListener("click", closeSearch); });
    sov.addEventListener("click", function (e) { if (e.target === sov || e.target.closest(".sov-res a")) closeSearch(); });
    sq.addEventListener("input", render);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !sov.hidden) closeSearch();
      if (e.key === "/" && sov.hidden && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) { e.preventDefault(); openSearch(); }
    });
  }

  /* 문의 양식: 유형 탭 + 메일 작성. 서버 저장 없이 방문자의 메일 앱으로 내용을 넘긴다. */
  var tabBtns = $$("[data-tab]"), forms = $$("form[data-form]");
  function pick(id) {
    tabBtns.forEach(function (b) { b.setAttribute("aria-selected", String(b.dataset.tab === id)); });
    forms.forEach(function (f) { f.hidden = f.dataset.form !== id; });
  }
  if (tabBtns.length) {
    tabBtns.forEach(function (b) { b.addEventListener("click", function () { pick(b.dataset.tab); }); });
    var h = location.hash.slice(1);
    if (h && forms.some(function (f) { return f.dataset.form === h; })) pick(h);
    window.addEventListener("hashchange", function () {
      var k = location.hash.slice(1);
      if (forms.some(function (f) { return f.dataset.form === k; })) pick(k);
    });
  }
  forms.forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!f.reportValidity()) return;
      var lines = [];
      $$("[name]", f).forEach(function (el) {
        if (el.type === "checkbox") return;
        var v = el.value.trim(); if (!v) return;
        lines.push("■ " + el.dataset.label + "\n" + v);
      });
      var first = $("[name]", f).value.trim();
      var subject = "[" + f.dataset.subject + "] " + first;
      var body = lines.join("\n\n");
      var out = $(".form-out", f);
      $("pre", out).textContent = subject + "\n\n" + body;
      out.hidden = false;
      out.scrollIntoView({ block: "nearest" });
      var a = $("a.mail-open", out);
      a.href = "mailto:" + f.dataset.to + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    });
  });
})();
