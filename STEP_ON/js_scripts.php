<?php
$JS_SCRIPTS = '
<script src="http://code.jquery.com/jquery-3.1.1.min.js"></script>
<script src="/assets/templates/js/bootstrap.min.js"></script>
<script src="/assets/templates/js/bootstrap.hover.menu.js"></script>

<!-- Yandex.Metrika counter -->
<script type="text/javascript" >
    (function (d, w, c) {
        (w[c] = w[c] || []).push(function() {
            try {
                w.yaCounter48632645 = new Ya.Metrika({
                    id:48632645,
                    clickmap:true,
                    trackLinks:true,
                    accurateTrackBounce:true
                });
            } catch(e) { }
        });

        var n = d.getElementsByTagName("script")[0],
            s = d.createElement("script"),
            f = function () { n.parentNode.insertBefore(s, n); };
        s.type = "text/javascript";
        s.async = true;
        s.src = "https://mc.yandex.ru/metrika/watch.js";

        if (w.opera == "[object Opera]") {
            d.addEventListener("DOMContentLoaded", f, false);
        } else { f(); }
    })(document, window, "yandex_metrika_callbacks");
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/48632645" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-118080983-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag(\'js\', new Date());

  gtag(\'config\', \'UA-118080983-1\');
</script>

<script src="/assets/templates/js/fancybox/jquery.fancybox.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery.touchswipe/1.6.4/jquery.touchSwipe.js"></script>
<script src="/assets/templates/js/fancybox/jquery.fancybox-buttons.js"></script>
<script src="/assets/templates/js/fancybox/jquery.fancybox-media.js"></script>
<script src="/assets/templates/js/fancybox/jquery.fancybox-thumbs.js"></script>
<script src="/assets/templates/js/fancybox/jquery.mousewheel.pack.js"></script>
<script type="text/javascript">
$(document).ready(function() {
$(\'.fancybox\').fancybox({
        width: "100%",
        margin: [0, 0, 0, 0],
        padding: [0, 0, 0, 0],
        openEffect  : \'none\',
        closeEffect : \'none\',
        prevEffect : \'fade\',
        nextEffect : \'fade\',
        closeBtn  : false,
        arrows: true,
        autoCenter : true,
        helpers : {
            title : null,
            overlay : {
                css : {
                    \'background\' : \'rgba(255, 255, 255, 0.95)\'
                }
            },
            title : {
                  type : \'float\'
              },

            buttons	: {
                tpl : \'<div id="fancybox-buttons"><a class="btnClose" title="Close" href="javascript:;" style="position: absolute; top: 10px; right: 10px;"></a></div>\'
            },


        },
        afterShow: function() {
            $(\'.fancybox-wrap\').swipe({
                swipe : function(event, direction) {
                    if (direction === \'left\' || direction === \'up\') {
                        $.fancybox.prev( direction );
                    } else {
                        $.fancybox.next( direction );
                    }
                }
            });

        },

        afterLoad : function() {
        },
        beforeShow : function() {
            this.title = (this.title ? \'\' + this.title + \'\' : \'\') + \' <span class="num">\' + (this.index + 1) + \' of \' + this.group.length + \' </span>\';
        }
    });

});
</script>
';

