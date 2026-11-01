---
title: "What is Glass Substrate — and Why It Could Reshape the Chip Packaging Industry?"
tags: [AI, Semiconductor]
date: 2026-10-31
author: "Colin Tan"
excerpt: "For thirty years chip substrates have been organic resin. AI packages have outgrown it. Intel shipped the first glass-core processor in January 2026 — and the race to scale it will be decided largely in Asia."
---

<p class="xp-lede">The chip inside your laptop sits on a substrate &#8212; a multi-layer board that connects the silicon die to the circuit board beneath it. For thirty years, that substrate has been made of organic resin. It works, mostly. But as AI chips grow larger, hotter, and more densely wired, organic substrates are warping under the heat, limiting how fine the wiring can get, and cracking yields. Glass is the answer the industry has converged on. In January 2026, Intel shipped the first commercial processor built on a glass core substrate. The race that follows will be decided largely in Asia.</p>

<div class="xp-two-col">
  <div>
    <p><b>What a substrate does &#8212; and why organic is failing.</b> A chip substrate is the mechanical and electrical bridge between a silicon die and the printed circuit board. It fans out the die&#8217;s dense array of contact points &#8212; spaced as little as 100 microns apart &#8212; into the coarser pitch the board can handle. It carries power in and signals out. Every AI accelerator, every processor, every DRAM package sits on one. For decades, the dominant material has been ABF &#8212; Ajinomoto Build-up Film, an organic resin originally developed for food packaging. ABF is inexpensive, compatible with existing equipment, and yielded to 3nm-class chips without modification. Its problem is physics: organic materials expand at roughly 15&#8211;17 parts per million per degree Celsius. Silicon expands at 3 ppm/&#xB0;C. At the temperatures of chip assembly &#8212; often above 260&#xB0;C &#8212; that mismatch generates stress. The substrate warps. Warpage kills yield and sets a hard upper bound on package size.</p>
    <p><b>The glass advantage: CTE, density, and signal integrity.</b> Glass expands at 3&#8211;5 ppm/&#xB0;C &#8212; nearly matching silicon. When the chip package heats up during assembly, chip and substrate move together rather than fighting each other. Warpage falls dramatically, yields improve, and the package can be scaled to sizes that organic substrates cannot reach without cracking. The second advantage is wiring density. Organic ABF resins limit how fine the lines and spaces between wires can be. Glass can support through-glass vias (TGVs) at pitches below 10 microns and enable routing densities up to ten times higher than ABF. The third is signal integrity: glass substrates cut signal loss by up to 40% versus organic, and improve data-movement power efficiency by as much as 50% &#8212; directly relevant for AI inference workloads where memory bandwidth is the binding constraint.</p>
  </div>
  <div>
    <p><b>Two approaches &#8212; and the companies placing bets.</b> The industry has split into two camps. The first uses a <em>glass core substrate</em>: the organic resin core layer is replaced with glass, while the build-up layers on top remain organic. Intel pioneered this approach and shipped it commercially in the Xeon 6+ &#8220;Clearwater Forest&#8221; processor, unveiled at CES 2026 &#8212; the first mass-produced chip on a glass core. Intel manufactures glass cores at its Chandler, Arizona facility and is offering the technology through Intel Foundry. It holds over 600 glass substrate patents.</p>
    <p>The second approach uses a <em>glass interposer</em>: a glass wafer replaces the silicon interposer that sits between chiplets and the organic substrate. Samsung Electro-Mechanics has moved its Sejong pilot line into full-scale validation, targeting mass production in H2 2026 and focusing on glass interposers for HBM4 memory packaging. Absolics &#8212; a US-Georgia subsidiary of South Korea&#8217;s SKC, backed by Applied Materials &#8212; is in pre-qualification with AMD and Amazon AWS. TSMC is co-developing glass-based fan-out panel-level packaging with Corning. BOE in China targeted glass substrate mass production by mid-2026. Glass suppliers AGC, Corning, SCHOTT, and Nippon Electric Glass are scaling capacity for all of them.</p>
    <p><b>The cost gap &#8212; and how it closes.</b> Glass substrates currently cost 2&#8211;3 times as much as their ABF equivalents. Yield is lower, at 75&#8211;85% against 90&#8211;95% for organic. The path to cost parity runs through panel size: the industry is moving from 300mm round wafers to 600mm &#xD7; 600mm rectangular glass panels, which cut substrate cost by an estimated 40&#8211;60% through area utilisation. That transition is expected to complete between 2028 and 2030, pulling glass within striking distance of premium ABF pricing for high-end packages.</p>
  </div>
</div>

<figure class="xp-exhibit">
  <div class="xp-exhibit-pill">EXHIBIT 1</div>
  <h3>The core problem glass solves: thermal expansion mismatch between chip and substrate</h3>
  <p class="xp-exhibit-sub">Coefficient of Thermal Expansion (CTE) in parts per million per &#xB0;C; lower and closer to silicon (3 ppm/&#xB0;C) means less mechanical stress during chip assembly</p>

  <svg viewBox="0 0 720 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Horizontal bar chart comparing CTE values of organic ABF substrate at 16 ppm, glass at 4 ppm, and silicon at 3 ppm">

    <line x1="120" y1="30" x2="120" y2="185" stroke="#D8DEE6" stroke-width="1"/>
    <line x1="260" y1="30" x2="260" y2="185" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="400" y1="30" x2="400" y2="185" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="540" y1="30" x2="540" y2="185" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="680" y1="30" x2="680" y2="185" stroke="#D8DEE6" stroke-width="0.6"/>

    <text x="120" y="198" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-size="10" fill="#5B6675">0</text>
    <text x="260" y="198" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-size="10" fill="#5B6675">5</text>
    <text x="400" y="198" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-size="10" fill="#5B6675">10</text>
    <text x="540" y="198" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-size="10" fill="#5B6675">15</text>
    <text x="680" y="198" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-size="10" fill="#5B6675">20</text>
    <text x="400" y="210" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#5B6675">ppm / &#xB0;C (lower = less stress on chip)</text>

    <rect x="120" y="47" width="448" height="36" fill="#C0392B" rx="1" opacity="0.85"/>
    <text x="10"  y="70" text-anchor="start" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10.5" fill="#0A2240">Organic ABF</text>
    <text x="578" y="70" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="12" fill="#C0392B">16 ppm/&#xB0;C</text>
    <line x1="204" y1="43" x2="568" y2="43" stroke="#C0392B" stroke-width="1.5" stroke-dasharray="3,2"/>
    <text x="386" y="38" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#C0392B">mismatch stress zone &#x2192; warpage</text>

    <rect x="120" y="97" width="112" height="36" fill="#00A6A6" rx="1"/>
    <rect x="120" y="97" width="140" height="36" fill="#00A6A6" rx="1" opacity="0.35"/>
    <text x="10"  y="120" text-anchor="start" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10.5" fill="#0A2240">Glass substrate</text>
    <text x="270" y="120" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="12" fill="#00A6A6">3&#x2013;5 ppm/&#xB0;C</text>
    <text x="270" y="133" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#00A6A6">near-perfect match to silicon</text>

    <rect x="120" y="145" width="84" height="36" fill="#0A2240" rx="1"/>
    <text x="10"  y="168" text-anchor="start" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10.5" fill="#0A2240">Silicon chip</text>
    <text x="214" y="168" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="12" fill="#0A2240">3 ppm/&#xB0;C</text>
    <text x="214" y="181" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">reference baseline</text>

    <line x1="204" y1="30" x2="204" y2="185" stroke="#E8A33D" stroke-width="1.5" stroke-dasharray="4,3"/>
    <text x="206" y="42" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8" fill="#E8A33D">silicon CTE</text>

  </svg>

  <p class="xp-exhibit-source">Source: Industry CTE values: organic ABF substrate 15&#x2013;17 ppm/&#xB0;C (Ajinomoto Fine-Techno technical data); glass substrate 3&#x2013;5 ppm/&#xB0;C; silicon chip ~3 ppm/&#xB0;C (standard semiconductor physics reference). TrendForce &#8220;Glass Substrates Are Breaking Through the AI Chip Packaging Bottleneck&#8221; (May 2026); Future Markets Inc. Global Glass Substrates for Semiconductors Market 2026&#x2013;2036.</p>
</figure>

<div class="xp-two-col">
  <div>
    <p><b>Why AI is the forcing function.</b> The shift to glass is not happening because organic substrates suddenly stopped working. It is happening because AI chip packages have grown to sizes and power densities that push organic substrates into failure modes that were previously theoretical. The NVIDIA Blackwell GB200 package spans more than 100mm &#xD7; 100mm &#8212; at that scale, thermal-expansion mismatch creates stress that ABF substrates cannot reliably absorb without warping. The next generation of AI accelerators is expected to push further, to 120mm &#xD7; 120mm and beyond. At those dimensions, glass is not optional &#8212; it is the only material that maintains mechanical stability. The co-packaged optics (CPO) trend compounds the problem: optical components are even more sensitive to substrate warpage than silicon chiplets.</p>
  </div>
  <div>
    <p><b>Asia&#8217;s role in the glass substrate supply chain.</b> The glass substrate industry is overwhelmingly an Asian story. South Korea leads on substrate manufacturing: Samsung Electro-Mechanics, LG Innotek, and SKC&#8217;s Absolics (whose Georgia facility is US-flagged but Korean-owned) hold the deepest technical know-how. Japan dominates glass and chemical supply: Corning&#8217;s Japanese operations, AGC, SCHOTT Japan, and Nippon Electric Glass are the primary glass feedstock suppliers; Ibiden, Shinko, and Toppan dominate the build-up film layers that sit above the glass core. Taiwan&#8217;s ASE and TSMC&#8217;s packaging arm are integrating glass into advanced fan-out processes. China&#8217;s BOE has committed to glass substrate mass production. The one structural risk: through-glass via drilling equipment is dominated by LPKF, a German company &#8212; a potential chokepoint analogous to ASML in EUV lithography.</p>
  </div>
</div>

<figure class="xp-exhibit">
  <div class="xp-exhibit-pill">EXHIBIT 2</div>
  <h3>Glass substrate advantages over organic ABF: three dimensions that matter for AI silicon</h3>
  <p class="xp-exhibit-sub">Performance improvements of glass vs organic ABF substrate; bars show magnitude of improvement in each dimension; data from industry sources as of 2026</p>

  <svg viewBox="0 0 720 252" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Three horizontal bars showing glass substrate advantages: routing density up to 10x higher, signal loss 40% lower, power efficiency 50% better">

    <rect x="0" y="0" width="720" height="28" fill="#EEF2F7" rx="1"/>
    <text x="120" y="18" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10" fill="#5B6675">METRIC</text>
    <text x="460" y="18" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10" fill="#5B6675">GLASS ADVANTAGE OVER ORGANIC ABF</text>
    <text x="660" y="18" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10" fill="#5B6675">GAIN</text>

    <rect x="0"   y="30" width="720" height="72" fill="#ffffff"/>
    <text x="10"  y="65" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="11" fill="#0A2240">Routing density</text>
    <text x="10"  y="79" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9" fill="#5B6675">lines / spaces in substrate</text>
    <text x="10"  y="93" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9" fill="#5B6675">wiring layers</text>
    <rect x="240" y="44" width="440" height="44" fill="#0A2240" rx="1"/>
    <rect x="240" y="44" width="44"  height="44" fill="#D8DEE6" rx="1"/>
    <text x="250" y="71" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8" fill="#5B6675">organic</text>
    <text x="480" y="70" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="18" fill="#ffffff">up to 10&#xD7;</text>
    <text x="692" y="70" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="13" fill="#0A2240">+900%</text>
    <line x1="0" y1="102" x2="720" y2="102" stroke="#D8DEE6" stroke-width="0.8"/>

    <rect x="0"   y="102" width="720" height="72" fill="#F8F9FB"/>
    <text x="10"  y="137" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="11" fill="#0A2240">Signal loss</text>
    <text x="10"  y="151" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9" fill="#5B6675">insertion loss vs ABF</text>
    <text x="10"  y="165" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9" fill="#5B6675">at high frequency</text>
    <rect x="240" y="116" width="440" height="44" fill="#E8EFF5" rx="1"/>
    <rect x="240" y="116" width="176" height="44" fill="#00A6A6" rx="1"/>
    <text x="252" y="142" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="14" fill="#ffffff">&#x2212;40%</text>
    <text x="430" y="142" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#9FB2CC">organic ABF baseline</text>
    <text x="692" y="142" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="13" fill="#00A6A6">40% less</text>
    <line x1="0"  y1="174" x2="720" y2="174" stroke="#D8DEE6" stroke-width="0.8"/>

    <rect x="0"   y="174" width="720" height="78" fill="#ffffff"/>
    <text x="10"  y="209" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="11" fill="#0A2240">Data-movement</text>
    <text x="10"  y="223" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="11" fill="#0A2240">power efficiency</text>
    <text x="10"  y="237" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9" fill="#5B6675">pJ per bit transferred</text>
    <rect x="240" y="188" width="440" height="44" fill="#E8EFF5" rx="1"/>
    <rect x="240" y="188" width="220" height="44" fill="#F2620F" rx="1"/>
    <text x="252" y="214" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="14" fill="#ffffff">&#x2212;50%</text>
    <text x="474" y="214" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#9FB2CC">organic ABF baseline</text>
    <text x="692" y="214" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="13" fill="#F2620F">50% better</text>
  </svg>

  <p class="xp-exhibit-source">Source: TokenRing &#8220;The Glass Revolution: Intel and Samsung Are Shattering the Silicon Packaging Ceiling&#8221; (January 2026); TrendForce glass substrate analysis (May 2026); Meticulous Next&#8482; &#8220;Glass Substrates and the Future of Chip Packaging&#8221; market brief (2026). Signal loss and power efficiency figures are industry guidance ranges; routing density improvement is relative to standard ABF build-up layers. Actual gains depend on design node and package architecture.</p>
</figure>

<blockquote class="xp-pull-quote">
  <p>&#8220;Glass substrates could capture 20&#x2013;30% of the advanced packaging market by 2036. The market grows from USD 0.15&#x2013;0.30 billion in 2026 to USD 8&#x2013;12 billion by 2036 &#8212; a 45&#x2013;50% CAGR that makes it one of the fastest-growing segments in semiconductor materials.&#8221;</p>
  <cite>Meticulous Next&#x2122; Foresight Brief &#8212; Glass Core Substrates and the Future of Chip Packaging, 2026</cite>
</blockquote>

<div class="xp-two-col">
  <div>
    <p><b>Three predictions for 2027&#x2013;2030.</b> First: glass core substrates will be the default for AI accelerators above $8,000 per chip by 2028. NVIDIA&#8217;s post-Rubin generation and the next Google TPU will both ship on glass cores, pulling the technology from Intel-only into the AI silicon mainstream. The warpage constraint at package sizes above 110mm &#xD7; 110mm makes this less a strategic choice than a physical necessity. The question is not whether NVIDIA adopts glass &#8212; it is whether TSMC&#8217;s glass-based packaging or Intel Foundry&#8217;s wins that business.</p>
    <p>Second: Samsung Electro-Mechanics will win at least one major HBM4 glass interposer qualification win before end of 2027. The technical case is strong &#8212; HBM4&#8217;s tighter bump pitch and power density make organic interposers marginal &#8212; and Samsung&#8217;s Sejong facility is the furthest along of any Asian substrate maker in glass interposer scale-up. SK Hynix, the dominant HBM supplier, has every incentive to qualify Samsung Electro-Mechanics.</p>
  </div>
  <div>
    <p>Third, and most contrarian: glass substrate cost parity with premium ABF arrives no earlier than 2031, two years later than the industry consensus. The 600mm &#xD7; 600mm panel transition will take longer than projected. Through-glass via drilling remains slow, equipment supply from LPKF is constrained, and yield ramp curves for glass are historically steeper than for organic. The companies that build glass substrate volume fastest &#8212; Samsung Electro-Mechanics and Absolics &#8212; will price it at a premium through 2030, not a commodity. The beneficiaries of that premium window are the glass suppliers: AGC and Nippon Electric Glass, both Japanese, are positioned to generate outsized margins from semiconductor-grade glass sheet supply throughout the decade.</p>
    <p><b>The structural risk no one discusses.</b> LPKF, a German laser equipment maker, holds a near-monopoly on the laser drilling systems that form through-glass vias. The same export-control dynamic that has defined EUV (ASML) and advanced deposition equipment could apply here if geopolitical conditions deteriorate further. Any Asian glass substrate maker investing heavily in capacity faces a single-point equipment dependency that is, as of now, entirely outside Asia&#8217;s control.</p>
  </div>
</div>

<figure class="xp-exhibit">
  <div class="xp-exhibit-pill">EXHIBIT 3</div>
  <h3>Glass substrate race: four leading players across two technical approaches</h3>
  <p class="xp-exhibit-sub">Status as of October 2026; glass core substrates replace the organic core layer; glass interposers replace the silicon interposer between chiplets and substrate</p>

  <svg viewBox="0 0 720 228" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Comparison table of Intel, Samsung Electro-Mechanics, Absolics, and TSMC glass substrate programs showing approach, facility, status, and target customers">

    <rect x="0"   y="0" width="720" height="30" fill="#0A2240"/>
    <text x="74"  y="20" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10" fill="#ffffff">COMPANY</text>
    <text x="224" y="20" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10" fill="#ffffff">APPROACH</text>
    <text x="364" y="20" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10" fill="#ffffff">FACILITY</text>
    <text x="499" y="20" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10" fill="#ffffff">STATUS (OCT 2026)</text>
    <text x="645" y="20" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10" fill="#ffffff">KEY CUSTOMERS</text>

    <line x1="149" y1="30" x2="149" y2="228" stroke="#D8DEE6" stroke-width="0.7"/>
    <line x1="299" y1="30" x2="299" y2="228" stroke="#D8DEE6" stroke-width="0.7"/>
    <line x1="429" y1="30" x2="429" y2="228" stroke="#D8DEE6" stroke-width="0.7"/>
    <line x1="569" y1="30" x2="569" y2="228" stroke="#D8DEE6" stroke-width="0.7"/>

    <rect x="0" y="30" width="720" height="50" fill="#ffffff"/>
    <line x1="0" y1="80" x2="720" y2="80" stroke="#D8DEE6" stroke-width="0.6"/>
    <text x="10"  y="50" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="11" fill="#0A2240">Intel</text>
    <text x="10"  y="65" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">United States</text>
    <text x="159" y="50" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#0A2240">Glass core substrate</text>
    <text x="159" y="63" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">Replaces organic core;      </text>
    <text x="159" y="74" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">600+ patents</text>
    <text x="309" y="50" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#0A2240">Chandler, Arizona</text>
    <text x="309" y="63" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">High-volume manufacturing</text>
    <rect x="431" y="33" width="136" height="24" fill="rgba(0,166,166,0.12)" rx="1"/>
    <text x="499" y="50" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10" fill="#00A6A6">&#x2713; Commercial (Xeon 6+)</text>
    <text x="499" y="65" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#00A6A6">First mass production, CES 2026</text>
    <text x="579" y="50" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#0A2240">Intel internal &#xB7; Intel Foundry</text>
    <text x="579" y="63" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">offering to external customers</text>

    <rect x="0" y="80" width="720" height="50" fill="#F8F9FB"/>
    <line x1="0" y1="130" x2="720" y2="130" stroke="#D8DEE6" stroke-width="0.6"/>
    <text x="10"  y="100" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="11" fill="#0A2240">Samsung</text>
    <text x="10"  y="113" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="11" fill="#0A2240">Electro-Mech.</text>
    <text x="10"  y="126" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">South Korea</text>
    <text x="159" y="100" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#0A2240">Glass interposer</text>
    <text x="159" y="113" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">Targets HBM4 packaging;</text>
    <text x="159" y="124" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">replaces silicon interposer</text>
    <text x="309" y="100" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#0A2240">Sejong, South Korea</text>
    <text x="309" y="113" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">Pilot &#x2192; full validation 2026</text>
    <rect x="431" y="83" width="136" height="24" fill="rgba(232,163,61,0.14)" rx="1"/>
    <text x="499" y="100" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10" fill="#E8A33D">&#x25B2; Mass prod. target H2 2026</text>
    <text x="499" y="113" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#E8A33D">Full validation underway</text>
    <text x="579" y="100" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#0A2240">SK Hynix (HBM4 target)</text>
    <text x="579" y="113" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">Samsung Electronics</text>

    <rect x="0" y="130" width="720" height="50" fill="#ffffff"/>
    <line x1="0" y1="180" x2="720" y2="180" stroke="#D8DEE6" stroke-width="0.6"/>
    <text x="10"  y="150" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="11" fill="#0A2240">Absolics</text>
    <text x="10"  y="163" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">SKC subsidiary, Korea/US</text>
    <text x="10"  y="176" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">Applied Materials backer</text>
    <text x="159" y="150" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#0A2240">Glass core substrate</text>
    <text x="159" y="163" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">Panel-level; targets</text>
    <text x="159" y="174" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">hyperscaler custom ASICs</text>
    <text x="309" y="150" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#0A2240">Covington, Georgia (US)</text>
    <text x="309" y="163" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">First commercial plant</text>
    <rect x="431" y="133" width="136" height="24" fill="rgba(232,163,61,0.14)" rx="1"/>
    <text x="499" y="150" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10" fill="#E8A33D">&#x25B2; Pre-qualification 2026</text>
    <text x="499" y="163" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#E8A33D">Volume ramp targeted 2027</text>
    <text x="579" y="150" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#0A2240">AMD &#xB7; Amazon AWS</text>
    <text x="579" y="163" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">In pre-qualification (early 2026)</text>

    <rect x="0" y="180" width="720" height="48" fill="#F8F9FB"/>
    <text x="10"  y="200" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="11" fill="#0A2240">TSMC / Corning</text>
    <text x="10"  y="213" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">Taiwan / United States JV</text>
    <text x="159" y="200" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#0A2240">Glass fan-out panel</text>
    <text x="159" y="213" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">Glass-based fan-out panel-level</text>
    <text x="159" y="224" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">packaging (FOPLP)</text>
    <text x="309" y="200" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#0A2240">Hsinchu, Taiwan</text>
    <text x="309" y="213" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">Co-development with Corning</text>
    <rect x="431" y="183" width="136" height="24" fill="rgba(10,34,64,0.08)" rx="1"/>
    <text x="499" y="200" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-weight="700" font-size="10" fill="#0A2240">Development phase</text>
    <text x="499" y="213" text-anchor="middle" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">Production timeline TBD</text>
    <text x="579" y="200" font-family="'Helvetica Neue',Arial,sans-serif" font-size="9.5" fill="#0A2240">Apple &#xB7; NVIDIA (targeted)</text>
    <text x="579" y="213" font-family="'Helvetica Neue',Arial,sans-serif" font-size="8.5" fill="#5B6675">Next-gen AI accelerators</text>
  </svg>

  <p class="xp-exhibit-source">Source: TokenRing &#8220;The Glass Revolution: Intel and Samsung Are Shattering the Silicon Packaging Ceiling&#8221; (January 2026) via Observer-Reporter; TrendForce glass substrates tag (trendforce.com); Future Markets Inc. Global Market for Glass Substrates for Semiconductors 2026&#x2013;2036; Meticulous Next&#x2122; Brief 2026. &#x2713; = commercial production confirmed; &#x25B2; = targeting / pre-production.</p>
</figure>

<div class="xp-callout">
  <div class="xp-callout-label">The Bottom Line</div>
  <p>Glass substrate is not an incremental packaging improvement. It is a material transition that the semiconductor industry is making under duress &#8212; forced by AI chip packages that have outgrown what organic resins can mechanically support. Intel has proven the technology is manufacturable at volume. Samsung, Absolics, and TSMC are racing to build the next industrial scale behind it. The market grows from a standing start of roughly $200 million today to an estimated $8&#x2013;12 billion by 2036 at 45&#x2013;50% annual growth &#8212; one of the steepest compound curves in semiconductor materials history. The risk for every Asian substrate maker watching this: LPKF&#8217;s laser drilling monopoly is the ASML problem in miniature. Asia is building the factories; a single European equipment maker controls the key to getting through the glass.</p>
</div>

<div class="xp-author-bio">
  <div class="xp-author-name">Colin Tan &nbsp;&#xB7;&nbsp; Editor, Asia Tech Feed</div>
  <p>Colin covers semiconductors, AI infrastructure, and supply-chain dynamics across the Asia-Pacific region. He tracks advanced packaging transitions from chiplets and HBM to co-packaged optics and glass substrates for the daily ATF digest. Reach him at <a href="mailto:colin.tan@asiatechfeed.com" style="color:#00A6A6">colin.tan@asiatechfeed.com</a> or connect on LinkedIn.</p>
</div>

<div class="xp-footer-grid">
  <div class="xp-key-numbers">
    <div class="xp-kn-label">Key Numbers</div>
    <div class="xp-kn-item">
      <div class="xp-kn-val">3&#x2013;5</div>
      <div class="xp-kn-desc">Glass CTE (ppm/&#xB0;C)<br>vs 16 for organic ABF</div>
    </div>
    <div class="xp-kn-item">
      <div class="xp-kn-val">10&#xD7;</div>
      <div class="xp-kn-desc">Routing density increase<br>vs organic ABF</div>
    </div>
    <div class="xp-kn-item">
      <div class="xp-kn-val">&#x2212;40%</div>
      <div class="xp-kn-desc">Signal loss reduction<br>vs ABF substrates</div>
    </div>
    <div class="xp-kn-item">
      <div class="xp-kn-val">$10B</div>
      <div class="xp-kn-desc">Market by 2036<br>(from $0.2B in 2026)</div>
    </div>
    <div class="xp-kn-item">
      <div class="xp-kn-val">600+</div>
      <div class="xp-kn-desc">Intel glass substrate<br>patents (as of 2026)</div>
    </div>
  </div>
  <div class="xp-related">
    <div class="xp-related-label">Related Coverage</div>
    <div class="xp-related-item">
      <span class="xp-related-tag">EXPLAINER</span>
      <h4>What is Co-Packaged Optics (CPO) &#8212; and why it replaces the pluggable transceiver?</h4>
      <p>CPO integrates optical components directly into the chip package &#8212; a transition that requires substrate flatness guarantees that only glass can reliably provide at scale.</p>
    </div>
    <div class="xp-related-item">
      <span class="xp-related-tag">EXPLAINER</span>
      <h4>What is a chiplet, and why has packaging become the real chokepoint in chipmaking?</h4>
      <p>Glass substrates and chiplet architectures are co-evolving: larger multi-chiplet packages are the primary driver demanding glass&#8217;s superior warpage control.</p>
    </div>
    <div class="xp-related-item">
      <span class="xp-related-tag">REPORT</span>
      <h4>Asia Tech Feed on Semiconductors: Outlook H2 2026&#x2013;2027</h4>
      <p>Our semiconductor outlook covers the advanced packaging roadmap &#8212; including glass substrate adoption timelines, Samsung vs TSMC packaging share, and HBM4 integration.</p>
    </div>
  </div>
</div>
