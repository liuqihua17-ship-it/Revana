"""
Demo data for Revana — pre-loaded Stanley vs Hydro Flask analysis.
  - 247 reviews fetched  |  189 trusted (76.5%)  |  58 filtered (23.5%)
  - Health score: 74/100
  - Amazon public totals (67,842 / 28,431) refer to all reviews on Amazon.
"""

import pandas as pd
from datetime import datetime, timedelta


def _date(days_ago):
    d = datetime.now() - timedelta(days=days_ago)
    return {"utc": d.strftime("%Y-%m-%dT%H:%M:%S.000Z"), "raw": d.strftime("%B %d, %Y")}


# ─────────────────────────────────────────────────────────────────────────────
# STANLEY — 247 RAW REVIEWS (R001-R189 trusted + F001-F058 filtered)
# ─────────────────────────────────────────────────────────────────────────────

STANLEY_REVIEWS_RAW = [
    {"id":"R001","rating":1,"title":"Lid leaks every single time","body":"I cannot overstate how frustrated I am with this lid. Every time I tilt my cup even slightly — getting into the car, reaching across the seat — water pours out. I've soaked my work bag twice and ruined a laptop keyboard. For a $45 cup marketed as 'cupholder compatible,' this is completely unacceptable. I've tried adjusting the position of the straw and the lid lock and nothing helps. Returning this immediately.","verified_purchase":True,"helpful_votes":312,"reviewer_name":"Jennifer M.","date":_date(12)},
    {"id":"R002","rating":5,"title":"Best tumbler I've ever owned","body":"I've been through six different tumblers in the last three years — Yeti, Hydro Flask, Contigo, and a few store brands — and the Stanley Quencher beats all of them. The thermal retention is genuinely exceptional. I put ice in at 7am and still have ice at 6pm in a 90-degree office. The cupholder fit is perfect for both my Honda Civic and my Toyota Camry. The handle makes it easy to carry without looking clumsy. Worth every penny.","verified_purchase":True,"helpful_votes":287,"reviewer_name":"Rachel T.","date":_date(18)},
    {"id":"R003","rating":2,"title":"Mold inside the straw after two weeks","body":"I wash this cup every single day. I use the cleaning brush that came with it. I let it air dry completely before capping it. Two weeks in, I pulled the straw out for deep cleaning and found black mold in the crevice where the straw meets the lid. The gap between the straw and lid is too tight to clean properly — the brush doesn't reach. Stanley should redesign the straw seal. This is a health concern, not just an aesthetic one.","verified_purchase":True,"helpful_votes":198,"reviewer_name":"Marcus D.","date":_date(25)},
    {"id":"R004","rating":5,"title":"Converted my entire office","body":"I bought this for myself six months ago and now four of my coworkers have one. The color selection is genuinely fun — I have the Fog color and get compliments constantly. But more than aesthetics, it just works. Cold stays cold, the handle is sturdy, and the flip straw is smooth. I've dropped it twice on concrete and there's not a single dent. The only thing I'd change is adding a second lid lock position but that's minor.","verified_purchase":True,"helpful_votes":156,"reviewer_name":"Ashley K.","date":_date(31)},
    {"id":"R005","rating":1,"title":"Paint chips within 3 months","body":"I paid $45 for this tumbler specifically because I wanted something that would look good long-term. Three months later the powder coat is chipping at the base and around the handle attachment points. I don't throw this cup or use it roughly — it sits on my desk and goes in my cupholder. For a premium-priced product this is embarrassing. Hydro Flask has had my other bottle for two years and the paint looks brand new.","verified_purchase":True,"helpful_votes":221,"reviewer_name":"Daniel W.","date":_date(8)},
    {"id":"R006","rating":4,"title":"Great except for the lid issue everyone mentions","body":"I read all the reviews before buying so I knew about the lid leak problem going in. In practice it only leaks if you tilt it past about 30 degrees, which you can mostly avoid. The thermal performance is outstanding — genuinely the best I've tested. The cupholder fit is perfect. The handle is well-positioned. If Stanley fixes the lid seal I'll bump this to five stars without hesitation.","verified_purchase":True,"helpful_votes":134,"reviewer_name":"Priya S.","date":_date(44)},
    {"id":"R007","rating":5,"title":"Completely replaced my water bottle habit","body":"I used to forget to drink water entirely. Since I got the Stanley Quencher I drink at least 80oz a day because I always have it with me. It fits in every cupholder I've tried including the narrow ones in my older Jeep. The straw is the right length. I've put it through the dishwasher weekly for four months and it looks brand new. The handle is the detail I didn't know I needed.","verified_purchase":True,"helpful_votes":201,"reviewer_name":"Taylor B.","date":_date(55)},
    {"id":"R008","rating":1,"title":"Ruined my car seat","body":"The lid leaked while it was sitting in my cupholder on a highway drive. I didn't even touch it — road vibration was enough to open the straw and let water pool around the base. Twelve ounces of water soaked through my leather seat. I contacted Stanley customer service and they offered me a 20% discount on my next purchase. I don't want a discount, I want a lid that doesn't leak while sitting still. Never buying Stanley again.","verified_purchase":True,"helpful_votes":445,"reviewer_name":"Chris H.","date":_date(6)},
    {"id":"R009","rating":3,"title":"Good product, some real problems worth knowing","body":"I've had the Stanley Quencher for about four months. The cold retention is excellent and the handle design is comfortable. The cupholder fit is genuinely good for most car models. That said the lid does leak if you tilt it, the straw area develops a slight odor if not cleaned obsessively, and the paint on mine has very minor chipping near the bottom. It's a good product but not a perfect one.","verified_purchase":True,"helpful_votes":88,"reviewer_name":"Kevin L.","date":_date(72)},
    {"id":"R010","rating":5,"title":"Worth every cent — the handle alone changes everything","body":"I've seen the comments about the lid leaking and it has not been my experience at all. I use mine daily including in the car and I've never had a leak. What I can say is that the handle makes this fundamentally different from every other tumbler I've tried. I can grab it one-handed without fumbling. I can hook it on a bag strap. The thermal performance is also genuinely excellent.","verified_purchase":True,"helpful_votes":167,"reviewer_name":"Megan F.","date":_date(89)},
    {"id":"R011","rating":2,"title":"Customer service was disappointing","body":"The cup itself is fine. What bothered me was Stanley's response when I emailed about the lid leaking. They sent a form response, asked me to submit a photo through a web portal that didn't work on mobile, and then went silent for two weeks. When I followed up they offered a replacement lid that took three weeks to arrive and didn't fix the problem. Hydro Flask replaced a faulty cap same-day, no questions asked.","verified_purchase":True,"helpful_votes":93,"reviewer_name":"Sandra P.","date":_date(101)},
    {"id":"R012","rating":5,"title":"The color strategy is brilliant and the product backs it up","body":"I'll admit I bought mine initially because the color was limited edition. But six months later I'm still using it every single day because it's genuinely the best tumbler I've tested. The ice retention is real. The cupholder fit is exactly right. The handle makes one-handed carrying natural. My daughter bought one after seeing mine and then my sister-in-law did the same.","verified_purchase":True,"helpful_votes":122,"reviewer_name":"Lisa R.","date":_date(115)},
    {"id":"R013","rating":1,"title":"Third one I've bought — all have the same lid defect","body":"I gave the first one the benefit of the doubt. Bought a second. Same lid leak. Bought a third from a different retailer. Still leaks. This is not a defective unit problem — it's a design flaw that Stanley has not fixed across multiple production runs. I'm switching to the Hydro Flask Wide Mouth which has no such issues.","verified_purchase":True,"helpful_votes":378,"reviewer_name":"Andrea C.","date":_date(14)},
    {"id":"R014","rating":4,"title":"Excellent thermal performance, minor complaints","body":"The thermal retention on this tumbler is legitimately excellent. I tested it against my Yeti Rambler and the Stanley kept ice longer by about 45 minutes in a warm room. The cupholder compatibility is as advertised. The handle is well-balanced. My only real complaint is that the straw develops a slight smell after a few weeks if you drink anything other than water.","verified_purchase":True,"helpful_votes":76,"reviewer_name":"Brian N.","date":_date(130)},
    {"id":"R015","rating":5,"title":"The only cup I've used every single day for a year","body":"I bought this fourteen months ago. I've used it every single day. It goes in the dishwasher weekly. It's been dropped on pavement twice. The handle has a small scratch and the base has minor scuffs from use but other than that it looks and performs like it did day one. The ice retention is still excellent. I will buy another one the day this one breaks.","verified_purchase":True,"helpful_votes":244,"reviewer_name":"Nicole J.","date":_date(145)},
    {"id":"R016","rating":1,"title":"Lid leaks, destroyed my work documents","body":"Carrying this in my work bag and the lid leaked. Soaked through my notebook and two printed reports. The seal on this lid is not adequate for a product marketed as portable drinkware. Do not carry this in a bag with anything important.","verified_purchase":True,"helpful_votes":289,"reviewer_name":"Tom A.","date":_date(9)},
    {"id":"R017","rating":5,"title":"Best gift I've ever given","body":"I bought five of these as Christmas gifts and every single recipient has messaged me saying it's the best gift they received. The colors are beautiful, the quality is obvious when you hold it, and the functionality is exactly as described. One friend said she's drunk twice as much water since getting it.","verified_purchase":True,"helpful_votes":143,"reviewer_name":"Emily S.","date":_date(200)},
    {"id":"R018","rating":3,"title":"Perfectly average — good but not revolutionary","body":"Cold stays cold for a long time — that's real. The handle is nice. The cupholder fit works. The lid leaks if you're not careful. The straw smell is annoying. It's a $45 cup that performs like a $35 cup. I like it but I wouldn't call it life-changing the way the reviews suggest.","verified_purchase":True,"helpful_votes":67,"reviewer_name":"Patrick M.","date":_date(88)},
    {"id":"R019","rating":2,"title":"Paint chipping at 4 months","body":"For a premium-priced tumbler the paint durability is disappointing. Chipping started at the base rim and around the handle rivets at about four months. Normal use — desk, cupholder, occasional hand carry. Not acceptable at this price point.","verified_purchase":True,"helpful_votes":112,"reviewer_name":"Grace K.","date":_date(22)},
    {"id":"R020","rating":5,"title":"Finally a cup I don't lose interest in","body":"The viral color releases are genius. I have three. My friends have them. But completely aside from the social aspect — it's a legitimately excellent product. Holds ice all day, fits my cupholder perfectly, the handle is a genuine practical improvement over handleless tumblers.","verified_purchase":True,"helpful_votes":198,"reviewer_name":"Hannah W.","date":_date(165)},
    {"id":"R021","rating":1,"title":"Lid mechanism is a design failure","body":"The flip straw mechanism is poorly engineered. The locking position is not secure enough to prevent accidental opening. Any pressure on the flip cover — from a bag, from setting it down wrong — and it pops open. Combined with the tilt-leak issue this cup is essentially uncontained liquid waiting to happen if you carry it anywhere.","verified_purchase":True,"helpful_votes":267,"reviewer_name":"Robert F.","date":_date(33)},
    {"id":"R022","rating":5,"title":"My gym bag essential for two years","body":"I've had mine for two years. Gym every morning, commute, work, home. Dishwasher weekly. Zero degradation in thermal performance. Handle still solid. Lid still works correctly. I replaced the straw once after chewing through it and the replacement was easy to find and cheap. This is what a durable premium product looks like.","verified_purchase":True,"helpful_votes":183,"reviewer_name":"Maria G.","date":_date(730)},
    {"id":"R023","rating":4,"title":"Great product, lid needs an engineering revision","body":"Five stars for thermal performance and handle design. Four stars overall because the lid seal is noticeably less secure than my Yeti at similar tilt angles. If you primarily use this at a desk or sitting upright you'll never notice. The cup itself is excellent.","verified_purchase":True,"helpful_votes":54,"reviewer_name":"James L.","date":_date(210)},
    {"id":"R024","rating":2,"title":"Straw mold is a real issue and Stanley knows it","body":"There are hundreds of reviews about mold in the straw crevice. Stanley has not fixed it. The design creates a gap that traps moisture and organic material that a standard brush can't reach. I now disassemble the entire straw and lid and soak everything in diluted white vinegar weekly. That's too much maintenance for a $45 cup.","verified_purchase":True,"helpful_votes":156,"reviewer_name":"Laura B.","date":_date(60)},
    {"id":"R025","rating":5,"title":"Converted from Hydro Flask and never looking back","body":"I was loyal to Hydro Flask for three years. My coworker convinced me to try the Stanley. The handle alone is worth the switch. The cupholder fit is better for my car. The color options are better. Thermal performance is comparable. The lid is the one area Hydro Flask wins but it's manageable.","verified_purchase":True,"helpful_votes":91,"reviewer_name":"Catherine P.","date":_date(280)},
    {"id":"R026","rating":1,"title":"Spilled an entire cup on myself while driving","body":"Highway driving, slight curve, cup in cupholder. Lid opened from vibration and road tilt. Full 40oz of water on my lap while driving 70mph. This is a safety issue, not just an inconvenience. The lid lock on this product is not adequate.","verified_purchase":True,"helpful_votes":521,"reviewer_name":"Steven R.","date":_date(17)},
    {"id":"R027","rating":5,"title":"The viral moment was earned — it's actually that good","body":"I was skeptical of the TikTok hype. I assumed it was a mediocre product with great marketing. I was wrong. It genuinely holds ice better than anything I've owned. The form factor with the handle is genuinely more practical than handleless bottles. The cupholder fit is precisely engineered. This product earned its moment.","verified_purchase":True,"helpful_votes":302,"reviewer_name":"Alexis T.","date":_date(340)},
    {"id":"R028","rating":3,"title":"Good for desk use, risky for commuting","body":"At my desk this cup is perfect. Cold all day, easy to sip, looks great. The moment I put it in my car bag I get anxious about leaking. That context-dependence is frustrating for something marketed as an everyday carry product.","verified_purchase":True,"helpful_votes":78,"reviewer_name":"Diana M.","date":_date(55)},
    {"id":"R029","rating":4,"title":"Excellent cup, wish I'd bought the 30oz instead","body":"The 40oz is genuinely large — I underestimated how much space it takes up. The thermal performance and handle design are excellent. I just have lid-hold anxiety when carrying it in crowded spaces. That's a preference thing, not a product defect.","verified_purchase":True,"helpful_votes":43,"reviewer_name":"Ryan C.","date":_date(190)},
    {"id":"R030","rating":2,"title":"Not worth the hype at this price","body":"I expected something exceptional based on the reviews and price. What I got is a decent tumbler with a known lid defect, moderate paint durability, and straw maintenance requirements that other brands at lower price points don't have. If this were $25 I'd give it four stars. At $45 the lid and paint issues are dealbreakers.","verified_purchase":True,"helpful_votes":134,"reviewer_name":"Michelle H.","date":_date(40)},
    {"id":"R031","rating":5,"body":"My kids have matching Stanleys now and they drink so much more water. The color options make it fun and the durability means I'm not replacing them constantly. Best purchase I made this year for the family.","title":"Kids love them","verified_purchase":True,"helpful_votes":76,"reviewer_name":"Susan V.","date":_date(95)},
    {"id":"R032","rating":1,"body":"Lid cracked at the hinge after four months of normal use. Not dropped, not stressed — the plastic just fatigued and cracked. A $45 cup should have a lid that lasts more than four months.","title":"Lid cracked at hinge","verified_purchase":True,"helpful_votes":88,"reviewer_name":"Mark T.","date":_date(125)},
    {"id":"R033","rating":5,"body":"I'm a nurse and I carry this through 12-hour shifts. Starts cold, stays cold, the handle means I can grab it quickly between patients, and it survives being set down hard on counters. Exactly what I need.","title":"Perfect for long shifts","verified_purchase":True,"helpful_votes":211,"reviewer_name":"Nurse_Kelly","date":_date(160)},
    {"id":"R034","rating":3,"body":"The cup does what it claims — keeps drinks cold for a long time. I'm docking two stars because the straw smell after coffee use is impossible to eliminate and the paint on my lid is already showing wear at six months.","title":"Works well, some durability issues","verified_purchase":True,"helpful_votes":52,"reviewer_name":"Joe B.","date":_date(185)},
    {"id":"R035","rating":1,"body":"I've cleaned this lid every single day for two months — full disassembly, brush cleaning, air dry — and it still has a faint sour smell that transfers to my water. I've replaced the straw. Still happens. The lid material is absorbing odors and there's no fix.","title":"Persistent odor cannot be eliminated","verified_purchase":True,"helpful_votes":143,"reviewer_name":"Tina F.","date":_date(62)},
    {"id":"R036","rating":5,"body":"Four years into Stanley ownership across three different models and the quality has been consistent. The Quencher is the best of the line because the handle finally makes it practical to carry. Thermal performance has never disappointed.","title":"Four year Stanley customer","verified_purchase":True,"helpful_votes":167,"reviewer_name":"Charles W.","date":_date(1200)},
    {"id":"R037","rating":2,"body":"Paint job chipped at three different points within five months. Handle attachment, base rim, and a small spot on the body. Normal use, no impacts. Premium pricing should come with premium finish durability.","title":"Paint durability is below premium standard","verified_purchase":True,"helpful_votes":98,"reviewer_name":"Angela D.","date":_date(150)},
    {"id":"R038","rating":5,"body":"Replaced my Yeti Rambler with this and the only thing I miss is the slightly more secure lid. Everything else — thermal performance, handle convenience, cupholder fit, color options — the Stanley wins or ties.","title":"Better than my Yeti in most ways","verified_purchase":True,"helpful_votes":134,"reviewer_name":"Brandon S.","date":_date(240)},
    {"id":"R039","rating":4,"body":"This is my third Stanley and each one has been reliable. Cold retention is consistently excellent. The handle makes a real daily difference. The only reason it's not five stars is the lid seal — I've learned to tilt-test every morning before leaving the house.","title":"Reliable, just manage the lid","verified_purchase":True,"helpful_votes":61,"reviewer_name":"Fiona M.","date":_date(310)},
    {"id":"R040","rating":1,"body":"The lid leaked on my school laptop. Screen is damaged. I'm a college student and this is a significant financial loss. Stanley's warranty process is long and I'm not confident it covers consequential damage. Very disappointed.","title":"Leaked on my laptop — significant damage","verified_purchase":True,"helpful_votes":398,"reviewer_name":"Student_Alex","date":_date(21)},
    {"id":"R041","rating":5,"body":"I work outdoors in Texas summers. This cup keeps ice from 6am through my entire shift. No other cup I've tried comes close. The handle means I can hook it on my belt loop or bag. The Stanley Quencher is genuinely engineered for real use.","title":"Works in Texas heat — genuinely","verified_purchase":True,"helpful_votes":287,"reviewer_name":"Carlos R.","date":_date(270)},
    {"id":"R042","rating":3,"body":"Good product let down by one design flaw: the straw attachment point cannot be cleaned adequately with any brush I've found. Three months in it has a smell I can't remove. The thermal performance and handle are excellent. Just fix the straw design.","title":"Great cup, unfixable straw issue","verified_purchase":True,"helpful_votes":73,"reviewer_name":"Patricia N.","date":_date(92)},
    {"id":"R043","rating":5,"body":"My husband bought me this after I mentioned wanting one. I've had it eight months and it's the first thing I grab every morning. Holds ice all day during my commute and desk work. The Frost color is gorgeous and still looks new.","title":"Eight months and still perfect","verified_purchase":True,"helpful_votes":112,"reviewer_name":"Vanessa O.","date":_date(245)},
    {"id":"R044","rating":2,"body":"The lid fails in a specific way: if you set the cup down and the flip lever is slightly open, any tilt causes a slow leak. This isn't obvious in normal use and I've had slow leaks drain into my bag multiple times before I understood the exact failure mode.","title":"Subtle lid failure mode ruins bags","verified_purchase":True,"helpful_votes":189,"reviewer_name":"Derek L.","date":_date(48)},
    {"id":"R045","rating":5,"body":"I've gifted six of these to family members and received zero complaints. Every person uses theirs daily. The thermal performance is consistently excellent. The handle is universally loved. This is a product that genuinely does what it says.","title":"Gifted six — zero complaints","verified_purchase":True,"helpful_votes":203,"reviewer_name":"Janet K.","date":_date(360)},
    {"id":"R046","rating":4,"body":"Good cup. Cold stays cold. Handle is useful. Wish the lid locked more securely.","title":"Solid but lid could be better","verified_purchase":True,"helpful_votes":12,"reviewer_name":"User_John","date":_date(50)},
    {"id":"R047","rating":5,"body":"Love love love this cup. Have had it six months and it's my daily driver. Gets so many compliments on the color.","title":"Love it","verified_purchase":True,"helpful_votes":8,"reviewer_name":"Sarah Q.","date":_date(180)},
    {"id":"R048","rating":1,"body":"Lid leaks. Paint chips. Customer service unhelpful. Not worth the premium price. Going back to Hydro Flask.","title":"Disappointed","verified_purchase":True,"helpful_votes":34,"reviewer_name":"Will E.","date":_date(35)},
    {"id":"R049","rating":3,"body":"It's okay. The thermal retention is good. The handle is nice. The lid makes me nervous in the car. For the price I expected more robust engineering.","title":"Good but not great","verified_purchase":True,"helpful_votes":19,"reviewer_name":"Carol F.","date":_date(75)},
    {"id":"R050","rating":5,"body":"Best cup I've ever had. Keeps drinks cold all day. Perfect for the gym and commute. The handle makes a huge difference.","title":"Best cup ever","verified_purchase":True,"helpful_votes":27,"reviewer_name":"Ryan M.","date":_date(110)},
    {"id":"R051","rating":2,"body":"Paint started chipping after just two months. Very disappointed with the finish quality on a $45 cup.","title":"Paint chipped at 2 months","verified_purchase":True,"helpful_votes":45,"reviewer_name":"Ellen S.","date":_date(65)},
    {"id":"R052","rating":5,"body":"My entire book club has Stanleys now. We coordinate colors. The thermal performance is excellent. Love the handle design.","title":"Book club favorite","verified_purchase":True,"helpful_votes":88,"reviewer_name":"Donna R.","date":_date(220)},
    {"id":"R053","rating":1,"body":"Lid leaked while in my briefcase. Damaged my iPad. Stanley's warranty process is frustratingly slow.","title":"Leaked on my iPad","verified_purchase":True,"helpful_votes":267,"reviewer_name":"Frank T.","date":_date(29)},
    {"id":"R054","rating":4,"body":"Really solid tumbler. Thermal retention is the best I've tested. The lid seal is slightly looser than my old Yeti but it works fine at desk use.","title":"Excellent thermal performance","verified_purchase":True,"helpful_votes":31,"reviewer_name":"Nina V.","date":_date(140)},
    {"id":"R055","rating":5,"body":"Three years in and still going strong. This is what product quality looks like. I've tried newer options but keep coming back to the Stanley.","title":"Three years strong","verified_purchase":True,"helpful_votes":156,"reviewer_name":"George A.","date":_date(1095)},
    {"id":"R056","rating":3,"body":"Works as described but I think the hype inflated expectations. It's a good tumbler not a magical one. Lid leak is a real issue others should know about.","title":"Good, not magical","verified_purchase":True,"helpful_votes":22,"reviewer_name":"Helen C.","date":_date(80)},
    {"id":"R057","rating":5,"body":"Bought this for hiking and it's perfect. Keeps water ice cold all day even in summer heat. The handle clips to my pack easily.","title":"Perfect hiking companion","verified_purchase":True,"helpful_votes":94,"reviewer_name":"Hiker_Dan","date":_date(300)},
    {"id":"R058","rating":2,"body":"The straw smell after six weeks of use is unpleasant despite daily cleaning. A design flaw Stanley has not addressed.","title":"Straw smell is persistent","verified_purchase":True,"helpful_votes":67,"reviewer_name":"Irene J.","date":_date(95)},
    {"id":"R059","rating":5,"body":"My daughter and I have matching Stanleys in different colors. She drinks twice as much water now. Worth it for that alone.","title":"Got daughter to drink water","verified_purchase":True,"helpful_votes":143,"reviewer_name":"MomOf2","date":_date(170)},
    {"id":"R060","rating":1,"body":"Three different units, all with the same lid seal defect. This is a systemic quality control issue, not a one-off.","title":"Same defect on three units","verified_purchase":True,"helpful_votes":312,"reviewer_name":"Jason B.","date":_date(19)},
    {"id":"R061","rating":4,"body":"Thermal performance is excellent. Handle design is practical. Would rate five stars if the lid seal were as tight as Yeti's.","title":"4 stars — great except lid","verified_purchase":True,"helpful_votes":38,"reviewer_name":"Karen O.","date":_date(255)},
    {"id":"R062","rating":5,"body":"I'm a teacher and I use this through 8-hour school days. Ice is still present by 3pm consistently. The students always ask about it.","title":"Teacher approved — ice all day","verified_purchase":True,"helpful_votes":178,"reviewer_name":"Teacher_Amy","date":_date(190)},
    {"id":"R063","rating":2,"body":"Powder coat finish is mediocre for a premium-priced product. Chipped at base and handle within four months of normal use.","title":"Powder coat chips too easily","verified_purchase":True,"helpful_votes":89,"reviewer_name":"Larry P.","date":_date(130)},
    {"id":"R064","rating":5,"body":"I resisted buying this for a year thinking it was hype. I was wrong. It's genuinely excellent. The handle makes everyday carry comfortable and the thermal retention is real.","title":"Skeptic converted","verified_purchase":True,"helpful_votes":201,"reviewer_name":"Mary U.","date":_date(400)},
    {"id":"R065","rating":3,"body":"Good product with a known lid leak issue. Fine for desk use. I wouldn't carry it in a bag with electronics.","title":"Good for desk, risky for commuting","verified_purchase":True,"helpful_votes":44,"reviewer_name":"Nathan Q.","date":_date(68)},
    {"id":"R066","rating":5,"body":"Best tumbler I've tested across eight different brands. Thermal performance wins, handle design wins, cupholder fit wins. Lid is second-best behind Yeti.","title":"Tested 8 brands — Stanley wins","verified_purchase":True,"helpful_votes":234,"reviewer_name":"Reviewer_Pro","date":_date(320)},
    {"id":"R067","rating":1,"body":"Lid leaked in my yoga bag on the way to class. Soaked my mat, clothes, and keys. Not safe for bags.","title":"Leaked in gym bag","verified_purchase":True,"helpful_votes":198,"reviewer_name":"Olivia K.","date":_date(26)},
    {"id":"R068","rating":4,"body":"Excellent cup overall. Cold retention is the best I've experienced. Only gripe is that the straw requires extra maintenance to stay odor-free.","title":"Excellent — minor straw maintenance needed","verified_purchase":True,"helpful_votes":56,"reviewer_name":"Peter L.","date":_date(215)},
    {"id":"R069","rating":5,"body":"I've been using mine for 18 months through every condition including camping, hiking, and daily commutes. Zero issues. The handle is indispensable once you have it.","title":"18 months, zero issues","verified_purchase":True,"helpful_votes":289,"reviewer_name":"Quinn A.","date":_date(550)},
    {"id":"R070","rating":2,"body":"Paint durability is the biggest disappointment. Chips appeared at three months at the base. For $45 I want it to look good for at least a year.","title":"Paint disappointment","verified_purchase":True,"helpful_votes":77,"reviewer_name":"Rose B.","date":_date(92)},
    {"id":"R071","rating":5,"body":"The viral hype is real and earned. Excellent thermal performance, great handle, perfect cupholder fit. Love the color options.","title":"Hype is earned","verified_purchase":True,"helpful_votes":165,"reviewer_name":"Sam C.","date":_date(380)},
    {"id":"R072","rating":1,"body":"Lid leak destroyed a $400 pair of noise-canceling headphones in my bag. Stanley denied warranty coverage.","title":"Ruined my headphones","verified_purchase":True,"helpful_votes":445,"reviewer_name":"Tom D.","date":_date(38)},
    {"id":"R073","rating":4,"body":"Good solid cup. Cold retention excellent. Handle a genuine improvement over handleless alternatives. Lid seal slightly less secure than Yeti but manageable.","title":"Solid — Yeti-comparable","verified_purchase":True,"helpful_votes":43,"reviewer_name":"Uma E.","date":_date(175)},
    {"id":"R074","rating":5,"body":"My third Stanley. Each one has lasted years. The thermal performance has never degraded. The handle design keeps improving. Best everyday carry cup available.","title":"Third Stanley, still loyal","verified_purchase":True,"helpful_votes":198,"reviewer_name":"Victor F.","date":_date(890)},
    {"id":"R075","rating":3,"body":"Good thermal retention and handle design. The lid anxiety and straw smell keep it at three stars for me. Would buy again but hoping for design improvements.","title":"Good but hoping for improvements","verified_purchase":True,"helpful_votes":29,"reviewer_name":"Wendy G.","date":_date(112)},
    {"id":"R076","rating":5,"body":"Doctor recommended staying hydrated after surgery. This cup made it easy — cold water all day, easy to sip, and the handle means I can carry it without gripping tight. Excellent for recovery.","title":"Perfect for recovery","verified_purchase":True,"helpful_votes":267,"reviewer_name":"Xena H.","date":_date(290)},
    {"id":"R077","rating":2,"body":"Lid leaked twice this week. Both times the cup was in the cupholder. I can't figure out what triggers it reliably which makes it unpredictable and therefore unsafe.","title":"Unpredictable lid leak","verified_purchase":True,"helpful_votes":134,"reviewer_name":"Yolanda I.","date":_date(42)},
    {"id":"R078","rating":5,"body":"Used mine through a cross-country road trip. Kept ice from Denver to LA with a single refill. The cupholder fit was perfect for six different car models we used. Outstanding.","title":"Cross-country road trip tested","verified_purchase":True,"helpful_votes":312,"reviewer_name":"Zach J.","date":_date(430)},
    {"id":"R079","rating":4,"body":"Really happy with this purchase. Thermal performance and handle design are excellent. I don't carry it in bags anymore after reading reviews about lid leaks.","title":"Happy — avoid bags just in case","verified_purchase":True,"helpful_votes":31,"reviewer_name":"Alice K.","date":_date(135)},
    {"id":"R080","rating":1,"body":"Lid leaks. Paint chips. Straw smells. For $45 this is not acceptable. Returning for a Hydro Flask.","title":"Three problems at once","verified_purchase":True,"helpful_votes":189,"reviewer_name":"Bob L.","date":_date(53)},
    {"id":"R081","rating":5,"body":"My coworkers thought I was being dramatic about my Stanley until they tried it. Now three of them have one. The thermal performance speaks for itself.","title":"Convinced three coworkers","verified_purchase":True,"helpful_votes":144,"reviewer_name":"Claire M.","date":_date(265)},
    {"id":"R082","rating":3,"body":"It works. Cold stays cold. Handle is convenient. The lid needs a redesign and the straw requires more maintenance than competing products.","title":"Works well, minor design issues","verified_purchase":True,"helpful_votes":23,"reviewer_name":"Dave N.","date":_date(88)},
    {"id":"R083","rating":5,"body":"I work in healthcare and this gets washed constantly and put through sterilization cycles. Still performing perfectly after eight months of medical-grade cleaning.","title":"Survives medical cleaning cycles","verified_purchase":True,"helpful_votes":221,"reviewer_name":"Eve O.","date":_date(244)},
    {"id":"R084","rating":2,"body":"Lid cracked at the hinge point after five months. Not from impact — the plastic fatigued from daily open/close cycles. Structural weakness.","title":"Lid hinge fatigued and cracked","verified_purchase":True,"helpful_votes":98,"reviewer_name":"Fred P.","date":_date(152)},
    {"id":"R085","rating":5,"body":"The limited color drops create real scarcity and I fall for it every time. But the product genuinely earns the loyalty. Excellent thermal performance and practical design.","title":"Worth the limited-drop hype","verified_purchase":True,"helpful_votes":176,"reviewer_name":"Gail Q.","date":_date(320)},
    {"id":"R086","rating":1,"body":"Lid failed in less than three months. Hinge cracked. Stanley said it was normal wear. A $45 lid should last longer than three months with normal daily use.","title":"Lid failed in 3 months","verified_purchase":True,"helpful_votes":134,"reviewer_name":"Harry R.","date":_date(92)},
    {"id":"R087","rating":5,"body":"I'm 65 and my arthritis makes gripping standard cups painful. The handle on this Stanley is the first cup design that's been genuinely comfortable for me. It's changed my daily hydration.","title":"Handle is arthritis-friendly","verified_purchase":True,"helpful_votes":289,"reviewer_name":"Irma S.","date":_date(400)},
    {"id":"R088","rating":4,"body":"Strong recommendation with the caveat: learn the lid mechanics before trusting it in a bag. Once you understand the tilt limit it's an excellent cup.","title":"Excellent with lid caveat","verified_purchase":True,"helpful_votes":47,"reviewer_name":"Jake T.","date":_date(185)},
    {"id":"R089","rating":5,"body":"Two years of daily use. Works like new. I've refilled it in parking lots, restaurants, hotel lobbies, gas stations. The most used object I own.","title":"Two years of daily use","verified_purchase":True,"helpful_votes":312,"reviewer_name":"Kate U.","date":_date(730)},
    {"id":"R090","rating":3,"body":"Good product. The three star rating comes from the lid seal being noticeably inferior to Hydro Flask. Everything else is excellent.","title":"Good but lid behind competitors","verified_purchase":True,"helpful_votes":34,"reviewer_name":"Liam V.","date":_date(115)},
    {"id":"R091","rating":5,"body":"The cupholder fit is specifically engineered and it shows. Every other tumbler I've had either doesn't fit or rattles. The Stanley sits perfectly.","title":"Engineered cupholder fit","verified_purchase":True,"helpful_votes":156,"reviewer_name":"Mia W.","date":_date(350)},
    {"id":"R092","rating":1,"body":"Paint chipping, lid leaking, straw smelling. This is not a premium product — it's a trendy product with premium pricing.","title":"Trendy not premium","verified_purchase":True,"helpful_votes":201,"reviewer_name":"Nick X.","date":_date(72)},
    {"id":"R093","rating":5,"body":"I've had mine for a year and it still looks and performs like day one. Whatever they coat this with resists scratches better than I expected.","title":"One year, looks like day one","verified_purchase":True,"helpful_votes":134,"reviewer_name":"Olivia Y.","date":_date(365)},
    {"id":"R094","rating":2,"body":"I understand the appeal but the lid leak issue is a real safety concern for anyone who commutes or carries electronics. Stanley needs to address this with a redesign.","title":"Safety concern for commuters","verified_purchase":True,"helpful_votes":167,"reviewer_name":"Paul Z.","date":_date(55)},
    {"id":"R095","rating":5,"body":"Bought after seeing my friend's. Have now gifted four. Everyone loves them. The thermal performance is consistently excellent across all the ones I've seen in use.","title":"Gifted four — all loved","verified_purchase":True,"helpful_votes":88,"reviewer_name":"Quinn A.","date":_date(280)},
    {"id":"R096","rating":4,"body":"Excellent product overall. I dock one star for the lid seal because I've had two minor drips in six months. Still the best tumbler I've used.","title":"Best tumbler despite lid","verified_purchase":True,"helpful_votes":42,"reviewer_name":"Rose B.","date":_date(180)},
    {"id":"R097","rating":5,"body":"I'm a personal trainer and recommend this to every client. Keeps water cold through two-hour sessions. The handle makes it easy to grab between sets.","title":"Personal trainer recommended","verified_purchase":True,"helpful_votes":198,"reviewer_name":"Sam C.","date":_date(220)},
    {"id":"R098","rating":1,"body":"Lid leaked in my camera bag. Condensation soaked around my camera body. I'm lucky it didn't cause damage. Don't carry this near electronics.","title":"Don't carry near electronics","verified_purchase":True,"helpful_votes":289,"reviewer_name":"Tina D.","date":_date(43)},
    {"id":"R099","rating":5,"body":"My husband bought me this for my birthday and I've used it every single day for eight months. The color is still beautiful. The thermal performance never disappoints.","title":"Eight months of daily happiness","verified_purchase":True,"helpful_votes":112,"reviewer_name":"Uma E.","date":_date(245)},
    {"id":"R100","rating":3,"body":"I like this cup. The thermal performance is real and the handle is a genuine quality-of-life improvement. I wish the lid seal was better engineered.","title":"Like it but lid needs work","verified_purchase":True,"helpful_votes":28,"reviewer_name":"Victor F.","date":_date(98)},
    {"id":"R101","rating":5,"body":"Hiking, camping, gym, commute — this cup handles everything. Thermal retention is genuinely excellent. Handle is practical. Cupholder fit is perfect.","title":"Handles everything","verified_purchase":True,"helpful_votes":167,"reviewer_name":"Wendy G.","date":_date(300)},
    {"id":"R102","rating":2,"body":"The lid problem is real and documented across hundreds of reviews. Stanley knows about it and hasn't fixed it. That's a choice.","title":"Known issue, unfixed","verified_purchase":True,"helpful_votes":234,"reviewer_name":"Xena H.","date":_date(66)},
    {"id":"R103","rating":5,"body":"I converted from Contigo after seeing this. Better thermal retention, better handle, better cupholder fit. The lid isn't quite as secure but the tradeoffs are worth it.","title":"Better than Contigo overall","verified_purchase":True,"helpful_votes":89,"reviewer_name":"Yolanda I.","date":_date(340)},
    {"id":"R104","rating":4,"body":"Really happy with this purchase. Would be five stars if the lid were as reliable as my old Hydro Flask. Everything else is superior.","title":"Superior except the lid","verified_purchase":True,"helpful_votes":54,"reviewer_name":"Zach J.","date":_date(205)},
    {"id":"R105","rating":5,"body":"I'm a stay-at-home parent and this cup goes everywhere with me. Morning school run, errands, workouts, evenings. It's the most used thing I own.","title":"Most used thing I own","verified_purchase":True,"helpful_votes":145,"reviewer_name":"Alice K.","date":_date(415)},
    {"id":"R106","rating":1,"body":"Lid leak cost me a ruined planner and two soaked notebooks in my work bag. Not what I expect from a $45 cup with this reputation.","title":"Ruined work bag contents","verified_purchase":True,"helpful_votes":178,"reviewer_name":"Bob L.","date":_date(31)},
    {"id":"R107","rating":5,"body":"The color variety genuinely adds joy to daily routines. I coordinate my cup with outfits which sounds silly but makes me happy. And the thermal performance is excellent.","title":"Joy in daily routine","verified_purchase":True,"helpful_votes":98,"reviewer_name":"Claire M.","date":_date(280)},
    {"id":"R108","rating":3,"body":"It works well overall. The lid is the elephant in the room — everyone knows about it, Stanley hasn't fixed it, and you just learn to live with it.","title":"Good cup, lid is the elephant","verified_purchase":True,"helpful_votes":67,"reviewer_name":"Dave N.","date":_date(78)},
    {"id":"R109","rating":5,"body":"My lab tests everything and I ran informal thermal retention tests on eight popular tumblers. The Stanley Quencher won by a measurable margin. Not just hype.","title":"Lab-tested thermal winner","verified_purchase":True,"helpful_votes":345,"reviewer_name":"Eve O.","date":_date(195)},
    {"id":"R110","rating":2,"body":"Third time the lid has leaked in five months of ownership. Always in the worst situation — bag with electronics, commute. Switching brands.","title":"Three leaks in five months","verified_purchase":True,"helpful_votes":156,"reviewer_name":"Fred P.","date":_date(152)},
    {"id":"R111","rating":5,"body":"I've recommended this to thirty people. Not one has complained about regret. The thermal performance is real and the handle makes it the best designed everyday cup available.","title":"Recommended to 30 people","verified_purchase":True,"helpful_votes":267,"reviewer_name":"Gail Q.","date":_date(450)},
    {"id":"R112","rating":4,"body":"Excellent cup. Four stars because the lid is slightly concerning when commuting with electronics. Five stars if that were fixed.","title":"Four stars, would be five","verified_purchase":True,"helpful_votes":39,"reviewer_name":"Harry R.","date":_date(167)},
    {"id":"R113","rating":5,"body":"My office switched to Stanleys as a team and everyone loves them. The color coordination became a thing. More importantly they just work.","title":"Whole office converted","verified_purchase":True,"helpful_votes":189,"reviewer_name":"Irma S.","date":_date(310)},
    {"id":"R114","rating":1,"body":"Lid leaked onto my cloth car seat, left a stain. The tilt threshold before leaking is too low for normal car use.","title":"Stained car seat","verified_purchase":True,"helpful_votes":123,"reviewer_name":"Jake T.","date":_date(48)},
    {"id":"R115","rating":5,"body":"I'm a runner and use this for long training runs. Keeps water cold even in direct sun. The handle means I can hook it to my vest. Perfect design.","title":"Runner approved","verified_purchase":True,"helpful_votes":156,"reviewer_name":"Kate U.","date":_date(260)},
    {"id":"R116","rating":3,"body":"Good product overall. Three stars because the lid issue is real and the straw smell is annoying. Five-star thermal performance pulls it to three overall.","title":"Thermal 5-star, lid 1-star = 3 overall","verified_purchase":True,"helpful_votes":45,"reviewer_name":"Liam V.","date":_date(104)},
    {"id":"R117","rating":5,"body":"I bought one. Then another for my car. Then one as a gift. The quality consistency across all three has been excellent. No variance in performance.","title":"Consistent quality across three","verified_purchase":True,"helpful_votes":134,"reviewer_name":"Mia W.","date":_date(380)},
    {"id":"R118","rating":2,"body":"Paint chipped at two months. Lid leaked at three. The product doesn't hold up to its premium price positioning.","title":"Fails premium price standard","verified_purchase":True,"helpful_votes":89,"reviewer_name":"Nick X.","date":_date(91)},
    {"id":"R119","rating":5,"body":"I use mine from 5am gym to 8pm bedtime. Ice is still present at the end of the day consistently. The handle makes one-handed carry natural. Best daily cup I've owned.","title":"5am to 8pm — ice still there","verified_purchase":True,"helpful_votes":201,"reviewer_name":"Olivia Y.","date":_date(310)},
    {"id":"R120","rating":4,"body":"Really great cup. I've stopped worrying about the lid because I don't carry it in bags — just car cupholder and desk. In those contexts it's flawless.","title":"Flawless in right context","verified_purchase":True,"helpful_votes":56,"reviewer_name":"Paul Z.","date":_date(195)},
    {"id":"R121","rating":5,"body":"My teenagers fight over who gets to use the Stanley. We've since bought one per person. The color options make everyone happy. Excellent product.","title":"Whole family has one now","verified_purchase":True,"helpful_votes":143,"reviewer_name":"Quinn A.","date":_date(265)},
    {"id":"R122","rating":1,"body":"Lid leaked and permanently stained my light-colored purse lining. Very disappointing for a branded premium product.","title":"Stained my purse","verified_purchase":True,"helpful_votes":234,"reviewer_name":"Rose B.","date":_date(37)},
    {"id":"R123","rating":5,"body":"The combination of cupholder fit plus handle plus thermal retention is a product design hat trick. No other tumbler does all three this well.","title":"Product design hat trick","verified_purchase":True,"helpful_votes":178,"reviewer_name":"Sam C.","date":_date(420)},
    {"id":"R124","rating":3,"body":"Good cup let down by lid design. The thermal performance deserves five stars. The lid design deserves one. Three stars is accurate.","title":"Accurate three stars","verified_purchase":True,"helpful_votes":34,"reviewer_name":"Tina D.","date":_date(115)},
    {"id":"R125","rating":5,"body":"I do long-distance cycling and this is my water bottle for rest stops. Keeps water cold through 4-hour rides in summer heat. The handle works with my bike mount.","title":"Cyclist approved","verified_purchase":True,"helpful_votes":167,"reviewer_name":"Uma E.","date":_date(290)},
    {"id":"R126","rating":2,"body":"Lid leaked in my yoga bag and soaked my mat. For a product that's marketed for active lifestyles the lid seal needs to be reliable at tilt angles beyond 30 degrees.","title":"Not safe for active lifestyle bags","verified_purchase":True,"helpful_votes":112,"reviewer_name":"Victor F.","date":_date(59)},
    {"id":"R127","rating":5,"body":"I'm a nutritionist and recommend this to clients for hydration tracking. The 40oz size is perfect for daily goals. The cold retention keeps water appealing all day.","title":"Nutritionist recommended","verified_purchase":True,"helpful_votes":189,"reviewer_name":"Wendy G.","date":_date(330)},
    {"id":"R128","rating":4,"body":"Great cup. I'd give five stars if the lid seal were better. As it is I use it only when I can control the tilt angle which limits its portability.","title":"Great with tilt limitations","verified_purchase":True,"helpful_votes":47,"reviewer_name":"Xena H.","date":_date(155)},
    {"id":"R129","rating":5,"body":"Converted a dozen friends over two years. Zero regrets reported. The product quality is consistent and the thermal performance is genuinely excellent.","title":"Converted a dozen friends","verified_purchase":True,"helpful_votes":223,"reviewer_name":"Yolanda I.","date":_date(720)},
    {"id":"R130","rating":1,"body":"The lid is dangerous. Leaks without warning. I've had water on my lap while driving twice. This needs a recall or redesign.","title":"Dangerous lid — needs recall","verified_purchase":True,"helpful_votes":389,"reviewer_name":"Zach J.","date":_date(24)},
    {"id":"R131","rating":5,"body":"Best cup I've owned in 10 years of buying quality drinkware. The combination of thermal performance, handle design, and cupholder fit is unmatched.","title":"Best in 10 years","verified_purchase":True,"helpful_votes":201,"reviewer_name":"Alice K.","date":_date(480)},
    {"id":"R132","rating":3,"body":"Decent cup. Not the revelatory product the reviews suggest. Good thermal retention and the handle is nice. The lid and straw issues are real.","title":"Good but not revelatory","verified_purchase":True,"helpful_votes":28,"reviewer_name":"Bob L.","date":_date(88)},
    {"id":"R133","rating":5,"body":"I work night shifts and this keeps my coffee hot and my water cold throughout. The handle means I can carry it one-handed through the hospital. Excellent product.","title":"Night shift essential","verified_purchase":True,"helpful_votes":167,"reviewer_name":"Claire M.","date":_date(210)},
    {"id":"R134","rating":2,"body":"Three separate lid issues: leaks when tilted, hinge cracked at 6 months, and the seal lost elasticity. One lid issue is bad luck. Three is a design problem.","title":"Three lid issues — design problem","verified_purchase":True,"helpful_votes":145,"reviewer_name":"Dave N.","date":_date(185)},
    {"id":"R135","rating":5,"body":"My Stanley is the most complimented object I own. People ask about the color, the brand, the handle. And then I tell them it also keeps ice all day and they're sold.","title":"Most complimented object I own","verified_purchase":True,"helpful_votes":134,"reviewer_name":"Eve O.","date":_date(390)},
    {"id":"R136","rating":4,"body":"Excellent product for desk users and car commuters. I wouldn't use it in a bag with valuables. In the right contexts it's a five-star cup.","title":"5-star in right contexts","verified_purchase":True,"helpful_votes":43,"reviewer_name":"Fred P.","date":_date(220)},
    {"id":"R137","rating":5,"body":"I've been recommending this to my corporate wellness clients for two years. Consistent positive feedback on thermal performance and the handle design.","title":"Corporate wellness recommended","verified_purchase":True,"helpful_votes":156,"reviewer_name":"Gail Q.","date":_date(730)},
    {"id":"R138","rating":1,"body":"Lid leaked on my work files during a commute. Important documents ruined. The lid on this product is a design failure that Stanley has not fixed.","title":"Documents ruined","verified_purchase":True,"helpful_votes":267,"reviewer_name":"Harry R.","date":_date(41)},
    {"id":"R139","rating":5,"body":"I bought this during a limited color drop and have never regretted it. The product lives up to the hype. Excellent every day for over a year.","title":"One year of no regrets","verified_purchase":True,"helpful_votes":112,"reviewer_name":"Irma S.","date":_date(365)},
    {"id":"R140","rating":3,"body":"Good thermal retention. Nice handle. Lid needs engineering improvement. Straw needs accessibility redesign for cleaning. Worth buying with those caveats.","title":"Worth buying with caveats","verified_purchase":True,"helpful_votes":34,"reviewer_name":"Jake T.","date":_date(128)},
    {"id":"R141","rating":5,"body":"I'm a physical therapist and the handle design is medically sound — ergonomic grip position reduces wrist strain. It's also just a great tumbler.","title":"Ergonomically sound design","verified_purchase":True,"helpful_votes":189,"reviewer_name":"Kate U.","date":_date(300)},
    {"id":"R142","rating":2,"body":"Lid leaks. That's the main issue and it hasn't been fixed. Everything else about the cup is good. But a leaking lid makes it unusable for commuting.","title":"Main issue: lid still leaks","verified_purchase":True,"helpful_votes":98,"reviewer_name":"Liam V.","date":_date(66)},
    {"id":"R143","rating":5,"body":"My elderly mother loves hers because the handle lets her carry it with her weak grip. That's a real accessibility win for a mainstream product.","title":"Accessibility win for elderly","verified_purchase":True,"helpful_votes":234,"reviewer_name":"Mia W.","date":_date(415)},
    {"id":"R144","rating":4,"body":"Strong recommendation. One star removed for the lid seal because I've been too anxious to carry it in my laptop bag. In cupholder and desk use it's flawless.","title":"One star for lid anxiety","verified_purchase":True,"helpful_votes":56,"reviewer_name":"Nick X.","date":_date(175)},
    {"id":"R145","rating":5,"body":"I'm a marathon runner. I test gear hard. This cup has held up to thousands of miles of training and racing. The thermal retention is consistent and the handle never loosened.","title":"Marathon-tested","verified_purchase":True,"helpful_votes":178,"reviewer_name":"Olivia Y.","date":_date(545)},
    {"id":"R146","rating":1,"body":"Lid leaked in my briefcase twice in two weeks. First time I thought it was a fluke. Second time I accepted it's a design flaw. Returning.","title":"Two leaks in two weeks","verified_purchase":True,"helpful_votes":156,"reviewer_name":"Paul Z.","date":_date(14)},
    {"id":"R147","rating":5,"body":"Four Stanleys in my household — different colors, all daily use. Zero durability complaints across two years. The product quality is genuinely consistent.","title":"Four in household, zero complaints","verified_purchase":True,"helpful_votes":143,"reviewer_name":"Quinn A.","date":_date(730)},
    {"id":"R148","rating":3,"body":"It's a good cup. The reviews that say it's perfect are overselling it. The reviews that say it's garbage are underselling it. Three stars is accurate.","title":"Three stars is accurate","verified_purchase":True,"helpful_votes":45,"reviewer_name":"Rose B.","date":_date(98)},
    {"id":"R149","rating":5,"body":"I've had mine for two years and the color still looks new, the lid still works, and the thermal performance is unchanged. Best investment in daily gear I've made.","title":"Two years, no degradation","verified_purchase":True,"helpful_votes":289,"reviewer_name":"Sam C.","date":_date(730)},
    {"id":"R150","rating":2,"body":"The lid is the entire problem. Fix the lid and this is a five-star product. Until then I can't recommend it to anyone who carries a bag.","title":"Fix the lid = 5 stars","verified_purchase":True,"helpful_votes":167,"reviewer_name":"Tina D.","date":_date(79)},
    {"id":"R151","rating":5,"body":"Keeps ice all day in summer heat. Handle is excellent. Cupholder fit is perfect. Highly recommend.","title":"Ice all day","verified_purchase":True,"helpful_votes":23,"reviewer_name":"Uma E.","date":_date(140)},
    {"id":"R152","rating":1,"body":"Lid leaked on my work bag. Third Stanley product I've tried with the same issue.","title":"Same lid issue every time","verified_purchase":True,"helpful_votes":78,"reviewer_name":"Victor F.","date":_date(51)},
    {"id":"R153","rating":5,"body":"Gift for my wife — she uses it every single day and loves the color. The thermal performance surprised her.","title":"Wife loves it","verified_purchase":True,"helpful_votes":31,"reviewer_name":"Wendy G.","date":_date(220)},
    {"id":"R154","rating":4,"body":"Great cup overall. Would be five stars without the lid seal concern. Excellent thermal performance.","title":"Great but for lid","verified_purchase":True,"helpful_votes":19,"reviewer_name":"Xena H.","date":_date(165)},
    {"id":"R155","rating":5,"body":"Still going strong at 14 months daily use. Dishwasher safe claim is accurate. Thermal retention unchanged.","title":"14 months strong","verified_purchase":True,"helpful_votes":67,"reviewer_name":"Yolanda I.","date":_date(430)},
    {"id":"R156","rating":3,"body":"Good product. Lid anxiety is real for commuters. Desk use is perfect. The thermals are excellent.","title":"Good for desk, anxiety for commuters","verified_purchase":True,"helpful_votes":15,"reviewer_name":"Zach J.","date":_date(90)},
    {"id":"R157","rating":5,"body":"Every commuter should have one. Cold all day, fits cupholder, handle for one-handed use. Perfect.","title":"Commuter essential","verified_purchase":True,"helpful_votes":44,"reviewer_name":"Alice K.","date":_date(280)},
    {"id":"R158","rating":2,"body":"Paint chipped early. Lid is unreliable. Expected more at this price.","title":"Below premium standard","verified_purchase":True,"helpful_votes":56,"reviewer_name":"Bob L.","date":_date(72)},
    {"id":"R159","rating":5,"body":"Used mine camping for a week. Ice lasted 18+ hours in each fill. Outstanding thermal retention in outdoor conditions.","title":"Camping tested — excellent","verified_purchase":True,"helpful_votes":89,"reviewer_name":"Claire M.","date":_date(310)},
    {"id":"R160","rating":1,"body":"Lid leaks. Paint chips. Both issues are well-documented and unfixed. Not buying Stanley again.","title":"Known issues still unfixed","verified_purchase":True,"helpful_votes":134,"reviewer_name":"Dave N.","date":_date(58)},
    {"id":"R161","rating":5,"body":"My book club does coordinated color orders. It's fun and the products are excellent. Cold all day, handle is practical.","title":"Coordinated book club order","verified_purchase":True,"helpful_votes":67,"reviewer_name":"Eve O.","date":_date(330)},
    {"id":"R162","rating":4,"body":"Really solid cup. I've stopped carrying it in bags as a precaution. In my car and at my desk it's perfect.","title":"Perfect in right settings","verified_purchase":True,"helpful_votes":28,"reviewer_name":"Fred P.","date":_date(148)},
    {"id":"R163","rating":5,"body":"The thermal retention genuinely surprised me. I expected good. I got excellent. Ice lasted all day in 85 degrees.","title":"Better thermal than expected","verified_purchase":True,"helpful_votes":112,"reviewer_name":"Gail Q.","date":_date(260)},
    {"id":"R164","rating":3,"body":"Three star cup. Good thermal. Handle is nice. Lid is a known problem. Straw needs better design.","title":"Three star is fair","verified_purchase":True,"helpful_votes":21,"reviewer_name":"Harry R.","date":_date(103)},
    {"id":"R165","rating":5,"body":"Best $45 I've spent on daily gear. Use it every day. Over a year in and zero complaints.","title":"Best $45 daily gear","verified_purchase":True,"helpful_votes":143,"reviewer_name":"Irma S.","date":_date(400)},
    {"id":"R166","rating":2,"body":"The lid issue is real and recurring. I've replaced the lid twice. Same problem both times.","title":"Replaced lid twice","verified_purchase":True,"helpful_votes":89,"reviewer_name":"Jake T.","date":_date(184)},
    {"id":"R167","rating":5,"body":"Used mine for 500 miles of cycling this summer. Reliable, cold, handles well. Outstanding for active use.","title":"500 miles cycling season","verified_purchase":True,"helpful_votes":156,"reviewer_name":"Kate U.","date":_date(210)},
    {"id":"R168","rating":4,"body":"Nearly perfect. The lid seal is the only thing holding it back from five stars. Thermal and handle are excellent.","title":"Nearly perfect","verified_purchase":True,"helpful_votes":34,"reviewer_name":"Liam V.","date":_date(195)},
    {"id":"R169","rating":5,"body":"I work in a hot kitchen and this keeps water cold through 10-hour shifts. Nothing else has done that. Outstanding product.","title":"Kitchen worker approved","verified_purchase":True,"helpful_votes":178,"reviewer_name":"Mia W.","date":_date(270)},
    {"id":"R170","rating":1,"body":"Lid leaked again. Third time in four months. I've tried every YouTube fix. Nothing works.","title":"Third leak in four months","verified_purchase":True,"helpful_votes":198,"reviewer_name":"Nick X.","date":_date(122)},
    {"id":"R171","rating":5,"body":"Best tumbler I've tested. Thermal wins, handle wins, cupholder fit wins. Lid is the one area competitors edge ahead but the tradeoffs favor Stanley.","title":"Overall best despite lid","verified_purchase":True,"helpful_votes":134,"reviewer_name":"Olivia Y.","date":_date(380)},
    {"id":"R172","rating":3,"body":"Solid three-star product. Thermal is great. Handle is great. Lid and straw need redesigns. Worth buying with those expectations.","title":"Solid three stars","verified_purchase":True,"helpful_votes":19,"reviewer_name":"Paul Z.","date":_date(93)},
    {"id":"R173","rating":5,"body":"Three years with the same one. No degradation. The durability of this product when it works correctly is outstanding.","title":"Three year durability","verified_purchase":True,"helpful_votes":201,"reviewer_name":"Quinn A.","date":_date(1095)},
    {"id":"R174","rating":2,"body":"Lid sealed poorly from day one. Returned for exchange. New one has the same issue. Design problem, not a defective unit problem.","title":"Both units same lid problem","verified_purchase":True,"helpful_votes":112,"reviewer_name":"Rose B.","date":_date(67)},
    {"id":"R175","rating":5,"body":"The color drops are fun and the product earns the loyalty. Thermal retention is consistently excellent. Handle makes daily carry natural.","title":"Earns the loyalty","verified_purchase":True,"helpful_votes":167,"reviewer_name":"Sam C.","date":_date(440)},
    {"id":"R176","rating":4,"body":"Very good cup. I remove one star for the lid because I've become anxious about carrying it in certain situations. Otherwise it's excellent.","title":"Very good minus one star","verified_purchase":True,"helpful_votes":38,"reviewer_name":"Tina D.","date":_date(155)},
    {"id":"R177","rating":5,"body":"Thirteen months daily use. Color looks new. Thermal unchanged. Handle solid. Lid works correctly. Outstanding longevity.","title":"Outstanding at 13 months","verified_purchase":True,"helpful_votes":189,"reviewer_name":"Uma E.","date":_date(395)},
    {"id":"R178","rating":1,"body":"Lid not safe for bags. Repeated leaks. Will not buy Stanley again.","title":"Not safe for bags","verified_purchase":True,"helpful_votes":145,"reviewer_name":"Victor F.","date":_date(83)},
    {"id":"R179","rating":5,"body":"I've recommended this to every person who asked about my cup. All of them have come back and thanked me. Excellent product.","title":"Everyone who asked is now a fan","verified_purchase":True,"helpful_votes":123,"reviewer_name":"Wendy G.","date":_date(510)},
    {"id":"R180","rating":3,"body":"Good product with specific failure modes. Thermal excellent. Handle great. Lid and straw need engineering attention.","title":"Good with known failure modes","verified_purchase":True,"helpful_votes":23,"reviewer_name":"Xena H.","date":_date(107)},
    {"id":"R181","rating":5,"body":"My daughter started drinking water instead of soda since I got her a Stanley. That alone makes it the best purchase I've made.","title":"Switched daughter from soda","verified_purchase":True,"helpful_votes":312,"reviewer_name":"Yolanda I.","date":_date(290)},
    {"id":"R182","rating":4,"body":"Four stars and would be five if Stanley fixed the lid. Thermal and handle are category-leading.","title":"Four stars, fix the lid for five","verified_purchase":True,"helpful_votes":45,"reviewer_name":"Zach J.","date":_date(170)},
    {"id":"R183","rating":5,"body":"I use mine at the gym, at work, and hiking on weekends. It handles all three contexts perfectly. Outstanding versatile product.","title":"Perfect across all contexts","verified_purchase":True,"helpful_votes":167,"reviewer_name":"Alice K.","date":_date(340)},
    {"id":"R184","rating":2,"body":"The lid problems cost Stanley a loyal customer. I loved the thermal performance. But the lid is not safe for my commute.","title":"Lost a loyal customer","verified_purchase":True,"helpful_votes":98,"reviewer_name":"Bob L.","date":_date(74)},
    {"id":"R185","rating":5,"body":"Two years of daily use and this cup is my most reliable possession. Never leaked, never chipped, thermal unchanged. Exceptional quality.","title":"Most reliable possession","verified_purchase":True,"helpful_votes":234,"reviewer_name":"Claire M.","date":_date(730)},
    {"id":"R186","rating":4,"body":"Excellent cup. The lid is the only thing stopping a five-star. In contexts where tilt is controlled it's a perfect product.","title":"Perfect in controlled contexts","verified_purchase":True,"helpful_votes":31,"reviewer_name":"Dave N.","date":_date(215)},
    {"id":"R187","rating":5,"body":"I've tested every major tumbler brand over five years. The Stanley Quencher is the best overall package despite the lid. Nothing else matches it on thermal plus handle plus cupholder.","title":"Best overall package tested","verified_purchase":True,"helpful_votes":289,"reviewer_name":"Eve O.","date":_date(545)},
    {"id":"R188","rating":3,"body":"Three stars is the honest rating. Good thermal. Good handle. Bad lid. Bad straw maintenance. Averages to three.","title":"Averages to three stars","verified_purchase":True,"helpful_votes":17,"reviewer_name":"Fred P.","date":_date(119)},
    {"id":"R189","rating":5,"body":"I'm retiring my Hydro Flask after four years for the Stanley because the handle makes such a practical difference. The thermal is comparable. The design is better.","title":"Retiring Hydro Flask for this","verified_purchase":True,"helpful_votes":178,"reviewer_name":"Gail Q.","date":_date(480)},

    # ── FILTERED REVIEWS F001-F058 (low-trust — unverified, short, burst pattern) ──
    {"id":"F001","rating":5,"body":"Great product!","title":"Love it","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Amazon Customer","date":_date(3)},
    {"id":"F002","rating":5,"body":"Amazing!","title":"5 stars","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Customer123","date":_date(3)},
    {"id":"F003","rating":5,"body":"Best cup ever!","title":"Love","verified_purchase":False,"helpful_votes":0,"reviewer_name":"AmazonUser456","date":_date(3)},
    {"id":"F004","rating":5,"body":"Highly recommend!","title":"Great","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Reviewer789","date":_date(3)},
    {"id":"F005","rating":5,"body":"Perfect!","title":"5/5","verified_purchase":False,"helpful_votes":0,"reviewer_name":"User001","date":_date(3)},
    {"id":"F006","rating":5,"body":"Works great.","title":"Good","verified_purchase":False,"helpful_votes":0,"reviewer_name":"A. Customer","date":_date(4)},
    {"id":"F007","rating":5,"body":"Love this product so much!","title":"Amazing purchase","verified_purchase":False,"helpful_votes":0,"reviewer_name":"CustXYZ","date":_date(4)},
    {"id":"F008","rating":1,"body":"Terrible!","title":"Bad","verified_purchase":False,"helpful_votes":0,"reviewer_name":"User999","date":_date(4)},
    {"id":"F009","rating":5,"body":"Great quality.","title":"Nice cup","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Amazon_Cust","date":_date(4)},
    {"id":"F010","rating":5,"body":"Excellent!","title":"Excellent","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Reviewer1","date":_date(4)},
    {"id":"F011","rating":5,"body":"Very good!","title":"Good product","verified_purchase":False,"helpful_votes":0,"reviewer_name":"User234","date":_date(5)},
    {"id":"F012","rating":5,"body":"Satisfied.","title":"Happy with purchase","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Customer567","date":_date(5)},
    {"id":"F013","rating":5,"body":"As described.","title":"As expected","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Reviewer2","date":_date(5)},
    {"id":"F014","rating":5,"body":"Would buy again!","title":"Repurchase","verified_purchase":False,"helpful_votes":0,"reviewer_name":"AmazonBuyer","date":_date(5)},
    {"id":"F015","rating":5,"body":"Nice.","title":"Nice","verified_purchase":False,"helpful_votes":0,"reviewer_name":"User111","date":_date(5)},
    {"id":"F016","rating":5,"body":"Exactly what I wanted.","title":"Perfect","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Cust222","date":_date(6)},
    {"id":"F017","rating":5,"body":"Fast shipping and great product.","title":"Fast shipping","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Buyer333","date":_date(6)},
    {"id":"F018","rating":5,"body":"Five stars!","title":"Five stars","verified_purchase":False,"helpful_votes":0,"reviewer_name":"User444","date":_date(6)},
    {"id":"F019","rating":5,"body":"Recommend.","title":"Recommend","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Amazon555","date":_date(6)},
    {"id":"F020","rating":5,"body":"Good quality!","title":"Quality","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Customer666","date":_date(6)},
    {"id":"F021","rating":5,"body":"Love the color!","title":"Beautiful color","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Reviewer3","date":_date(7)},
    {"id":"F022","rating":5,"body":"Great buy!","title":"Great buy","verified_purchase":False,"helpful_votes":0,"reviewer_name":"User777","date":_date(7)},
    {"id":"F023","rating":5,"body":"Worth it!","title":"Worth it","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Buyer888","date":_date(7)},
    {"id":"F024","rating":1,"body":"Do not buy.","title":"Avoid","verified_purchase":False,"helpful_votes":0,"reviewer_name":"HaterUser","date":_date(7)},
    {"id":"F025","rating":5,"body":"Looks great!","title":"Looks good","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Visual999","date":_date(7)},
    {"id":"F026","rating":5,"body":"My favorite!","title":"Favorite cup","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Amazon000","date":_date(8)},
    {"id":"F027","rating":5,"body":"Super happy!","title":"Happy","verified_purchase":False,"helpful_votes":0,"reviewer_name":"HappyUser1","date":_date(8)},
    {"id":"F028","rating":5,"body":"Perfect size!","title":"Right size","verified_purchase":False,"helpful_votes":0,"reviewer_name":"SizeUser2","date":_date(8)},
    {"id":"F029","rating":5,"body":"Cold all day!","title":"Cold","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Cold3","date":_date(8)},
    {"id":"F030","rating":5,"body":"Fits my cupholder!","title":"Fits cupholder","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Cup4","date":_date(8)},
    {"id":"F031","rating":5,"body":"Stanley is the best!","title":"Best brand","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Brand5","date":_date(9)},
    {"id":"F032","rating":5,"body":"My friend loves hers too!","title":"Friends love it","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Friend6","date":_date(9)},
    {"id":"F033","rating":5,"body":"Totally worth it!","title":"Worth every penny","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Worth7","date":_date(9)},
    {"id":"F034","rating":5,"body":"So happy with this!","title":"Happy purchase","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Happy8","date":_date(9)},
    {"id":"F035","rating":5,"body":"Great product overall!","title":"Overall great","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Overall9","date":_date(9)},
    {"id":"F036","rating":5,"body":"Arrived fast.","title":"Fast delivery","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Fast10","date":_date(10)},
    {"id":"F037","rating":5,"body":"Very pretty.","title":"Pretty","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Pretty11","date":_date(10)},
    {"id":"F038","rating":5,"body":"Sturdy and nice.","title":"Sturdy","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Sturdy12","date":_date(10)},
    {"id":"F039","rating":5,"body":"Love love love!","title":"Love","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Love13","date":_date(10)},
    {"id":"F040","rating":5,"body":"Absolutely perfect.","title":"Absolute perfection","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Perfect14","date":_date(10)},
    {"id":"F041","rating":5,"body":"Best gift ever!","title":"Gift","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Gift15","date":_date(11)},
    {"id":"F042","rating":5,"body":"Bought for my daughter.","title":"For daughter","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Mom16","date":_date(11)},
    {"id":"F043","rating":5,"body":"Works as expected.","title":"Expected","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Expected17","date":_date(11)},
    {"id":"F044","rating":5,"body":"Nice product!","title":"Nice","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Nice18","date":_date(11)},
    {"id":"F045","rating":5,"body":"Totally recommend!","title":"Recommend","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Rec19","date":_date(11)},
    {"id":"F046","rating":5,"body":"Keeps drinks cold!","title":"Cold drinks","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Cold20","date":_date(12)},
    {"id":"F047","rating":5,"body":"The handle is nice.","title":"Handle","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Handle21","date":_date(12)},
    {"id":"F048","rating":5,"body":"Very stylish!","title":"Stylish","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Style22","date":_date(12)},
    {"id":"F049","rating":5,"body":"Great value!","title":"Value","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Value23","date":_date(12)},
    {"id":"F050","rating":5,"body":"Love the design!","title":"Design","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Design24","date":_date(12)},
    {"id":"F051","rating":1,"body":"Not worth it.","title":"Skip it","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Skip25","date":_date(13)},
    {"id":"F052","rating":5,"body":"Happy with my order!","title":"Happy order","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Order26","date":_date(13)},
    {"id":"F053","rating":5,"body":"Exactly as described!","title":"As described","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Desc27","date":_date(13)},
    {"id":"F054","rating":5,"body":"Perfect for coffee!","title":"Coffee","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Coffee28","date":_date(13)},
    {"id":"F055","rating":5,"body":"Very pleased!","title":"Pleased","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Pleased29","date":_date(13)},
    {"id":"F056","rating":5,"body":"Looks even better in person!","title":"Beautiful","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Beauty30","date":_date(14)},
    {"id":"F057","rating":5,"body":"Already ordered another!","title":"Ordered again","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Repeat31","date":_date(14)},
    {"id":"F058","rating":5,"body":"This cup is great!","title":"Great cup","verified_purchase":False,"helpful_votes":0,"reviewer_name":"Cup32","date":_date(14)},
]


# ─────────────────────────────────────────────────────────────────────────────
# PRODUCT INFO
# ─────────────────────────────────────────────────────────────────────────────

STANLEY_PRODUCT_INFO = {
    "title": "Stanley Quencher H2.0 FlowState Tumbler 40oz — Cupholder Compatible Insulated Stainless Steel Cup with Lid and Straw",
    "asin": "DEMO_STANLEY",
    "rating": 4.2,
    "ratings_total": 67842,
    "image_url": "assets/stanley.jpg",
    "brand": "Stanley",
    "price": "$45.00",
}

HYDROFLASK_PRODUCT_INFO = {
    "title": "Hydro Flask Wide Mouth Water Bottle 40oz — Stainless Steel Insulated with Flex Cap",
    "asin": "DEMO_HF",
    "rating": 4.4,
    "ratings_total": 28431,
    "image_url": "assets/hydroflask.jpg",
    "brand": "Hydro Flask",
    "price": "$49.95",
}

STANLEY_FILTER_SUMMARY = {
    "total_fetched": 247,
    "trusted_count": 189,
    "filtered_count": 58,
    "fake_percentage": 23.5,
    "noise_removed_label": "23.5% noise removed",
}


# ─────────────────────────────────────────────────────────────────────────────
# ANALYSIS
# ─────────────────────────────────────────────────────────────────────────────

STANLEY_ANALYSIS = {
    "health_score": 74,
    "health_label": "Good",
    "executive_summary": (
        "The Stanley Quencher dominates the premium tumbler market with exceptional thermal "
        "performance and cult-like brand loyalty, but faces a critical product design vulnerability: "
        "a leaking lid that has destroyed customers' laptops, bags, and trust. The brand's viral "
        "color strategy and cupholder compatibility are genuine differentiators, but the lid issue "
        "is an escalating reputational risk that competitors are actively exploiting."
    ),
    "complaint_themes": [
        {
            "theme": "Lid leaks when tilted — ruins bags and electronics",
            "frequency_pct": 35,
            "emotional_intensity": "CRITICAL",
            "example_quotes": [
                "Soaked my work bag twice and ruined a laptop keyboard",
                "Full 40oz of water on my lap while driving 70mph — this is a safety issue",
            ],
            "recommendation": "Redesign the lid seal mechanism to prevent leaking at angles up to 45 degrees. Add a secondary lock position. This is the #1 reason customers switch to competitors.",
            "star_impact": -0.4,
        },
        {
            "theme": "Straw and lid develops mold in hard-to-clean crevices",
            "frequency_pct": 22,
            "emotional_intensity": "HIGH",
            "example_quotes": [
                "Found black mold in the crevice where the straw meets the lid",
                "Persistent odor despite full daily disassembly and cleaning",
            ],
            "recommendation": "Redesign straw-lid interface with smooth accessible surfaces. Include a dedicated thin cleaning brush with every purchase.",
            "star_impact": -0.25,
        },
        {
            "theme": "Paint and powder coat chips within months",
            "frequency_pct": 18,
            "emotional_intensity": "MEDIUM",
            "example_quotes": [
                "Chipping at the base and around the handle attachment points at three months",
                "Premium pricing should come with premium finish durability",
            ],
            "recommendation": "Switch to more durable ceramic or industrial powder coat finish. Offer a finish warranty for the first year.",
            "star_impact": -0.2,
        },
        {
            "theme": "Customer service slow and unhelpful for warranty claims",
            "frequency_pct": 12,
            "emotional_intensity": "HIGH",
            "example_quotes": [
                "Offered 20% discount when I wanted a lid that doesn't leak",
                "Warranty process is long and the portal doesn't work on mobile",
            ],
            "recommendation": "Implement same-day replacement policy for verified lid defect complaints. Hydro Flask's no-questions-asked replacement is the benchmark.",
            "star_impact": -0.15,
        },
    ],
    "praise_themes": [
        {
            "theme": "Exceptional cold and hot retention — ice lasts all day",
            "frequency_pct": 78,
            "example_quotes": [
                "Ice at 7am still present at 6pm in a 90-degree office",
                "Keeps water cold through 12-hour shifts consistently",
            ],
            "recommendation": "Lead with the 12-hour cold retention claim in all advertising. Real customer language: 'still ice cold after my entire shift' is more credible than spec claims.",
        },
        {
            "theme": "Handle design improves daily usability significantly",
            "frequency_pct": 67,
            "example_quotes": [
                "I didn't realize how much I struggled with handleless bottles until I had the option",
                "Hook it on my bag strap, carry it while holding other things",
            ],
            "recommendation": "The handle is your most underrated differentiator vs Hydro Flask. Lead with the functional benefit in all competitive comparisons.",
        },
        {
            "theme": "Perfect cupholder fit — a genuine differentiator",
            "frequency_pct": 52,
            "example_quotes": [
                "Fits every cupholder I've tried including narrow ones in my older Jeep",
                "Sits perfectly — no rattling like every other tumbler I've tried",
            ],
            "recommendation": "Cupholder compatibility is a direct competitive advantage over Hydro Flask. Make this a primary feature in listings and ads.",
        },
        {
            "theme": "Color variety drives repeat purchases and gifting",
            "frequency_pct": 45,
            "example_quotes": [
                "Limited edition drops create genuine excitement and scarcity",
                "My entire office coordinates colors — gifting creates brand awareness",
            ],
            "recommendation": "Push the collect-them-all and gifting angle heavily. Bundle gift sets with popular color combinations.",
        },
    ],
    "risk_alerts": [
        {
            "level": "CRITICAL",
            "alert": "Lid leak is #1 churn driver — customers explicitly name Hydro Flask as alternative",
            "action": "Engineering fix required. Estimate: +0.4 stars if resolved.",
        },
        {
            "level": "HIGH",
            "alert": "Electronics damage claims create product liability exposure",
            "action": "Legal review recommended. Add clear lid-lock instructions to packaging.",
        },
        {
            "level": "MEDIUM",
            "alert": "Paint durability complaints trending upward in 2024-2025",
            "action": "Audit coating supplier quality across recent production runs.",
        },
    ],
    "buyer_personas": [
        {
            "name": "The Daily Commuter",
            "share_pct": 38,
            "description": "Uses Stanley for car commute and desk work. Values cupholder fit and handle. Anxious about lid leaks when carrying electronics.",
            "key_message": "Engineered for your commute — cupholder-compatible, one-handed handle.",
        },
        {
            "name": "The Hydration Enthusiast",
            "share_pct": 29,
            "description": "Tracks water intake, uses large format for daily goals. Driven by thermal performance and size. Often influences purchase decisions for friends and family.",
            "key_message": "40oz, ice-cold all day. Your daily hydration solved.",
        },
        {
            "name": "The Color Collector",
            "share_pct": 21,
            "description": "Motivated by limited color drops and gifting. Builds brand loyalty through social proof. Drives repeat purchases and word-of-mouth.",
            "key_message": "New colors every season. Collect yours.",
        },
        {
            "name": "The Active Professional",
            "share_pct": 12,
            "description": "Uses Stanley through long work shifts (nurses, teachers, trainers). Values durability and reliable thermal performance. Recommends to colleagues.",
            "key_message": "Built for 12-hour days. Trusted by professionals.",
        },
    ],
    "keywords": [
        "cupholder compatible tumbler",
        "leakproof insulated cup",
        "handle tumbler 40oz",
        "ice retention all day",
        "stainless steel tumbler handle",
        "stanley quencher alternative",
        "40oz tumbler commuter",
        "powder coat tumbler color",
        "dishwasher safe tumbler",
        "premium drinkware gift",
    ],
    "listing_bullets": [
        "CUPHOLDER-ENGINEERED FIT — Precision-tapered base fits standard and narrow car cupholders perfectly. No rattle, no fumbling. Designed for your commute.",
        "ICE ALL DAY GUARANTEED — Advanced vacuum insulation keeps drinks ice-cold for 12+ hours, hot for 7+ hours. Verified by thousands of daily users across every climate.",
        "ONE-HANDED HANDLE DESIGN — Ergonomic rotating handle lets you carry, hook, and grip naturally. Arthritis-friendly, commuter-tested, gym-approved.",
        "LEAKPROOF LID WITH FLIP STRAW — FlowState lid with secure flip lock and two opening positions. Dishwasher safe.",
        "40oz IN SEASONAL COLORS — Available in limited seasonal colorways. BPA-free, stainless steel, built to last years.",
    ],
}

HYDROFLASK_REVIEWS_SAMPLE = [
    {"id":"HF001","rating":5,"body":"Hydro Flask keeps my water cold all day. The lid seal is perfect — I carry this in my backpack with my laptop and have zero anxiety about leaks. Customer service when I had a lid issue was outstanding: replacement shipped same day, no questions asked.","title":"Perfect lid, outstanding service","verified_purchase":True,"helpful_votes":234,"reviewer_name":"Marcus T.","date":_date(45)},
    {"id":"HF002","rating":3,"body":"The thermal performance is excellent but the bottle is heavy and doesn't fit in my car cupholder. I have to hold it while driving which is inconvenient. The Stanley fits perfectly in cupholders which is why my coworkers prefer it.","title":"Good thermals, doesn't fit cupholder","verified_purchase":True,"helpful_votes":189,"reviewer_name":"Sara K.","date":_date(78)},
    {"id":"HF003","rating":5,"body":"I switched from Stanley because of the lid leak issue and Hydro Flask's lid is noticeably more secure. I can tilt this at any angle without anxiety. The trade-off is no handle and it doesn't fit my car cupholder, but the peace of mind is worth it.","title":"Switched from Stanley — lid is better","verified_purchase":True,"helpful_votes":312,"reviewer_name":"Jennifer A.","date":_date(32)},
    {"id":"HF004","rating":4,"body":"Great bottle with excellent thermal retention. My main complaints are that it doesn't fit standard car cupholders and there's no handle, which makes carrying it less convenient than I'd like.","title":"Great but no handle, no cupholder fit","verified_purchase":True,"helpful_votes":145,"reviewer_name":"David M.","date":_date(120)},
    {"id":"HF005","rating":5,"body":"The Hydro Flask customer service is the best I've experienced in consumer products. I had a minor lid issue two years after purchase and they replaced the entire bottle without question. That's how you build brand loyalty.","title":"Customer service is unmatched","verified_purchase":True,"helpful_votes":267,"reviewer_name":"Lisa R.","date":_date(200)},
    {"id":"HF006","rating":2,"body":"The bottle is too wide to fit in most car cupholders. I bought this for commuting and it doesn't work for my primary use case. The thermal performance is excellent but useless if I can't carry it conveniently.","title":"Doesn't fit car cupholder","verified_purchase":True,"helpful_votes":198,"reviewer_name":"Tom B.","date":_date(56)},
    {"id":"HF007","rating":5,"body":"The powder coat finish on my Hydro Flask still looks brand new at two years of daily use. I had a Stanley for comparison and the Stanley started chipping at three months. The finish quality difference is significant.","title":"Finish quality is excellent","verified_purchase":True,"helpful_votes":156,"reviewer_name":"Anna C.","date":_date(730)},
    {"id":"HF008","rating":4,"body":"Excellent bottle. The thermal retention is comparable to Stanley. The lid is more secure which I prefer. The downsides are no handle and no cupholder compatibility. Different product for different needs.","title":"More secure lid than Stanley","verified_purchase":True,"helpful_votes":87,"reviewer_name":"Chris D.","date":_date(180)},
    {"id":"HF009","rating":3,"body":"Good product but I miss having a handle like the Stanley. Carrying this long distances without a handle is tiring. I use it at my desk where the cupholder issue doesn't matter.","title":"Wish it had a handle","verified_purchase":True,"helpful_votes":134,"reviewer_name":"Patricia E.","date":_date(95)},
    {"id":"HF010","rating":5,"body":"No lid leak issues in 18 months of daily use including being tossed in bags with electronics. I came from the Stanley and the lid difference is night and day. I'd go back to Stanley for the handle and cupholder fit but not the lid.","title":"No lid leaks — Stanley comparison","verified_purchase":True,"helpful_votes":289,"reviewer_name":"Robert F.","date":_date(550)},
]

COMPETITOR_GAP_ANALYSIS = {
    "my_advantages": [
        {"advantage": "Cupholder compatibility — engineered to fit standard car cupholders", "evidence": "Hydro Flask reviews repeatedly cite inability to fit cupholders as a primary frustration.", "marketing_angle": "The only premium tumbler engineered for your cupholder"},
        {"advantage": "Ergonomic handle for one-handed carry", "evidence": "Hydro Flask customers explicitly say they miss having a handle for long commutes.", "marketing_angle": "The handle Hydro Flask doesn't have"},
        {"advantage": "Extensive seasonal color collection", "evidence": "Stanley color drops generate documented social excitement and repeat purchases.", "marketing_angle": "New colors every season. Collect yours."},
    ],
    "my_vulnerabilities": [
        {"vulnerability": "Lid leak — Hydro Flask lid is consistently rated more secure", "evidence": "Multiple Stanley defectors cite Hydro Flask lid security as the reason for switching. 'The lid difference is night and day.'", "fix_recommendation": "Redesign lid seal to prevent leaking at angles up to 45 degrees."},
        {"vulnerability": "Powder coat durability inferior to Hydro Flask", "evidence": "Hydro Flask reviews praise finish at 2+ years. Stanley reports chipping at 3-5 months.", "fix_recommendation": "Invest in more durable finish technology or introduce a finish warranty."},
        {"vulnerability": "Customer service response — Hydro Flask same-day replacement is the benchmark", "evidence": "Hydro Flask customers describe same-day replacement as brand-defining. Stanley customers report weeks-long warranty processes.", "fix_recommendation": "Implement same-day replacement policy for verified lid defect complaints."},
    ],
    "market_opportunity": "Stanley owns the daily commuter and gifting markets with superior cupholder fit, handle ergonomics, and color variety. Fix the lid and paint to neutralize Hydro Flask's primary competitive argument.",
    "positioning_statement": "The tumbler that fits your life — your cupholder, your hand, your style. Handle included. Straw included. Cupholder fit guaranteed.",
    "head_to_head_scores": {
        "quality_perception":  {"mine": 7, "competitor": 9},
        "value_for_money":     {"mine": 8, "competitor": 6},
        "customer_service":    {"mine": 5, "competitor": 9},
        "shipping_packaging":  {"mine": 8, "competitor": 7},
        "ease_of_use":         {"mine": 9, "competitor": 5},
    },
}

SENTIMENT_TRENDS = {
    "monthly_data": [
        {"month":"2025-06","review_count":18,"average_rating":4.3,"verified_purchase_rate":78.0,"complaint_rate":17.0,"praise_rate":61.0},
        {"month":"2025-07","review_count":21,"average_rating":4.2,"verified_purchase_rate":76.0,"complaint_rate":19.0,"praise_rate":57.0},
        {"month":"2025-08","review_count":24,"average_rating":4.1,"verified_purchase_rate":74.0,"complaint_rate":21.0,"praise_rate":54.0},
        {"month":"2025-09","review_count":19,"average_rating":4.0,"verified_purchase_rate":73.0,"complaint_rate":26.0,"praise_rate":53.0},
        {"month":"2025-10","review_count":22,"average_rating":3.9,"verified_purchase_rate":71.0,"complaint_rate":32.0,"praise_rate":45.0},
        {"month":"2025-11","review_count":17,"average_rating":3.8,"verified_purchase_rate":70.0,"complaint_rate":35.0,"praise_rate":41.0},
        {"month":"2025-12","review_count":28,"average_rating":4.1,"verified_purchase_rate":77.0,"complaint_rate":25.0,"praise_rate":54.0},
        {"month":"2026-01","review_count":16,"average_rating":4.0,"verified_purchase_rate":75.0,"complaint_rate":31.0,"praise_rate":44.0},
        {"month":"2026-02","review_count":14,"average_rating":3.9,"verified_purchase_rate":71.0,"complaint_rate":36.0,"praise_rate":43.0},
        {"month":"2026-03","review_count":11,"average_rating":3.8,"verified_purchase_rate":73.0,"complaint_rate":36.0,"praise_rate":45.0},
        {"month":"2026-04","review_count":9, "average_rating":3.7,"verified_purchase_rate":67.0,"complaint_rate":44.0,"praise_rate":33.0},
        {"month":"2026-05","review_count":8, "average_rating":3.6,"verified_purchase_rate":63.0,"complaint_rate":50.0,"praise_rate":25.0},
    ],
    "trend_direction": "declining",
    "trend_magnitude": -7.5,
    "spike_months": ["2026-04", "2026-05"],
    "insight": (
        "Sentiment is declining — average rating dropped from 4.3 in June 2025 to 3.6 in May 2026, "
        "a 0.7-star decline over 12 months. Complaint rate tripled from 17% to 50%. "
        "Lid issue is the primary driver. Complaint spike in April-May 2026 correlates with "
        "increased social media coverage of lid leak incidents."
    ),
}

DEMO_DATA = {
    "stanley": {
        "product_info":    STANLEY_PRODUCT_INFO,
        "reviews_raw":     STANLEY_REVIEWS_RAW,
        "filter_summary":  STANLEY_FILTER_SUMMARY,
        "analysis":        STANLEY_ANALYSIS,
        "trends":          SENTIMENT_TRENDS,
    },
    "hydroflask": {
        "product_info":  HYDROFLASK_PRODUCT_INFO,
        "reviews_raw":   HYDROFLASK_REVIEWS_SAMPLE,
    },
    "competitor_gap": COMPETITOR_GAP_ANALYSIS,
}


# ─────────────────────────────────────────────────────────────────────────────
# get_demo_data() — bridge for app.py compatibility
# ─────────────────────────────────────────────────────────────────────────────

def get_demo_data(product_num: int = 1) -> dict:
    trusted_raw  = [r for r in STANLEY_REVIEWS_RAW if r["id"].startswith("R")]
    filtered_raw = [r for r in STANLEY_REVIEWS_RAW if r["id"].startswith("F")]

    trusted_df  = pd.DataFrame(trusted_raw)
    filtered_df = pd.DataFrame(filtered_raw)
    all_df      = pd.DataFrame(STANLEY_REVIEWS_RAW)
    trusted_df["trust_score"]  = 80
    filtered_df["trust_score"] = 20

    fs = STANLEY_FILTER_SUMMARY
    verified_count = trusted_df["verified_purchase"].eq(True).sum()
    filter_stats = {
        "total_reviews_analyzed": fs["total_fetched"],
        "trusted_count":          fs["trusted_count"],
        "flagged_count":          fs["filtered_count"],
        "fake_percentage":        fs["fake_percentage"],
        "verified_purchase_rate": round(verified_count / len(trusted_df) * 100, 1),
        "average_trust_score":    80.0,
    }

    pi = {
        "title":          STANLEY_PRODUCT_INFO["title"],
        "asin":           STANLEY_PRODUCT_INFO["asin"],
        "overall_rating": STANLEY_PRODUCT_INFO["rating"],
        "total_reviews":  STANLEY_PRODUCT_INFO["ratings_total"],
        "image_url":      STANLEY_PRODUCT_INFO["image_url"],
        "brand":          STANLEY_PRODUCT_INFO.get("brand", "Stanley"),
        "price":          STANLEY_PRODUCT_INFO.get("price", "$45.00"),
    }

    raw_a = STANLEY_ANALYSIS
    level_map = {"CRITICAL": "critical", "HIGH": "high", "MEDIUM": "medium", "LOW": "low"}

    complaint_themes = []
    for ct in raw_a.get("complaint_themes", []):
        si = ct.get("star_impact", 0)
        complaint_themes.append({
            "theme":                     ct["theme"],
            "frequency_pct":             ct["frequency_pct"],
            "emotional_intensity":       level_map.get(ct.get("emotional_intensity","medium").upper(), "medium"),
            "example_quotes":            ct.get("example_quotes", []),
            "improvement_recommendation": ct.get("recommendation", ""),
            "estimated_rating_impact":   f"{si:+.1f} stars if fixed" if isinstance(si, (int, float)) else str(si),
        })

    praise_themes = []
    for pt in raw_a.get("praise_themes", []):
        praise_themes.append({
            "theme":          pt["theme"],
            "frequency_pct":  pt["frequency_pct"],
            "example_quotes": pt.get("example_quotes", []),
            "marketing_angle": pt.get("recommendation", ""),
        })

    risk_alerts = []
    for ra in raw_a.get("risk_alerts", []):
        lv = ra.get("level", "medium")
        risk_alerts.append({
            "alert_type":         ra.get("alert", ""),
            "severity":           level_map.get(lv.upper(), lv.lower()),
            "description":        ra.get("alert", ""),
            "recommended_action": ra.get("action", ""),
        })

    persona_extras = [
        ("Cupholder compatibility, all-day cold retention, one-handed handle", "Lid leaking in work bag and damaging electronics"),
        ("40oz size for all-day hydration, ice retention, visible progress", "Straw odor after weeks of use"),
        ("Limited edition colors, social currency, gifting variety",           "Paint chipping on limited edition colors"),
        ("Handle for quick access, all-day ice retention, durability",         "Weight when full during long shifts"),
    ]
    buyer_personas = []
    for i, bp in enumerate(raw_a.get("buyer_personas", [])):
        loves, frustrates = persona_extras[i] if i < len(persona_extras) else ("Great product", "Minor issues")
        buyer_personas.append({
            "persona_name":         bp.get("name", ""),
            "percentage":           bp.get("share_pct", 25),
            "description":          bp.get("description", ""),
            "what_they_love":       loves,
            "what_frustrates_them": frustrates,
            "marketing_message":    bp.get("key_message", ""),
        })

    analysis = {
        "overall_health_score":    raw_a.get("health_score", 74),
        "executive_summary":       raw_a.get("executive_summary", ""),
        "complaint_themes":        complaint_themes,
        "praise_themes":           praise_themes,
        "listing_bullets":         raw_a.get("listing_bullets", []),
        "listing_title_suggestion": "Stanley Quencher H2.0 FlowState Tumbler 40oz | Cupholder Compatible | Keeps Ice 12+ Hours | Ergonomic Handle | 40+ Colors | Straw Lid Included",
        "buyer_personas":          buyer_personas,
        "risk_alerts":             risk_alerts,
        "keyword_opportunities":   raw_a.get("keywords", []),
        "pricing_sentiment":       "Customers accept the $45 price when the product performs well. Paint chipping and lid leaking create a strong perceived value mismatch.",
        "seasonal_patterns":       "Strong gifting spikes around holidays and wedding season. Limited edition color drops generate their own demand spikes independent of seasons.",
    }

    from collections import Counter
    ratings = [r.get("rating") for r in STANLEY_REVIEWS_RAW if r.get("rating")]
    rc = Counter(ratings)
    total_r = len(ratings)
    rating_distribution = {
        str(s): {"count": rc.get(s, 0), "percentage": round(rc.get(s, 0) / total_r * 100, 1) if total_r else 0.0}
        for s in range(1, 6)
    }

    hf_df = pd.DataFrame(HYDROFLASK_REVIEWS_SAMPLE)
    hf_df["trust_score"] = 78
    hf_pi = {
        "title":          HYDROFLASK_PRODUCT_INFO["title"],
        "asin":           HYDROFLASK_PRODUCT_INFO["asin"],
        "overall_rating": HYDROFLASK_PRODUCT_INFO["rating"],
        "total_reviews":  HYDROFLASK_PRODUCT_INFO["ratings_total"],
        "image_url":      HYDROFLASK_PRODUCT_INFO["image_url"],
    }
    hf_verified = hf_df["verified_purchase"].eq(True).sum()

    return {
        "product_info":        pi,
        "reviews_df":          all_df,
        "trusted_reviews":     trusted_df,
        "filter_stats":        filter_stats,
        "analysis":            analysis,
        "trends":              SENTIMENT_TRENDS,
        "rating_distribution": rating_distribution,
        "has_competitor":      True,
        "competitor": {
            "product_info":        hf_pi,
            "reviews_df":          hf_df,
            "trusted_reviews":     hf_df,
            "filter_stats": {
                "total_reviews_analyzed": len(hf_df),
                "trusted_count":          len(hf_df),
                "flagged_count":          0,
                "fake_percentage":        0.0,
                "verified_purchase_rate": round(hf_verified / len(hf_df) * 100, 1),
                "average_trust_score":    78.0,
            },
            "trends":              SENTIMENT_TRENDS,
            "rating_distribution": {
                "5": {"count": 5, "percentage": 50.0},
                "4": {"count": 2, "percentage": 20.0},
                "3": {"count": 2, "percentage": 20.0},
                "2": {"count": 1, "percentage": 10.0},
                "1": {"count": 0, "percentage": 0.0},
            },
        },
        "gap_analysis": COMPETITOR_GAP_ANALYSIS,
    }


# ─────────────────────────────────────────────────────────────────────────────
# SELF-CHECK
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    total   = len(STANLEY_REVIEWS_RAW)
    trusted = len([r for r in STANLEY_REVIEWS_RAW if r["id"].startswith("R")])
    filtered = len([r for r in STANLEY_REVIEWS_RAW if r["id"].startswith("F")])
    ok = (total == STANLEY_FILTER_SUMMARY["total_fetched"] and
          trusted == STANLEY_FILTER_SUMMARY["trusted_count"] and
          filtered == STANLEY_FILTER_SUMMARY["filtered_count"])
    print(f"Total:    {total}  (expected 247)")
    print(f"Trusted:  {trusted}  (expected 189)")
    print(f"Filtered: {filtered}  (expected 58)")
    print(f"Health:   {STANLEY_ANALYSIS['health_score']}/100")
    print(f"\n{'✅ Numbers are consistent' if ok else '❌ MISMATCH — fix required'}")
