(function(){var e,t,a,i,r
e=window,t=function(u,D){"use strict"
if(!D.getElementsByClassName){return}var O,H,P=D.documentElement,d=u.Date,i=u.HTMLPictureElement,U="addEventListener",k="getAttribute",I=u[U],$=u.setTimeout,s=u.requestAnimationFrame||$,o=u.requestIdleCallback,q=/^picture$/i,r=["load","error","lazyincluded","_lazyloaded"],a={},j=Array.prototype.forEach,G=function(e,t){if(!a[t]){a[t]=new RegExp("(\\s|^)"+t+"(\\s|$)")}return a[t].test(e[k]("class")||"")&&a[t]},K=function(e,t){if(!G(e,t)){e.setAttribute("class",(e[k]("class")||"").trim()+" "+t)}},Q=function(e,t){var a
if(a=G(e,t)){e.setAttribute("class",(e[k]("class")||"").replace(a," "))}},J=function(t,a,e){var i=e?U:"removeEventListener"
if(e){J(t,a)}r.forEach(function(e){t[i](e,a)})},V=function(e,t,a,i,r){var n=D.createEvent("Event")
if(!a){a={}}a.instance=O
n.initEvent(t,!i,!r)
n.detail=a
e.dispatchEvent(n)
return n},X=function(e,t){var a
if(!i&&(a=u.picturefill||H.pf)){if(t&&t.src&&!e[k]("srcset")){e.setAttribute("srcset",t.src)}a({reevaluate:true,elements:[e]})}else if(t&&t.src){e.src=t.src}},Y=function(e,t){return(getComputedStyle(e,null)||{})[t]},l=function(e,t,a){a=a||e.offsetWidth
while(a<H.minSize&&t&&!e._lazysizesWidth){a=t.offsetWidth
t=t.parentNode}return a},Z=function(){var a,i
var t=[]
var r=[]
var n=t
var l=function(){var e=n
n=t.length?r:t
a=true
i=false
while(e.length){e.shift()()}a=false}
var e=function(e,t){if(a&&!t){e.apply(this,arguments)}else{n.push(e)
if(!i){i=true;(D.hidden?$:s)(l)}}}
e._lsFlush=l
return e}(),ee=function(a,e){return e?function(){Z(a)}:function(){var e=this
var t=arguments
Z(function(){a.apply(e,t)})}},te=function(e){var a
var i=0
var r=H.throttleDelay
var n=H.ricTimeout
var t=function(){a=false
i=d.now()
e()}
var l=o&&n>49?function(){o(t,{timeout:n})
if(n!==H.ricTimeout){n=H.ricTimeout}}:ee(function(){$(t)},true)
return function(e){var t
if(e=e===true){n=33}if(a){return}a=true
t=r-(d.now()-i)
if(t<0){t=0}if(e||t<9){l()}else{$(l,t)}}},ae=function(e){var t,a
var i=99
var r=function(){t=null
e()}
var n=function(){var e=d.now()-a
if(e<i){$(n,i-e)}else{(o||r)(r)}}
return function(){a=d.now()
if(!t){t=$(n,i)}}};(function(){var e
var t={lazyClass:"lazyload",loadedClass:"lazyloaded",loadingClass:"lazyloading",preloadClass:"lazypreload",errorClass:"lazyerror",autosizesClass:"lazyautosizes",srcAttr:"data-src",srcsetAttr:"data-srcset",sizesAttr:"data-sizes",minSize:40,customMedia:{},init:true,expFactor:1.5,hFac:.8,loadMode:2,loadHidden:true,ricTimeout:0,throttleDelay:125}
H=u.lazySizesConfig||u.lazysizesConfig||{}
for(e in t){if(!(e in H)){H[e]=t[e]}}$(function(){if(H.init){n()}})})()
var e=function(){var v,m,f,y,e
var g,z,h,p,A,b,C
var n=/^img$/i
var c=/^iframe$/i
var E="onscroll"in u&&!/(gle|ing)bot/.test(navigator.userAgent)
var w=0
var L=0
var _=0
var N=-1
var M=function(e){_--
if(!e||_<0||!e.target){_=0}}
var x=function(e){if(C==null){C=Y(D.body,"visibility")=="hidden"}return C||Y(e.parentNode,"visibility")!="hidden"&&Y(e,"visibility")!="hidden"}
var F=function(e,t){var a
var i=e
var r=x(e)
h-=t
b+=t
p-=t
A+=t
while(r&&(i=i.offsetParent)&&i!=D.body&&i!=P){r=(Y(i,"opacity")||1)>0
if(r&&Y(i,"overflow")!="visible"){a=i.getBoundingClientRect()
r=A>a.left&&p<a.right&&b>a.top-1&&h<a.bottom+1}}return r}
var t=function(){var e,t,a,i,r,n,l,s,o,u,d,f
var c=O.elements
if((y=H.loadMode)&&_<8&&(e=c.length)){t=0
N++
for(;t<e;t++){if(!c[t]||c[t]._lazyRace){continue}if(!E||O.prematureUnveil&&O.prematureUnveil(c[t])){R(c[t])
continue}if(!(s=c[t][k]("data-expand"))||!(n=s*1)){n=L}if(!u){u=!H.expand||H.expand<1?P.clientHeight>500&&P.clientWidth>500?500:370:H.expand
O._defEx=u
d=u*H.expFactor
f=H.hFac
C=null
if(L<d&&_<1&&N>2&&y>2&&!D.hidden){L=d
N=0}else if(y>1&&N>1&&_<6){L=u}else{L=w}}if(o!==n){g=innerWidth+n*f
z=innerHeight+n
l=n*-1
o=n}a=c[t].getBoundingClientRect()
if((b=a.bottom)>=l&&(h=a.top)<=z&&(A=a.right)>=l*f&&(p=a.left)<=g&&(b||A||p||h)&&(H.loadHidden||x(c[t]))&&(m&&_<3&&!s&&(y<3||N<4)||F(c[t],n))){R(c[t])
r=true
if(_>9){break}}else if(!r&&m&&!i&&_<4&&N<4&&y>2&&(v[0]||H.preloadAfterLoad)&&(v[0]||!s&&(b||A||p||h||c[t][k](H.sizesAttr)!="auto"))){i=v[0]||c[t]}}if(i&&!r){R(i)}}}
var a=te(t)
var S=function(e){var t=e.target
if(t._lazyCache){delete t._lazyCache
return}M(e)
K(t,H.loadedClass)
Q(t,H.loadingClass)
J(t,T)
V(t,"lazyloaded")}
var i=ee(S)
var T=function(e){i({target:e.target})}
var B=function(t,a){try{t.contentWindow.location.replace(a)}catch(e){t.src=a}}
var W=function(e){var t
var a=e[k](H.srcsetAttr)
if(t=H.customMedia[e[k]("data-media")||e[k]("media")]){e.setAttribute("media",t)}if(a){e.setAttribute("srcset",a)}}
var l=ee(function(t,e,a,i,r){var n,l,s,o,u,d
if(!(u=V(t,"lazybeforeunveil",e)).defaultPrevented){if(i){if(a){K(t,H.autosizesClass)}else{t.setAttribute("sizes",i)}}l=t[k](H.srcsetAttr)
n=t[k](H.srcAttr)
if(r){s=t.parentNode
o=s&&q.test(s.nodeName||"")}d=e.firesLoad||"src"in t&&(l||n||o)
u={target:t}
K(t,H.loadingClass)
if(d){clearTimeout(f)
f=$(M,2500)
J(t,T,true)}if(o){j.call(s.getElementsByTagName("source"),W)}if(l){t.setAttribute("srcset",l)}else if(n&&!o){if(c.test(t.nodeName)){B(t,n)}else{t.src=n}}if(r&&(l||o)){X(t,{src:n})}}if(t._lazyRace){delete t._lazyRace}Q(t,H.lazyClass)
Z(function(){var e=t.complete&&t.naturalWidth>1
if(!d||e){if(e){K(t,"ls-is-cached")}S(u)
t._lazyCache=true
$(function(){if("_lazyCache"in t){delete t._lazyCache}},9)}if(t.loading=="lazy"){_--}},true)})
var R=function(e){if(e._lazyRace){return}var t
var a=n.test(e.nodeName)
var i=a&&(e[k](H.sizesAttr)||e[k]("sizes"))
var r=i=="auto"
if((r||!m)&&a&&(e[k]("src")||e.srcset)&&!e.complete&&!G(e,H.errorClass)&&G(e,H.lazyClass)){return}t=V(e,"lazyunveilread").detail
if(r){ie.updateElem(e,true,e.offsetWidth)}e._lazyRace=true
_++
l(e,t,r,i,a)}
var r=ae(function(){H.loadMode=3
a()})
var s=function(){if(H.loadMode==3){H.loadMode=2}r()}
var o=function(){if(m){return}if(d.now()-e<999){$(o,999)
return}m=true
H.loadMode=3
a()
I("scroll",s,true)}
return{_:function(){e=d.now()
O.elements=D.getElementsByClassName(H.lazyClass)
v=D.getElementsByClassName(H.lazyClass+" "+H.preloadClass)
I("scroll",a,true)
I("resize",a,true)
if(u.MutationObserver){new MutationObserver(a).observe(P,{childList:true,subtree:true,attributes:true})}else{P[U]("DOMNodeInserted",a,true)
P[U]("DOMAttrModified",a,true)
setInterval(a,999)}I("hashchange",a,true);["focus","mouseover","click","load","transitionend","animationend"].forEach(function(e){D[U](e,a,true)})
if(/d$|^c/.test(D.readyState)){o()}else{I("load",o)
D[U]("DOMContentLoaded",a)
$(o,2e4)}if(O.elements.length){t()
Z._lsFlush()}else{a()}},checkElems:a,unveil:R,_aLSL:s}}(),ie=function(){var a
var n=ee(function(e,t,a,i){var r,n,l
e._lazysizesWidth=i
i+="px"
e.setAttribute("sizes",i)
if(q.test(t.nodeName||"")){r=t.getElementsByTagName("source")
for(n=0,l=r.length;n<l;n++){r[n].setAttribute("sizes",i)}}if(!a.detail.dataAttr){X(e,a.detail)}})
var i=function(e,t,a){var i
var r=e.parentNode
if(r){a=l(e,r,a)
i=V(e,"lazybeforesizes",{width:a,dataAttr:!!t})
if(!i.defaultPrevented){a=i.detail.width
if(a&&a!==e._lazysizesWidth){n(e,r,i,a)}}}}
var e=function(){var e
var t=a.length
if(t){e=0
for(;e<t;e++){i(a[e])}}}
var t=ae(e)
return{_:function(){a=D.getElementsByClassName(H.autosizesClass)
I("resize",t)},checkElems:t,updateElem:i}}(),n=function(){if(!n.i){n.i=true
ie._()
e._()}}
return O={cfg:H,autoSizer:ie,loader:e,init:n,uP:X,aC:K,rC:Q,hC:G,fire:V,gW:l,rAF:Z}}(e,e.document),e.lazySizes=t,"object"==typeof module&&module.exports&&(module.exports=t),a=window,r=function(){i(a.lazySizes),a.removeEventListener("lazyunveilread",r,!0)},i=(i=function(i,y,g){"use strict"
var r=[].slice,n=/blur-up["']*\s*:\s*["']*(always|auto)/,l=/image\/(jpeg|png|gif|svg\+xml)/,s="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",o=function(e){var t=e.getAttribute("data-media")||e.getAttribute("media"),a=e.getAttribute("type")
return(!a||l.test(a))&&(!t||i.matchMedia(g.cfg.customMedia[t]||t).matches)},u=function(e,t){var a,i=e?r.call(e.querySelectorAll("source, img")):[t]
return i.forEach(function(e){if(!a){var t=e.getAttribute("data-lowsrc")
t&&o(e)&&(a=t)}}),a},d=function(e,a,i,r){var n,t,l=!1,s=!1,o="always"==r?0:Date.now(),u=0,d=(e||a).parentNode,f=function(){if(i){var t=function(e){l=!0,n||(n=e.target),g.rAF(function(){g.rC(a,"ls-blur-up-is-loading"),n&&g.aC(n,"ls-blur-up-loaded")}),n&&(n.removeEventListener("load",t),n.removeEventListener("error",t))};(n=y.createElement("img")).addEventListener("load",t),n.addEventListener("error",t),n.className="ls-blur-up-img",n.src=i,n.alt="",n.setAttribute("aria-hidden","true"),d.insertBefore(n,(e||a).nextSibling),"always"!=r&&(n.style.visibility="hidden",setTimeout(function(){g.rAF(function(){s||(n.style.visibility="")})},20))}},c=function(){n&&g.rAF(function(){g.rC(a,"ls-blur-up-is-loading")
try{n.parentNode.removeChild(n)}catch(e){}n=null})},v=function(e){u++,s=e||s,e?c():1<u&&setTimeout(c,5e3)},m=function(){a.removeEventListener("load",m),a.removeEventListener("error",m),n&&g.rAF(function(){n&&g.aC(n,"ls-original-loaded")}),"always"!=r&&(!l||Date.now()-o<66)?v(!0):v()}
f(),a.addEventListener("load",m),a.addEventListener("error",m),g.aC(a,"ls-blur-up-is-loading"),t=function(e){d==e.target&&(g.aC(n||a,"ls-inview"),v(),d.removeEventListener("lazybeforeunveil",t))},d.getAttribute("data-expand")||d.setAttribute("data-expand",-1),d.addEventListener("lazybeforeunveil",t),g.aC(d,g.cfg.lazyClass)}
i.addEventListener("lazybeforeunveil",function(e){var t,a,i=e.detail
i.instance==g&&i.blurUp&&("PICTURE"!=(a=(t=e.target).parentNode).nodeName&&(a=null),d(a,t,u(a,t)||s,i.blurUp))}),i.addEventListener("lazyunveilread",function(e){var t,a,i=e.detail
i.instance==g&&(t=e.target,((a=(getComputedStyle(t,null)||{fontFamily:""}).fontFamily.match(n))||t.getAttribute("data-lowsrc"))&&(i.blurUp=a&&a[1]||g.cfg.blurupMode||"always"))})}).bind(null,a,a.document),"object"==typeof module&&module.exports?i(require("lazysizes")):a.lazySizes?r():a.addEventListener("lazyunveilread",r,!0)}).call(this)
