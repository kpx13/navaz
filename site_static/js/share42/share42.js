/* share42.com | 04.03.2012 | (c) Dimox */
function share42(f){d=document.getElementsByTagName('div');for(var i=0;i<d.length;i++){if(d[i].className.indexOf('share42init')!=-1){if(d[i].getAttribute('data-url')!=-1)u=d[i].getAttribute('data-url');if(d[i].getAttribute('data-title')!=-1)t=d[i].getAttribute('data-title');if(!u)u=location.href;if(!t)t=document.title;u=encodeURIComponent(u);t=encodeURIComponent(t);var s=new Array('"#" onclick="window.open(\'http://www.facebook.com/sharer.php?u='+u+'&t='+t+'\', \'_blank\', \'scrollbars=0, resizable=1, menubar=0, left=200, top=200, width=550, height=440, toolbar=0, status=0\');return false" title="Поделиться в Facebook"','"#" onclick="window.open(\'http://twitter.com/share?text='+t+'&url='+u+'\', \'_blank\', \'scrollbars=0, resizable=1, menubar=0, left=200, top=200, width=550, height=440, toolbar=0, status=0\');return false" title="Добавить в Twitter"','"#" onclick="window.open(\'http://vk.com/share.php?url='+u+'\', \'_blank\', \'scrollbars=0, resizable=1, menubar=0, left=200, top=200, width=554, height=421, toolbar=0, status=0\');return false" title="Поделиться В Контакте"','"http://www.feedburner.com/fb/a/emailFlare?loc=ru_RU&itemTitle='+t+'&uri='+u+'" title="Отправить на e-mail другу"');var l='';for(j=0;j<s.length;j++)l+='<a rel="nofollow" style="display:inline-block;vertical-align:bottom;width:16px;height:16px;margin:0 6px 6px 0;padding:0;outline:none;background:url('+f+'icons.png) -'+16*j+'px 0 no-repeat" href='+s[j]+' target="_blank"></a>';d[i].innerHTML='<span id="share42">'+l+'</span>';}}};