"""Shared SVG helpers and colour tokens for the DRISHTI-PGK deck figures.

Every generated figure is written so that:

  * each colour is referenced as  style="fill:var(--f-accent, #0b5cad)"
    i.e. a CSS custom property WITH a fallback.  Inlined in deck.html the
    property resolves from the deck's single token block, so restyling the
    deck recolours every figure at once.  Opened standalone, the fallback
    below applies.
  * no <style> element is emitted, so an inlined figure cannot leak rules
    into the deck.  All presentation is per-element.

To change the standalone colours, edit TOKEN and re-run make_figures.py.
"""

# Colour roles.  Names match the figure tokens in deck.html's token block.
TOKEN = {
    "f-ink":    "#10151b",              # primary text + figure strokes
    "f-ink2":   "#46525f",              # secondary text
    "f-ink3":   "#7b8794",              # captions, axis labels, ticks
    "f-rule":   "#d9dee4",              # hairlines, gridlines, axes
    "f-band":   "#f2f5f8",              # panel / plot background tint
    "f-paper":  "#ffffff",
    "f-accent": "#0b5cad",              # THE accent: data, emphasis, rules
    "f-tint":   "rgba(11,92,173,.13)",  # accent at 13% - shaded bands, fills
    "f-tint2":  "rgba(11,92,173,.30)",
    "f-flag":   "#a4551a",              # placeholders + open decisions only
    "f-flagt":  "rgba(164,85,26,.13)",
}

FONT = ("-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, "
        "'Helvetica Neue', Arial, sans-serif")


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def _val(prop, v):
    """Resolve a colour token name to var(--token, fallback); other CSS passes through."""
    if isinstance(v, str) and v in TOKEN:
        return "var(--%s, %s)" % (v, TOKEN[v])
    if prop == "opacity" and isinstance(v, (int, float)):
        return "%g" % v
    return v


def _style(**kv):
    out = []
    for k, v in kv.items():
        if v is None:
            continue
        prop = k.replace("_", "-")
        # CSS values must not carry a double quote: they would close the
        # enclosing style="..." attribute and break the XML parse.
        out.append("%s:%s" % (prop, str(_val(prop, v)).replace('"', "'")))
    return ";".join(out)


def open_svg(w, h, title, desc, extra=""):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %g %g" '
        'width="%g" height="%g" role="img" aria-label="%s" '
        'style="%s">\n<title>%s</title>\n<desc>%s</desc>\n%s'
        % (w, h, w, h, esc(title), _style(font_family=FONT, display="block"),
           esc(title), esc(desc), extra)
    )


def close_svg():
    return "</svg>\n"


def txt(x, y, s, size=10, fill="f-ink", anchor="start", weight="400",
        style=None, ls=None, italic=False):
    st = _style(font_size="%gpx" % size, fill=fill, font_weight=weight,
                letter_spacing=ls, font_style="italic" if italic else None)
    if style:
        st += ";" + style
    return ('<text x="%g" y="%g" text-anchor="%s" style="%s">%s</text>\n'
            % (x, y, anchor, st, esc(s)))


def line(x1, y1, x2, y2, stroke="f-rule", sw=1, dash=None, cap=None):
    return ('<line x1="%g" y1="%g" x2="%g" y2="%g" style="%s"/>\n'
            % (x1, y1, x2, y2,
               _style(stroke=stroke, stroke_width="%g" % sw,
                      stroke_dasharray=dash, stroke_linecap=cap)))


def rect(x, y, w, h, fill="none", stroke=None, sw=1, rx=0, dash=None, opacity=None):
    return ('<rect x="%g" y="%g" width="%g" height="%g" rx="%g" style="%s"/>\n'
            % (x, y, w, h, rx,
               _style(fill=fill, stroke=stroke, stroke_width="%g" % sw,
                      stroke_dasharray=dash, opacity=opacity)))


def circle(cx, cy, r, fill="none", stroke=None, sw=1):
    return ('<circle cx="%g" cy="%g" r="%g" style="%s"/>\n'
            % (cx, cy, r, _style(fill=fill, stroke=stroke, stroke_width="%g" % sw)))


def poly(points, fill="none", stroke=None, sw=1, dash=None):
    pts = " ".join("%g,%g" % p for p in points)
    return ('<polygon points="%s" style="%s"/>\n'
            % (pts, _style(fill=fill, stroke=stroke, stroke_width="%g" % sw,
                           stroke_dasharray=dash)))


def path(d, fill="none", stroke=None, sw=1, dash=None, cap=None, join=None):
    return ('<path d="%s" style="%s"/>\n'
            % (d, _style(fill=fill, stroke=stroke, stroke_width="%g" % sw,
                         stroke_dasharray=dash, stroke_linecap=cap,
                         stroke_linejoin=join)))


def arrow_defs(name, color="f-ink2"):
    """A small triangular marker; colour resolved through the token fallback."""
    return (
        '<defs><marker id="%s" viewBox="0 0 8 8" refX="7" refY="4" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        '<path d="M0,1 L7,4 L0,7 z" style="fill:var(--%s, %s)"/></marker></defs>\n'
        % (name, color, TOKEN[color]))


def mline(name, x1, y1, x2, y2, color="f-ink2", sw=1.2, dash=None):
    return ('<line x1="%g" y1="%g" x2="%g" y2="%g" marker-end="url(#%s)" style="%s"/>\n'
            % (x1, y1, x2, y2, name,
               _style(stroke=color, stroke_width="%g" % sw,
                      stroke_dasharray=dash)))


def write_svg(path, body):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)
    return path
