(function(){
  var PF = window.PF || {single:false, site:location.origin + "/"};
  var toastEl = document.querySelector(".toast"), tt;
  function toast(m){ if(!toastEl) return; toastEl.textContent = m; toastEl.classList.add("on"); clearTimeout(tt); tt = setTimeout(function(){ toastEl.classList.remove("on"); }, 2600); }
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* single-file preview: route between home and case studies on the hash */
  if (PF.single){
    var home = document.getElementById("home");
    var cases = Array.prototype.slice.call(document.querySelectorAll("article.case"));
    var baseTitle = document.title;
    var route = function(){
      var h = (location.hash || "").slice(1);
      var target = h && document.getElementById(h);
      var isCase = !!(target && target.classList.contains("case"));
      cases.forEach(function(c){ c.hidden = c !== target; });
      home.hidden = isCase;
      if (isCase){
        document.title = target.querySelector("h1").textContent + " case study, Daniel Njoku";
        window.scrollTo(0, 0);
        var h1 = target.querySelector("h1"); h1.setAttribute("tabindex", "-1"); h1.focus({preventScroll:true});
      } else {
        document.title = baseTitle;
        if (target) target.scrollIntoView(); else window.scrollTo(0, 0);
        placeBus(0, true);
      }
    };
    window.addEventListener("hashchange", route);
    route();
  }

  /* copy a shareable link to a case study */
  document.addEventListener("click", function(ev){
    var b = ev.target.closest && ev.target.closest(".copy"); if (!b) return;
    var url = PF.single ? PF.site + "work/" + b.getAttribute("data-id") + "/" : location.href.split("#")[0];
    try { navigator.clipboard.writeText(url).then(function(){ toast("Link copied"); }, function(){ toast(url); }); }
    catch (e) { toast(url); }
  });

  /* the danfo: drives in on load, then rolls to whichever stop you point at */
  var bus = document.querySelector(".bus"), track = document.querySelector(".route-track");
  var stops = Array.prototype.slice.call(document.querySelectorAll(".stop"));
  function placeBus(i, instant){
    if (!bus || !track || !stops[i]) return;
    var dot = stops[i].querySelector(".dot");
    var x = dot.getBoundingClientRect().left - track.getBoundingClientRect().left + dot.offsetWidth / 2 - bus.offsetWidth / 2;
    if (instant) { bus.style.transition = "none"; bus.style.transform = "translateX(" + x + "px)"; bus.offsetWidth; bus.style.transition = ""; }
    else bus.style.transform = "translateX(" + x + "px)";
    stops.forEach(function(s, j){ s.classList.toggle("here", j === i); });
  }
  if (bus && stops.length){
    var current = 0;
    if (reduce) { placeBus(0, true); bus.classList.add("in"); }
    else {
      bus.style.transform = "translateX(-120px)";
      setTimeout(function(){ bus.classList.add("in"); placeBus(0); }, 450);
    }
    stops.forEach(function(s, i){
      var go = function(){ current = i; placeBus(i); };
      s.addEventListener("mouseenter", go); s.addEventListener("focusin", go);
    });
    window.addEventListener("resize", function(){ placeBus(current, true); });
  }
})();
