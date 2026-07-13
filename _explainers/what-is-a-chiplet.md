---
title: "What is a Chiplet, and Why Has Packaging Become the Real Chokepoint in Chipmaking?"
tags: [AI, Semiconductor]
date: 2026-07-14
author: "Colin Tan"
excerpt: "Packaging, not the transistor, is now the constraint that decides whether an AI accelerator ships on time — and CoWoS capacity has become the industry's newest single point of failure."
---

<p class="xp-lede">For six decades, semiconductor progress meant one thing: shrinking transistors. That logic still holds for raw compute density — but it no longer describes what separates the chips that ship from the chips that don't. In 2026, the real chokepoint in AI silicon is not the lithography machine. It is the package.</p>

<div class="xp-two-col">
  <div>
    <p><b>What a chiplet is.</b> A chiplet is a small, modular die designed to connect to other dies within a single package rather than function as a standalone chip. Instead of manufacturing one enormous monolithic die containing every processor function — compute cores, memory controllers, I/O interfaces, accelerators — engineers divide that functionality across several smaller dies, each optimised for its task and fabricated on whichever process node makes economic sense.</p>
    <p>The yield logic is what drives adoption. The proportion of working dies on a wafer falls exponentially as die area grows. A monolithic flagship GPU approaching 600mm² on a leading node achieves 50–55% yield; a 100mm² chiplet consistently achieves 90% or better. Every failed die on a $20,000 wafer is wasted cost. Chiplets restructure that equation — at the price of a new engineering challenge: connecting them fast enough to behave as a single unified chip.</p>
  </div>
  <div>
    <p><b>Who pioneered it and where it stands.</b> AMD launched the modern chiplet era with its Zen architecture in 2017, separating CPU compute dies from the I/O die and manufacturing each on its optimal node. NVIDIA's Rubin and Intel's Granite Rapids follow the same discipline. Apple's M-series achieves related goals through tight memory-logic co-packaging rather than discrete chiplet interconnects — a distinction that underlines chiplets as an economic strategy, not a single rigid architecture.</p>
    <p>What every chiplet design shares is the package. The package must carry data between dies at bandwidths that would have required on-chip wiring a generation ago. A modern AI accelerator demands terabytes per second of die-to-die interconnect. That demand has spawned an entirely new tier of semiconductor infrastructure — and exposed the industry's newest single point of failure.</p>
  </div>
</div>

<!-- ── EXHIBIT 1: Yield vs Die Area curve ────────────────── -->
<figure class="xp-exhibit">
  <div class="xp-exhibit-pill">EXHIBIT 1</div>
  <h3>Chiplet yield advantage: why smaller dies dominate leading-edge economics</h3>
  <p class="xp-exhibit-sub">Illustrative yield curve using Poisson model (D = 0.1 defects/cm²); annotated with real-world die examples</p>

  <svg viewBox="0 0 720 248" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Line chart showing yield falling exponentially with die area">
    <defs>
      <style>
        .yl{font-family:'Helvetica Neue',Arial,sans-serif;font-size:10.5px;fill:#5B6675}
        .ya{font-family:'Helvetica Neue',Arial,sans-serif;font-size:10px;fill:#5B6675}
        .yb{font-family:'Helvetica Neue',Arial,sans-serif;font-weight:700;font-size:10px;fill:#0A2240}
        .yz{font-family:'Helvetica Neue',Arial,sans-serif;font-size:9.5px;fill:#00A6A6}
        .yh{font-family:'Helvetica Neue',Arial,sans-serif;font-size:9.5px;fill:#F2620F}
        .ytitle{font-family:'Helvetica Neue',Arial,sans-serif;font-size:10px;fill:#5B6675}
      </style>
      <!-- Arrow marker for annotation lines -->
      <marker id="yArr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <polygon points="0 0,6 3,0 6" fill="#F2620F"/>
      </marker>
      <marker id="tArr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <polygon points="0 0,6 3,0 6" fill="#00A6A6"/>
      </marker>
    </defs>

    <!-- Chart area: x=62 to x=690 (628px wide), y=25 to y=215 (190px tall) -->
    <!-- X: 0–800mm² → 628/800=0.785px/mm², offset x=62 -->
    <!-- Y: 0–100% → 190/100=1.9px/%, y_bottom=215 -->

    <!-- Gridlines Y at 20%=177, 40%=139, 60%=101, 80%=63 -->
    <line x1="62" y1="177" x2="690" y2="177" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="62" y1="139" x2="690" y2="139" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="62" y1="101" x2="690" y2="101" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="62" y1="63"  x2="690" y2="63"  stroke="#D8DEE6" stroke-width="0.6"/>
    <!-- X-axis -->
    <line x1="62" y1="215" x2="690" y2="215" stroke="#D8DEE6" stroke-width="0.8"/>

    <!-- Y-axis labels (right-aligned at x=56) -->
    <text x="56" y="29"  text-anchor="end" class="yl">100%</text>
    <text x="56" y="67"  text-anchor="end" class="yl">80%</text>
    <text x="56" y="105" text-anchor="end" class="yl">60%</text>
    <text x="56" y="143" text-anchor="end" class="yl">40%</text>
    <text x="56" y="181" text-anchor="end" class="yl">20%</text>
    <text x="56" y="219" text-anchor="end" class="yl">0%</text>
    <!-- Y-axis title (rotated) -->
    <text transform="rotate(-90,16,120)" x="16" y="120" text-anchor="middle" class="ytitle">Die yield (%)</text>

    <!-- X-axis labels -->
    <text x="62"  y="230" text-anchor="middle" class="ya">0</text>
    <text x="219" y="230" text-anchor="middle" class="ya">200mm²</text>
    <text x="376" y="230" text-anchor="middle" class="ya">400mm²</text>
    <text x="533" y="230" text-anchor="middle" class="ya">600mm²</text>
    <text x="690" y="230" text-anchor="middle" class="ya">800mm²</text>
    <text x="376" y="244" text-anchor="middle" class="ytitle">Die area</text>

    <!-- Sweet spot shading (0–100mm²: x=62 to x=141) -->
    <rect x="62" y="25" width="79" height="190" fill="#00A6A6" opacity="0.09" rx="0"/>

    <!-- Area under curve (subtle navy fill) -->
    <path d="M 62,215 L 62,25 L 101,34 L 141,43 L 180,51 L 219,59 L 258,67 L 298,74 L 337,81 L 376,88 L 415,94 L 455,100 L 494,105 L 533,111 L 572,116 L 612,121 L 651,125 L 690,130 L 690,215 Z"
          fill="#0A2240" opacity="0.04"/>

    <!-- Yield curve -->
    <!-- Points: area(mm²) → x=62+(area×0.785), yield%=e^(-0.001×area) → y=215-(yield×1.9) -->
    <!-- 0→(62,25) 50→(101,34) 100→(141,43) 150→(180,51) 200→(219,59) 250→(258,67) 300→(298,74) -->
    <!-- 350→(337,81) 400→(376,88) 450→(415,94) 500→(455,100) 550→(494,105) 600→(533,111) -->
    <!-- 650→(572,116) 700→(612,121) 750→(651,125) 800→(690,130) -->
    <polyline
      points="62,25 101,34 141,43 180,51 219,59 258,67 298,74 337,81 376,88 415,94 455,100 494,105 533,111 572,116 612,121 651,125 690,130"
      stroke="#0A2240" stroke-width="2.8" fill="none" stroke-linejoin="round"/>

    <!-- Sweet spot zone label — positioned in the open space BELOW the curve inside the zone -->
    <!-- Curve at x=62-141 is at y=25-43, so y=105+ is safely below -->
    <text x="65" y="105" class="yz" font-weight="700">Sweet spot</text>
    <text x="65" y="118" class="yz">&#8804;100mm&#178;</text>
    <text x="65" y="131" class="yz">Yield: 90%+</text>
    <text x="65" y="148" class="yz" font-size="9">(e.g. AMD Zen 5</text>
    <text x="65" y="160" class="yz" font-size="9">CCD ~84mm&#178;)</text>

    <!-- H100 annotation — text placed ABOVE curve to left of vertical line -->
    <!-- Curve at x=533 is y=111; place text at y=56-82 to clear the curve -->
    <text x="527" y="56"  text-anchor="end" class="yh" font-weight="700">H100 die</text>
    <text x="527" y="69"  text-anchor="end" class="yh">~600mm&#178;</text>
    <text x="527" y="82"  text-anchor="end" class="yh">yield ~55%</text>
    <!-- Leader line from text to curve point -->
    <line x1="502" y1="84" x2="529" y2="113"
          stroke="#F2620F" stroke-width="1.3" stroke-dasharray="3,2"
          marker-end="url(#yArr)"/>
    <!-- Dashed vertical reference line to x-axis -->
    <line x1="533" y1="111" x2="533" y2="215"
          stroke="#F2620F" stroke-width="1.1" stroke-dasharray="4,3" opacity="0.5"/>
    <!-- Dot at curve point -->
    <circle cx="533" cy="111" r="4" fill="#F2620F"/>

    <!-- Chiplet dot at 100mm² -->
    <circle cx="141" cy="43" r="4" fill="#00A6A6"/>
  </svg>

  <p class="xp-exhibit-source">Source: Poisson yield model (Y = e&#8315;&#8317;DA&#8318;, D = 0.1 defects/cm²) — standard industry approximation. Real-world yield varies by node, design, and fab. H100 die area from public NVIDIA/TSMC disclosures. ATF illustration.</p>
</figure>

<!-- ── EXHIBIT 2: Cost comparison stacked bars ───────────── -->
<figure class="xp-exhibit">
  <div class="xp-exhibit-pill">EXHIBIT 2</div>
  <h3>Chiplet economics: lower die cost offsets higher packaging cost — with room to spare</h3>
  <p class="xp-exhibit-sub">Illustrative cost breakdown per unit, USD; hypothetical 600mm² equivalent compute at leading node</p>

  <svg viewBox="0 0 720 272" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Stacked bar chart comparing monolithic vs chiplet cost breakdown">
    <defs>
      <style>
        .ca{font-family:'Helvetica Neue',Arial,sans-serif;font-size:10.5px;fill:#5B6675}
        .cb{font-family:'Helvetica Neue',Arial,sans-serif;font-weight:700;font-size:10.5px;fill:#fff}
        .cc{font-family:'Helvetica Neue',Arial,sans-serif;font-weight:700;font-size:10.5px;fill:#0A2240}
        .cd{font-family:'Helvetica Neue',Arial,sans-serif;font-weight:700;font-size:11px;fill:#5B6675}
        .ce{font-family:'Helvetica Neue',Arial,sans-serif;font-weight:700;font-size:22px;fill:#F2620F}
        .cf{font-family:'Helvetica Neue',Arial,sans-serif;font-size:11px;fill:#F2620F}
        .cg{font-family:'Helvetica Neue',Arial,sans-serif;font-weight:700;font-size:12px;fill:#0A2240}
        .ch{font-family:'Helvetica Neue',Arial,sans-serif;font-size:10px;fill:#5B6675}
      </style>
    </defs>

    <!-- Chart: y_bottom=225, height=185px (y=40 to y=225), scale=185/$3500=0.05286px/$ -->
    <!-- Y-axis at x=130 -->

    <!-- Gridlines: $1000→y=172, $2000→y=119, $3000→y=66 -->
    <line x1="130" y1="225" x2="600" y2="225" stroke="#D8DEE6" stroke-width="0.8"/>
    <line x1="130" y1="172" x2="600" y2="172" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="130" y1="119" x2="600" y2="119" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="130" y1="66"  x2="600" y2="66"  stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="130" y1="40"  x2="600" y2="40"  stroke="#D8DEE6" stroke-width="0.5" opacity="0.5"/>

    <!-- Y-axis labels at x=124 (right-aligned) -->
    <text x="124" y="229" text-anchor="end" class="ca">$0</text>
    <text x="124" y="176" text-anchor="end" class="ca">$1k</text>
    <text x="124" y="123" text-anchor="end" class="ca">$2k</text>
    <text x="124" y="70"  text-anchor="end" class="ca">$3k</text>

    <!-- ═══ MONOLITHIC bar (x=145, width=130) ═══ -->
    <!-- Die $3,200 → 169px: y=56 to y=225 -->
    <rect x="145" y="56"  width="130" height="169" fill="#C0392B" rx="1"/>
    <!-- Pkg $200 → 11px: y=45 to y=56 -->
    <rect x="145" y="45"  width="130" height="11"  fill="#13335E" rx="1"/>

    <!-- Bar labels inside (die cost) -->
    <text x="210" y="128" text-anchor="middle" class="cb">Die cost</text>
    <text x="210" y="143" text-anchor="middle" class="cb">$3,200</text>
    <!-- Pkg label above small bar -->
    <text x="145" y="41"  class="ch">+ $200 pkg</text>
    <!-- Total label above bar -->
    <text x="210" y="32"  text-anchor="middle" class="cd">TOTAL $3,400</text>

    <!-- Group label -->
    <text x="210" y="244" text-anchor="middle" class="cg">MONOLITHIC</text>
    <text x="210" y="257" text-anchor="middle" class="ch">One 600mm² die</text>

    <!-- ═══ CHIPLET bar (x=430, width=130) ═══ -->
    <!-- Die $600 → 32px: y=193 to y=225 -->
    <rect x="430" y="193" width="130" height="32"  fill="#00A6A6" rx="1"/>
    <!-- Adv pkg $800 → 42px: y=151 to y=193 -->
    <rect x="430" y="151" width="130" height="42"  fill="#0A2240" rx="1"/>

    <!-- Die cost label (inside thin bar) -->
    <text x="495" y="214" text-anchor="middle" class="cb" font-size="9.5">Die cost: $600</text>
    <!-- Pkg label inside bar -->
    <text x="495" y="169" text-anchor="middle" class="cb">Adv. pkg</text>
    <text x="495" y="182" text-anchor="middle" class="cb">$800</text>
    <!-- Total label above bar -->
    <text x="495" y="138" text-anchor="middle" class="cd">TOTAL $1,400</text>

    <!-- Group label -->
    <text x="495" y="244" text-anchor="middle" class="cg">CHIPLET</text>
    <text x="495" y="257" text-anchor="middle" class="ch">Six 100mm² dies</text>

    <!-- ═══ Savings annotation (between groups) ═══ -->
    <!-- Vertical bracket line at x=340 from y=45 (mono top) to y=151 (chiplet top) -->
    <line x1="290" y1="45"  x2="310" y2="45"  stroke="#F2620F" stroke-width="1.4"/>
    <line x1="290" y1="151" x2="310" y2="151" stroke="#F2620F" stroke-width="1.4"/>
    <line x1="299" y1="45"  x2="299" y2="151" stroke="#F2620F" stroke-width="1.4"/>
    <!-- Bracket at right -->
    <line x1="299" y1="45"  x2="314" y2="45"  stroke="#F2620F" stroke-width="1.4"/>
    <line x1="299" y1="151" x2="314" y2="151" stroke="#F2620F" stroke-width="1.4"/>
    <!-- Savings text centred on bracket -->
    <text x="325" y="90"  class="ce">59%</text>
    <text x="325" y="108" class="cf">lower</text>
    <text x="325" y="122" class="cf">total cost</text>

    <!-- Legend -->
    <rect x="130" y="263" width="12" height="8" fill="#C0392B" rx="1"/>
    <text x="146" y="270" class="ch">Die cost (monolithic)</text>
    <rect x="302" y="263" width="12" height="8" fill="#00A6A6" rx="1"/>
    <text x="318" y="270" class="ch">Die cost (chiplet)</text>
    <rect x="450" y="263" width="12" height="8" fill="#0A2240" rx="1"/>
    <text x="466" y="270" class="ch">Advanced packaging</text>
  </svg>

  <p class="xp-exhibit-source">Source: Illustrative model based on SemiAnalysis yield-cost framework; TSMC advanced node wafer pricing (industry estimates); McKinsey semiconductor cost model (2024). Numbers are illustrative — actual cost varies by design, volume, and vendor agreement.</p>
</figure>

<blockquote class="xp-pull-quote">
  <p>&#8220;The question that determines whether an AI accelerator ships on schedule is not &#8216;can you print at 2nm?&#8217; It is &#8216;can you get a CoWoS slot?&#8217;&#8221;</p>
  <cite>Colin Tan, Editor — Asia Tech Feed</cite>
</blockquote>

<div class="xp-two-col">
  <div>
    <p><b>Why CoWoS became the bottleneck.</b> TSMC's CoWoS — Chip on Wafer on Substrate — sits at the centre of the AI supply chain. In CoWoS-S, chiplets are mounted on a silicon interposer providing thousands of microbumps at pitches as fine as 40μm; in CoWoS-L, the interposer is extended with a localised silicon bridge. The result is die-to-die bandwidth measured in terabytes per second — versus the gigabytes a PCB trace can manage.</p>
    <p>The constraint is capacity, not technology. CoWoS output more than doubled in 2025 to roughly 70,000 wafers per month and is on track to double again by end-2026 to approximately 140,000. It is still not enough. NVIDIA has reportedly secured over 60% of TSMC's 2026 CoWoS allocation for the Rubin ramp alone. The package slot, not the silicon wafer, is what limits how many AI accelerators ship this year.</p>
  </div>
  <div>
    <p><b>The geography of packaging.</b> The advanced packaging map is overwhelmingly Asian. TSMC dominates with CoWoS and its 3D stacking platform SoIC. ASE Group — the world's largest OSAT — operates primarily in Taiwan and Malaysia. Amkor's Korean and Malaysian facilities, JCET in China, and Unimicron's ABF substrate plants all sit within this region.</p>
    <p>Japan is co-locating packaging with wafer production at Rapidus' Chitose campus. Malaysia's Penang corridor absorbs OSAT overflow as supply chains de-risk from Taiwan concentration. India's semiconductor ambitions are explicitly packaging-first: the Tata Electronics and CG Power OSAT projects target assembly and test, not wafer fabrication. The logic is straightforward — advanced packaging does not require EUV lithography, so entry barriers are lower even as strategic value rises rapidly.</p>
  </div>
</div>

<!-- ── EXHIBIT 3: CoWoS supply vs demand ─────────────────── -->
<figure class="xp-exhibit">
  <div class="xp-exhibit-pill">EXHIBIT 3</div>
  <h3>Supply doubles twice — and still chases demand every year through 2027</h3>
  <p class="xp-exhibit-sub">CoWoS-equivalent advanced packaging capacity (supply, bars) vs estimated AI accelerator demand (line), thousand wafers per month</p>

  <svg viewBox="0 0 720 262" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bar and line chart showing CoWoS supply vs AI demand 2023 to 2027">
    <defs>
      <style>
        .ma{font-family:'Helvetica Neue',Arial,sans-serif;font-size:10.5px;fill:#5B6675}
        .mb{font-family:'Helvetica Neue',Arial,sans-serif;font-weight:700;font-size:10.5px;fill:#0A2240}
        .mc{font-family:'Helvetica Neue',Arial,sans-serif;font-weight:700;font-size:10.5px;fill:#F2620F}
        .md{font-family:'Helvetica Neue',Arial,sans-serif;font-size:9px;fill:#F2620F}
        .me{font-family:'Helvetica Neue',Arial,sans-serif;font-weight:700;font-size:11px;fill:#0A2240}
        .mf{font-family:'Helvetica Neue',Arial,sans-serif;font-size:10.5px;fill:#5B6675}
      </style>
      <marker id="mArr" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
        <polygon points="0 0,7 3.5,0 7" fill="#F2620F"/>
      </marker>
    </defs>

    <!-- Chart: x=62 to x=690 (628px), y=30 to y=218 (188px), y_bottom=218 -->
    <!-- Scale: 188/230 = 0.817 px/k WPM -->

    <!-- Y-axis gridlines: 50k→y=177, 100k→y=136, 150k→y=95, 200k→y=54 -->
    <line x1="62" y1="218" x2="690" y2="218" stroke="#D8DEE6" stroke-width="0.8"/>
    <line x1="62" y1="177" x2="690" y2="177" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="62" y1="136" x2="690" y2="136" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="62" y1="95"  x2="690" y2="95"  stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="62" y1="54"  x2="690" y2="54"  stroke="#D8DEE6" stroke-width="0.6"/>

    <!-- Y-axis labels -->
    <text x="56" y="222" text-anchor="end" class="ma">0</text>
    <text x="56" y="181" text-anchor="end" class="ma">50k</text>
    <text x="56" y="140" text-anchor="end" class="ma">100k</text>
    <text x="56" y="99"  text-anchor="end" class="ma">150k</text>
    <text x="56" y="58"  text-anchor="end" class="ma">200k</text>

    <!-- Bar x positions (width=72, gap=40, start=116):
         2023: x=116, 2024: x=228, 2025: x=340, 2026F: x=452, 2027F: x=564
         Bar centers: 152, 264, 376, 488, 600 -->

    <!-- Supply bar heights (k WPM × 0.817):
         10k→8.2px y=210, 35k→28.6px y=189, 70k→57.2px y=161,
         140k→114.4px y=104, 200k→163.5px y=54 (approx 55) -->

    <!-- 2023: 10k WPM -->
    <rect x="116" y="210" width="72" height="8"   fill="#D8DEE6" rx="1"/>
    <text x="152" y="205" text-anchor="middle" class="mb">10k</text>
    <text x="152" y="235" text-anchor="middle" class="ma">2023</text>

    <!-- 2024: 35k WPM -->
    <rect x="228" y="189" width="72" height="29"  fill="#8A94A6" rx="1"/>
    <text x="264" y="184" text-anchor="middle" class="mb">35k</text>
    <text x="264" y="235" text-anchor="middle" class="ma">2024</text>

    <!-- 2025: 70k WPM -->
    <rect x="340" y="161" width="72" height="57"  fill="#0A2240" rx="1"/>
    <text x="376" y="156" text-anchor="middle" class="mb">70k</text>
    <text x="376" y="235" text-anchor="middle" class="ma">2025</text>

    <!-- 2026F: 140k WPM (teal = forecast) -->
    <rect x="452" y="104" width="72" height="114" fill="#00A6A6" rx="1"/>
    <text x="488" y="99"  text-anchor="middle" class="mb">140k</text>
    <text x="488" y="235" text-anchor="middle" class="me">2026F</text>

    <!-- 2027F: 200k WPM (teal, slightly lower opacity) -->
    <rect x="564" y="55"  width="72" height="163" fill="#00A6A6" rx="1" opacity="0.80"/>
    <text x="600" y="50"  text-anchor="middle" class="mb">200k</text>
    <text x="600" y="235" text-anchor="middle" class="me">2027F</text>

    <!-- Gap shading at 2026F: demand y=86, supply top y=104, gap=18px -->
    <!-- Demand y values: 13k→207, 47k→180, 84k→149, 162k→86, 212k→45 -->
    <rect x="452" y="86" width="72" height="18" fill="#F2620F" opacity="0.18" rx="1"/>

    <!-- Demand line -->
    <polyline points="152,207 264,180 376,149 488,86 600,45"
              stroke="#F2620F" stroke-width="2.4" fill="none"
              stroke-linecap="round" stroke-linejoin="round"/>
    <!-- Demand line dots -->
    <circle cx="152" cy="207" r="4.5" fill="#F2620F"/>
    <circle cx="264" cy="180" r="4.5" fill="#F2620F"/>
    <circle cx="376" cy="149" r="4.5" fill="#F2620F"/>
    <circle cx="488" cy="86"  r="4.5" fill="#F2620F"/>
    <circle cx="600" cy="45"  r="4.5" fill="#F2620F"/>

    <!-- Gap annotation: arrow from label to gap zone at 2026F -->
    <!-- Label placed in clear space left of 2026F bar, above supply -->
    <text x="396" y="68"  class="mc" font-weight="700" font-size="10">Supply gap</text>
    <text x="396" y="81"  class="md">Demand exceeds</text>
    <text x="396" y="93"  class="md">supply ~2027F</text>
    <line x1="444" y1="80" x2="453" y2="93"
          stroke="#F2620F" stroke-width="1.3" marker-end="url(#mArr)"/>

    <!-- Legend -->
    <rect x="152" y="250" width="14" height="10" fill="#00A6A6" rx="1"/>
    <text x="170" y="259" class="mf">CoWoS supply capacity</text>
    <!-- Orange line segment -->
    <line x1="355" y1="255" x2="375" y2="255" stroke="#F2620F" stroke-width="2.4"/>
    <circle cx="365" cy="255" r="4" fill="#F2620F"/>
    <text x="382" y="259" class="mf">Estimated AI accelerator demand (WPM-equivalent)</text>
  </svg>

  <p class="xp-exhibit-source">Source: TrendForce; Focus Taiwan / TSMC Technology Symposium (2026); Commercial Times; Tom's Hardware. Demand line is ATF estimate derived from hyperscaler GPU order disclosures and CoWoS wafer intensity ratios. 2026–27 are forecasts.</p>
</figure>

<div class="xp-two-col">
  <div>
    <p><b>What comes next: CoPoS and the panel revolution.</b> Two technologies define the next inflection. CoPoS — chip on panel on substrate — scales CoWoS from a 300mm round wafer to a rectangular panel, cutting per-unit packaging cost by an estimated 40–60%. A single Rubin-scale package today occupies most of a 300mm wafer; panel-level packaging changes that arithmetic fundamentally. TSMC has a pilot line running with volume production targeted for 2028–29. The transition would represent the most significant reduction in AI accelerator packaging cost since CoWoS itself was introduced.</p>
  </div>
  <div>
    <p><b>3D stacking and the shift of gravity.</b> The second frontier is 3D stacking. TSMC's SoIC bonds dies face-to-face using hybrid bonding — copper-to-copper connections at 9μm pitch with no solder bump — enabling memory-to-logic bandwidth no interposer can match. Intel's Foveros Direct achieves similar densities. When 3D packaging matures at volume scale, estimated around 2028–30, the centre of gravity in chipmaking shifts further from the wafer fab toward the package house. The era of packaging as an afterthought — a low-margin service attached to real semiconductor work — is definitively over.</p>
  </div>
</div>

<div class="xp-callout">
  <div class="xp-callout-label">The Bottom Line</div>
  <p>The transistor count on a chip still matters. But in 2026, the question that determines whether an AI accelerator ships on schedule — and at what cost — is not "can you print at 2nm?" It is "can you get a CoWoS slot?" Packaging has become the most strategically valuable, most supply-constrained, and most geographically concentrated step in modern chipmaking. Any organisation buying, building, or pricing around AI infrastructure should understand it with the same rigour as the silicon itself.</p>
</div>

<div class="xp-author-bio">
  <div class="xp-author-name">Colin Tan &nbsp;·&nbsp; Editor, Asia Tech Feed</div>
  <p>Colin covers semiconductors, AI infrastructure and supply-chain dynamics across the Asia-Pacific region. He has tracked the chiplet transition and advanced packaging buildout since AMD's first Zen chiplet release and writes the daily ATF digest. Reach him at <a href="mailto:colin.tan@asiatechfeed.com">colin.tan@asiatechfeed.com</a> or connect on LinkedIn.</p>
</div>

<div class="xp-footer-grid">
  <div class="xp-key-numbers">
    <div class="xp-kn-label">Key Numbers</div>
    <div class="xp-kn-item"><div class="xp-kn-val">90%+</div><div class="xp-kn-desc">Chiplet die yield<br>at ≤100mm²</div></div>
    <div class="xp-kn-item"><div class="xp-kn-val">~59%</div><div class="xp-kn-desc">Cost reduction<br>vs monolithic</div></div>
    <div class="xp-kn-item"><div class="xp-kn-val">&gt;60%</div><div class="xp-kn-desc">NVIDIA share of<br>2026 CoWoS slots</div></div>
    <div class="xp-kn-item"><div class="xp-kn-val">140k</div><div class="xp-kn-desc">CoWoS WPM target<br>end-2026F</div></div>
    <div class="xp-kn-item"><div class="xp-kn-val">2028–29</div><div class="xp-kn-desc">CoPoS panel-level<br>volume timeline</div></div>
  </div>
  <div class="xp-related">
    <div class="xp-related-label">Related Coverage</div>
    <div class="xp-related-item">
      <span class="xp-related-tag">REPORT</span>
      <h4>Asia Tech Feed on Semiconductors: Outlook H2 2026–2027</h4>
      <p>Full-length research report covering memflation, TSMC's packaging ramp, China's parallel stack, and ten falsifiable predictions through end-2027.</p>
    </div>
    <div class="xp-related-item">
      <span class="xp-related-tag">EXPLAINER</span>
      <h4>What is HBM memory and why does it matter for AI pricing?</h4>
      <p>HBM is the memory architecture inside every flagship AI accelerator — and the component now setting the floor on AI infrastructure costs globally.</p>
    </div>
    <div class="xp-related-item">
      <span class="xp-related-tag">ANALYSIS</span>
      <h4>TSMC's CoPoS pilot: can panel-level packaging halve accelerator costs by 2029?</h4>
      <p>Panel-level packaging could transform the economics of AI silicon. We assess the technology readiness, yield risks, and who benefits first.</p>
    </div>
  </div>
</div>
