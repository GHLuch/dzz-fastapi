import{s as dt,e as l,a as j,c as o,b as d,g as N,d as A,f as c,h as i,i as L,j as Z,k as s,l as q,p as X,n as z,r as pt,m as ht,o as _t,q as Y,t as vt}from"../chunks/scheduler.CNyn7n1I.js";import{S as mt,i as bt}from"../chunks/index.BeSP3sf6.js";import{g as gt}from"../chunks/entry.CbpJ59DM.js";import{t as ft}from"../chunks/task_store.CRjp3V4u.js";function yt(r){let t,n="Нажимите, чтобы загрузить изображение";return{c(){t=l("span"),t.textContent=n},l(a){t=o(a,"SPAN",{"data-svelte-h":!0}),N(t)!=="svelte-m6p24x"&&(t.textContent=n)},m(a,f){Z(a,t,f),r[10](t)},p:z,d(a){a&&c(t),r[10](null)}}}function Ct(r){let t,n;return{c(){t=l("img"),this.h()},l(a){t=o(a,"IMG",{style:!0,src:!0,alt:!0}),this.h()},h(){L(t,"width","100%"),L(t,"height","100%"),L(t,"object-fit","cover"),vt(t.src,n="")||i(t,"src",n),i(t,"alt","Preview")},m(a,f){Z(a,t,f),r[9](t)},p:z,d(a){a&&c(t),r[9](null)}}}function xt(r){let t,n,a,f="Загрузите изображение",I,u,b,g,E,y,x,O,p,U,C,e,h,_,$="Очистить",J,w,tt='<button type="submit" class="file-button-4">Перейти к этапу обработки</button>',K,P,T,k,et="Очистить",Q,D,st="Перейти к этапу обработки",W,nt;function at(m,V){return m[4]?Ct:yt}let B=at(r),v=B(r);return{c(){t=l("div"),n=l("div"),a=l("p"),a.textContent=f,I=j(),u=l("form"),b=l("div"),g=l("div"),E=l("div"),y=l("label"),x=l("input"),O=j(),p=l("div"),v.c(),U=j(),C=l("div"),e=l("nav"),h=l("p"),_=l("button"),_.textContent=$,J=j(),w=l("p"),w.innerHTML=tt,K=j(),P=l("nav"),T=l("p"),k=l("button"),k.textContent=et,Q=j(),D=l("button"),D.textContent=st,this.h()},l(m){t=o(m,"DIV",{class:!0});var V=d(t);n=o(V,"DIV",{class:!0});var F=d(n);a=o(F,"P",{"data-svelte-h":!0}),N(a)!=="svelte-1jojxko"&&(a.textContent=f),I=A(F),u=o(F,"FORM",{class:!0});var M=d(u);b=o(M,"DIV",{class:!0});var lt=d(b);g=o(lt,"DIV",{class:!0});var ot=d(g);E=o(ot,"DIV",{class:!0});var rt=d(E);y=o(rt,"LABEL",{class:!0});var S=d(y);x=o(S,"INPUT",{type:!0,accept:!0}),O=A(S),p=o(S,"DIV",{style:!0});var it=d(p);v.l(it),it.forEach(c),S.forEach(c),rt.forEach(c),ot.forEach(c),lt.forEach(c),U=A(M),C=o(M,"DIV",{class:!0});var R=d(C);e=o(R,"NAV",{class:!0});var H=d(e);h=o(H,"P",{});var ct=d(h);_=o(ct,"BUTTON",{class:!0,"data-svelte-h":!0}),N(_)!=="svelte-j82y25"&&(_.textContent=$),ct.forEach(c),J=A(H),w=o(H,"P",{"data-svelte-h":!0}),N(w)!=="svelte-1uash8m"&&(w.innerHTML=tt),H.forEach(c),K=A(R),P=o(R,"NAV",{class:!0});var ut=d(P);T=o(ut,"P",{});var G=d(T);k=o(G,"BUTTON",{class:!0,"data-svelte-h":!0}),N(k)!=="svelte-j82y25"&&(k.textContent=et),Q=A(G),D=o(G,"BUTTON",{type:!0,class:!0,"data-svelte-h":!0}),N(D)!=="svelte-1aaccqx"&&(D.textContent=st),G.forEach(c),ut.forEach(c),R.forEach(c),M.forEach(c),F.forEach(c),V.forEach(c),this.h()},h(){i(x,"type","file"),i(x,"accept","image/*"),L(p,"width","650px"),L(p,"height","350px"),L(p,"margin","10px"),i(y,"class","label"),i(E,"class","form-group"),i(g,"class","example-1"),i(b,"class","column-file-loading"),i(_,"class","file-button-2"),i(e,"class","nav-max-770px"),i(k,"class","file-button-2"),i(D,"type","submit"),i(D,"class","file-button-4"),i(P,"class","nav-min-770px"),i(C,"class","column-file-box"),i(u,"class","py-2"),i(n,"class","column-file"),i(t,"class","row")},m(m,V){Z(m,t,V),s(t,n),s(n,a),s(n,I),s(n,u),s(u,b),s(b,g),s(g,E),s(E,y),s(y,x),s(y,O),s(y,p),v.m(p,null),r[11](p),s(u,U),s(u,C),s(C,e),s(e,h),s(h,_),s(e,J),s(e,w),s(C,K),s(C,P),s(P,T),s(T,k),s(T,Q),s(T,D),W||(nt=[q(x,"change",r[8]),q(x,"change",r[6]),q(_,"click",X(r[5])),q(k,"click",X(r[5])),q(u,"submit",X(r[7]))],W=!0)},p(m,[V]){B===(B=at(m))&&v?v.p(m,V):(v.d(1),v=B(m),v&&(v.c(),v.m(p,null)))},i:z,o:z,d(m){m&&c(t),v.d(),r[11](null),W=!1,pt(nt)}}}function Et(r,t,n){let a;ht(r,ft,e=>n(12,a=e));let f,I,u,b,g=!1;function E(){n(0,f=null),u.setAttribute("src","")}function y(){const e=f[0];if(e){n(4,g=!0);const h=new FileReader;h.addEventListener("load",function(){u.setAttribute("src",h.result)}),h.readAsDataURL(e);return}n(4,g=!1)}async function x(){const e=new FormData;console.log(f),e.append("image",f[0]);try{const _=await(await fetch("/api/image/upload",{method:"POST",body:e})).json();console.log(_),_t(ft,a=_.task_id,a),gt("/result")}catch(h){console.error("Error uploading file:",h)}}function O(){f=this.files,n(0,f)}function p(e){Y[e?"unshift":"push"](()=>{u=e,n(2,u)})}function U(e){Y[e?"unshift":"push"](()=>{b=e,n(3,b)})}function C(e){Y[e?"unshift":"push"](()=>{I=e,n(1,I)})}return[f,I,u,b,g,E,y,x,O,p,U,C]}class Vt extends mt{constructor(t){super(),bt(this,t,Et,xt,dt,{})}}export{Vt as component};
