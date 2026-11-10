import json
import os

with open("kone_synthetic_dataset.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

json_str = json.dumps(raw_data, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>KONE Marketing OS — Growth Intelligence Layer</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* ==========================================================================
       KONE OFFICIAL DESIGN SYSTEM TOKENS (Extracted from www.kone.com)
       ========================================================================== */
    :root {{
      /* Colors */
      --color-primary-1: #1450f5;
      --color-primary-2: #00061f;
      --color-primary-3: #f5f8ff;
      --color-primary-4: #66a8cc;
      --color-primary-5: #ffcc66;
      --color-primary-6: #f7faff;
      --color-primary-7: #e7edfe;
      --color-primary-8: #dae4ff;
      --color-primary-9: #bbccfc;
      --color-primary-10: #9fb8fc;
      --color-primary-11: #82a2fa;
      --color-primary-12: #668efa;
      --color-primary-13: #4a78f7;
      --color-primary-14: #2f64f7;
      --color-primary-15: #1a4dd9;
      --color-primary-16: #1e48bd;
      --color-primary-17: #2042a1;
      --color-primary-18: #203b85;
      --color-primary-19: #1d3169;
      --color-primary-20: #18264d;
      --color-primary-21: #122658;
      --color-primary-22: #112044;
      --color-primary-23: #f3f3ff;
      --color-primary-24: #dedeff;
      --color-primary-25: #cac9ff;
      --color-primary-26: #b9b8ff;
      --color-primary-27: #a4a3ff;
      --color-primary-28: #8e8dfc;
      --color-primary-29: #7b79fc;
      --color-primary-30: #6a68fc;
      --color-primary-31: #5654fc;
      --color-primary-32: #4644e2;
      --color-primary-33: #3836c9;
      --color-primary-34: #2c2ab0;
      --color-primary-35: #212099;
      --color-primary-36: #1a1880;
      --color-primary-37: #121066;
      --color-primary-38: #0b0a4d;
      --color-primary-39: #060533;
      --color-primary-40: #e4f9ff;
      --color-primary-41: #d2f5ff;
      --color-neutral-1: #141414;
      --color-neutral-2: #e8e9eb;
      --color-neutral-3: #888888;
      --color-neutral-4: #323232;
      --color-neutral-5: #f4f5f7;
      --color-neutral-6: #6e6f73;
      --color-neutral-7: #575759;
      --color-neutral-8: #7a7c80;
      --color-neutral-9: #646464;
      --color-neutral-10: #111111;
      --color-neutral-11: #efeff1;
      --color-neutral-12: #d7d8db;
      --color-accent-1: #2b333f;
      --color-accent-2: #73859f;
      --color-accent-3: #7e96ab;
      --color-accent-4: #fafbfc;
      --color-accent-5: #f7f8fa;
      --color-accent-6: #111a30;
      --color-accent-7: #080b14;

      /* Typography */
      --font-heading: 'VideoJS', 'KONE Information', 'Inter SemiBold', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-body: 'Inter Regular', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-font-3: 'Inter SemiBold', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-font-4: 'KONE Information', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-font-5: 'Consolas', 'JetBrains Mono', 'Courier New', monospace;

      /* Spacing scale */
      --space-1: 1px;
      --space-2: 4px;
      --space-3: 5px;
      --space-4: 6px;
      --space-5: 8px;
      --space-6: 9px;
      --space-7: 10px;
      --space-8: 12px;
      --space-9: 13px;
      --space-10: 14px;
      --space-11: 15px;
      --space-12: 16px;
      --space-13: 20px;
      --space-14: 23px;
      --space-15: 24px;
      --space-16: 30px;
      --space-17: 32px;
      --space-18: 40px;
      --space-19: 48px;
      --space-20: 60px;

      /* Border radii */
      --radius-1: 2px;
      --radius-2: 3px;
      --radius-3: 4px;
      --radius-4: 8px;
      --radius-5: 15px;

      /* Shadows */
      --shadow-1: 0 0 1em #fff;
      --shadow-2: 0 0 0 3px hsla(0,0%,100%,.7);
      --shadow-3: 0 0 3px rgba(0,0,0,.35);
      --shadow-4: 0 4px 10px rgba(0,0,0,.25);
      --shadow-5: 0 0 1px 0 rgba(20,20,20,.06),0 10px 15px -3px rgba(20,20,20,.1),0 4px 6px -2px rgba(20,20,20,.05);
      --shadow-6: 0 3px 5px rgba(0,0,0,.25);

      /* Semantic UI Glassmorphism System Mappings */
      --bg-base: var(--color-accent-7);
      --bg-surface: rgba(17, 26, 48, 0.75);
      --bg-surface-elevated: rgba(18, 38, 88, 0.85);
      --bg-glass-card: rgba(17, 26, 48, 0.65);
      --bg-glass-card-hover: rgba(24, 38, 77, 0.82);
      --border-glass: rgba(218, 228, 255, 0.12);
      --border-glass-bright: rgba(20, 80, 245, 0.45);
      --border-glass-subtle: rgba(218, 228, 255, 0.06);

      --kone-blue: var(--color-primary-1);
      --kone-blue-dark: var(--color-primary-21);
      --kone-cyan: var(--color-primary-4);
      --kone-cyan-light: var(--color-primary-40);
      --kone-electric: var(--color-primary-1);

      --text-primary: var(--color-primary-6);
      --text-secondary: var(--color-neutral-12);
      --text-muted: var(--color-accent-2);

      --accent-emerald: #10B981;
      --accent-amber: var(--color-primary-5);
      --accent-rose: #F43F5E;
      --accent-purple: var(--color-primary-28);
      --accent-indigo: var(--color-primary-13);

      --radius-sm: var(--radius-3);
      --radius-md: var(--radius-4);
      --radius-lg: var(--radius-5);
      --radius-xl: 20px;

      --shadow-glass: var(--shadow-5), var(--shadow-4);
      --shadow-glow: 0 0 25px rgba(20, 80, 245, 0.35);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-body);
      background-color: var(--color-accent-7);
      color: var(--color-primary-3);
      min-height: 100vh;
      overflow-x: hidden;
      line-height: 1.5;
      position: relative;
    }}

    /* Ambient glowing background orbs */
    .ambient-glow {{
      position: fixed;
      border-radius: 50%;
      filter: blur(140px);
      pointer-events: none;
      z-index: 0;
      opacity: 0.35;
      animation: float 25s ease-in-out infinite alternate;
    }}
    .glow-1 {{
      top: -150px;
      left: 10%;
      width: 600px;
      height: 600px;
      background: radial-gradient(circle, var(--color-primary-1), transparent 70%);
    }}
    .glow-2 {{
      top: 30%;
      right: -100px;
      width: 550px;
      height: 550px;
      background: radial-gradient(circle, rgba(102, 168, 204, 0.35), transparent 70%);
      animation-duration: 20s;
    }}
    .glow-3 {{
      bottom: -150px;
      left: 25%;
      width: 700px;
      height: 700px;
      background: radial-gradient(circle, rgba(18, 38, 88, 0.5), transparent 70%);
      animation-duration: 30s;
    }}

    @keyframes float {{
      0% {{ transform: translate(0, 0) scale(1); }}
      50% {{ transform: translate(40px, 30px) scale(1.08); }}
      100% {{ transform: translate(-30px, -20px) scale(0.95); }}
    }}

    /* App Layout */
    .app-wrapper {{
      position: relative;
      z-index: 1;
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }}

    /* Header */
    header.app-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: var(--space-10) var(--space-16);
      background: rgba(17, 26, 48, 0.85);
      backdrop-filter: blur(24px) saturate(180%);
      -webkit-backdrop-filter: blur(24px) saturate(180%);
      border-bottom: 1px solid var(--border-glass);
      position: sticky;
      top: 0;
      z-index: 100;
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: var(--space-12);
    }}

    .kone-brand {{
      display: flex;
      align-items: center;
      gap: var(--space-10);
      text-decoration: none;
      color: inherit;
    }}

    .kone-logo-svg {{
      width: 105px;
      height: 41px;
      display: block;
      border-radius: var(--radius-3);
      box-shadow: 0 2px 10px rgba(20, 80, 245, 0.35);
    }}

    .brand-title-group {{
      display: flex;
      flex-direction: column;
    }}

    .brand-title {{
      font-family: var(--font-heading);
      font-size: 1.15rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #FFFFFF;
      display: flex;
      align-items: center;
      gap: var(--space-5);
    }}

    .brand-subtitle {{
      font-family: var(--font-font-4);
      font-size: 0.72rem;
      color: var(--color-primary-4);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 600;
    }}

    .header-center {{
      display: flex;
      align-items: center;
      gap: var(--space-8);
    }}

    .scenario-pill {{
      display: flex;
      align-items: center;
      gap: var(--space-5);
      padding: var(--space-4) var(--space-10);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-glass);
      border-radius: 9999px;
      font-size: 0.75rem;
      color: var(--color-accent-2);
      font-family: var(--font-body);
    }}

    .scenario-pill .clock-icon {{
      color: var(--color-primary-4);
      display: inline-block;
    }}

    .scenario-pill strong {{
      color: var(--color-primary-6);
      font-family: var(--font-font-3);
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: var(--space-8);
    }}

    /* Persona Selector */
    .persona-container {{
      display: flex;
      align-items: center;
      gap: var(--space-7);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-glass);
      border-radius: 9999px;
      padding: var(--space-2) var(--space-10) var(--space-2) var(--space-4);
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .persona-container:hover {{
      border-color: var(--color-primary-1);
      background: rgba(20, 80, 245, 0.12);
      box-shadow: 0 0 12px rgba(20, 80, 245, 0.3);
    }}

    .persona-avatar {{
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--color-primary-1), var(--color-primary-13));
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 700;
      color: #FFF;
      box-shadow: 0 0 10px rgba(20, 80, 245, 0.4);
      font-family: var(--font-font-3);
    }}

    .persona-info {{
      display: flex;
      flex-direction: column;
      text-align: left;
    }}
    .persona-name {{
      font-family: var(--font-font-3);
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--color-primary-6);
      line-height: 1.1;
    }}
    .persona-role {{
      font-family: var(--font-body);
      font-size: 0.65rem;
      color: var(--color-accent-2);
    }}

    /* Top Action Buttons */
    .btn-action {{
      display: inline-flex;
      align-items: center;
      gap: var(--space-4);
      padding: var(--space-5) var(--space-10);
      border-radius: var(--radius-4);
      font-family: var(--font-font-3);
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-glass);
      color: var(--color-primary-3);
    }}
    .btn-action:hover {{
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(218, 228, 255, 0.3);
      transform: translateY(-1px);
    }}
    .btn-action.active {{
      background: rgba(20, 80, 245, 0.18);
      border-color: var(--color-primary-1);
      color: #FFFFFF;
      box-shadow: 0 0 12px rgba(20, 80, 245, 0.3);
    }}
    .btn-primary {{
      background: linear-gradient(135deg, var(--color-primary-1), var(--color-primary-15));
      border: 1px solid var(--color-primary-13);
      color: #FFFFFF;
      box-shadow: 0 4px 14px rgba(20, 80, 245, 0.4);
      border-radius: var(--radius-4);
    }}
    .btn-primary:hover {{
      background: linear-gradient(135deg, var(--color-primary-14), var(--color-primary-1));
      box-shadow: 0 6px 18px rgba(20, 80, 245, 0.55);
      transform: translateY(-1px);
    }}

    /* Global Context Banner */
    .persona-banner {{
      background: linear-gradient(90deg, rgba(20, 80, 245, 0.16), rgba(102, 168, 204, 0.08), rgba(17, 26, 48, 0.4));
      border-bottom: 1px solid var(--border-glass);
      padding: var(--space-5) var(--space-16);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.78rem;
    }}
    .banner-left {{
      display: flex;
      align-items: center;
      gap: var(--space-7);
    }}
    .banner-tag {{
      background: var(--color-primary-1);
      color: white;
      padding: var(--space-1) var(--space-5);
      border-radius: var(--radius-3);
      font-family: var(--font-font-3);
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 0.04em;
    }}
    .banner-text {{
      color: var(--color-neutral-12);
      font-family: var(--font-body);
    }}
    .banner-quote {{
      font-style: italic;
      color: var(--color-primary-4);
      font-family: var(--font-body);
    }}

    /* Navigation Tabs Bar */
    nav.app-nav {{
      background: rgba(17, 26, 48, 0.75);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-glass);
      padding: 0 var(--space-16);
      display: flex;
      align-items: center;
      gap: var(--space-2);
      overflow-x: auto;
      scrollbar-width: none;
    }}
    nav.app-nav::-webkit-scrollbar {{
      display: none;
    }}

    .nav-tab {{
      display: inline-flex;
      align-items: center;
      gap: var(--space-5);
      padding: var(--space-8) var(--space-12);
      font-family: var(--font-font-3);
      font-size: 0.82rem;
      font-weight: 500;
      color: var(--color-accent-2);
      border-bottom: 2px solid transparent;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
      background: transparent;
      border-top: none;
      border-left: none;
      border-right: none;
    }}
    .nav-tab:hover {{
      color: var(--color-primary-6);
      background: rgba(255, 255, 255, 0.03);
    }}
    .nav-tab.active {{
      color: #FFFFFF;
      font-weight: 600;
      border-bottom-color: var(--color-primary-1);
      background: linear-gradient(180deg, transparent, rgba(20, 80, 245, 0.12));
    }}
    .nav-tab .tab-num {{
      font-family: var(--font-font-5);
      font-size: 0.68rem;
      padding: var(--space-1) var(--space-3);
      border-radius: var(--radius-2);
      background: rgba(255, 255, 255, 0.06);
      color: var(--color-accent-3);
    }}
    .nav-tab.active .tab-num {{
      background: rgba(20, 80, 245, 0.25);
      color: var(--color-primary-8);
    }}
    .nav-tab .tab-badge-critical {{
      background: rgba(244, 63, 94, 0.2);
      border: 1px solid rgba(244, 63, 94, 0.4);
      color: #FB7185;
      font-size: 0.62rem;
      padding: var(--space-1) var(--space-4);
      border-radius: 999px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    /* Main Container */
    main.main-content {{
      flex: 1;
      padding: var(--space-15) var(--space-16) var(--space-19);
      max-width: 1720px;
      width: 100%;
      margin: 0 auto;
    }}

    /* Bento Grid System */
    .bento-grid {{
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: var(--space-13);
      margin-bottom: var(--space-15);
    }}

    .col-12 {{ grid-column: span 12; }}
    .col-8 {{ grid-column: span 8; }}
    .col-7 {{ grid-column: span 7; }}
    .col-6 {{ grid-column: span 6; }}
    .col-5 {{ grid-column: span 5; }}
    .col-4 {{ grid-column: span 4; }}
    .col-3 {{ grid-column: span 3; }}

    @media (max-width: 1200px) {{
      .col-8, .col-7, .col-5, .col-4, .col-6 {{ grid-column: span 12; }}
    }}

    /* Glass Cards */
    .glass-card {{
      background: var(--bg-glass-card);
      backdrop-filter: blur(20px) saturate(180%);
      -webkit-backdrop-filter: blur(20px) saturate(180%);
      border: 1px solid var(--border-glass);
      border-radius: var(--radius-5);
      padding: var(--space-14);
      box-shadow: var(--shadow-5);
      position: relative;
      overflow: hidden;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .glass-card:hover {{
      border-color: rgba(20, 80, 245, 0.45);
      background: var(--bg-glass-card-hover);
      box-shadow: var(--shadow-4), 0 10px 30px -10px rgba(20, 80, 245, 0.3);
      transform: translateY(-2px);
    }}
    .glass-card.highlight-card {{
      border-color: rgba(20, 80, 245, 0.6);
      background: linear-gradient(135deg, rgba(24, 38, 77, 0.85), rgba(17, 26, 48, 0.7));
      box-shadow: var(--shadow-5), 0 0 25px rgba(20, 80, 245, 0.3);
    }}

    .card-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: var(--space-12);
    }}
    .card-eyebrow {{
      font-family: var(--font-font-4);
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--color-primary-4);
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: var(--space-4);
    }}
    .card-title {{
      font-family: var(--font-heading);
      font-size: 1.12rem;
      font-weight: 700;
      color: #FFFFFF;
      letter-spacing: -0.01em;
    }}
    .card-subtitle {{
      font-family: var(--font-body);
      font-size: 0.78rem;
      color: var(--color-accent-2);
      margin-top: var(--space-1);
    }}

    /* Badges */
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: var(--space-2);
      padding: var(--space-2) var(--space-5);
      border-radius: 9999px;
      font-size: 0.68rem;
      font-weight: 600;
      letter-spacing: 0.02em;
    }}
    .badge-kone {{
      background: rgba(20, 80, 245, 0.2);
      border: 1px solid rgba(20, 80, 245, 0.5);
      color: var(--color-primary-8);
    }}
    .badge-synthetic {{
      background: rgba(142, 141, 252, 0.18);
      border: 1px solid rgba(142, 141, 252, 0.45);
      color: var(--color-primary-28);
    }}
    .badge-emerald {{
      background: rgba(16, 185, 129, 0.16);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #34D399;
    }}
    .badge-amber {{
      background: rgba(255, 204, 102, 0.16);
      border: 1px solid rgba(255, 204, 102, 0.4);
      color: var(--color-primary-5);
    }}
    .badge-rose {{
      background: rgba(244, 63, 94, 0.16);
      border: 1px solid rgba(244, 63, 94, 0.4);
      color: #FB7185;
    }}

    /* KPI Headline Scorecards */
    .scorecard-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: var(--space-12);
      margin-bottom: var(--space-13);
    }}
    .scorecard {{
      background: rgba(255, 255, 255, 0.025);
      border: 1px solid var(--border-glass);
      border-radius: var(--radius-4);
      padding: var(--space-12);
      box-shadow: var(--shadow-6);
      transition: all 0.2s ease;
    }}
    .scorecard:hover {{
      background: rgba(255, 255, 255, 0.05);
      border-color: rgba(218, 228, 255, 0.25);
      transform: translateY(-2px);
      box-shadow: var(--shadow-4);
    }}
    .scorecard-label {{
      font-family: var(--font-body);
      font-size: 0.72rem;
      color: var(--color-accent-2);
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: var(--space-4);
    }}
    .scorecard-val {{
      font-family: var(--font-font-5);
      font-size: 1.75rem;
      font-weight: 800;
      color: #FFFFFF;
      letter-spacing: -0.02em;
      line-height: 1.1;
    }}
    .scorecard-delta {{
      font-family: var(--font-font-3);
      font-size: 0.72rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: var(--space-2);
      margin-top: var(--space-4);
    }}
    .delta-positive {{ color: var(--accent-emerald); }}
    .delta-warning {{ color: var(--accent-amber); }}
    .delta-neutral {{ color: var(--color-accent-2); }}

    /* Data Tables */
    .table-container {{
      width: 100%;
      overflow-x: auto;
      border-radius: var(--radius-4);
      border: 1px solid var(--border-glass-subtle);
      background: rgba(17, 26, 48, 0.45);
    }}
    table.kone-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-family: var(--font-body);
      font-size: 0.8rem;
    }}
    table.kone-table th {{
      padding: var(--space-8) var(--space-10);
      background: rgba(18, 38, 88, 0.7);
      color: var(--color-accent-3);
      font-family: var(--font-font-3);
      font-weight: 600;
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      border-bottom: 1px solid var(--border-glass);
      white-space: nowrap;
    }}
    table.kone-table td {{
      padding: var(--space-8) var(--space-10);
      border-bottom: 1px solid var(--border-glass-subtle);
      color: var(--color-primary-6);
      vertical-align: middle;
    }}
    table.kone-table tr:hover td {{
      background: rgba(20, 80, 245, 0.08);
    }}
    table.kone-table tr.clickable {{
      cursor: pointer;
    }}

    /* Progress bar */
    .progress-bar-bg {{
      width: 100%;
      height: 6px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 999px;
      overflow: hidden;
      margin-top: var(--space-2);
    }}
    .progress-bar-fill {{
      height: 100%;
      border-radius: 999px;
      background: linear-gradient(90deg, var(--color-primary-1), var(--color-primary-4));
    }}

    /* Modal / Slide-out Drawer */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(8, 11, 20, 0.82);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: var(--space-13);
    }}
    .modal-overlay.open {{
      display: flex;
    }}
    .modal-card {{
      background: rgba(17, 26, 48, 0.94);
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
      border: 1px solid var(--color-primary-13);
      border-radius: var(--radius-5);
      max-width: 780px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), var(--shadow-glow);
      padding: var(--space-16);
      position: relative;
    }}
    .modal-close {{
      position: absolute;
      top: var(--space-13);
      right: var(--space-13);
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border-glass);
      color: var(--color-accent-2);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .modal-close:hover {{
      background: rgba(244, 63, 94, 0.2);
      border-color: var(--accent-rose);
      color: #FFF;
    }}

    /* Interactive Simulation Controls */
    .sim-slider-group {{
      margin-bottom: var(--space-12);
    }}
    .sim-slider-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: var(--space-4);
      font-size: 0.78rem;
    }}
    .sim-slider-label {{
      color: var(--color-accent-2);
      font-weight: 500;
      font-family: var(--font-body);
    }}
    .sim-slider-val {{
      font-weight: 700;
      color: var(--color-primary-10);
      font-family: var(--font-font-5);
    }}
    input[type=range].sim-slider {{
      -webkit-appearance: none;
      width: 100%;
      height: 6px;
      border-radius: var(--radius-3);
      background: rgba(218, 228, 255, 0.15);
      outline: none;
    }}
    input[type=range].sim-slider::-webkit-slider-thumb {{
      -webkit-appearance: none;
      appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: var(--color-primary-1);
      cursor: pointer;
      box-shadow: 0 0 12px rgba(20, 80, 245, 0.7);
      transition: transform 0.15s ease;
    }}
    input[type=range].sim-slider::-webkit-slider-thumb:hover {{
      transform: scale(1.2);
      background: var(--color-primary-13);
    }}

    /* Narrative Scene Player */
    .scene-navigator {{
      display: flex;
      gap: var(--space-5);
      overflow-x: auto;
      padding-bottom: var(--space-7);
      margin-bottom: var(--space-13);
    }}
    .scene-pill-btn {{
      padding: var(--space-5) var(--space-10);
      border-radius: var(--radius-4);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-glass);
      color: var(--color-accent-2);
      font-size: 0.74rem;
      white-space: nowrap;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: var(--space-1);
    }}
    .scene-pill-btn:hover {{
      background: rgba(255, 255, 255, 0.08);
      color: var(--color-primary-6);
    }}
    .scene-pill-btn.active {{
      background: rgba(20, 80, 245, 0.18);
      border-color: var(--color-primary-1);
      color: #FFFFFF;
      box-shadow: 0 0 10px rgba(20, 80, 245, 0.3);
    }}
    .scene-pill-btn .scene-num {{
      font-family: var(--font-font-5);
      font-size: 0.65rem;
      color: var(--color-primary-10);
      font-weight: 700;
      text-transform: uppercase;
    }}

    /* SVG Charts Canvas */
    .chart-container {{
      width: 100%;
      position: relative;
    }}

    /* Utility */
    .flex-between {{ display: flex; align-items: center; justify-content: space-between; }}
    .flex-gap-8 {{ display: flex; align-items: center; gap: var(--space-5); }}
    .flex-gap-12 {{ display: flex; align-items: center; gap: var(--space-8); }}
    .text-cyan {{ color: var(--color-primary-4); }}
    .text-emerald {{ color: var(--accent-emerald); }}
    .text-amber {{ color: var(--color-primary-5); }}
    .text-rose {{ color: var(--accent-rose); }}
    .font-mono {{ font-family: var(--font-font-5); }}

    /* Tab content view containers */
    .tab-view {{
      display: none;
      animation: fadeIn 0.25s ease;
    }}
    .tab-view.active {{
      display: block;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Print Styles */
    @media print {{
      body {{ background: white; color: black; }}
      .app-header, .persona-banner, .app-nav, .ambient-glow {{ display: none !important; }}
      .glass-card {{ background: #FFF !important; border: 1px solid #CCC !important; color: #000 !important; }}
      .tab-view {{ display: block !important; page-break-after: always; }}
    }}
  </style>
</head>
<body>
  <!-- Ambient background glow elements -->
  <div class="ambient-glow glow-1"></div>
  <div class="ambient-glow glow-2"></div>
  <div class="ambient-glow glow-3"></div>

  <div class="app-wrapper">
    <!-- Main Application Header -->
    <header class="app-header">
      <div class="header-left">
        <a href="#sense" class="kone-brand" onclick="switchTab('sense')">
          <!-- Official KONE SVG Logo -->
          <svg class="kone-logo-svg" viewBox="0 0 226 88" aria-label="KONE logo">
            <rect width="226" height="88" fill="#0058A3"/>
            <path d="M0 88H51.0117V0H0V88Z" fill="white"/>
            <path d="M116.596 0H167.607V88H116.596V0Z" fill="white"/>
            <path d="M58.2991 0H109.311V88H58.2991V0Z" fill="white"/>
            <path d="M174.99 88H226.002V0H174.99V88Z" fill="white"/>
            <path d="M0 88H51.0117V0H0V88ZM31.9391 62.8327L19.1105 44.9872V62.8327H9.13196V25.1693H19.1124V41.6007L31.4657 25.1693H43.2187L29.5776 42.8985L44.1542 62.8327H31.9391Z" fill="#1450F5"/>
            <path d="M116.596 88V0H167.607V88H116.596ZM150.421 62.8307H158.742V25.1693H149.482V45.6294L134.178 25.1693H125.461V62.8307H134.691V40.785L150.421 62.8307Z" fill="#1450F5"/>
            <path d="M83.8012 33.2153C78.4834 33.2153 74.3738 37.6157 74.3738 43.9924C74.3738 50.369 78.4815 54.7694 83.8012 54.7694C89.1209 54.7694 93.2267 50.3842 93.2267 43.9924C93.2267 37.6005 89.1039 33.2153 83.8012 33.2153Z" fill="#1450F5"/>
            <path d="M58.2991 88V0H109.311V88H58.2991ZM64.3971 43.9924C64.3971 55.6518 73.0481 63.6597 83.803 63.6597C94.5618 63.6597 103.213 55.6537 103.213 43.9924C103.213 32.3311 94.558 24.3403 83.803 24.3403C73.0481 24.3403 64.3971 32.333 64.3971 43.9924Z" fill="#1450F5"/>
            <path d="M174.99 0V88H226.002V0H174.99ZM214.654 33.4688H196.199V39.8359H211.63L211.626 47.8992H196.201V54.2853H214.656V62.8345H186.342V25.1655H214.656L214.654 33.4688Z" fill="#1450F5"/>
          </svg>
          <div class="brand-title-group">
            <span class="brand-title">Marketing OS</span>
            <span class="brand-subtitle">Growth Intelligence Layer</span>
          </div>
        </a>
      </div>

      <div class="header-center">
        <div class="scenario-pill">
          <span class="clock-icon">⏱</span>
          <span>Scenario Clock: <strong>Mon 1 Feb 2027</strong></span>
          <span style="opacity: 0.5;">|</span>
          <span>Launch: <strong>15 Mar 2027</strong></span>
          <span style="opacity: 0.5;">|</span>
          <span>Day-90: <strong>13 Jun 2027</strong></span>
        </div>
      </div>

      <div class="header-right">
        <!-- Persona Switcher -->
        <div class="persona-container" onclick="cyclePersona()" title="Click to switch persona perspective">
          <div class="persona-avatar" id="currentPersonaAvatar">AV</div>
          <div class="persona-info">
            <div class="persona-name" id="currentPersonaName">Anna Virtanen</div>
            <div class="persona-role" id="currentPersonaRole">Dir. Growth Intelligence (Espoo)</div>
          </div>
          <span style="font-size: 0.65rem; color: var(--kone-cyan);">▼</span>
        </div>

        <!-- Telemetry Status Pill -->
        <div class="scenario-pill" style="border-color: rgba(20, 80, 245, 0.4); background: rgba(20, 80, 245, 0.1); padding: 5px 12px;">
          <span style="width: 8px; height: 8px; border-radius: 50%; background: #10B981; display: inline-block; box-shadow: 0 0 8px #10B981;"></span>
          <span style="font-size: 0.72rem; color: var(--color-primary-8); font-weight: 600;">38 Buildings Active</span>
        </div>
      </div>
    </header>

    <!-- Contextual Persona & Theme Banner -->
    <div class="persona-banner">
      <div class="banner-left">
        <span class="banner-tag" id="bannerTag">LEADERSHIP THEME</span>
        <span class="banner-text" id="bannerText">"If KONE only knew what KONE knows" — Turning connected asset & technician signals into shared growth decisions.</span>
      </div>
      <div class="banner-right">
        <span class="banner-quote" id="bannerQuote">Hans's Monday Morning View: Awareness → Consideration → Purchase → Delivery → Loyalty</span>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <nav class="app-nav">
      <button class="nav-tab active" id="tab-btn-sense" onclick="switchTab('sense')">
        <span class="tab-num">01</span>
        <span>Sense</span>
      </button>
      <button class="nav-tab" id="tab-btn-diagnose" onclick="switchTab('diagnose')">
        <span class="tab-num">02</span>
        <span>Diagnose</span>
      </button>
      <button class="nav-tab" id="tab-btn-prioritise" onclick="switchTab('prioritise')">
        <span class="tab-num">03</span>
        <span>Prioritise</span>
      </button>
      <button class="nav-tab" id="tab-btn-replicate" onclick="switchTab('replicate')">
        <span class="tab-num">04</span>
        <span>Replicate</span>
        <span class="tab-badge-critical">Critical Screen</span>
      </button>
      <button class="nav-tab" id="tab-btn-execution" onclick="switchTab('execution')">
        <span class="tab-num">05</span>
        <span>Execution (Act 2)</span>
      </button>
      <button class="nav-tab" id="tab-btn-learn" onclick="switchTab('learn')">
        <span class="tab-num">06</span>
        <span>Learn (Day-90)</span>
      </button>
      <button class="nav-tab" id="tab-btn-ingredients" onclick="switchTab('ingredients')">
        <span class="tab-num">07</span>
        <span>Ingredients</span>
      </button>
      <button class="nav-tab" id="tab-btn-simulation" onclick="switchTab('simulation')">
        <span class="tab-num">08</span>
        <span>Simulation Sandbox</span>
      </button>
      <button class="nav-tab" id="tab-btn-workshop" onclick="switchTab('workshop')">
        <span class="tab-num">09</span>
        <span>Workshop & Script</span>
      </button>
    </nav>

    <!-- Main Content Container -->
    <main class="main-content">
      
      <!-- ========================================== -->
      <!-- VIEW 1: SENSE — Marketing's Monday Morning View -->
      <!-- ========================================== -->
      <section class="tab-view active" id="view-sense">
        <!-- Anchors Scorecard Grid -->
        <div class="scorecard-grid">
          <div class="scorecard">
            <div class="scorecard-label">
              <span>Service & Modernization Share</span>
              <span class="badge badge-kone">[KONE] Q3 '26</span>
            </div>
            <div class="scorecard-val">65%</div>
            <div class="scorecard-delta delta-positive">
              <span>↑ Core Growth Engine</span>
              <span style="color: var(--text-muted); font-size:0.65rem;">(Sales share)</span>
            </div>
          </div>

          <div class="scorecard">
            <div class="scorecard-label">
              <span>Connected Service Base</span>
              <span class="badge badge-kone">[KONE] Q3 '26</span>
            </div>
            <div class="scorecard-val">&gt; 45%</div>
            <div class="scorecard-delta delta-positive">
              <span>↑ Active Telemetry Signal</span>
              <span style="color: var(--text-muted); font-size:0.65rem;">(Expanding global advantage)</span>
            </div>
          </div>

          <div class="scorecard">
            <div class="scorecard-label">
              <span>Modernization Order Growth</span>
              <span class="badge badge-kone">[KONE] Q3 '26</span>
            </div>
            <div class="scorecard-val">~10%</div>
            <div class="scorecard-delta delta-positive">
              <span>↑ Led group order growth</span>
              <span style="color: var(--text-muted); font-size:0.65rem;">(Comparable rates)</span>
            </div>
          </div>

          <div class="scorecard">
            <div class="scorecard-label">
              <span>Monitored Scenario Base</span>
              <span class="badge badge-synthetic">[SYNTHETIC]</span>
            </div>
            <div class="scorecard-val">944,000</div>
            <div class="scorecard-delta delta-neutral">
              <span>7 European Markets</span>
              <span style="color: var(--text-muted); font-size:0.65rem;">(Installed elevators)</span>
            </div>
          </div>
        </div>

        <!-- Bento Grid: Opportunity Register + Signal Flow -->
        <div class="bento-grid">
          <!-- Opportunity Register -->
          <div class="glass-card col-8 highlight-card">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">
                  <span>●</span>
                  <span>Monday Morning Opportunity Register (Table A2)</span>
                  <span class="badge badge-synthetic">[SYNTHETIC]</span>
                </div>
                <h2 class="card-title">Where Commercial Signals Meet Latent Demand</h2>
                <p class="card-subtitle">Monday 1 February 2027, 09:00. Algorithmic triage across 7 key markets.</p>
              </div>
              <button class="btn-action" onclick="switchTab('diagnose')">Diagnose DACH →</button>
            </div>

            <div class="table-container">
              <table class="kone-table">
                <thead>
                  <tr>
                    <th>Case ID</th>
                    <th>Opportunity & Play</th>
                    <th>Signal Detected</th>
                    <th>Annual Potential</th>
                    <th>Confidence</th>
                    <th>Recommended Action</th>
                  </tr>
                </thead>
                <tbody id="opportunityTableBody">
                  <!-- Populated by JS -->
                </tbody>
              </table>
            </div>

            <div style="margin-top: 14px; padding: 12px; background: rgba(0, 163, 224, 0.05); border: 1px solid rgba(0, 163, 224, 0.2); border-radius: 8px; font-size: 0.76rem; color: #CBD5E1;">
              <strong style="color: var(--kone-cyan);">Strategic Takeaway:</strong> Modernization is growing, but Iberia's activation rate is lagging at 40% of the DACH rate despite having an identical old installed base (36% vs 38% 15+ years). This creates an immediate EUR 6.1m replication opportunity.
            </div>
          </div>

          <!-- Signal Journey Diagram -->
          <div class="glass-card col-4">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">SIGNAL TO DECISION FLOW</div>
                <h3 class="card-title" style="font-size: 0.98rem;">The Connected Brain</h3>
              </div>
              <span class="badge badge-kone">Concept</span>
            </div>

            <div style="display: flex; flex-direction: column; gap: 10px; font-size: 0.74rem;">
              <div style="padding: 10px; background: rgba(255, 255, 255, 0.03); border-radius: 8px; border-left: 3px solid var(--kone-cyan);">
                <div style="font-weight: 700; color: #FFF;">1. Connected Elevators (45%+)</div>
                <div style="color: var(--text-secondary);">Continuous sensor telemetry: usage cycles, door stops, vibration anomalies.</div>
              </div>
              <div style="padding: 10px; background: rgba(255, 255, 255, 0.03); border-radius: 8px; border-left: 3px solid var(--accent-emerald);">
                <div style="font-weight: 700; color: #FFF;">2. Service Technician Referrals</div>
                <div style="color: var(--text-secondary);">Maintenance techs spot aged shafts on site and submit 2-question qualification.</div>
              </div>
              <div style="padding: 10px; background: rgba(255, 255, 255, 0.03); border-radius: 8px; border-left: 3px solid var(--kone-blue);">
                <div style="font-weight: 700; color: #FFF;">3. Marketing OS Opportunity Triage</div>
                <div style="color: var(--text-secondary);">Matches building equipment to modular One Week replacement eligibility.</div>
              </div>
              <div style="padding: 10px; background: rgba(255, 255, 255, 0.03); border-radius: 8px; border-left: 3px solid var(--accent-purple);">
                <div style="font-weight: 700; color: #FFF;">4. Handover to Local Markets</div>
                <div style="color: var(--text-secondary);">Packaged briefs with 62% reusable content & field enablement routines.</div>
              </div>
            </div>
          </div>

          <!-- Market Comparison Matrix (Table A1) -->
          <div class="glass-card col-12">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">7-MARKET COMPARISON MATRIX (TABLE A1)</div>
                <h3 class="card-title">Installed Base & Modernization Readiness Baseline</h3>
                <p class="card-subtitle">Synthetic scenario dataset modeling service-base elevators, installation age, and activation.</p>
              </div>
              <div class="flex-gap-8">
                <span class="badge badge-synthetic">[SYNTHETIC DEMO DATA]</span>
              </div>
            </div>

            <div class="table-container">
              <table class="kone-table">
                <thead>
                  <tr>
                    <th>Market</th>
                    <th>Base Units</th>
                    <th>15+ Years (%)</th>
                    <th>Connected (%)</th>
                    <th>Activation Rate (%)</th>
                    <th>Baseline Conversion (%)</th>
                    <th>Relative to DACH</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody id="marketTableBody">
                  <!-- Populated by JS -->
                </tbody>
              </table>
            </div>
            
            <div style="margin-top: 12px; font-size: 0.72rem; color: var(--text-muted); display: flex; justify-content: space-between;">
              <span>*Base means modeled service-base elevators. Age is installation age, not building age. Activation is share of eligible accounts contacted in prior 90 days.</span>
              <span>Scope: 7 European benchmark markets</span>
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- VIEW 2: DIAGNOSE — Why Is This Happening? -->
      <!-- ========================================== -->
      <section class="tab-view" id="view-diagnose">
        <div class="bento-grid">
          <!-- Main Diagnostic Waterfall -->
          <div class="glass-card col-8 highlight-card">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">
                  <span>●</span>
                  <span>DACH ORDER SURGE DECOMPOSITION (TABLES A3 & A4)</span>
                  <span class="badge badge-synthetic">[SYNTHETIC]</span>
                </div>
                <h2 class="card-title">Why DACH, Not DACH's Campaign?</h2>
                <p class="card-subtitle">Q4 2026 order index grew +23.0% QoQ (+27.3 pts YoY). Modeled driver breakdown.</p>
              </div>
              <div style="text-align: right;">
                <div style="font-size: 1.5rem; font-weight: 800; color: var(--accent-emerald);">+27.3 pts</div>
                <div style="font-size: 0.68rem; color: var(--text-secondary);">YoY Growth Index</div>
              </div>
            </div>

            <!-- Custom SVG Waterfall Chart -->
            <div id="diagnoseWaterfallContainer" style="margin: 20px 0; min-height: 240px;">
              <!-- Rendered via JS -->
            </div>

            <!-- Driver Breakdown Table -->
            <div class="table-container">
              <table class="kone-table">
                <thead>
                  <tr>
                    <th>Hypothesized Driver</th>
                    <th>Contribution</th>
                    <th>Share (%)</th>
                    <th>Field Evidence & Supporting Observation</th>
                  </tr>
                </thead>
                <tbody id="dachDriversTableBody">
                  <!-- Populated by JS -->
                </tbody>
              </table>
            </div>
          </div>

          <!-- Field Reality Callout & Quotation -->
          <div class="glass-card col-4">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">THE CRUCIAL INSIGHT</div>
                <h3 class="card-title" style="font-size: 1rem;">Anna & Jonas's Diagnosis</h3>
              </div>
              <span class="badge badge-kone">Field Reality</span>
            </div>

            <div style="background: rgba(0, 88, 163, 0.15); border: 1px solid rgba(0, 163, 224, 0.3); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
              <div style="font-size: 0.85rem; font-style: italic; color: #FFFFFF; line-height: 1.6; margin-bottom: 10px;">
                "The campaign is the newest thing we have, so it takes the credit. But the evidence says the account list did the work: standard shafts converted 2.4x better, and technicians flagged 1,900 accounts. If that is right, it changes what we scale."
              </div>
              <div style="display: flex; align-items: center; justify-content: space-between; font-size: 0.72rem;">
                <span style="color: var(--kone-cyan); font-weight: 600;">— Jonas Weber & Anna Virtanen</span>
                <span style="color: var(--text-muted);">Scene 3 Field Diagnosis</span>
              </div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 12px; font-size: 0.75rem;">
              <div style="padding: 12px; background: rgba(255, 255, 255, 0.03); border-radius: 8px; border: 1px solid var(--border-glass);">
                <div style="font-weight: 700; color: var(--accent-emerald); margin-bottom: 4px;">Standard Shaft Conversion: 2.4x</div>
                <div style="color: var(--text-secondary);">48 / 100 quotes ordered on standard shafts vs only 20 / 100 on non-standard shafts. Standardized modularity is the commercial catalyst.</div>
              </div>

              <div style="padding: 12px; background: rgba(255, 255, 255, 0.03); border-radius: 8px; border: 1px solid var(--border-glass);">
                <div style="font-weight: 700; color: var(--kone-cyan); margin-bottom: 4px;">Technician Referrals: 1,900 Accounts</div>
                <div style="color: var(--text-secondary);">Maintenance crews opened doors that cold digital ads could never reach. Service integration is marketing's strongest weapon.</div>
              </div>

              <div style="padding: 12px; background: rgba(255, 255, 255, 0.03); border-radius: 8px; border: 1px solid var(--border-glass);">
                <div style="font-weight: 700; color: var(--accent-rose); margin-bottom: 4px;">Creative Alone: +0.5 pts</div>
                <div style="color: var(--text-secondary);">Aided recall was identical (42% vs 41%). Marketing cannot simply broadcast glossy ads to other markets and expect DACH's results.</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- VIEW 3: PRIORITISE — What Deserves Leadership Attention? -->
      <!-- ========================================== -->
      <section class="tab-view" id="view-prioritise">
        <div class="bento-grid">
          <!-- Decision Thresholds & Multi-Criteria Matrix -->
          <div class="glass-card col-8 highlight-card">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">
                  <span>●</span>
                  <span>PRIORITISATION & DECISION RULES (TABLES A5, A6, A7)</span>
                  <span class="badge badge-synthetic">[SYNTHETIC]</span>
                </div>
                <h2 class="card-title">Four Candidates. One Worth Scaling Now.</h2>
                <p class="card-subtitle">Leadership rule: Annual potential &gt;= EUR 5.0m, Suitability match &gt;= 75/100, Confidence &gt;= 70/100.</p>
              </div>
              <button class="btn-action btn-primary" onclick="switchTab('replicate')">Proceed to Replicate Iberia →</button>
            </div>

            <div class="table-container">
              <table class="kone-table">
                <thead>
                  <tr>
                    <th>Candidate</th>
                    <th>Value /5</th>
                    <th>Strategic /5</th>
                    <th>Ease /5</th>
                    <th>Speed /5</th>
                    <th>Confidence /5</th>
                    <th>Priority /100</th>
                    <th>Est. Potential</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody id="prioritiseTableBody">
                  <!-- Populated by JS -->
                </tbody>
              </table>
            </div>

            <div style="margin-top: 16px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; font-size: 0.74rem;">
              <div style="padding: 10px; background: rgba(255, 255, 255, 0.03); border-radius: 8px; border-left: 2px solid var(--accent-emerald);">
                <strong style="color: #FFF;">Iberia (Priority 91):</strong> Clears all gates. Base profile matches DACH, local leadership ready to partner.
              </div>
              <div style="padding: 10px; background: rgba(255, 255, 255, 0.03); border-radius: 8px; border-left: 2px solid var(--kone-cyan);">
                <strong style="color: #FFF;">Benelux (Priority 70):</strong> Strategic interest, but potential EUR 3.4m is below threshold. Marked for "Adapt & Test".
              </div>
              <div style="padding: 10px; background: rgba(255, 255, 255, 0.03); border-radius: 8px; border-left: 2px solid var(--text-muted);">
                <strong style="color: #FFF;">Poland & UK (Priority &lt; 55):</strong> Low equipment fit and readiness. Retained on hold to prevent fragmented focus.
              </div>
            </div>
          </div>

          <!-- Suitability Match Radar & Formula -->
          <div class="glass-card col-4">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">GOVERNANCE & GATES</div>
                <h3 class="card-title" style="font-size: 0.98rem;">The Replication Policy</h3>
              </div>
              <span class="badge badge-kone">Decision Model</span>
            </div>

            <div style="font-size: 0.76rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 16px;">
              <strong style="color: #FFF;">Priority Formula:</strong>
              <div class="font-mono" style="padding: 8px; background: rgba(0, 0, 0, 0.3); border-radius: 6px; margin: 6px 0; font-size: 0.7rem; color: var(--kone-cyan);">
                Priority = 100 × (0.30·Val + 0.25·Strat + 0.15·Ease + 0.15·Speed + 0.15·Conf) / 5
              </div>
              <div style="margin-top: 8px;">
                <strong style="color: #FFF;">Replication Gate Requirements:</strong>
                <ul style="margin-left: 16px; margin-top: 4px; display: flex; flex-direction: column; gap: 4px;">
                  <li>Annual commercial potential ≥ EUR 5.0m</li>
                  <li>Suitability match score ≥ 75 / 100</li>
                  <li>Evidence confidence ≥ 70 / 100</li>
                  <li>Local operational feasibility & sign-off</li>
                </ul>
              </div>
            </div>

            <!-- Radar chart representation for Iberia vs Benelux -->
            <div id="prioritiseRadarContainer" style="min-height: 200px; display: flex; align-items: center; justify-content: center;">
              <!-- Rendered via JS -->
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- VIEW 4: REPLICATE — The Critical Screen -->
      <!-- ========================================== -->
      <section class="tab-view" id="view-replicate">
        <!-- Hero Spotlight on the Handover -->
        <div class="glass-card highlight-card" style="margin-bottom: 24px; border-left: 4px solid var(--kone-cyan);">
          <div class="card-header">
            <div>
              <div class="card-eyebrow">
                <span>★</span>
                <span>THE CRITICAL WORKSHOP SCREEN</span>
                <span class="badge badge-kone">Focal Discussion Point</span>
              </div>
              <h2 class="card-title" style="font-size: 1.35rem;">"If KONE Only Knew What KONE Knows"</h2>
              <p class="card-subtitle">Replicating 'Life, upgraded in ONE week' from DACH to Iberia. What travels vs what must be rebuilt locally.</p>
            </div>
            <span class="badge badge-synthetic">Suitability Match: 84 / 100</span>
          </div>

          <div style="padding: 16px; background: rgba(0, 163, 224, 0.08); border: 1px solid rgba(0, 163, 224, 0.25); border-radius: 10px; font-size: 0.82rem; color: #E2E8F0; line-height: 1.6;">
            <strong>The Core Principle:</strong> Replication is a collaborative handover, not a central mandate broadcast. The German playbook relies on 5 capabilities. In Iberia, <strong>two of them are not running</strong> and must be rebuilt locally before any campaign is launched.
          </div>
        </div>

        <div class="bento-grid">
          <!-- 5 Playbook Elements & Gap Analysis -->
          <div class="glass-card col-8">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">CAPABILITY MATCH & GAP RESOLUTION (TABLES A8 & 7)</div>
                <h3 class="card-title">The Five Elements of the Playbook</h3>
              </div>
            </div>

            <div class="table-container">
              <table class="kone-table">
                <thead>
                  <tr>
                    <th>Element</th>
                    <th>Status in DACH (Source)</th>
                    <th>Status in Iberia</th>
                    <th>What Is Needed Locally</th>
                    <th>Ownership</th>
                  </tr>
                </thead>
                <tbody id="playbookTableBody">
                  <!-- Populated by JS -->
                </tbody>
              </table>
            </div>
          </div>

          <!-- Global to Local Handover Accord -->
          <div class="glass-card col-4">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">LOCAL REALITY CHECK</div>
                <h3 class="card-title" style="font-size: 0.98rem;">The Scope Negotiation</h3>
              </div>
              <span class="badge badge-amber">Field Friction</span>
            </div>

            <div style="font-size: 0.78rem; line-height: 1.6; display: flex; flex-direction: column; gap: 12px;">
              <div style="padding: 12px; background: rgba(255, 255, 255, 0.03); border-radius: 8px; border: 1px solid var(--border-glass);">
                <div style="color: var(--kone-cyan); font-weight: 700; margin-bottom: 4px;">Marc Puig (KONE Iberia):</div>
                <p style="color: #E2E8F0; font-style: italic;">"The German account list assumes every building has an installation year on file. Ours does not. Give me 6 weeks to clean up the data and I will take 38 buildings, not the initial 120."</p>
              </div>

              <div style="padding: 12px; background: rgba(255, 255, 255, 0.03); border-radius: 8px; border: 1px solid var(--border-glass);">
                <div style="color: var(--accent-emerald); font-weight: 700; margin-bottom: 4px;">Anna Virtanen (Global HQ):</div>
                <p style="color: #E2E8F0; font-style: italic;">"Take the 38. Validate each asset before quoting. We will review the next cohort only after the pilot and capacity check."</p>
              </div>

              <div style="padding: 12px; background: rgba(0, 88, 163, 0.2); border-radius: 8px; border: 1px solid rgba(0, 163, 224, 0.3);">
                <div style="font-weight: 700; color: #FFF; margin-bottom: 4px;">Handover Agreement Signed:</div>
                <ul style="margin-left: 16px; color: var(--text-secondary); font-size: 0.72rem;">
                  <li>Scope: 38 buildings (45 elevator quotes)</li>
                  <li>Preparation: 21 calendar days (22 Feb - 14 Mar)</li>
                  <li>Launch Target: 15 March 2027</li>
                  <li>Target Conversion: &gt; 30% (vs 24% baseline)</li>
                </ul>
              </div>

              <button class="btn-action btn-primary" style="justify-content: center; width: 100%;" onclick="switchTab('execution')">
                Open Marc Puig's Iberia Console →
              </button>
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- VIEW 5: EXECUTION — Act 2 Iberia Workspace -->
      <!-- ========================================== -->
      <section class="tab-view" id="view-execution">
        <!-- Execution Header & Persona Banner -->
        <div class="glass-card highlight-card" style="margin-bottom: 20px;">
          <div class="flex-between">
            <div class="flex-gap-12">
              <div class="persona-avatar" style="width: 44px; height: 44px; font-size: 1.1rem;">MP</div>
              <div>
                <div class="card-eyebrow">ACT 2 | MARKET EXECUTION WORKSPACE</div>
                <h2 class="card-title">Marc Puig — Modernization Lead, KONE Iberia</h2>
                <p class="card-subtitle">38 Buildings Pilot | 21 Calendar Days Preparation | Launch: 15 March 2027</p>
              </div>
            </div>
            <div class="flex-gap-8">
              <span class="badge badge-emerald">Pre-Launch Gate: 96 / 100</span>
              <button class="btn-action" onclick="toggleFieldEnablementGate()">Toggle Final Field Gate (100%)</button>
            </div>
          </div>
        </div>

        <div class="bento-grid">
          <!-- Content Supply Chain Efficiency -->
          <div class="glass-card col-6">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">CONTENT SUPPLY CHAIN TRANSFORMATION (TABLE A9)</div>
                <h3 class="card-title">Create Once, Adapt Everywhere</h3>
                <p class="card-subtitle">100 total assets: 62% Reuse, 31% Adapt, 7% New.</p>
              </div>
              <span class="badge badge-kone">Supply Chain</span>
            </div>

            <!-- Content Supply Chain Visual Breakdown -->
            <div style="margin-bottom: 16px;">
              <div style="display: flex; height: 28px; border-radius: 8px; overflow: hidden; margin-bottom: 8px;">
                <div style="width: 62%; background: var(--kone-blue); display: flex; align-items: center; justify-content: center; color: white; font-size: 0.72rem; font-weight: 700;" title="Direct Reuse: 62 assets">
                  Reuse 62%
                </div>
                <div style="width: 31%; background: var(--kone-cyan); display: flex; align-items: center; justify-content: center; color: white; font-size: 0.72rem; font-weight: 700;" title="Local Adaptation: 31 assets">
                  Adapt 31%
                </div>
                <div style="width: 7%; background: var(--accent-amber); display: flex; align-items: center; justify-content: center; color: black; font-size: 0.72rem; font-weight: 700;" title="New Creation: 7 assets">
                  New 7%
                </div>
              </div>
              <div style="display: flex; justify-content: space-between; font-size: 0.72rem; color: var(--text-secondary);">
                <span>■ 62 Direct Reuse (Technical blueprints, 3D shaft anims)</span>
                <span>■ 31 Localized (Spanish copy, elevator codes)</span>
                <span>■ 7 Net New (Local case studies)</span>
              </div>
            </div>

            <!-- Asset Categories Table -->
            <div class="table-container">
              <table class="kone-table">
                <thead>
                  <tr>
                    <th>Asset Category</th>
                    <th>Count</th>
                    <th>Reuse</th>
                    <th>Adapt</th>
                    <th>New</th>
                    <th>Provenance Source</th>
                  </tr>
                </thead>
                <tbody id="contentAssetsTableBody">
                  <!-- Populated by JS -->
                </tbody>
              </table>
            </div>
          </div>

          <!-- Launch Readiness Gates (Table A10) -->
          <div class="glass-card col-6">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">WEIGHTED LAUNCH READINESS CHECKPOINT (TABLE A10)</div>
                <h3 class="card-title">Launch Gate Scorecard</h3>
                <p class="card-subtitle">96 / 100 Pre-launch score. Safety, claims, and field gates.</p>
              </div>
              <div style="text-align: right;">
                <div id="readinessTotalScore" style="font-size: 1.4rem; font-weight: 800; color: var(--kone-cyan);">96 / 100</div>
                <div style="font-size: 0.65rem; color: var(--text-secondary);">Launch Readiness</div>
              </div>
            </div>

            <div class="table-container">
              <table class="kone-table">
                <thead>
                  <tr>
                    <th>Checkpoint</th>
                    <th>Weight</th>
                    <th>Completion</th>
                    <th>Points</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody id="launchReadinessTableBody">
                  <!-- Populated by JS -->
                </tbody>
              </table>
            </div>

            <div style="margin-top: 12px; padding: 10px; background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 8px; font-size: 0.72rem; color: #FCD34D;">
              <strong>Mandatory Gate Policy:</strong> A 96/100 score is not permission to launch. Field Enablement (currently 80%) must reach 100% completion before elevator activation begins.
            </div>
          </div>

          <!-- 38-Building Cohort Explorer (Table A11) -->
          <div class="glass-card col-12">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">
                  <span>●</span>
                  <span>COMPLETE 38-BUILDING PILOT COHORT (TABLE A11)</span>
                  <span class="badge badge-synthetic">[SYNTHETIC]</span>
                </div>
                <h3 class="card-title">Iberia Pilot Buildings Explorer</h3>
                <p class="card-subtitle">Click any building to inspect telemetry, shaft dimensions, and conversion status.</p>
              </div>

              <!-- Cohort Filters -->
              <div class="flex-gap-8" style="flex-wrap: wrap;">
                <input type="text" id="buildingSearchInput" placeholder="Search building or street..." oninput="filterCohortTable()" style="padding: 6px 12px; background: rgba(255, 255, 255, 0.06); border: 1px solid var(--border-glass); border-radius: 6px; color: white; font-size: 0.76rem; width: 180px;">
                <select id="cityFilterSelect" onchange="filterCohortTable()" style="padding: 6px 10px; background: rgba(255, 255, 255, 0.06); border: 1px solid var(--border-glass); border-radius: 6px; color: white; font-size: 0.76rem;">
                  <option value="ALL">All Cities (7)</option>
                  <option value="Barcelona">Barcelona</option>
                  <option value="Madrid">Madrid</option>
                  <option value="Seville">Seville</option>
                  <option value="Valencia">Valencia</option>
                  <option value="Bilbao">Bilbao</option>
                  <option value="Zaragoza">Zaragoza</option>
                  <option value="Malaga">Malaga</option>
                </select>
                <select id="shaftFilterSelect" onchange="filterCohortTable()" style="padding: 6px 10px; background: rgba(255, 255, 255, 0.06); border: 1px solid var(--border-glass); border-radius: 6px; color: white; font-size: 0.76rem;">
                  <option value="ALL">All Shaft Types</option>
                  <option value="Standard">Standard Shaft (32)</option>
                  <option value="Non-standard">Non-standard (6)</option>
                </select>
                <select id="statusFilterSelect" onchange="filterCohortTable()" style="padding: 6px 10px; background: rgba(255, 255, 255, 0.06); border: 1px solid var(--border-glass); border-radius: 6px; color: white; font-size: 0.76rem;">
                  <option value="ALL">All Outcomes</option>
                  <option value="Converted">Converted (14)</option>
                  <option value="Quote Presented">Quote Presented (24)</option>
                </select>
              </div>
            </div>

            <!-- Cohort Summary Stats Bar -->
            <div style="display: flex; gap: 16px; margin-bottom: 14px; padding: 10px 14px; background: rgba(255, 255, 255, 0.02); border-radius: 8px; font-size: 0.75rem;">
              <span>Total Buildings: <strong style="color: #FFF;" id="filteredBuildingsCount">38</strong></span>
              <span style="opacity: 0.3;">|</span>
              <span>Quotes Presented: <strong style="color: var(--kone-cyan);" id="filteredQuotesCount">45</strong></span>
              <span style="opacity: 0.3;">|</span>
              <span>Orders Booked: <strong style="color: var(--accent-emerald);" id="filteredOrdersCount">14</strong></span>
              <span style="opacity: 0.3;">|</span>
              <span>Quote Conversion: <strong style="color: var(--accent-emerald);" id="filteredConversionRate">31.1%</strong></span>
              <span style="opacity: 0.3;">|</span>
              <span>Age Verified: <strong style="color: var(--accent-amber);" id="filteredAgeVerified">31 / 38 (81.6%)</strong></span>
            </div>

            <!-- Table of 38 Buildings -->
            <div class="table-container" style="max-height: 420px; overflow-y: auto;">
              <table class="kone-table">
                <thead>
                  <tr>
                    <th>Building ID</th>
                    <th>City & Address</th>
                    <th>Install Year</th>
                    <th>Age</th>
                    <th>Shaft Type</th>
                    <th>Quoted Units</th>
                    <th>Ordered Units</th>
                    <th>Age Verified</th>
                    <th>Status</th>
                    <th>Site Days</th>
                  </tr>
                </thead>
                <tbody id="cohortTableBody">
                  <!-- Populated by JS -->
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- VIEW 6: LEARN — Day-90 Outcomes & Feedback -->
      <!-- ========================================== -->
      <section class="tab-view" id="view-learn">
        <!-- Review Date Header -->
        <div class="glass-card highlight-card" style="margin-bottom: 24px;">
          <div class="flex-between">
            <div>
              <div class="card-eyebrow">
                <span>●</span>
                <span>DAY-90 POST-LAUNCH REVIEW (TABLE A12)</span>
                <span class="badge badge-synthetic">[SYNTHETIC]</span>
              </div>
              <h2 class="card-title">Closing the Loop: Results Become the Next Decision</h2>
              <p class="card-subtitle">Sunday 13 June 2027. Reviewing Iberia pilot outcomes against DACH assumptions and baseline.</p>
            </div>
            <div style="text-align: right;">
              <span class="badge badge-emerald" style="font-size: 0.8rem; padding: 6px 14px;">LR-IB-01 Generated</span>
            </div>
          </div>
        </div>

        <div class="bento-grid">
          <!-- Day-90 KPI Cards -->
          <div class="scorecard col-3">
            <div class="scorecard-label">Quote Conversion Rate</div>
            <div class="scorecard-val" style="color: var(--accent-emerald);">31.1%</div>
            <div class="scorecard-delta delta-positive">↑ +7.1 pts vs 24% baseline</div>
          </div>

          <div class="scorecard col-3">
            <div class="scorecard-label">Booked Pilot Value</div>
            <div class="scorecard-val">€341.6k</div>
            <div class="scorecard-delta delta-positive">14 units × €24,400</div>
          </div>

          <div class="scorecard col-3">
            <div class="scorecard-label">Average Days on Site</div>
            <div class="scorecard-val" style="color: var(--kone-cyan);">6.4 days</div>
            <div class="scorecard-delta delta-positive">↓ vs 21 days conventional</div>
          </div>

          <div class="scorecard col-3">
            <div class="scorecard-label">Field Referrals Exceeded</div>
            <div class="scorecard-val" style="color: var(--accent-purple);">112</div>
            <div class="scorecard-delta delta-positive">↑ vs 90 target (+24.4%)</div>
          </div>

          <!-- Day-90 Outcomes Full Table -->
          <div class="glass-card col-8">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">PILOT OUTCOME VERIFICATION</div>
                <h3 class="card-title">Measured Metrics vs Conventional Baseline</h3>
              </div>
            </div>

            <div class="table-container">
              <table class="kone-table">
                <thead>
                  <tr>
                    <th>Measure</th>
                    <th>Synthetic Outcome</th>
                    <th>Baseline / Benchmark</th>
                    <th>Operational Interpretation</th>
                  </tr>
                </thead>
                <tbody id="day90TableBody">
                  <!-- Populated by JS -->
                </tbody>
              </table>
            </div>
          </div>

          <!-- The Two Realities & Learning Record LR-IB-01 -->
          <div class="glass-card col-4">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">HONEST LEARNING RECORD</div>
                <h3 class="card-title" style="font-size: 0.98rem;">Record LR-IB-01</h3>
              </div>
              <span class="badge badge-amber">Gap Documented</span>
            </div>

            <div style="font-size: 0.78rem; line-height: 1.6; display: flex; flex-direction: column; gap: 12px;">
              <div style="padding: 12px; background: rgba(16, 185, 129, 0.08); border-radius: 8px; border: 1px solid rgba(16, 185, 129, 0.25);">
                <div style="font-weight: 700; color: var(--accent-emerald);">What Proved Out:</div>
                <ul style="margin-left: 16px; margin-top: 4px; color: #E2E8F0;">
                  <li><strong>14 / 14 orders</strong> occurred in standard shafts!</li>
                  <li>Installation averaged <strong>6.4 days</strong> (vs 21 days).</li>
                  <li>Referral routine delivered <strong>112 leads</strong>.</li>
                </ul>
              </div>

              <div style="padding: 12px; background: rgba(245, 158, 11, 0.08); border-radius: 8px; border: 1px solid rgba(245, 158, 11, 0.25);">
                <div style="font-weight: 700; color: var(--accent-amber);">Where We Fell Short (The Gap):</div>
                <ul style="margin-left: 16px; margin-top: 4px; color: #E2E8F0;">
                  <li>Installation-age verification reached only <strong>31 / 38 (81.6%)</strong>.</li>
                  <li>7 records were provisional estimates.</li>
                  <li>Non-standard shafts had <strong>0% conversion</strong> (0 / 6 quotes).</li>
                </ul>
              </div>

              <div style="padding: 12px; background: rgba(0, 88, 163, 0.15); border-radius: 8px; border: 1px solid rgba(0, 163, 224, 0.3);">
                <strong style="color: #FFF;">Closing Decision for Next Market:</strong>
                <p style="color: var(--text-secondary); margin-top: 4px; font-size: 0.72rem;">
                  Benelux is recommended for <em>discovery testing only</em>, not immediate mass scaling. Pre-condition: mandatory technical shaft clearance checks before quotes are issued.
                </p>
              </div>

              <button class="btn-action btn-primary" style="justify-content: center;" onclick="switchTab('ingredients')">
                Explore Reusable Ingredients →
              </button>
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- VIEW 7: INGREDIENTS — Reusable Capability Library -->
      <!-- ========================================== -->
      <section class="tab-view" id="view-ingredients">
        <div class="glass-card highlight-card" style="margin-bottom: 24px;">
          <div class="flex-between">
            <div>
              <div class="card-eyebrow">
                <span>●</span>
                <span>HOW LEARNING BECOMES REUSABLE CAPABILITY (TABLE A13)</span>
                <span class="badge badge-kone">Content Supply Chain</span>
              </div>
              <h2 class="card-title">The Five Reusable Ingredients (IG-01 to IG-05)</h2>
              <p class="card-subtitle">Transferring validated tools, governance templates, and legal claims to subsequent markets without reinvention.</p>
            </div>
            <button class="btn-action btn-primary" onclick="packageBeneluxBrief()">
              <span>⚡</span>
              <span>Package into Benelux Discovery Brief</span>
            </button>
          </div>
        </div>

        <div class="bento-grid" id="ingredientsGrid">
          <!-- Populated by JS -->
        </div>

        <!-- Assembly Preview Card -->
        <div class="glass-card" id="beneluxPackagePreview" style="margin-top: 10px; display: none; border-color: var(--kone-cyan);">
          <div class="card-header">
            <div>
              <div class="card-eyebrow text-cyan">NEXT MARKET APPLICATION</div>
              <h3 class="card-title">Benelux Discovery Brief (Generated from Reusable Ingredients)</h3>
            </div>
            <span class="badge badge-emerald">Ready for Discovery</span>
          </div>
          <div style="font-size: 0.8rem; color: #CBD5E1; line-height: 1.6;">
            <p><strong>Inherited Playbook Ingredients:</strong> IG-01 (Account Eligibility Checklist) + IG-02 (Technician Referral Guide) + IG-03 (Approved One-Week Claim with Disruption Caveat) + LR-IB-01 (81.6% Age Verification Correction).</p>
            <p style="margin-top: 8px;"><strong>Benelux Scope:</strong> 50-building targeted discovery cohort in Brussels & Amsterdam. Hard technical prerequisite: 100% pre-quote shaft geometry verification.</p>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- VIEW 8: SIMULATION SANDBOX — Interactive What-If Engine -->
      <!-- ========================================== -->
      <section class="tab-view" id="view-simulation">
        <div class="glass-card highlight-card" style="margin-bottom: 24px;">
          <div class="flex-between">
            <div>
              <div class="card-eyebrow">
                <span>●</span>
                <span>STRATEGIC WHAT-IF SIMULATION ENGINE</span>
                <span class="badge badge-synthetic">[SYNTHETIC SIMULATOR]</span>
              </div>
              <h2 class="card-title">Simulate Cross-Market Replication & Scaling</h2>
              <p class="card-subtitle">Adjust parameters live in the leadership workshop to test operational outcomes, conversions, and commercial value.</p>
            </div>

            <!-- Presets -->
            <div class="flex-gap-8">
              <span style="font-size: 0.72rem; color: var(--text-secondary);">Load Preset:</span>
              <button class="btn-action" onclick="loadSimPreset('iberia_actual')">Iberia Pilot</button>
              <button class="btn-action" onclick="loadSimPreset('benelux_scale')">Benelux Scale</button>
              <button class="btn-action" onclick="loadSimPreset('dach_benchmark')">DACH Benchmark</button>
              <button class="btn-action" onclick="loadSimPreset('high_disruption')">High Disruption</button>
            </div>
          </div>
        </div>

        <div class="bento-grid">
          <!-- Simulation Parameter Controls -->
          <div class="glass-card col-5">
            <div class="card-header">
              <div>
                <div class="card-eyebrow">SIMULATION CONTROLS</div>
                <h3 class="card-title" style="font-size: 1.05rem;">Operational Levers</h3>
              </div>
              <button class="btn-action" style="font-size: 0.7rem; padding: 4px 8px;" onclick="resetSimParams()">Reset Defaults</button>
            </div>

            <div class="sim-slider-group">
              <div class="sim-slider-header">
                <span class="sim-slider-label">Target Market</span>
                <select id="simMarketSelect" onchange="runSimulation()" style="padding: 4px 8px; background: rgba(255, 255, 255, 0.08); border: 1px solid var(--border-glass); border-radius: 6px; color: white; font-size: 0.75rem;">
                  <option value="Iberia">Iberia (96,000 base)</option>
                  <option value="Benelux">Benelux (61,000 base)</option>
                  <option value="Poland">Poland (58,000 base)</option>
                  <option value="UK and Ireland">UK & Ireland (142,000 base)</option>
                  <option value="DACH">DACH (268,000 base)</option>
                </select>
              </div>
            </div>

            <div class="sim-slider-group">
              <div class="sim-slider-header">
                <span class="sim-slider-label">Pilot Cohort Size (Buildings)</span>
                <span class="sim-slider-val" id="valSimCohort">38 buildings</span>
              </div>
              <input type="range" class="sim-slider" id="sliderSimCohort" min="10" max="150" step="1" value="38" oninput="runSimulation()">
            </div>

            <div class="sim-slider-group">
              <div class="sim-slider-header">
                <span class="sim-slider-label">Standard Shaft Qualification Ratio</span>
                <span class="sim-slider-val" id="valSimShaftRatio">84%</span>
              </div>
              <input type="range" class="sim-slider" id="sliderSimShaftRatio" min="30" max="100" step="1" value="84" oninput="runSimulation()">
              <div style="font-size: 0.65rem; color: var(--text-muted); margin-top: 3px;">Standard shafts convert at 2.4x vs non-standard.</div>
            </div>

            <div class="sim-slider-group">
              <div class="sim-slider-header">
                <span class="sim-slider-label">Service Technician Referral Volume</span>
                <span class="sim-slider-val" id="valSimReferrals">112 referrals</span>
              </div>
              <input type="range" class="sim-slider" id="sliderSimReferrals" min="20" max="300" step="5" value="112" oninput="runSimulation()">
            </div>

            <div class="sim-slider-group">
              <div class="sim-slider-header">
                <span class="sim-slider-label">Installation-Age Data Verification Rate</span>
                <span class="sim-slider-val" id="valSimAgeVerified">82%</span>
              </div>
              <input type="range" class="sim-slider" id="sliderSimAgeVerified" min="40" max="100" step="1" value="82" oninput="runSimulation()">
              <div style="font-size: 0.65rem; color: var(--text-muted); margin-top: 3px;">Unverified age records experience 50% lower quote acceptance.</div>
            </div>

            <div class="sim-slider-group">
              <div class="sim-slider-header">
                <span class="sim-slider-label">Average Modernization Order Price</span>
                <span class="sim-slider-val" id="valSimAvgOrder">€24,400</span>
              </div>
              <input type="range" class="sim-slider" id="sliderSimAvgOrder" min="16000" max="32000" step="400" value="24400" oninput="runSimulation()">
            </div>

            <div class="sim-slider-group">
              <div class="sim-slider-header">
                <span class="sim-slider-label">Content Reuse Ratio</span>
                <span class="sim-slider-val" id="valSimContentReuse">62%</span>
              </div>
              <input type="range" class="sim-slider" id="sliderSimContentReuse" min="20" max="95" step="1" value="62" oninput="runSimulation()">
              <div style="font-size: 0.65rem; color: var(--text-muted); margin-top: 3px;">Higher reuse cuts preparation time from 60 to 21 days.</div>
            </div>
          </div>

          <!-- Dynamic Simulation Projection Results -->
          <div class="glass-card col-7">
            <div class="card-header">
              <div>
                <div class="card-eyebrow text-cyan">LIVE PROJECTION MATRIX</div>
                <h3 class="card-title">Simulated Commercial & Operational Impact</h3>
              </div>
              <span class="badge badge-emerald" id="simFeasibilityBadge">High Feasibility</span>
            </div>

            <!-- Dynamic Projected Scorecards -->
            <div class="scorecard-grid" style="grid-template-columns: repeat(3, 1fr); margin-bottom: 20px;">
              <div class="scorecard">
                <div class="scorecard-label">Simulated Quotes</div>
                <div class="scorecard-val" id="simResultQuotes" style="color: var(--kone-cyan);">45</div>
                <div class="scorecard-delta delta-neutral" id="simResultQuoteDelta">Across 38 buildings</div>
              </div>

              <div class="scorecard">
                <div class="scorecard-label">Simulated Orders</div>
                <div class="scorecard-val" id="simResultOrders" style="color: var(--accent-emerald);">14</div>
                <div class="scorecard-delta delta-positive" id="simResultConvRate">31.1% conversion</div>
              </div>

              <div class="scorecard">
                <div class="scorecard-label">Projected Booked Value</div>
                <div class="scorecard-val" id="simResultRevenue">€341.6k</div>
                <div class="scorecard-delta delta-positive">Pilot pipeline booked</div>
              </div>

              <div class="scorecard">
                <div class="scorecard-label">Customer Disruption Days Saved</div>
                <div class="scorecard-val" id="simResultDaysSaved" style="color: var(--accent-purple);">146 days</div>
                <div class="scorecard-delta delta-positive">6.4 vs 21 days on site</div>
              </div>

              <div class="scorecard">
                <div class="scorecard-label">Content Supply Chain Days</div>
                <div class="scorecard-val" id="simResultContentDays" style="color: #38BDF8;">21 days</div>
                <div class="scorecard-delta delta-positive">↓ from 60 agency days</div>
              </div>

              <div class="scorecard">
                <div class="scorecard-label">Strategic Risk Index</div>
                <div class="scorecard-val" id="simResultRisk" style="color: var(--accent-emerald);">Low (14%)</div>
                <div class="scorecard-delta delta-neutral">Data gap mitigated</div>
              </div>
            </div>

            <!-- Visual Bar Comparison -->
            <div style="background: rgba(0, 0, 0, 0.25); border-radius: 12px; padding: 18px; border: 1px solid var(--border-glass);">
              <div style="font-size: 0.8rem; font-weight: 700; color: #FFF; margin-bottom: 12px;">Simulation Sensitivity Breakdown</div>
              
              <div style="margin-bottom: 12px;">
                <div class="flex-between" style="font-size: 0.72rem; margin-bottom: 4px;">
                  <span style="color: var(--text-secondary);">Conversion vs Conventional Baseline (24.0%):</span>
                  <span style="font-weight: 700; color: var(--accent-emerald);" id="simSensitivityConv">+7.1 pts</span>
                </div>
                <div class="progress-bar-bg">
                  <div class="progress-bar-fill" id="simProgressConv" style="width: 62%;"></div>
                </div>
              </div>

              <div style="margin-bottom: 12px;">
                <div class="flex-between" style="font-size: 0.72rem; margin-bottom: 4px;">
                  <span style="color: var(--text-secondary);">Shaft Standardisation Efficiency Ratio:</span>
                  <span style="font-weight: 700; color: var(--kone-cyan);" id="simSensitivityShaft">84% qualified</span>
                </div>
                <div class="progress-bar-bg">
                  <div class="progress-bar-fill" id="simProgressShaft" style="width: 84%; background: linear-gradient(90deg, var(--kone-cyan), #38BDF8);"></div>
                </div>
              </div>

              <div>
                <div class="flex-between" style="font-size: 0.72rem; margin-bottom: 4px;">
                  <span style="color: var(--text-secondary);">Data Verification Integrity:</span>
                  <span style="font-weight: 700; color: var(--accent-amber);" id="simSensitivityData">82% complete</span>
                </div>
                <div class="progress-bar-bg">
                  <div class="progress-bar-fill" id="simProgressData" style="width: 82%; background: linear-gradient(90deg, var(--accent-amber), #FCD34D);"></div>
                </div>
              </div>
            </div>

            <div style="margin-top: 16px; font-size: 0.74rem; color: var(--text-secondary); line-height: 1.5;">
              <strong style="color: #FFF;">Workshop Discussion Prompt:</strong> Notice that increasing cohort size without improving standard shaft qualification yields diminishing returns. Scaling requires shaft geometry pre-checks.
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- VIEW 9: WORKSHOP & SCRIPT STORY — The Two-Act Film -->
      <!-- ========================================== -->
      <section class="tab-view" id="view-workshop">
        <div class="glass-card highlight-card" style="margin-bottom: 24px;">
          <div class="flex-between">
            <div>
              <div class="card-eyebrow">
                <span>🎬</span>
                <span>EXECUTIVE WORKSHOP FILM & SCRIPT READER</span>
                <span class="badge badge-kone">Live Companion</span>
              </div>
              <h2 class="card-title">KONE Marketing OS: Full Script & Facilitator Walkthrough</h2>
              <p class="card-subtitle">Designed for Petra (CMO) and 15 senior marketing leaders. Follow Anna & Marc through 2 Acts and 9 Scenes.</p>
            </div>
            <div class="flex-gap-8">
              <span class="badge badge-kone" style="font-size: 0.72rem; padding: 5px 12px;">
                <span>Facilitator Script Companion</span>
              </span>
            </div>
          </div>
        </div>

        <!-- Scene Navigator Pills -->
        <div class="scene-navigator" id="sceneNavContainer">
          <!-- Populated by JS -->
        </div>

        <div class="bento-grid">
          <!-- Current Scene Transcript Card -->
          <div class="glass-card col-8">
            <div class="card-header">
              <div>
                <div class="card-eyebrow text-cyan" id="sceneActLabel">ACT 1: THE MONDAY MORNING VIEW</div>
                <h3 class="card-title" id="sceneTitle">Scene 1 | Opening Title & Premise</h3>
                <p class="card-subtitle" id="sceneTimecode">Timecode: 0:00 to 0:45</p>
              </div>
              <button class="btn-action" id="sceneJumpBtn" onclick="jumpToSceneScreen()">Jump to App Screen →</button>
            </div>

            <!-- Dialogue Box with Speaker Badge -->
            <div style="background: rgba(0, 0, 0, 0.35); border-radius: 12px; padding: 22px; border: 1px solid var(--border-glass); margin-bottom: 20px;">
              <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                <span class="badge badge-kone" id="sceneSpeaker">Voice-over</span>
                <span style="font-size: 0.72rem; color: var(--text-muted);" id="sceneTargetScreen">Target: Growth Control Tower</span>
              </div>
              <div style="font-size: 0.95rem; line-height: 1.7; color: #FFFFFF;" id="sceneDialogue">
                <!-- Dialogue text -->
              </div>
            </div>

            <div style="display: flex; gap: 16px; font-size: 0.78rem;">
              <div style="flex: 1; padding: 12px; background: rgba(255, 255, 255, 0.025); border-radius: 8px; border: 1px solid var(--border-glass);">
                <strong style="color: var(--kone-cyan);">On-Screen Headline:</strong>
                <p style="color: var(--text-secondary); margin-top: 4px;" id="sceneHeadline"></p>
              </div>
              <div style="flex: 1; padding: 12px; background: rgba(255, 255, 255, 0.025); border-radius: 8px; border: 1px solid var(--border-glass);">
                <strong style="color: var(--accent-emerald);">Workshop Objective:</strong>
                <p style="color: var(--text-secondary); margin-top: 4px;" id="sceneTakeaway"></p>
              </div>
            </div>
          </div>

          <!-- Three Critical Questions for the Room -->
          <div class="glass-card col-4">
            <div class="card-header">
              <div>
                <div class="card-eyebrow text-amber">WORKSHOP DISCUSSION</div>
                <h3 class="card-title" style="font-size: 0.98rem;">Three Questions for the Room</h3>
              </div>
              <span class="badge badge-kone">Interactive Poll</span>
            </div>

            <div style="display: flex; flex-direction: column; gap: 14px;" id="workshopQuestionsContainer">
              <!-- Rendered via JS -->
            </div>
          </div>
        </div>
      </section>

    </main>
  </div>

  <!-- Modal Building Detail Inspector -->
  <div class="modal-overlay" id="buildingModal" onclick="closeModal(event)">
    <div class="modal-card" onclick="event.stopPropagation()">
      <button class="modal-close" onclick="closeBuildingModal()">✕</button>
      <div id="buildingModalContent">
        <!-- Rendered via JS -->
      </div>
    </div>
  </div>

  <!-- Embedded Synthetic Data & App Engine -->
  <script>
    // Global Application Data injected from JSON
    const APP_DATA = {json_str};

    // Application State
    let currentTab = 'sense';
    let currentPersonaIdx = 0;
    let currentSceneIdx = 0;
    let isFieldGateOpen = false;
    let activeBuilding = null;

    // Simulation Live Parameters
    let simState = {{
      market: 'Iberia',
      cohortSize: 38,
      shaftRatio: 84,
      referrals: 112,
      ageVerifiedPct: 82,
      avgOrder: 24400,
      contentReuse: 62
    }};

    // Initialize application
    window.addEventListener('DOMContentLoaded', () => {{
      renderOpportunities();
      renderMarketTable();
      renderDachDrivers();
      renderPrioritiseTable();
      renderPlaybookTable();
      renderContentEfficiency();
      renderLaunchReadiness();
      renderCohortTable();
      renderDay90Outcomes();
      renderIngredients();
      renderSceneNavigator();
      renderWorkshopQuestions();
      runSimulation();
    }});

    // Tab Navigation
    function switchTab(tabId) {{
      currentTab = tabId;
      document.querySelectorAll('.tab-view').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-tab').forEach(el => el.classList.remove('active'));
      
      const targetView = document.getElementById(`view-${{tabId}}`);
      const targetBtn = document.getElementById(`tab-btn-${{tabId}}`);
      
      if (targetView) targetView.classList.add('active');
      if (targetBtn) targetBtn.classList.add('active');
      
      window.scrollTo({{ top: 0, behavior: 'smooth' }});

      if (tabId === 'diagnose') {{
        renderDiagnoseWaterfall();
      }} else if (tabId === 'prioritise') {{
        renderRadarVisual();
      }}
    }}

    // Persona Cycling
    function cyclePersona() {{
      currentPersonaIdx = (currentPersonaIdx + 1) % APP_DATA.personas.length;
      const persona = APP_DATA.personas[currentPersonaIdx];
      
      document.getElementById('currentPersonaAvatar').textContent = persona.avatar;
      document.getElementById('currentPersonaName').textContent = persona.name;
      document.getElementById('currentPersonaRole').textContent = `${{persona.title}} (${{persona.location}})`;
      
      const bannerTag = document.getElementById('bannerTag');
      const bannerText = document.getElementById('bannerText');
      const bannerQuote = document.getElementById('bannerQuote');
      
      bannerTag.textContent = persona.name.toUpperCase();
      bannerText.textContent = `${{persona.role}}: ${{persona.focus}}`;
      bannerQuote.textContent = `Location: ${{persona.location}}`;
    }}

    // Render Opportunity Register (Table A2)
    function renderOpportunities() {{
      const tbody = document.getElementById('opportunityTableBody');
      tbody.innerHTML = '';
      
      APP_DATA.opportunities.forEach(op => {{
        const tr = document.createElement('tr');
        tr.className = 'clickable';
        tr.onclick = () => {{
          if (op.actionType === 'diagnose') switchTab('diagnose');
          else if (op.actionType === 'replicate') switchTab('replicate');
        }};
        
        tr.innerHTML = `
          <td class="font-mono" style="color: var(--kone-cyan);">${{op.id}}</td>
          <td>
            <div style="font-weight: 600; color: #FFF;">${{op.market}} — ${{op.play}}</div>
            <div style="font-size: 0.7rem; color: var(--text-secondary);">${{op.description}}</div>
          </td>
          <td><span style="font-weight: 500;">${{op.signal}}</span></td>
          <td class="font-mono" style="font-weight: 700; color: #FFF;">EUR ${{op.potential}}m</td>
          <td>
            <div style="display: flex; align-items: center; gap: 6px;">
              <span class="font-mono">${{op.confidence}}%</span>
              <div style="width: 50px; height: 4px; background: rgba(255,255,255,0.1); border-radius: 99px;">
                <div style="width: ${{op.confidence}}%; height: 100%; background: var(--kone-cyan); border-radius: 99px;"></div>
              </div>
            </div>
          </td>
          <td>
            <span class="badge ${{op.actionType === 'replicate' ? 'badge-emerald' : 'badge-kone'}}">
              ${{op.action}} →
            </span>
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Render Market Comparison (Table A1)
    function renderMarketTable() {{
      const tbody = document.getElementById('marketTableBody');
      tbody.innerHTML = '';
      
      APP_DATA.markets.forEach(m => {{
        const tr = document.createElement('tr');
        const dachRel = ((m.activation / 62) * 100).toFixed(0);
        
        tr.innerHTML = `
          <td>
            <div style="font-weight: 700; color: #FFF;">${{m.name}}</div>
            <div style="font-size: 0.68rem; color: var(--text-muted);">${{m.flag}}</div>
          </td>
          <td class="font-mono">${{m.baseUnits.toLocaleString()}}</td>
          <td>
            <div class="flex-between font-mono" style="font-size: 0.72rem;">
              <span>${{m.age15Plus}}%</span>
            </div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" style="width: ${{m.age15Plus}}%;"></div></div>
          </td>
          <td>
            <div class="flex-between font-mono" style="font-size: 0.72rem;">
              <span>${{m.connected}}%</span>
            </div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" style="width: ${{m.connected}}%; background: var(--kone-cyan);"></div></div>
          </td>
          <td>
            <div class="flex-between font-mono" style="font-size: 0.72rem;">
              <span style="font-weight: 700; color: ${{m.id === 'iberia' ? 'var(--accent-amber)' : 'inherit'}};">${{m.activation}}%</span>
            </div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" style="width: ${{m.activation}}%; background: ${{m.id === 'iberia' ? 'var(--accent-amber)' : 'var(--kone-blue)'}};"></div></div>
          </td>
          <td class="font-mono">${{m.conversion}}%</td>
          <td>
            <span class="badge ${{m.id === 'iberia' ? 'badge-amber' : 'badge-kone'}}" style="font-size: 0.68rem;">
              ${{dachRel}}% of DACH
            </span>
          </td>
          <td>
            <span class="badge ${{m.id === 'dach' ? 'badge-kone' : (m.id === 'iberia' ? 'badge-emerald' : 'badge-synthetic')}}">
              ${{m.status}}
            </span>
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Render DACH Drivers (Table A4)
    function renderDachDrivers() {{
      const tbody = document.getElementById('dachDriversTableBody');
      tbody.innerHTML = '';
      
      APP_DATA.dachDrivers.forEach(d => {{
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>
            <div style="font-weight: 700; color: #FFF;">${{d.driver}}</div>
            <div style="font-size: 0.68rem; color: var(--kone-cyan);">${{d.type}}</div>
          </td>
          <td class="font-mono" style="font-weight: 700; color: var(--accent-emerald);">+${{d.points}} pts</td>
          <td class="font-mono">${{d.share}}%</td>
          <td style="font-size: 0.76rem; color: var(--text-secondary);">${{d.observation}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Custom SVG Waterfall Chart for Diagnose
    function renderDiagnoseWaterfall() {{
      const container = document.getElementById('diagnoseWaterfallContainer');
      if (!container) return;

      const drivers = APP_DATA.dachDrivers;
      let running = 0;
      const points = [];
      
      drivers.forEach(d => {{
        const start = running;
        running += d.points;
        points.push({{ name: d.driver.split(' ')[0] + ' ' + (d.driver.split(' ')[1] || ''), pts: d.points, start, end: running }});
      }});

      let svgHtml = `
        <svg viewBox="0 0 650 200" style="width: 100%; height: auto; font-family: Inter, sans-serif;">
          <defs>
            <linearGradient id="barGrad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#10B981"/>
              <stop offset="100%" stop-color="#059669"/>
            </linearGradient>
            <linearGradient id="totalGrad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#00A3E0"/>
              <stop offset="100%" stop-color="#0058A3"/>
            </linearGradient>
          </defs>
          <line x1="40" y1="160" x2="620" y2="160" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
      `;

      const barWidth = 65;
      const spacing = 95;
      const startX = 60;
      const scale = 4.6; // px per pt

      points.forEach((p, idx) => {{
        const x = startX + idx * spacing;
        const h = p.pts * scale;
        const y = 160 - (p.end * scale);
        
        svgHtml += `
          <rect x="${{x}}" y="${{y}}" width="${{barWidth}}" height="${{h}}" rx="4" fill="url(#barGrad)"/>
          <text x="${{x + barWidth/2}}" y="${{y - 6}}" text-anchor="middle" fill="#34D399" font-size="11" font-weight="700">+${{p.pts}}</text>
          <text x="${{x + barWidth/2}}" y="178" text-anchor="middle" fill="#94A3B8" font-size="10">${{p.name}}</text>
        `;
      }});

      // Total bar
      const totalX = startX + points.length * spacing;
      const totalH = 27.3 * scale;
      const totalY = 160 - totalH;
      svgHtml += `
        <rect x="${{totalX}}" y="${{totalY}}" width="${{barWidth}}" height="${{totalH}}" rx="4" fill="url(#totalGrad)"/>
        <text x="${{totalX + barWidth/2}}" y="${{totalY - 6}}" text-anchor="middle" fill="#38BDF8" font-size="12" font-weight="800">+27.3</text>
        <text x="${{totalX + barWidth/2}}" y="178" text-anchor="middle" fill="#FFF" font-size="10" font-weight="700">Total YoY</text>
      </svg>`;

      container.innerHTML = svgHtml;
    }}

    // Render Prioritise Matrix (Table A7)
    function renderPrioritiseTable() {{
      const tbody = document.getElementById('prioritiseTableBody');
      tbody.innerHTML = '';
      
      APP_DATA.prioritisation.forEach(p => {{
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>
            <div style="font-weight: 700; color: #FFF;">${{p.market}}</div>
            <div style="font-size: 0.68rem; color: var(--kone-cyan);">Match: ${{p.weightedMatch}} / 100</div>
          </td>
          <td class="font-mono">${{p.valueScore}}</td>
          <td class="font-mono">${{p.strategicScore}}</td>
          <td class="font-mono">${{p.easeScore}}</td>
          <td class="font-mono">${{p.speedScore}}</td>
          <td class="font-mono">${{p.confidenceScore}}</td>
          <td>
            <span class="font-mono" style="font-size: 1rem; font-weight: 800; color: ${{p.badgeColor === 'emerald' ? 'var(--accent-emerald)' : '#FFF'}};">
              ${{p.priority}}
            </span>
          </td>
          <td class="font-mono" style="font-weight: 700;">EUR ${{p.potential}}m</td>
          <td>
            <span class="badge badge-${{p.badgeColor}}">${{p.recommendation}}</span>
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // SVG Radar Representation in Prioritise
    function renderRadarVisual() {{
      const container = document.getElementById('prioritiseRadarContainer');
      if (!container) return;

      container.innerHTML = `
        <svg viewBox="0 0 260 220" style="width: 100%; max-width: 260px; height: auto;">
          <polygon points="130,20 220,90 190,190 70,190 40,90" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
          <polygon points="130,50 195,100 170,170 90,170 65,100" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
          <!-- Iberia Polygon (84 match) -->
          <polygon points="130,28 205,95 180,180 80,175 48,92" fill="rgba(0, 163, 224, 0.25)" stroke="#00A3E0" stroke-width="2"/>
          <!-- Benelux Polygon (61 match) -->
          <polygon points="130,70 175,110 145,155 105,150 78,115" fill="rgba(139, 92, 246, 0.2)" stroke="#8B5CF6" stroke-width="1.5" stroke-dasharray="3,3"/>
          <text x="130" y="14" text-anchor="middle" fill="#CBD5E1" font-size="9">Customer Fit</text>
          <text x="228" y="94" text-anchor="start" fill="#CBD5E1" font-size="9">Equipment</text>
          <text x="195" y="205" text-anchor="middle" fill="#CBD5E1" font-size="9">Delivery</text>
          <text x="65" y="205" text-anchor="middle" fill="#CBD5E1" font-size="9">Readiness</text>
          <text x="32" y="94" text-anchor="end" fill="#CBD5E1" font-size="9">Commercial</text>
        </svg>
      `;
    }}

    // Render Playbook 5 Elements (Table A8 & 7)
    function renderPlaybookTable() {{
      const tbody = document.getElementById('playbookTableBody');
      tbody.innerHTML = '';
      
      APP_DATA.playbookElements.forEach(item => {{
        const isNotRunning = item.iberiaStatus.toLowerCase().includes('not running');
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>
            <div style="font-weight: 700; color: #FFF;">${{item.element}}</div>
            <div style="font-size: 0.68rem; color: var(--kone-cyan);">${{item.type}}</div>
          </td>
          <td style="font-size: 0.75rem; color: var(--text-secondary);">${{item.dachStatus}}</td>
          <td>
            <span class="badge ${{isNotRunning ? 'badge-rose' : 'badge-amber'}}">
              ${{item.iberiaStatus}}
            </span>
          </td>
          <td style="font-size: 0.76rem; color: #E2E8F0; font-weight: 500;">${{item.needed}}</td>
          <td style="font-size: 0.72rem; color: var(--text-muted);">${{item.owner}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Render Content Efficiency & Readiness
    function renderContentEfficiency() {{
      const tbody = document.getElementById('contentAssetsTableBody');
      tbody.innerHTML = '';
      
      APP_DATA.contentEfficiency.details.forEach(cat => {{
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight: 600; color: #FFF;">${{cat.category}}</td>
          <td class="font-mono">${{cat.count}}</td>
          <td class="font-mono" style="color: var(--kone-cyan);">${{cat.reuse}}</td>
          <td class="font-mono" style="color: var(--kone-cyan-light);">${{cat.adapt}}</td>
          <td class="font-mono" style="color: var(--accent-amber);">${{cat.new}}</td>
          <td style="font-size: 0.72rem; color: var(--text-secondary);">${{cat.source}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function renderLaunchReadiness() {{
      const tbody = document.getElementById('launchReadinessTableBody');
      tbody.innerHTML = '';
      
      APP_DATA.launchReadiness.forEach(item => {{
        const isAction = item.completion < 100;
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight: 600; color: #FFF;">${{item.check}}</td>
          <td class="font-mono">${{item.weight}}%</td>
          <td>
            <div class="flex-between font-mono" style="font-size: 0.72rem;">
              <span>${{item.completion}}%</span>
            </div>
            <div class="progress-bar-bg">
              <div class="progress-bar-fill" style="width: ${{item.completion}}%; background: ${{isAction ? 'var(--accent-amber)' : 'var(--accent-emerald)'}};"></div>
            </div>
          </td>
          <td class="font-mono" style="font-weight: 700;">${{item.points.toFixed(1)}}</td>
          <td>
            <span class="badge ${{isAction ? 'badge-amber' : 'badge-emerald'}}">${{item.status}}</span>
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function toggleFieldEnablementGate() {{
      isFieldGateOpen = !isFieldGateOpen;
      const fieldItem = APP_DATA.launchReadiness.find(i => i.check.includes('Field'));
      if (fieldItem) {{
        fieldItem.completion = isFieldGateOpen ? 100 : 80;
        fieldItem.points = isFieldGateOpen ? 20.0 : 16.0;
        fieldItem.status = isFieldGateOpen ? 'Approved & Ready' : 'Action Required (80% -> 100%)';
      }}
      
      const totalPoints = APP_DATA.launchReadiness.reduce((acc, i) => acc + i.points, 0);
      document.getElementById('readinessTotalScore').textContent = `${{totalPoints.toFixed(0)}} / 100`;
      renderLaunchReadiness();
    }}

    // Render 38 Buildings Cohort Table
    function renderCohortTable() {{
      const tbody = document.getElementById('cohortTableBody');
      tbody.innerHTML = '';
      
      const searchVal = document.getElementById('buildingSearchInput')?.value.toLowerCase() || '';
      const cityVal = document.getElementById('cityFilterSelect')?.value || 'ALL';
      const shaftVal = document.getElementById('shaftFilterSelect')?.value || 'ALL';
      const statusVal = document.getElementById('statusFilterSelect')?.value || 'ALL';

      const filtered = APP_DATA.cohort.filter(b => {{
        const matchSearch = b.id.toLowerCase().includes(searchVal) || b.address.toLowerCase().includes(searchVal) || b.city.toLowerCase().includes(searchVal);
        const matchCity = cityVal === 'ALL' || b.city === cityVal;
        const matchShaft = shaftVal === 'ALL' || b.shaft === shaftVal;
        const matchStatus = statusVal === 'ALL' || b.status === statusVal;
        return matchSearch && matchCity && matchShaft && matchStatus;
      }});

      // Update counters
      document.getElementById('filteredBuildingsCount').textContent = filtered.length;
      const totalQuotes = filtered.reduce((acc, b) => acc + b.quotedUnits, 0);
      const totalOrders = filtered.reduce((acc, b) => acc + b.orderedUnits, 0);
      const verifiedCount = filtered.filter(b => b.ageVerified === 'Yes').length;
      
      document.getElementById('filteredQuotesCount').textContent = totalQuotes;
      document.getElementById('filteredOrdersCount').textContent = totalOrders;
      document.getElementById('filteredConversionRate').textContent = totalQuotes > 0 ? `${{((totalOrders / totalQuotes) * 100).toFixed(1)}}%` : '0%';
      document.getElementById('filteredAgeVerified').textContent = `${{verifiedCount}} / ${{filtered.length}}`;

      filtered.forEach(b => {{
        const tr = document.createElement('tr');
        tr.className = 'clickable';
        tr.onclick = () => openBuildingModal(b.id);
        
        tr.innerHTML = `
          <td class="font-mono" style="font-weight: 700; color: var(--kone-cyan);">${{b.id}}</td>
          <td>
            <div style="font-weight: 600; color: #FFF;">${{b.city}}</div>
            <div style="font-size: 0.68rem; color: var(--text-muted);">${{b.address}}</div>
          </td>
          <td class="font-mono">${{b.installYear}}</td>
          <td class="font-mono">${{b.age}} yrs</td>
          <td>
            <span class="badge ${{b.shaft === 'Standard' ? 'badge-emerald' : 'badge-amber'}}">
              ${{b.shaft}}
            </span>
          </td>
          <td class="font-mono">${{b.quotedUnits}}</td>
          <td class="font-mono" style="font-weight: 700; color: ${{b.orderedUnits > 0 ? 'var(--accent-emerald)' : 'var(--text-muted)'}};">${{b.orderedUnits}}</td>
          <td>
            <span class="badge ${{b.ageVerified === 'Yes' ? 'badge-kone' : 'badge-rose'}}">
              ${{b.ageVerified}}
            </span>
          </td>
          <td>
            <span class="badge ${{b.status === 'Converted' ? 'badge-emerald' : 'badge-kone'}}">
              ${{b.status}}
            </span>
          </td>
          <td class="font-mono" style="color: var(--kone-cyan);">
            ${{b.daysOnSite ? `${{b.daysOnSite}} d` : '—'}}
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function filterCohortTable() {{
      renderCohortTable();
    }}

    // Building Inspector Modal
    function openBuildingModal(buildingId) {{
      const building = APP_DATA.cohort.find(b => b.id === buildingId);
      if (!building) return;
      activeBuilding = building;

      const content = document.getElementById('buildingModalContent');
      content.innerHTML = `
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
          <div>
            <div class="card-eyebrow text-cyan">BUILDING DOSSIER & ASSET TELEMETRY</div>
            <h2 class="card-title" style="font-size: 1.4rem;">${{building.id}} — ${{building.city}}</h2>
            <p style="font-size: 0.8rem; color: var(--text-secondary);">${{building.address}} (${{building.buildingType}})</p>
          </div>
          <span class="badge ${{building.status === 'Converted' ? 'badge-emerald' : 'badge-amber'}}" style="font-size: 0.85rem; padding: 6px 14px;">
            ${{building.status}}
          </span>
        </div>

        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 24px;">
          <div class="scorecard">
            <div class="scorecard-label">Installation Year</div>
            <div class="scorecard-val" style="font-size: 1.3rem;">${{building.installYear}}</div>
            <div class="scorecard-delta delta-neutral">${{building.age}} years old</div>
          </div>
          <div class="scorecard">
            <div class="scorecard-label">Shaft Geometry</div>
            <div class="scorecard-val" style="font-size: 1.3rem; color: ${{building.shaft === 'Standard' ? 'var(--accent-emerald)' : 'var(--accent-amber)'}};">${{building.shaft}}</div>
            <div class="scorecard-delta delta-neutral">Modular clearance</div>
          </div>
          <div class="scorecard">
            <div class="scorecard-label">Quotes & Orders</div>
            <div class="scorecard-val" style="font-size: 1.3rem; color: var(--kone-cyan);">${{building.orderedUnits}} / ${{building.quotedUnits}}</div>
            <div class="scorecard-delta delta-positive">${{building.orderedUnits > 0 ? 'Converted order' : 'Awaiting decision'}}</div>
          </div>
          <div class="scorecard">
            <div class="scorecard-label">Days on Site</div>
            <div class="scorecard-val" style="font-size: 1.3rem; color: #38BDF8;">${{building.daysOnSite ? `${{building.daysOnSite}} days` : 'N/A'}}</div>
            <div class="scorecard-delta delta-positive">${{building.disruptionSaved > 0 ? `${{building.disruptionSaved.toFixed(1)}} days saved` : '—'}}</div>
          </div>
        </div>

        <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: 12px; padding: 18px; margin-bottom: 20px;">
          <h4 style="font-size: 0.9rem; color: #FFF; margin-bottom: 10px;">Telemetry & Field Verification</h4>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; font-size: 0.78rem;">
            <div><strong style="color: var(--text-secondary);">Age Record Status:</strong> <span class="badge ${{building.ageVerified === 'Yes' ? 'badge-emerald' : 'badge-rose'}}">${{building.ageVerified}}</span></div>
            <div><strong style="color: var(--text-secondary);">Technician Lead:</strong> ${{building.technicianLead}} (Routine maintenance check)</div>
            <div><strong style="color: var(--text-secondary);">24/7 Connected IoT Status:</strong> ${{building.connectedActivated ? '<span class="text-emerald">● Activated & Connected</span>' : '<span class="text-amber">○ Planned for Q3</span>'}}</div>
            <div><strong style="color: var(--text-secondary);">Order Booked Value:</strong> <span class="font-mono text-cyan">EUR ${{building.orderValue.toLocaleString()}}</span></div>
          </div>
        </div>

        <div style="padding: 14px; background: rgba(0, 88, 163, 0.15); border: 1px solid rgba(0, 163, 224, 0.3); border-radius: 8px; font-size: 0.78rem; color: #E2E8F0;">
          <strong>Field Technician Observation:</strong> "Building manager reported persistent door interlock alerts. High tenant disruption sensitivity. Standard shaft dimensions verified with 1-week modular replacement kit."
        </div>
      `;

      document.getElementById('buildingModal').classList.add('open');
    }}

    function closeBuildingModal() {{
      document.getElementById('buildingModal').classList.remove('open');
    }}

    function closeModal(e) {{
      if (e.target.id === 'buildingModal') {{
        closeBuildingModal();
      }}
    }}

    // Render Day-90 Outcomes
    function renderDay90Outcomes() {{
      const tbody = document.getElementById('day90TableBody');
      tbody.innerHTML = '';
      
      const rows = [
        {{ m: 'Quote Conversion', val: '14 / 45 = 31.1%', base: '24.0% Iberia baseline', interp: '+7.1 percentage points vs baseline. 14 orders booked.' }},
        {{ m: 'Pilot Order Value', val: 'EUR 341,600', base: 'EUR 24,400 / unit', interp: '14 units booked value (contracted backlog, not recognized revenue).' }},
        {{ m: 'Installation Progress', val: '10 completed, 4 pending', base: '38 cohort buildings', interp: 'Zero safety claims or premature completion statements on pending lifts.' }},
        {{ m: 'Days on Site', val: '6.4 days average', base: '21 days conventional', interp: '14.6 days disruption eliminated per elevator shaft.' }},
        {{ m: '24/7 Connected Telemetry', val: '10 activated, 4 planned', base: '45%+ global share', interp: 'Activated units actively stream real-time operational health.' }},
        {{ m: 'Technician Referrals', val: '112 referrals', base: '90 referral target', interp: '+22 above target. Technician routine strongly adopted.' }},
        {{ m: 'Installation Age Verification', val: '31 / 38 = 81.6%', base: '100% pre-quote gate', interp: 'Seven records remained provisional. Data gate missed.' }}
      ];

      rows.forEach(r => {{
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight: 700; color: #FFF;">${{r.m}}</td>
          <td class="font-mono" style="font-weight: 700; color: var(--accent-emerald);">${{r.val}}</td>
          <td class="font-mono" style="color: var(--text-secondary);">${{r.base}}</td>
          <td style="font-size: 0.76rem; color: #CBD5E1;">${{r.interp}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Render Ingredients (Table A13)
    function renderIngredients() {{
      const grid = document.getElementById('ingredientsGrid');
      grid.innerHTML = '';

      APP_DATA.ingredients.forEach(ig => {{
        const card = document.createElement('div');
        card.className = 'glass-card col-4';
        card.innerHTML = `
          <div class="card-header">
            <div>
              <div class="card-eyebrow text-cyan">${{ig.id}} | ${{ig.reusability}}</div>
              <h3 class="card-title" style="font-size: 1.05rem;">${{ig.name}}</h3>
            </div>
            <span class="badge badge-emerald">${{ig.status}}</span>
          </div>
          <p style="font-size: 0.76rem; color: #E2E8F0; line-height: 1.5; margin-bottom: 14px;">${{ig.description}}</p>
          <div style="padding: 10px; background: rgba(0, 0, 0, 0.3); border-radius: 8px; font-size: 0.72rem; color: var(--kone-cyan); margin-bottom: 12px;">
            <strong>Operating Rule:</strong> ${{ig.guideline}}
          </div>
          <div class="flex-between" style="font-size: 0.7rem; color: var(--text-muted);">
            <span>Owner: ${{ig.owner}}</span>
            <span>Origin: ${{ig.origin}}</span>
          </div>
        `;
        grid.appendChild(card);
      }});
    }}

    function packageBeneluxBrief() {{
      const preview = document.getElementById('beneluxPackagePreview');
      preview.style.display = 'block';
      preview.scrollIntoView({{ behavior: 'smooth' }});
    }}

    // Simulation Live Sandbox Engine
    function runSimulation() {{
      simState.cohortSize = parseInt(document.getElementById('sliderSimCohort').value);
      simState.shaftRatio = parseInt(document.getElementById('sliderSimShaftRatio').value);
      simState.referrals = parseInt(document.getElementById('sliderSimReferrals').value);
      simState.ageVerifiedPct = parseInt(document.getElementById('sliderSimAgeVerified').value);
      simState.avgOrder = parseInt(document.getElementById('sliderSimAvgOrder').value);
      simState.contentReuse = parseInt(document.getElementById('sliderSimContentReuse').value);
      simState.market = document.getElementById('simMarketSelect').value;

      // Update slider labels
      document.getElementById('valSimCohort').textContent = `${{simState.cohortSize}} buildings`;
      document.getElementById('valSimShaftRatio').textContent = `${{simState.shaftRatio}}%`;
      document.getElementById('valSimReferrals').textContent = `${{simState.referrals}} referrals`;
      document.getElementById('valSimAgeVerified').textContent = `${{simState.ageVerifiedPct}}%`;
      document.getElementById('valSimAvgOrder').textContent = `€${{simState.avgOrder.toLocaleString()}}`;
      document.getElementById('valSimContentReuse').textContent = `${{simState.contentReuse}}%`;

      // Computational Simulation Model
      // Quotes roughly 1.18 quotes per building
      const quotes = Math.round(simState.cohortSize * 1.184);
      
      // Standard shaft proportion
      const stdQuotes = Math.round(quotes * (simState.shaftRatio / 100));
      const nonStdQuotes = quotes - stdQuotes;

      // Conversion rates:
      // Standard shaft base: 37% (scaled by referrals and data verification)
      // Non-standard shaft base: 3%
      const dataFactor = 0.5 + (simState.ageVerifiedPct / 100) * 0.5;
      const refFactor = Math.min(1.25, 0.8 + (simState.referrals / 200) * 0.4);

      const stdConv = Math.min(0.55, 0.36 * dataFactor * refFactor);
      const nonStdConv = 0.04 * dataFactor;

      const orders = Math.round((stdQuotes * stdConv) + (nonStdQuotes * nonStdConv));
      const convRate = quotes > 0 ? ((orders / quotes) * 100).toFixed(1) : '0';
      const revenue = orders * simState.avgOrder;
      const daysSaved = orders * 14.6;
      const contentDays = Math.round(60 * (1 - (simState.contentReuse / 100) * 0.65));
      const riskScore = Math.max(5, Math.round(100 - (simState.shaftRatio * 0.4 + simState.ageVerifiedPct * 0.4 + simState.contentReuse * 0.2)));

      // Render Outputs
      document.getElementById('simResultQuotes').textContent = quotes;
      document.getElementById('simResultOrders').textContent = orders;
      document.getElementById('simResultConvRate').textContent = `${{convRate}}% conversion`;
      document.getElementById('simResultRevenue').textContent = `€${{(revenue / 1000).toFixed(1)}}k`;
      document.getElementById('simResultDaysSaved').textContent = `${{Math.round(daysSaved)}} days`;
      document.getElementById('simResultContentDays').textContent = `${{contentDays}} days`;
      
      const riskEl = document.getElementById('simResultRisk');
      riskEl.textContent = `${{riskScore < 20 ? 'Low' : (riskScore < 35 ? 'Moderate' : 'Elevated')}} (${{riskScore}}%)`;
      riskEl.style.color = riskScore < 20 ? 'var(--accent-emerald)' : (riskScore < 35 ? 'var(--accent-amber)' : 'var(--accent-rose)');

      document.getElementById('simSensitivityConv').textContent = `${{(convRate - 24.0).toFixed(1)}} pts`;
      document.getElementById('simSensitivityShaft').textContent = `${{simState.shaftRatio}}% qualified`;
      document.getElementById('simSensitivityData').textContent = `${{simState.ageVerifiedPct}}% verified`;

      document.getElementById('simProgressConv').style.width = `${{Math.min(100, convRate * 2)}}%`;
      document.getElementById('simProgressShaft').style.width = `${{simState.shaftRatio}}%`;
      document.getElementById('simProgressData').style.width = `${{simState.ageVerifiedPct}}%`;
    }}

    function loadSimPreset(presetKey) {{
      if (presetKey === 'iberia_actual') {{
        document.getElementById('simMarketSelect').value = 'Iberia';
        document.getElementById('sliderSimCohort').value = 38;
        document.getElementById('sliderSimShaftRatio').value = 84;
        document.getElementById('sliderSimReferrals').value = 112;
        document.getElementById('sliderSimAgeVerified').value = 82;
        document.getElementById('sliderSimAvgOrder').value = 24400;
        document.getElementById('sliderSimContentReuse').value = 62;
      }} else if (presetKey === 'benelux_scale') {{
        document.getElementById('simMarketSelect').value = 'Benelux';
        document.getElementById('sliderSimCohort').value = 50;
        document.getElementById('sliderSimShaftRatio').value = 90;
        document.getElementById('sliderSimReferrals').value = 140;
        document.getElementById('sliderSimAgeVerified').value = 95;
        document.getElementById('sliderSimAvgOrder').value = 20000;
        document.getElementById('sliderSimContentReuse').value = 75;
      }} else if (presetKey === 'dach_benchmark') {{
        document.getElementById('simMarketSelect').value = 'DACH';
        document.getElementById('sliderSimCohort').value = 100;
        document.getElementById('sliderSimShaftRatio').value = 92;
        document.getElementById('sliderSimReferrals').value = 240;
        document.getElementById('sliderSimAgeVerified').value = 98;
        document.getElementById('sliderSimAvgOrder').value = 23500;
        document.getElementById('sliderSimContentReuse').value = 85;
      }} else if (presetKey === 'high_disruption') {{
        document.getElementById('simMarketSelect').value = 'Iberia';
        document.getElementById('sliderSimCohort').value = 60;
        document.getElementById('sliderSimShaftRatio').value = 65;
        document.getElementById('sliderSimReferrals').value = 80;
        document.getElementById('sliderSimAgeVerified').value = 60;
        document.getElementById('sliderSimAvgOrder').value = 26000;
        document.getElementById('sliderSimContentReuse').value = 50;
      }}
      runSimulation();
    }}

    function resetSimParams() {{
      loadSimPreset('iberia_actual');
    }}

    // Workshop Script Player & Scene Navigation
    function renderSceneNavigator() {{
      const container = document.getElementById('sceneNavContainer');
      container.innerHTML = '';

      APP_DATA.scriptScenes.forEach((s, idx) => {{
        const btn = document.createElement('button');
        btn.className = `scene-pill-btn ${{idx === currentSceneIdx ? 'active' : ''}}`;
        btn.id = `scene-btn-${{idx}}`;
        btn.onclick = () => selectScene(idx);
        btn.innerHTML = `
          <span class="scene-num">Scene ${{s.scene}} (${{s.timecode}})</span>
          <span style="font-weight: 600;">${{s.title}}</span>
        `;
        container.appendChild(btn);
      }});

      updateSceneDisplay();
    }}

    function selectScene(idx) {{
      currentSceneIdx = idx;
      document.querySelectorAll('.scene-pill-btn').forEach(b => b.classList.remove('active'));
      document.getElementById(`scene-btn-${{idx}}`).classList.add('active');
      updateSceneDisplay();
    }}

    function updateSceneDisplay() {{
      const s = APP_DATA.scriptScenes[currentSceneIdx];
      document.getElementById('sceneActLabel').textContent = s.act.toUpperCase();
      document.getElementById('sceneTitle').textContent = `Scene ${{s.scene}} | ${{s.title}}`;
      document.getElementById('sceneTimecode').textContent = `Timecode: ${{s.timecode}}`;
      document.getElementById('sceneSpeaker').textContent = s.speaker;
      document.getElementById('sceneTargetScreen').textContent = `Screen Target: ${{s.screenTarget.toUpperCase()}}`;
      document.getElementById('sceneDialogue').textContent = `"${{s.dialogue}}"`;
      document.getElementById('sceneHeadline').textContent = s.headline;
      document.getElementById('sceneTakeaway').textContent = s.takeaway;
    }}

    function jumpToSceneScreen() {{
      const s = APP_DATA.scriptScenes[currentSceneIdx];
      switchTab(s.screenTarget);
    }}


    // Workshop Interactive Discussion Questions
    function renderWorkshopQuestions() {{
      const container = document.getElementById('workshopQuestionsContainer');
      container.innerHTML = '';

      APP_DATA.workshopQuestions.forEach(q => {{
        const box = document.createElement('div');
        box.style.padding = '12px';
        box.style.background = 'rgba(255, 255, 255, 0.03)';
        box.style.borderRadius = '8px';
        box.style.border = '1px solid var(--border-glass)';
        
        box.innerHTML = `
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
            <span class="badge badge-kone">${{q.id}}</span>
            <span style="font-size: 0.65rem; color: var(--text-muted);">5-Min Leadership Dialogue</span>
          </div>
          <div style="font-size: 0.8rem; font-weight: 700; color: #FFF; margin-bottom: 6px;">${{q.question}}</div>
          <div style="font-size: 0.7rem; color: var(--text-secondary); margin-bottom: 10px;">${{q.context}}</div>
          <div style="display: flex; flex-direction: column; gap: 4px;">
            ${{q.options.map((opt, i) => `
              <button onclick="voteOption('${{q.id}}', ${{i}}, this)" style="text-align: left; padding: 6px 10px; background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border-glass-subtle); border-radius: 6px; color: #CBD5E1; font-size: 0.72rem; cursor: pointer; transition: all 0.15s ease;">
                ${{opt}}
              </button>
            `).join('')}}
          </div>
        `;
        container.appendChild(box);
      }});
    }}

    function voteOption(qId, optIdx, btnEl) {{
      const parent = btnEl.parentElement;
      parent.querySelectorAll('button').forEach(b => {{
        b.style.background = 'rgba(255, 255, 255, 0.05)';
        b.style.borderColor = 'var(--border-glass-subtle)';
        b.style.color = '#CBD5E1';
      }});
      btnEl.style.background = 'rgba(0, 163, 224, 0.2)';
      btnEl.style.borderColor = 'var(--kone-cyan)';
      btnEl.style.color = '#FFFFFF';
    }}

  </script>
</body>
</html>
"""

# Write to index.html and kone-marketing-os.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("kone-marketing-os.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Build complete! index.html ({len(html_content)} bytes) and kone-marketing-os.html successfully written.")
