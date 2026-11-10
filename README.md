# KONE Assisted Decisioning System (ADS)

> **Growth Control Tower & Modernization Orchestration Platform**  
> Built for KONE Global Marketing by Cognizant Moment.

---

## 🌟 Overview

The **KONE Assisted Decisioning System (ADS)** is an enterprise decision orchestration platform designed to sense market signals across European elevator portfolios, diagnose conversion variance, dynamically prioritize growth plays, simulate capital allocation, orchestrate field technicians and sales teams, and close the loop with continuous Bayesian learning.

Designed using KONE's light brand theme and design system tokens extracted from [kone.com/innovation](https://www.kone.com/global/en/innovation.html), the application runs completely standalone as a redistributable, single-file HTML experience with zero external runtime dependencies.

---

## 🚀 Live Demo & How to Run

1. **Direct Browser Execution**:
   Simply open `index.html` in any modern web browser (Chrome, Safari, Edge, Firefox).
   ```bash
   open index.html
   ```
   *No build step, no npm install, and no local server required.*

2. **GitHub Pages Deployment**:
   - The repository is structured with `index.html` at root, ready for immediate publishing via GitHub Pages (`Settings -> Pages -> Deploy from main branch`).

---

## 🧭 The 8-Stage Closed-Loop Decision Flywheel

1. **Sense (Portfolio Telemetry & Lattice)**:
   - Senses 2.87M maintenance contracts across 7 European operating units (DACH, Iberia, Benelux, Poland, UK & Ireland, France, Nordics).
   - Identifies high-risk/high-potential anomalies (e.g., Iberia's 34,500 aging units with low 90-day activation).
   - Includes real-time synthetic telemetry jitter simulation (incremental/decremental drift).

2. **Diagnose (Root Cause Attribution)**:
   - Decomposes the +22-point conversion gap between DACH (46%) and Iberia (24%).
   - Demonstrates that the gap is operational (technician lead capture and 5-day disruption guarantees), not creative or media spend.

3. **Prioritise (Bayesian Opportunity Ranking)**:
   - Multi-objective candidate ranking across EBITDA yield, feasibility match, and confidence.
   - Dynamically shifts confidence priors as field evidence lands.

4. **Simulate (Monte Carlo Capital Allocation)**:
   - Interactive slider control (€0M to €20M) with detents at €5M, €8.4M (Recommended), and €10M.
   - Real-time curve updates for projected revenue, ROI, and payback period.

5. **Orchestrate (Closed-Loop Field Dispatch)**:
   - Decision records committed to execution across Field Marketing, Sales Ops, and Service Technicians.
   - Interactive 38-building pilot cohort in Madrid and Barcelona with detailed shaft dimension audits, lift counts, and quote values.

6. **Replicate (Playbook Codification)**:
   - Identifies what travels vs. what must adapt locally across markets.
   - Showcases KONE breakthrough innovations: EcoDisc®, UltraRope®, DX Class, JumpLift™, 24/7 Connected Services, and Carbon Production.

7. **Optimise (Day-90 Realized Outcomes)**:
   - Reviews real pilot outcomes (38 quotes delivered, 39.5% conversion, 151 total days on site saved, 112 technician leads).
   - Interactive sensitivity levers (referral bonus, bracket pre-assembly, digital quotation shifts).

8. **Learn (Institutional Memory Bank)**:
   - Closed-loop Bayesian learning updating model priors from 0.62 to 0.84, eliminating organizational amnesia.

---

## 📁 Repository Structure

```
├── index.html                           # Primary standalone redistributable application (334 KB)
├── kone-marketing-os.html               # Mirror copy of standalone application
├── kone_synthetic_dataset.json          # Enriched synthetic telemetry & market dataset
├── build_assisted_decisioning_system.py # Python builder script generating standalone HTML
├── kone_logo.jpg                        # Official KONE brand logo asset
├── cognizant_logo.png                   # Official Cognizant Moment brand logo asset
├── script_full.txt                      # 9-Scene boardroom script transcript
├── session_brief.txt                    # Strategic context & session brief
└── KONE_Marketing-OS_Script.docx        # Original requirements document
```

---

## 🎨 Design System & Branding

- **Typography**: Inter / VideoJS / KONE Information
- **Palette**: KONE Primary Blue (`#1450F5`), Dark Ink (`#00061F`), Soft Blue Tint (`#F5F8FF`), Pure White (`#FFFFFF`)
- **UI Architecture**: Glassmorphic panels, elevation shadows, responsive tables, interactive modals, and slide-out coverage drawer
- **Co-Branding**: KONE top brand header and Cognizant Moment footer credit

---

## 📄 License
Internal confidential prototype for KONE Global Marketing & Cognizant Moment.
