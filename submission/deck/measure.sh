#!/bin/bash
#
# measure.sh - check that no slide in deck.html runs under its footer.
#
# WHY THIS EXISTS
#   Each slide is a fixed 1280 x 720 px box with overflow:hidden. Content that
#   grows past the footer is not an error the browser reports: it is silently
#   clipped, or it overlaps the footline. The type scale in deck.html is set
#   close to the floor of what is comfortable, so a slide only has to grow by
#   one bullet for that to happen. This script reports how much slack each
#   slide has left.
#
# HOW IT WORKS
#   It writes a scratch copy of the deck with a measuring script appended, opens
#   it in headless Chrome, and reads the numbers back out of the DOM. Nothing
#   in submission/deck/ is modified.
#
# USAGE
#   ./measure.sh              # check deck.html sitting next to this script
#   ./measure.sh other.html   # check another deck in the same shape
#
# READING THE OUTPUT
#   slackVsFooter  px of clear space between the lowest content and the footer.
#                  Positive is fine. Negative means the content is under the
#                  footer or clipped, and the slide needs a shorter bullet.
#   contentEndsAt  where the lowest content ends, measured from the slide top.
#   pastSlide      how much has been clipped off the 720 px page. Must be 0.
#   overRight      content spilling past the right edge. Must be 0.
#   colgroup N     intrinsic content height of each column in a grid, so you can
#                  see WHICH column is the tall one instead of guessing.
#
# Requires Google Chrome. Set CHROME=... to use another build.

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
DECK="${1:-$HERE/deck.html}"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
TMP="${TMPDIR:-/tmp}/deck-measure-$$.html"

if [ ! -f "$DECK" ]; then
  echo "no such deck: $DECK" >&2
  exit 1
fi
if [ ! -x "$CHROME" ]; then
  echo "no Chrome at: $CHROME  (set CHROME=/path/to/chrome)" >&2
  exit 1
fi

cleanup() { rm -f "$TMP"; }
trap cleanup EXIT

python3 - "$DECK" "$TMP" <<'PY'
import sys

src, dst = sys.argv[1], sys.argv[2]
html = open(src, encoding="utf-8").read()

probe = r'''
<pre id="REPORT" style="font:12px monospace;white-space:pre"></pre>
<script>
(function(){
  var out=[];
  var desc=function(el){
    return (el.className||el.tagName)+' :: '+
           (el.textContent||'').trim().replace(/\s+/g,' ').slice(0,58);
  };
  document.querySelectorAll('.slide').forEach(function(s,i){
    var sr=s.getBoundingClientRect();
    var foot=s.querySelector('.s-foot');
    var footTop=foot?foot.getBoundingClientRect().top:sr.bottom;
    var deepest=0, deepEl='', right=0, rightEl='';
    s.querySelectorAll('*').forEach(function(el){
      if(el.closest('.s-foot')) return;
      var cs=getComputedStyle(el);
      if(cs.display==='none'||cs.visibility==='hidden') return;
      var r=el.getBoundingClientRect();
      if(!r.width && !r.height) return;
      if(r.bottom>deepest){ deepest=r.bottom; deepEl=desc(el); }
      if(r.right>right){ right=r.right; rightEl=desc(el); }
    });
    var slack=footTop-deepest;
    out.push('SLIDE '+(i+1)
      +' | slackVsFooter='+slack.toFixed(1)+'px'
      +' | contentEndsAt='+(deepest-sr.top).toFixed(0)
      +' | pastSlide='+Math.max(0,deepest-sr.bottom).toFixed(1)
      +' | overRight='+Math.max(0,right-sr.right).toFixed(1));
    if(slack<8)  out.push('    TIGHT bottom -> '+deepEl);
    if(right-sr.right>0.5) out.push('    OVERRIGHT -> '+rightEl);
    s.querySelectorAll('.cols').forEach(function(g,gi){
      var kids=[].slice.call(g.children).filter(function(c){
        return getComputedStyle(c).display!=='none';
      });
      if(!kids.length) return;
      out.push('    colgroup '+gi+' content heights: '+kids.map(function(c,ci){
        var ct=c.getBoundingClientRect().top, max=0;
        var stack=[].slice.call(c.children);
        while(stack.length){
          var el=stack.pop();
          var r=el.getBoundingClientRect();
          if(r.bottom-ct>max) max=r.bottom-ct;
          [].forEach.call(el.children, function(ch){
            if(getComputedStyle(ch).display!=='none' && ch.tagName!=='SVG') stack.push(ch);
          });
        }
        return ci+':'+max.toFixed(0);
      }).join('  '));
    });
  });
  document.getElementById('REPORT').textContent='ZZREPORTZZ\n'+out.join('\n')+'\nZZENDZZ';
})();
</script>
'''

open(dst, "w", encoding="utf-8").write(html.replace("</body>", probe + "\n</body>"))
PY

"$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
  --virtual-time-budget=6000 --window-size=1280,720 \
  --dump-dom "file://$TMP" 2>/dev/null \
  | sed -n '/ZZREPORTZZ/,/ZZENDZZ/p' \
  | grep -E '^(SLIDE |    (colgroup|TIGHT|OVER|OVERLAP))' || true

if [ ! -s "$TMP" ]; then
  echo "chrome failed to render the deck" >&2
  exit 1
fi
