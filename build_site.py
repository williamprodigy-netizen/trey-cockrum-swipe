#!/usr/bin/env python3
"""Build the PB Trading swipe site. Run: python3 build_site.py"""
import sys, os, glob, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/TREY_COCKRUM_Swipe")


def _probe(p):
    try:
        return int(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True, timeout=60).stdout.strip()))
    except Exception:
        return 0


def video_library():
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/**/*.mp4"), recursive=True)):
        mb = os.path.getsize(p) / 1e6
        rows.append((os.path.basename(p), _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     ROLES.get(os.path.basename(p), "")))
    return rows


ROLES = {}

CONFIG = {
 "SITE": "Trey Cockrum — Kaizen",
 "CREATOR": "Trey Cockrum",
 "ADS_KEY": "trey_cockrum",
 "FUNNEL_IDS": ["F065"],
 "CAPTURED": "18 August 2026",
 "REPO": REPO,
 "PACKAGE": "~/Downloads/Swipes/TREY_COCKRUM_Swipe",
 "BLURB": "Placing <b>Christian men</b> into high-ticket sales roles. The whole funnel is built on one "
          "promise the rest of this file cannot make: <b>you get the founder on the call, not a setter.</b>",
 "PAGES": [("index.html","Overview"),("analysis.html","Analysis"),
              ("transcripts.html","Transcripts"),("videos.html","Video library")],
 "STATS": [("ICP","Christian men in sales"),("Placed claim","130+ men trained + placed"),
           ("Booking","OnceHub"),("Call promise","<b>Trey himself, not a team member</b>"),
           ("Ads found","<b>none</b>"),("Stack","ClickFunnels + Wistia + Typeform"),
           ("Push","PushCrew"),("Price","never stated")],
 "OFFER": [("Promise","&ldquo;We help <b>Christian men in sales</b> earn 6-figures online in this "
                      "underground, mission-driven industry&hellip; <b>without sacrificing their "
                      "work-life-balance</b>&rdquo;"),
   ("Proof scale","&ldquo;<b>130+ men trained + placed</b> &mdash; proof &amp; details inside&rdquo;"),
   ("Named results","G&uuml;rkan $20k&rarr;$250k/m (later $1.5M/m) · Jimmy $0&rarr;$50k/m in 45 days · Frederick $40k&rarr;$200k/m"),
   ("The differentiator","<b>&ldquo;Grab a call with me! (Not a team member, actually me.)&rdquo;</b>"),
   ("Path","Opt-in &rarr; Kaizen results page &rarr; OnceHub booking &rarr; thank-you with a confirmation gate"),
   ("Price","<b>Never stated</b>")],
 "FINDINGS": [
  ("&ldquo;Not a team member, actually me&rdquo; &mdash; he sells the absence of a setter",
   "The booking CTA appears repeatedly as <b>&ldquo;Grab a call with me! (Not a team member, actually "
   "me.)&rdquo;</b> Every competitor in this file routes to a setter, and every prospect knows it. He "
   "turns that shared knowledge into the differentiator, and the parenthetical does all the work. "
   "<b>We cannot copy this &mdash; we run setters &mdash; but it names exactly what our leads suspect "
   "when they book.</b>"),
  ("The ICP is a faith, not a demographic",
   "&ldquo;Christian men in sales.&rdquo; Not an age, not an income band. It selects on identity and "
   "values, which makes the &ldquo;mission-driven industry&rdquo; framing land as a moral fit rather "
   "than a job. Same structural move as Suprahuman's &ldquo;former athletes&rdquo; &mdash; "
   "<b>identity beats demography</b>, twice in one swipe file."),
  ("The thank-you page threatens to cancel the appointment",
   "<i>&ldquo;Final step: watch this short video to see how to secure your appointment! "
   "<b>(It may be canceled otherwise.)</b>&rdquo;</i> Watching is not encouraged, it is a condition of "
   "keeping the slot. Her Closing Academy runs the identical mechanic. <b>Sixth competitor putting "
   "work between booking and attending.</b>"),
  ("He puts a live sales call on the thank-you page",
   "&ldquo;How does this industry work? <b>(See a live sales call lower on this page.)</b>&rdquo; "
   "Showing the actual job being done, to someone who has just booked, answers &ldquo;what would I "
   "even be doing&rdquo; better than any description. Multiple Wistia videos sit on that page."),
  ("No ads, anywhere",
   "Searched the ad index by landing-page domain (<code>treycockrum.com</code>, zero results) and by "
   "brand name (returns Trey McBride the NFL player, Wawa, DailyOM &mdash; the documented failure mode "
   "of free-text brand queries). <b>No evidence he is running paid.</b> The funnel is built for organic "
   "&mdash; one page is literally named <code>kaizen-ig-bio</code>, an Instagram bio link. Caveat: the "
   "index is not exhaustive and absence is weaker evidence than presence."),
 ],
 "FUNNEL": [
  ("Opt-in","treycockrum.com/optin-6353651917...",'&ldquo;Christian men in sales&hellip; 130+ men trained + placed.&rdquo; Wistia VSL. Meta Pixel, GA, ClickFunnels, Typeform, PushCrew, Intercom.'),
  ("Kaizen results","treycockrum.com/kaizen-ig-bio17382...",'<span class="tag good">the mechanic</span> Named results with real numbers. OnceHub embed. &ldquo;Not a team member, actually me.&rdquo; <b>Named for an IG bio link.</b>'),
  ("Thank-you","treycockrum.com/ty-page17477...",'&ldquo;Final step&hellip; <b>it may be canceled otherwise</b>.&rdquo; Live sales call recording + FAQ. Multiple Wistia videos.'),
 ],
 "TRANSCRIPT_GROUPS": [],
 "SLIDE_PAGES": [],
 "ANALYSIS": """
<div class="note"><b>Will asked whether he has ads. He does not &mdash; not that we can find.</b>
Zero results for <code>treycockrum.com</code> in the ad index, and his money page is literally named
<code>kaizen-ig-bio</code>. This is an organic, Instagram-fed funnel.</div>

<h2 class="sec">The one line worth the whole capture</h2>
<p><b>&ldquo;Grab a call with me! (Not a team member, actually me.)&rdquo;</b></p>
<p>Every high-ticket prospect has learned that &ldquo;book a call&rdquo; means a setter reading a
script. Trey does not argue that setters are bad &mdash; he just removes the doubt, in a
parenthetical, and lets the reader draw the conclusion. It is the single highest-leverage sentence in
this capture and it costs nothing to write.</p>
<p><span class="tag">READ</span> We run setters and should keep running them. But this names the exact
suspicion our booked leads carry into the call, and it is worth deciding what <i>our</i> honest
version of that reassurance sounds like &mdash; who they will speak to, and why that person is the
right one.</p>

<h2 class="sec">Identity as ICP, for the second time in this file</h2>
<div class="tablewrap"><table>
<tr><th>Who</th><th>ICP</th><th>What it selects on</th></tr>
<tr><td>Suprahuman</td><td>&ldquo;Soft and out of shape <b>former athletes</b>&rdquo;</td><td>Who you used to be</td></tr>
<tr><td><b>Trey Cockrum</b></td><td>&ldquo;<b>Christian men</b> in sales&rdquo;</td><td>What you believe</td></tr>
<tr><td>Viral Coach</td><td>Local business owners</td><td>Demography &mdash; and it needs 12 proof cards to survive it</td></tr>
</table></div>
<p style="margin-top:12px">The two identity-led funnels need far less proof to be believed, because
the prospect has already self-selected before reading a number. <b>Ours is demographic.</b></p>

<h2 class="sec">The results page is unusually specific</h2>
<p>&ldquo;G&uuml;rkan Ordueri &mdash; $20k/m to $250k/m <i>(eventually $1.5M/m after this
interview)</i>&rdquo;. The parenthetical update is the tell: it says the interview is old and the
student kept growing after it, which is a claim you can only make if the relationship was real.
&ldquo;Jimmy &mdash; $0 to $50k/m in 45d&rdquo; and &ldquo;Frederick &mdash; $40k/m to $200k/m&rdquo;
follow the same before&rarr;after shape. <span class="tag">EVIDENCE</span> These are his claims, on
his page, recorded as claims.</p>

<h2 class="sec">The stack says organic</h2>
<p>ClickFunnels + Wistia + Typeform + OnceHub + Intercom + <b>PushCrew</b> + Meta Pixel + GA. The Meta
Pixel is present but no ads are running against it &mdash; consistent with a pixel left installed from
past testing, or warming an audience for later. PushCrew (browser push) matters more here: for an
organic funnel with no ad retargeting budget, push is the only free way to reach a visitor twice.
<b>Dlucs runs PushCrew too</b> &mdash; the only two in the file, and both are organic-led.</p>

<h2 class="sec">What is missing</h2>
<ul><li><b>The Wistia videos are identified but not pulled</b> &mdash; the opt-in VSL
(<code>j3eyxzdezq</code>) and three on the thank-you page, including the live sales call.</li>
<li><b>No price</b> anywhere in the funnel.</li>
<li><b>No emails</b> &mdash; opt-in never submitted.</li>
<li><b>No ad library to analyse</b>, per the finding above.</li></ul>
""",
}
CONFIG['VIDEOS'] = video_library()

if __name__ == '__main__':
    build(CONFIG)
