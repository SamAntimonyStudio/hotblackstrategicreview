s=open('index.html').read()
i=s.find('<section class="stage"'); j=s.rfind('</section>')+len('</section>')
head, tail = s[:i], s[j:]
head = head.replace('<title>','<title>Second read · ').replace('Antimony 2026</span><span class="r">Hot Black','Antimony 2026</span><span class="r">Hot Black · Second read')

ATOM = '<svg class="atom" viewBox="0 0 100 100" fill="none"><g stroke="currentColor" stroke-width="2"><ellipse cx="50" cy="50" rx="47" ry="17"/><ellipse cx="50" cy="50" rx="47" ry="17" transform="rotate(60 50 50)"/><ellipse cx="50" cy="50" rx="47" ry="17" transform="rotate(120 50 50)"/></g><circle cx="50" cy="50" r="6" fill="var(--ink)"/><circle cx="97" cy="50" r="3.4" fill="var(--blue)"/><circle cx="26.5" cy="9" r="3.4" fill="var(--coral)"/><circle cx="26.5" cy="91" r="3.4" fill="var(--lilac)"/></svg>'
ATOM_D = ATOM.replace('fill="var(--ink)"','fill="var(--on-dark)"').replace('fill="var(--blue)"','fill="var(--on-dark)"').replace('fill="var(--coral)"','fill="var(--on-dark)"').replace('fill="var(--lilac)"','fill="var(--on-dark)"')
HEAD = '<div class="head"><span>Antimony 2026</span><span class="r">Hot Black &middot; Second read</span></div>'

def slide(inner, cls=""):
    return f'<section class="stage">\n<div class="slide {cls}">\n<div class="pad">\n{HEAD}\n{inner}\n</div>\n</div>\n</section>\n'

def row(tag, title, body, right, color, last=False):
    bb = "" if last else "border-bottom:1px solid var(--line)"
    r = f'<div style="flex:0 0 17cqw;font-size:1.06cqw;line-height:1.3;color:var(--muted)">{right}</div>' if right else ""
    return f'''<div style="display:flex;gap:1.4cqw;align-items:center;padding:.7cqw 0 .7cqw 1.1cqw;border-left:.35cqw solid var(--{color});{bb}">
    <div style="flex:0 0 21cqw"><div class="tag" style="color:var(--muted);margin-bottom:.15cqw">{tag}</div><div style="font-size:1.66cqw;font-weight:700;line-height:1.05">{title}</div></div>
    <div style="flex:1;font-size:1.2cqw;line-height:1.34;color:var(--ink-soft)">{body}</div>{r}
  </div>'''

S=[]

# 1 cover
S.append(slide(f'''
<div class="grow flex between" style="margin-top:1.6cqw">
  <div class="col" style="max-width:66cqw;justify-content:center">
    <div class="flex" style="gap:.8cqw;margin-bottom:1.8cqw">
      <span class="pill pill-pink">A Second Read</span>
      <span class="pill pill-ink">Hot Black</span>
    </div>
    <div class="hero">You already published<br>the evidence.<br>To the wrong audience.</div>
    <div class="lede" style="margin-top:1.8cqw;max-width:54cqw">In July we said the rigour stops at the studio door. We were wrong by one building. It leaves the door, goes to the awards judges, and never comes back.</div>
    <div class="flex" style="gap:.7cqw;margin-top:2.2cqw;flex-wrap:wrap">
      <span class="pill pill-blue">Prepared for Sophie Safrin</span>
      <span class="pill pill-cream">October 2026</span>
      <span class="pill pill-ink">Follows the July read</span>
    </div>
  </div>
  <div class="col" style="align-items:flex-end;justify-content:center">
    <div style="width:16cqw;height:16cqw;color:var(--pink)">{ATOM}</div>
  </div>
</div>
<div class="foot">
  <div class="logo-word-blk" style="width:18cqw;height:4.1cqw"></div>
  <div class="cats"><span>Brand</span><span class="sep">|</span><span>Digital</span><span class="sep">|</span><span>Content</span><span class="sep">|</span><span>Growth</span></div>
</div>'''))

# 2 what changed
S.append(slide('''
<div class="kicker">01 <span class="dot">&middot;</span> Since July</div>
<div class="h1">Three things changed</div>
<div class="lede" style="margin:.85cqw 0 1cqw">None of them came from us asking for a meeting.</div>
<div class="grow col" style="justify-content:center">'''+
row("One","You asked for room","Fair. The July deck was twenty-two slides and a reverse brief, and the right response to that is time. We used ours differently.","What we did instead is on the next slides.","pink")+
row("Two","Asahi went live","Published July 2026. 9,000 sqm, a working laboratory, a portfolio of brands under one roof. Same four fields as ANZ in 2021: who, where, when, how big.","The gap is current, not historical.","blue")+
row("Three","We read your award entries","Better Future Sydney 2022, Melbourne 2022. Public pages. They carry the numbers, the budget, the constraints and the decisions the website leaves out.","This is the slide that changes the diagnosis.","coral",last=True)+
'''</div>'''))

# 3 statement
S.append(slide(f'''
<div class="kicker" style="color:var(--on-dark)">02 <span class="dot">&middot;</span> The correction</div>
<div class="grow flex between" style="align-items:center">
  <div class="statement" style="max-width:74cqw;color:var(--on-dark)">
    You do not have a capture problem. You write the evidence down every time you enter an award. You have a routing problem. It goes to the judges and stops.
  </div>
  <div style="width:16cqw;height:16cqw;color:rgba(249,243,220,.9);flex:none;margin-left:2cqw">{ATOM_D}</div>
</div>''',"bleed-coral"))

# 4 ANZ evidence
S.append(slide('''
<div class="kicker">03 <span class="dot">&middot;</span> The evidence</div>
<div class="h2" style="max-width:82cqw;margin:.6cqw 0 1cqw">ANZ Sydney, in your words.<br>Two audiences, <span class="hl">two different projects</span>.</div>
<div class="lede" style="margin-bottom:1.3cqw">Both are Hot Black's copy. One is on hotblack.design. The other is on betterfutureawards.com, where a client never looks.</div>
<div class="grid g2" style="flex:none;height:21.5cqw">
  <div class="card c-peach">
    <div class="c-lab">What the website says</div>
    <div class="c-title">14 levels of urban-city inspired workspace</div>
    <div class="c-body">Mini city. Client floor. Venture lab. Warm neutral tones. Pocket parks. Lakkari Pitt's carpet. All true, all about the design, and nothing a CFO can forward.</div>
  </div>
  <div class="card c-blue">
    <div class="c-lab">What the award entry says</div>
    <div class="c-title">21 floors consolidated to 14. Executive floors removed. Tight budget. Carpet tiles reclaimed floor to floor.</div>
    <div class="c-body">Furniture reused. Existing stairs, services and floorplates. Environmental graphics instead of a refit. Charopy waste technology. The commercial brief, written by you, for a panel of designers.</div>
  </div>
</div>
<div class="lede" style="margin-top:1.1cqw;max-width:84cqw">Same project. Same author. The version a procurement panel would score is the one they cannot find.</div>'''))

# 5 Sportsbet evidence
S.append(slide('''
<div class="kicker">03 <span class="dot">&middot;</span> The evidence</div>
<div class="h2" style="max-width:82cqw;margin:.6cqw 0 1cqw">The <span class="hl">cleanest commercial brief</span> you have.<br>The site buries it.</div>
<div class="lede" style="margin-bottom:1.3cqw">A merger, more people, the same floorplate. The website leads with home-away-from-home. The award entry leads with what the building had to do.</div>
<div class="grid g3" style="flex:none;height:18cqw">
  <div class="card c-peach">
    <div class="c-lab">The site</div>
    <div class="c-title">Doesn't take itself too seriously</div>
    <div class="c-body">Neutral palette, pops of colour, sporting forms with a mature hand. Every studio's caption.</div>
  </div>
  <div class="card c-blue">
    <div class="c-lab">The award entry</div>
    <div class="c-title">Very little new build. Kitchens retained. A prayer room and a mothers' room.</div>
    <div class="c-body">The podium opened as the townhall floor. Silver, Melbourne 2022. None of it on the site.</div>
  </div>
  <div class="card c-pink">
    <div class="c-lab">The hook</div>
    <div class="c-title">A falcon family that outranked the builder</div>
    <div class="c-body">Thirty years on the facade. Louvres beside the nest. A programme built around nesting season. The best story Hot Black owns, and it lives on an awards site.</div>
  </div>
</div>
<div class="lede" style="margin-top:1.1cqw;max-width:84cqw">The capital argument and the human story were both already written. Neither was published anywhere you own.</div>'''))

# 6 why it changes the cost
S.append(slide('''
<div class="kicker">04 <span class="dot">&middot;</span> Why this matters</div>
<div class="h2" style="max-width:82cqw;margin:.6cqw 0 1cqw">July's plan priced in research.<br><span class="hl">Your archive already did it.</span></div>
<div class="lede" style="margin-bottom:1.3cqw">The Proof Rebuild assumed we would go back to clients, run post-occupancy interviews, and reconstruct the commercial brief from memory. For every awarded project, you have already written it down and the client has already approved it.</div>
<div class="grid g3" style="flex:none;height:17.5cqw">
  <div class="card c-lilac">
    <div class="c-lab">Faster</div>
    <div class="c-title">Six weeks, not a quarter</div>
    <div class="c-body">The brief, constraint and decision exist in your own words for every entered project. Routing, not research.</div>
  </div>
  <div class="card c-blue">
    <div class="c-lab">Easier to clear</div>
    <div class="c-title">The client already signed it off</div>
    <div class="c-body">An award entry goes out with the client's blessing. Republishing the same facts on your site is a conversation, not a negotiation.</div>
  </div>
  <div class="card c-pink">
    <div class="c-lab">Repeatable</div>
    <div class="c-title">You already have the habit</div>
    <div class="c-body">Every future entry becomes the case study and the posts by default. No new discipline to learn, only a second destination for work you already do.</div>
  </div>
</div>'''))

# 7 the test
S.append(slide('''
<div class="kicker">05 <span class="dot">&middot;</span> The test</div>
<div class="h1">We rebuilt three. Nothing was written new.</div>
<div class="lede" style="margin:.85cqw 0 1cqw">ANZ, Sportsbet and Asahi, as case studies and as a month of feed, in your system rather than ours. Every fact traces to your site or your award entry. The links are on the last slide.</div>
<div class="grow col" style="justify-content:center">'''+
row("ANZ Sydney","21 floors became 14. Nobody lost a desk.","Was: 14 levels of urban-city inspired workspace. Now the lease question, the decision to build a city instead of a stack, and the executive floors that went.","Source: Better Future Sydney 2022 entry","pink")+
row("Sportsbet","More people, the same floorplate.","Was: an energised, vibrant HQ. Now the merger, the strategy that set the desk ratio, the building kept, and the falcons.","Source: Melbourne Design Awards 2022 entry","blue")+
row("Asahi","A lab, a marketing floor &amp; a family of brands. One roof.","Was: infusing emotion into the workplace. Now a business built by acquisition, a vertical narrative so no brand had to lose, and a working lab inside an office.","Source: hotblack.design, July 2026","coral",last=True)+
'''</div>'''))

# 8 what's still missing
S.append(slide('''
<div class="kicker">06 <span class="dot">&middot;</span> What is still missing</div>
<div class="h2" style="max-width:82cqw;margin:.6cqw 0 1cqw">Four numbers and one sentence per project.<br><span class="hl">Only you can ask.</span></div>
<div class="lede" style="margin-bottom:1.3cqw">The rebuilt pages carry blue fields, deliberately empty. They are the figures the client holds and the quote only the client can give. Everything else is done.</div>
<div class="grid g3" style="flex:none;height:18cqw">
  <div class="card c-blue">
    <div class="c-lab">ANZ</div>
    <div class="c-title">Attendance against the pre-move benchmark</div>
    <div class="c-body">Plus reuse percentage, client-floor utilisation, and the staff survey delta. The lease question, answered.</div>
  </div>
  <div class="card c-blue">
    <div class="c-lab">Sportsbet</div>
    <div class="c-title">Headcount before and after on 7,700 sqm</div>
    <div class="c-body">Plus base build retained, the desk ratio shift, and the lease not taken. The single strongest line you could publish this year.</div>
  </div>
  <div class="card c-pink">
    <div class="c-lab">Asahi, this month</div>
    <div class="c-title">Sites consolidated and first-quarter attendance</div>
    <div class="c-body">Ask now, while the sponsor is proud of it. In a year it is a month of chasing. This one has a clock on it.</div>
  </div>
</div>'''))

# 9 point of view revised
S.append(slide('''
<div class="kicker">07 <span class="dot">&middot;</span> Our point of view, revised</div>
<div class="h2" style="max-width:82cqw;margin:.6cqw 0 1cqw">Route it. Request it. Repeat it.<br>The proof system is <span class="hl">mostly plumbing</span>.</div>
<div class="lede" style="margin-bottom:1.4cqw">July's answer was a proof system built from scratch. The sharper version is three habits laid over something you already do.</div>
<div class="grid g3" style="flex:none;height:17.1cqw">
  <div class="card c-peach">
    <div class="c-lab">Route</div>
    <div class="c-title">Award entry to site to feed</div>
    <div class="c-body">Every entered project gets the five-row case study and the carousel. The awards copy is the first draft. The judges stop being the only readers.</div>
  </div>
  <div class="card c-lilac">
    <div class="c-lab">Request</div>
    <div class="c-title">The client's number, at handover</div>
    <div class="c-body">Four figures and a sentence, asked while the sponsor is proud. Built into the close-out, not chased a year later.</div>
  </div>
  <div class="card c-pink">
    <div class="c-lab">Repeat</div>
    <div class="c-title">The entry writes the content</div>
    <div class="c-body">Change nothing about how you enter awards. Change where the entry goes afterwards. One habit, two destinations.</div>
  </div>
</div>'''))

# 10 system revised
S.append(slide('''
<div class="kicker">08 <span class="dot">&middot;</span> The system, reordered</div>
<div class="h1">Same four workstreams. Prove moves first.</div>
<div class="lede" style="margin:.85cqw 0 1cqw">In July, Position came first because we thought the evidence had to be built. It already exists, so the fastest credible move is to publish it.</div>
<div class="grow col" style="justify-content:center">'''+
row("One","Prove","Twelve workplace projects rebuilt from their award entries and the site. Blue fields requested from the six clients most likely to answer. Feed rebuilt in the same pass.","Was: workstream two. Now first, because the material is in hand.","pink")+
row("Two","Position","Sector doors built for the buyer. Craft and evidence together, at a scale no competing studio has managed.","Unchanged.","blue")+
row("Three","Publish","An owned home for the argument, Sophie's channel carrying it, and the award-to-feed routine your team runs.","Simplified: the routine replaces the content system.","coral")+
row("Four","Convert","A diagnostic and a proof kit, so the pitch is assembled rather than rebuilt.","Unchanged.","lilac",last=True)+
'''</div>'''))

# 11 investment
S.append(slide('''
<div class="kicker">09 <span class="dot">&middot;</span> Investment</div>
<div class="h1">Same ranges. A faster first ninety days.</div>
<div class="lede" style="margin:.85cqw 0 1.2cqw">The July numbers hold. What changed is what the Foundation delivers in the first six weeks, because your archive did the research. AUD, excluding GST, ranges not quotes.</div>
<div class="grid g3" style="flex:none;height:23.5cqw">
  <div class="card c-peach">
    <div class="c-lab">Foundation</div>
    <div class="c-title">The Proof Rebuild</div>
    <div style="font-size:3.2cqw;font-weight:800;line-height:1;letter-spacing:-.03em;margin:.55cqw 0 .35cqw">$34k</div>
    <div class="c-body">Now twelve case studies rather than six, the feed rebuilt alongside, and the blue-field requests drafted and sent. Six weeks. Closes the scoreable gap faster than July promised.</div>
  </div>
  <div class="card c-pink">
    <div class="c-lab">Recommended</div>
    <div class="c-title">The Authority Engine</div>
    <div style="font-size:3.2cqw;font-weight:800;line-height:1;letter-spacing:-.03em;margin:.55cqw 0 .35cqw">$68k <span style="font-size:1.35cqw;font-weight:600;letter-spacing:0">+ $6.5k/mo</span></div>
    <div class="c-body">Everything in Foundation, plus the owned platform, Sophie's channel, and the award-to-feed routine built into how you already enter awards. The one that answers what you asked.</div>
  </div>
  <div class="card c-lilac">
    <div class="c-lab">Market leader</div>
    <div class="c-title">The Instrument</div>
    <div style="font-size:3.2cqw;font-weight:800;line-height:1;letter-spacing:-.03em;margin:.55cqw 0 .35cqw">$110k <span style="font-size:1.35cqw;font-weight:600;letter-spacing:0">+ $9.5k/mo</span></div>
    <div class="c-body">Everything above, plus your own named diagnostic. The only version that becomes an asset rather than a campaign.</div>
  </div>
</div>'''))

# 12 decision path
S.append(slide('''
<div class="kicker">10 <span class="dot">&middot;</span> Decision path</div>
<div class="h1">Three things, in order</div>
<div class="lede" style="margin:.85cqw 0 1cqw">The first two cost nothing and do not need us.</div>
<div class="grow col" style="justify-content:center">'''+
row("Step one &middot; this week","Read the three","samantimonystudio.github.io/hotblackstrategicreview/evidence and /feed. Put them beside the live pages. If the argument does not hold, tell us where.","","pink")+
row("Step two &middot; this week","Ask Asahi for the number","Sites consolidated and first-quarter attendance. One email to the project sponsor while the move is three months old. Whatever happens with us, do this.","","blue")+
row("Step three &middot; when ready","Half a day on the other twenty","We pull the award entries for every project you have ever entered, agree which six clients to ask, and scope the Foundation properly.","","coral",last=True)+
'''</div>'''))

# 13 close
S.append(slide(f'''
<div class="grow flex between" style="align-items:center">
  <div class="col" style="max-width:70cqw;justify-content:center">
    <div class="hero">Different as usual.<br>Everywhere except<br>where buyers look.</div>
    <div class="lede" style="margin-top:1.8cqw;max-width:52cqw">The judges have read your best work for years. Your clients' procurement panels never have. Same words. Second destination.</div>
  </div>
  <div class="col" style="align-items:flex-end;justify-content:center">
    <div style="width:16cqw;height:16cqw;color:var(--pink)">{ATOM}</div>
  </div>
</div>
<div class="foot">
  <div class="logo-word-blk" style="width:18cqw;height:4.1cqw"></div>
  <div class="cats"><span>Antimony Studio</span><span class="sep">|</span><span>St Kilda, Melbourne</span><span class="sep">|</span><span>October 2026</span></div>
</div>'''))

import os
os.makedirs('second-read',exist_ok=True)
open('second-read/index.html','w').write(head+"\n".join(S)+tail)
print("slides",len(S))
