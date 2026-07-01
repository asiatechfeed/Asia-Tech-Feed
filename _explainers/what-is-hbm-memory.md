---
title: "What is HBM Memory, and Why Does It Matter for AI Pricing"
tags: [AI, Semiconductor]
date: 2026-07-01
author: "Colin Tan"
excerpt: "HBM has stopped being a line item inside a GPU spec sheet — it's now the price-setter for AI infrastructure, and the mechanism by which AI data-centre costs flow back to consumer electronics buyers."
---

<p class="xp-lede">Every conversation about AI costs eventually arrives at the same uncomfortable number. Not the GPU price — the memory price. High-Bandwidth Memory, or HBM, is the component that makes modern AI accelerators work. It is also, in 2026, the component making them expensive, scarce, and the primary lever setting the floor on AI infrastructure costs worldwide.</p>

<div class="xp-two-col">
  <div>
    <p><b>The basic problem HBM solves.</b> Training a large language model is, at its core, a data-movement problem. The GPU's processing cores are fast enough — the bottleneck is feeding them data quickly enough to keep them busy. Conventional DRAM, mounted on a PCB some distance from the chip, cannot do that. HBM solves it by stacking multiple DRAM dies vertically, connecting them through thousands of through-silicon vias (TSVs), and mounting the entire stack directly on the same silicon interposer as the logic die. The result is a memory interface orders of magnitude wider and faster than anything a standard slot can achieve.</p>
    <p>The numbers are stark. A DDR5 stick delivers roughly 67 GB/s. HBM3E — the standard in 2026's flagship accelerators — delivers 1,180 GB/s per stack: nearly 18× more. HBM4, now in volume production, pushes past 1,500 GB/s. An NVIDIA B200 carries eight HBM3E stacks; aggregate bandwidth available to its compute cores exceeds 8 TB/s. No other memory architecture comes close.</p>
  </div>
  <div>
    <p><b>Why the cost matters so much right now.</b> HBM is not cheap to make. Each gigabyte consumes roughly three times the wafer capacity of equivalent DDR5, reflecting yield loss from stacking, the TSV process, and wafer thinning requirements. The result is a 5–6× price premium per gigabyte over standard DRAM. HBM3E costs approximately $8–10 per GB against DDR5's $1.50–2. That arithmetic reaches into every AI accelerator on the market: HBM now accounts for 30–40% of the total manufacturing cost of a flagship AI chip. For the B200, memory alone costs roughly $2,400 — exceeding the logic die itself.</p>
    <p>The supply side compounds this. Three companies — SK hynix, Samsung and Micron — control essentially all HBM production. SK hynix holds 50–55% of the market and is sold out through 2026. Samsung began commercial HBM4 shipments in February 2026. Micron is expanding aggressively but from a small base. With hyperscalers signing multi-year lockup contracts covering an estimated 35–40% of global DRAM wafer capacity through 2029, the spot market for HBM does not meaningfully exist.</p>
  </div>
</div>

<figure class="xp-exhibit">
  <div class="xp-exhibit-pill">EXHIBIT 1</div>
  <h3>HBM delivers up to 24× the bandwidth of standard memory</h3>
  <p class="xp-exhibit-sub">Memory bandwidth, GB/s per stack or module — HBM4 is projected for 2026</p>

  <svg viewBox="0 0 720 262" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Horizontal bar chart comparing memory bandwidth">
    <defs>
      <style>
        .ax{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;fill:#5B6675;font-size:11px}
        .val{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-weight:700;font-size:11px;fill:#0A2240}
        .val-teal{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-weight:700;font-size:11px;fill:#00A6A6}
        .tag{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:9.5px;fill:#8A94A6}
        .legend-lbl{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:10.5px;fill:#5B6675}
      </style>
    </defs>

    <text x="142" y="29"  text-anchor="end" class="ax">DDR5</text>
    <text x="142" y="63"  text-anchor="end" class="ax">LPDDR5X</text>
    <text x="142" y="97"  text-anchor="end" class="ax">GDDR6X</text>
    <text x="142" y="131" text-anchor="end" class="ax">HBM2E</text>
    <text x="142" y="165" text-anchor="end" class="ax">HBM3</text>
    <text x="142" y="199" text-anchor="end" class="ax">HBM3E</text>
    <text x="142" y="233" text-anchor="end" class="ax">HBM4</text>

    <text x="150" y="29"  class="tag">(per DIMM)</text>
    <text x="150" y="63"  class="tag">(mobile)</text>
    <text x="150" y="97"  class="tag">(GPU)</text>
    <text x="150" y="131" class="tag">(2020)</text>
    <text x="150" y="165" class="tag">(2022)</text>
    <text x="150" y="199" class="tag">(2024)</text>
    <text x="150" y="233" class="tag">(2026F)</text>

    <rect x="252" y="14"  width="17"  height="22" fill="#D8DEE6" rx="1"/>
    <text x="275" y="29"  class="val">67 GB/s</text>

    <rect x="252" y="48"  width="17"  height="22" fill="#D8DEE6" rx="1"/>
    <text x="275" y="63"  class="val">68 GB/s</text>

    <rect x="252" y="82"  width="147" height="22" fill="#8A94A6" rx="1"/>
    <text x="405" y="97"  class="val">576 GB/s</text>

    <rect x="252" y="116" width="117" height="22" fill="#93B8F0" rx="1"/>
    <text x="375" y="131" class="val">460 GB/s</text>

    <rect x="252" y="150" width="208" height="22" fill="#2563EB" rx="1"/>
    <text x="466" y="165" class="val">819 GB/s</text>

    <rect x="252" y="184" width="300" height="22" fill="#0A2240" rx="1"/>
    <text x="558" y="199" class="val" fill="#ffffff">1,180 GB/s</text>

    <rect x="252" y="218" width="407" height="22" fill="#00A6A6" rx="1"/>
    <text x="665" y="233" class="val-teal">1,600+ GB/s</text>

    <line x1="664" y1="20"  x2="664" y2="228" stroke="#F2620F" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="668" y="60"  font-family="Helvetica Neue,Arial,sans-serif" font-size="11" font-weight="700" fill="#F2620F">~24×</text>
    <text x="668" y="73"  font-family="Helvetica Neue,Arial,sans-serif" font-size="10" fill="#F2620F">vs DDR5</text>

    <rect x="252" y="250" width="12" height="8" fill="#D8DEE6" rx="1"/>
    <text x="269" y="258" class="legend-lbl">Standard DRAM</text>
    <rect x="382" y="250" width="12" height="8" fill="#8A94A6" rx="1"/>
    <text x="399" y="258" class="legend-lbl">Graphics DRAM</text>
    <rect x="510" y="250" width="12" height="8" fill="#93B8F0" rx="1"/>
    <text x="527" y="258" class="legend-lbl">HBM (prev. gen)</text>
    <rect x="630" y="250" width="12" height="8" fill="#00A6A6" rx="1"/>
    <text x="647" y="258" class="legend-lbl">HBM4</text>
  </svg>

  <p class="xp-exhibit-source">Source: JEDEC specifications (HBM3E, HBM4); Silicon Analysts (June 2026); PatSnap; SemiAnalysis. ATF compilation. HBM4 bandwidth is a projected figure.</p>
</figure>

<figure class="xp-exhibit">
  <div class="xp-exhibit-pill">EXHIBIT 2</div>
  <h3>Memory is now the largest single cost line in an AI accelerator</h3>
  <p class="xp-exhibit-sub">Estimated manufacturing cost breakdown (COGS), USD — not selling price</p>

  <svg viewBox="0 0 720 290" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Grouped bar chart comparing H100 and B200 manufacturing cost breakdown">
    <defs>
      <style>
        .cax{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;fill:#5B6675;font-size:10.5px}
        .ctitle{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-weight:700;font-size:12px;fill:#0A2240}
        .cval{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-weight:700;font-size:10.5px;fill:#0A2240}
        .cval-w{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-weight:700;font-size:10.5px;fill:#fff}
        .ctotal{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-weight:700;font-size:11px;fill:#5B6675}
        .chbm{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-weight:700;font-size:10px;fill:#C0392B}
      </style>
    </defs>

    <line x1="42" y1="220" x2="690" y2="220" stroke="#D8DEE6" stroke-width="0.7"/>
    <line x1="42" y1="165" x2="690" y2="165" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="42" y1="110" x2="690" y2="110" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="42" y1="55"  x2="690" y2="55"  stroke="#D8DEE6" stroke-width="0.6"/>

    <text x="36" y="224" text-anchor="end" class="cax">$0</text>
    <text x="36" y="169" text-anchor="end" class="cax">$800</text>
    <text x="36" y="114" text-anchor="end" class="cax">$1,600</text>
    <text x="36" y="59"  text-anchor="end" class="cax">$2,400</text>

    <text x="198" y="14" text-anchor="middle" class="ctitle">NVIDIA H100</text>
    <text x="198" y="28" text-anchor="middle" class="ctotal">Total COGS ~$3,320</text>

    <rect x="60"  y="199" width="60" height="21"  fill="#8A94A6" rx="1"/>
    <text x="90"  y="196" text-anchor="middle" class="cval">$300</text>
    <text x="90"  y="235" text-anchor="middle" class="cax">Logic</text>
    <text x="90"  y="247" text-anchor="middle" class="cax">(TSMC)</text>

    <rect x="132" y="126" width="60" height="94" fill="#C0392B" rx="1"/>
    <text x="162" y="122" text-anchor="middle" class="cval">$1,350</text>
    <text x="162" y="235" text-anchor="middle" class="cax">HBM</text>
    <text x="162" y="247" text-anchor="middle" class="cax">memory</text>
    <text x="162" y="168" text-anchor="middle" class="cval-w">41%</text>

    <rect x="204" y="168" width="60" height="52" fill="#0A2240" rx="1"/>
    <text x="234" y="164" text-anchor="middle" class="cval">$750</text>
    <text x="234" y="235" text-anchor="middle" class="cax">CoWoS</text>
    <text x="234" y="247" text-anchor="middle" class="cax">pkg</text>

    <rect x="276" y="156" width="60" height="64" fill="#D8DEE6" rx="1"/>
    <text x="306" y="152" text-anchor="middle" class="cval">$920</text>
    <text x="306" y="235" text-anchor="middle" class="cax">Test &amp;</text>
    <text x="306" y="247" text-anchor="middle" class="cax">assembly</text>

    <line x1="362" y1="36" x2="362" y2="255" stroke="#D8DEE6" stroke-width="1" stroke-dasharray="4,4"/>

    <text x="518" y="14" text-anchor="middle" class="ctitle">NVIDIA B200</text>
    <text x="518" y="28" text-anchor="middle" class="ctotal">Total COGS ~$5,100</text>

    <rect x="380" y="187" width="60" height="33" fill="#8A94A6" rx="1"/>
    <text x="410" y="183" text-anchor="middle" class="cval">$480</text>
    <text x="410" y="235" text-anchor="middle" class="cax">Logic</text>
    <text x="410" y="247" text-anchor="middle" class="cax">(TSMC)</text>

    <rect x="452" y="54"  width="60" height="166" fill="#C0392B" rx="1"/>
    <text x="482" y="50"  text-anchor="middle" class="cval">$2,400</text>
    <text x="482" y="235" text-anchor="middle" class="cax">HBM</text>
    <text x="482" y="247" text-anchor="middle" class="cax">memory</text>
    <text x="482" y="132" text-anchor="middle" class="cval-w">47%</text>

    <rect x="524" y="144" width="60" height="76" fill="#0A2240" rx="1"/>
    <text x="554" y="140" text-anchor="middle" class="cval">$1,100</text>
    <text x="554" y="235" text-anchor="middle" class="cax">CoWoS</text>
    <text x="554" y="247" text-anchor="middle" class="cax">pkg</text>

    <rect x="596" y="142" width="60" height="78" fill="#D8DEE6" rx="1"/>
    <text x="626" y="138" text-anchor="middle" class="cval">$1,120</text>
    <text x="626" y="235" text-anchor="middle" class="cax">Test &amp;</text>
    <text x="626" y="247" text-anchor="middle" class="cax">assembly</text>

    <text x="162" y="275" text-anchor="middle" class="chbm">HBM = 41% of COGS</text>
    <text x="482" y="275" text-anchor="middle" class="chbm">HBM = 47% of COGS</text>
  </svg>

  <p class="xp-exhibit-source">Source: Silicon Analysts (June 2026); Epoch AI cost model; SemiAnalysis. Figures are independent analyst estimates — not disclosed by or confirmed by NVIDIA.</p>
</figure>

<blockquote class="xp-pull-quote">
  <p>&#8220;For the B200, memory costs more than the logic die. HBM has stopped being a component and become the product.&#8221;</p>
  <cite>Colin Tan, Editor — Asia Tech Feed</cite>
</blockquote>

<div class="xp-two-col">
  <div>
    <p><b>The ripple effect on AI pricing.</b> When memory is both scarce and expensive, the cost does not stay inside the data centre. Cloud providers renting GPU instances to AI developers pay through higher hardware acquisition costs. Developers building on those instances pay through instance pricing that does not fall as fast as per-token model costs. And device makers — from laptop OEMs to smartphone brands — pay because every HBM wafer start is a consumer DRAM wafer start that did not happen. Gartner estimates DRAM contract prices rose 125% across 2026, with meaningful relief not expected before late 2027.</p>
    <p>The generation transition makes this more acute, not less. HBM4 introduces a custom logic base die — the base layer can now be specified by the chip buyer. What that means in practice: already-scarce advanced packaging capacity gets further fragmented by customer-specific variants. The bespoke nature of 2027's HBM market means supply cannot simply be reallocated when demand shifts.</p>
  </div>
  <div>
    <p><b>Three things to watch.</b> The HBM market is not a normal commodity cycle, and the signals that matter are not the usual ones.</p>
    <p>First: wafer allocation. Any revision to the multi-year DRAM wafer lockups held by hyperscalers will move prices faster than new capacity additions. Second: HBM4E customisation traction. The degree to which large AI labs adopt custom base dies determines whether the supply pool splinters — raising costs — or consolidates into standard parts. Third: China's domestic HBM program. CXMT is working toward domestic HBM production, but TSV and packaging steps remain well behind Korean leaders. If China closes the gap faster than expected, it adds capacity to a constrained market; if it stays constrained, Huawei's Ascend accelerator program hits a ceiling in memory, not logic.</p>
    <p>The HBM market will reach an estimated $58 billion in 2026 — up from $16 billion two years prior — on track for $90 billion in 2027, with Micron's CEO guiding a total addressable market above $100 billion by 2030.</p>
  </div>
</div>

<figure class="xp-exhibit">
  <div class="xp-exhibit-pill">EXHIBIT 3</div>
  <h3>The HBM market grew 9× in two years — and is not done</h3>
  <p class="xp-exhibit-sub">Global HBM revenue, $ billion; 2026–27 are forecasts</p>

  <svg viewBox="0 0 720 268" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bar chart of HBM market size 2022 to 2027">
    <defs>
      <style>
        .mx{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;fill:#5B6675;font-size:11px}
        .mv{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-weight:700;font-size:11px;fill:#0A2240}
        .mv-hi{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-weight:700;font-size:11px;fill:#F2620F}
        .myr{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:11.5px;fill:#5B6675}
        .myr-b{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-weight:700;font-size:11.5px;fill:#0A2240}
        .mcagr{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-weight:700;font-size:11px;fill:#F2620F}
        .mtam{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:10px;fill:#E8A33D}
      </style>
    </defs>

    <line x1="52" y1="210" x2="695" y2="210" stroke="#D8DEE6" stroke-width="0.8"/>
    <line x1="52" y1="174" x2="695" y2="174" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="52" y1="138" x2="695" y2="138" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="52" y1="102" x2="695" y2="102" stroke="#D8DEE6" stroke-width="0.6"/>
    <line x1="52" y1="66"  x2="695" y2="66"  stroke="#D8DEE6" stroke-width="0.6"/>

    <text x="46" y="214" text-anchor="end" class="mx">$0</text>
    <text x="46" y="178" text-anchor="end" class="mx">$20B</text>
    <text x="46" y="142" text-anchor="end" class="mx">$40B</text>
    <text x="46" y="106" text-anchor="end" class="mx">$60B</text>
    <text x="46" y="70"  text-anchor="end" class="mx">$80B</text>

    <line x1="52" y1="30" x2="695" y2="30" stroke="#E8A33D" stroke-width="1.3" stroke-dasharray="5,4"/>
    <text x="698" y="34" class="mtam">$100B</text>
    <text x="698" y="46" class="mtam">TAM by</text>
    <text x="698" y="58" class="mtam">2030</text>
    <text x="698" y="70" class="mtam">(Micron)</text>

    <rect x="72"  y="202" width="68" height="8"   fill="#D8DEE6" rx="1"/>
    <text x="106" y="197" text-anchor="middle" class="mv">$3.5B</text>
    <text x="106" y="226" text-anchor="middle" class="myr">2022</text>

    <rect x="179" y="202" width="68" height="8"   fill="#D8DEE6" rx="1"/>
    <text x="213" y="197" text-anchor="middle" class="mv">$4B</text>
    <text x="213" y="226" text-anchor="middle" class="myr">2023</text>

    <rect x="286" y="181" width="68" height="29"  fill="#8A94A6" rx="1"/>
    <text x="320" y="176" text-anchor="middle" class="mv">$16B</text>
    <text x="320" y="226" text-anchor="middle" class="myr">2024</text>

    <rect x="393" y="147" width="68" height="63"  fill="#0A2240" rx="1"/>
    <text x="427" y="142" text-anchor="middle" class="mv">$35B</text>
    <text x="427" y="226" text-anchor="middle" class="myr">2025</text>

    <rect x="500" y="106" width="68" height="104" fill="#00A6A6" rx="1"/>
    <text x="534" y="101" text-anchor="middle" class="mv-hi">$58B</text>
    <text x="534" y="226" text-anchor="middle" class="myr-b">2026F</text>

    <rect x="607" y="48"  width="68" height="162" fill="#00A6A6" rx="1" opacity="0.85"/>
    <text x="641" y="43"  text-anchor="middle" class="mv-hi">$90B</text>
    <text x="641" y="226" text-anchor="middle" class="myr-b">2027F</text>

    <path d="M 354 160 Q 430 80 607 60" stroke="#F2620F" stroke-width="1.6" fill="none"
          marker-end="url(#arr)" stroke-dasharray="none"/>
    <defs>
      <marker id="arr" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
        <polygon points="0 0, 7 3.5, 0 7" fill="#F2620F"/>
      </marker>
    </defs>
    <text x="380" y="148" text-anchor="middle" class="mcagr">2024–27F</text>
    <text x="380" y="161" text-anchor="middle" class="mcagr">CAGR ~78%</text>
  </svg>

  <p class="xp-exhibit-source">Source: Morgan Stanley; Micron investor guidance (CEO, fiscal Q1 2026 earnings call); TrendForce; ATF estimates for 2026–27F. Historical data from industry analyst composite.</p>
</figure>

<div class="xp-two-col">
  <div>
    <p><b>What customisation means for pricing power.</b> The introduction of custom base dies in HBM4E changes competitive dynamics in ways headline market-share numbers do not capture. When a hyperscaler embeds its own logic into the base die, it becomes technically dependent on a specific vendor's process — creating switching costs that did not exist when HBM was a standard part. That favours memory makers in the short term; it locks in relationships and justifies higher pricing for bespoke configurations.</p>
    <p>The Micron–TSMC partnership for HBM4E is the clearest expression of this logic: Micron brings DRAM expertise, TSMC brings the advanced logic process for the base die, and together they can offer a fully integrated solution that neither could supply alone. Samsung's advantage is that it can do both in-house — but it first needs to prove yield consistency on 12-high HBM3E before those integrated ambitions translate into market share.</p>
  </div>
  <div>
    <p><b>The forecast, and the honest uncertainty around it.</b> HBM demand grows 77% in 2026 and 68% in 2027 per TrendForce. Those numbers rest on one assumption: that the hyperscaler capex programmes underpinning them do not slow materially. Cloud giants have guided aggregate 2026 data-centre investment above $725 billion; if that number revises down in late 2026 earnings calls, HBM demand projections follow within one quarter.</p>
    <p>The structural case is sound regardless of timing. Every new GPU generation demands more HBM per unit — NVIDIA's Rubin Ultra targets 512 GB per GPU, versus 80 GB for the H100 two years ago. That is a 6× increase in memory per chip in a single product generation. The industry can debate when AI capex plateaus. It cannot debate the direction of per-chip memory requirements. HBM's share of accelerator cost goes up before it comes down, and any organisation that buys, builds or prices around AI infrastructure needs to model that assumption explicitly — not treat it as a footnote.</p>
  </div>
</div>

<div class="xp-callout">
  <div class="xp-callout-label">The Bottom Line</div>
  <p>HBM is no longer a line item inside a GPU spec sheet. It is the price-setter for AI infrastructure, the supply constraint on accelerator shipments, and the mechanism by which AI data-centre costs flow back to consumer electronics buyers who never ordered a single GPU. Understanding HBM means understanding why AI got more expensive the same year it got more capable — and why that tension persists through at least 2027.</p>
</div>

<div class="xp-author-bio">
  <div class="xp-author-name">Colin Tan &nbsp;·&nbsp; Editor, Asia Tech Feed</div>
  <p>Colin covers semiconductors, AI infrastructure and supply-chain dynamics across the Asia-Pacific region. He has tracked the memory industry through three full cycles and writes the daily ATF digest. Reach him at <a href="mailto:colin.tan@asiatechfeed.com">colin.tan@asiatechfeed.com</a> or connect on LinkedIn.</p>
</div>

<div class="xp-footer-grid">
  <div class="xp-key-numbers">
    <div class="xp-kn-label">Key Numbers</div>
    <div class="xp-kn-item"><div class="xp-kn-val">24×</div><div class="xp-kn-desc">More bandwidth:<br>HBM4 vs DDR5</div></div>
    <div class="xp-kn-item"><div class="xp-kn-val">30–40%</div><div class="xp-kn-desc">of B200 COGS<br>is HBM</div></div>
    <div class="xp-kn-item"><div class="xp-kn-val">3×</div><div class="xp-kn-desc">More wafer area<br>per GB vs DDR5</div></div>
    <div class="xp-kn-item"><div class="xp-kn-val">$8–10</div><div class="xp-kn-desc">per GB:<br>HBM3E price</div></div>
    <div class="xp-kn-item"><div class="xp-kn-val">$58B</div><div class="xp-kn-desc">HBM market<br>size, 2026F</div></div>
  </div>
  <div class="xp-related">
    <div class="xp-related-label">Related Coverage</div>
    <div class="xp-related-item">
      <span class="xp-related-tag">REPORT</span>
      <h4>Asia Tech Feed on Semiconductors: Outlook H2 2026–2027</h4>
      <p>Full-length research report covering memflation, TSMC's packaging ramp, China's parallel stack, and ten falsifiable predictions through end-2027.</p>
    </div>
    <div class="xp-related-item">
      <span class="xp-related-tag">ANALYSIS</span>
      <h4>The CoWoS bottleneck: why packaging decides who ships AI chips</h4>
      <p>Advanced packaging — not silicon — is the gate on 2026 accelerator supply. We map the constraint from Taichung to Chiayi.</p>
    </div>
    <div class="xp-related-item">
      <span class="xp-related-tag">DATA</span>
      <h4>HBM vendor tracker: SK hynix, Samsung, Micron market share update</h4>
      <p>Monthly update on HBM3E supply allocation, HBM4 qualification timelines, and pricing signals from the three suppliers.</p>
    </div>
  </div>
</div>
