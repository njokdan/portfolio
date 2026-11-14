(function(){
  var BASE = "https://njokdan.github.io/portfolio/";
  var home = document.getElementById("home");
  var cases = Array.prototype.slice.call(document.querySelectorAll("article.case"));
  var baseTitle = document.title;
  var toastEl = document.querySelector(".toast"), tt;
  function toast(m){ toastEl.textContent = m; toastEl.classList.add("on"); clearTimeout(tt); tt = setTimeout(function(){ toastEl.classList.remove("on"); }, 2600); }

  function route(){
    var h = (location.hash || "").slice(1);
    var target = h && document.getElementById(h);
    var isCase = target && target.classList.contains("case");
    cases.forEach(function(c){ c.hidden = c !== target; });
    home.hidden = !!isCase;
    if (isCase){
      document.title = target.querySelector("h1").textContent + " case study, Daniel Njoku";
      window.scrollTo(0, 0);
      var h1 = target.querySelector("h1"); h1.setAttribute("tabindex", "-1"); h1.focus({preventScroll:true});
    } else {
      document.title = baseTitle;
      if (target) target.scrollIntoView(); else if (!h || h === "top") window.scrollTo(0, 0);
    }
  }
  window.addEventListener("hashchange", route);
  route();

  document.addEventListener("click", function(ev){
    var b = ev.target.closest(".copy"); if (!b) return;
    var url = BASE + "#" + b.getAttribute("data-id");
    try {
      navigator.clipboard.writeText(url).then(function(){ toast("Link copied"); }, function(){ toast(url); });
    } catch (e) { toast(url); }
  });
})();
