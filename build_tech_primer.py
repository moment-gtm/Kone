#!/usr/bin/env python3
"""
KONE Assisted Decisioning System - Technical Architecture & Client Defense Guide Builder
Generates a comprehensive, standalone, redistributable HTML technical document (tech-architecture.html).
Prepares the team for client technical evaluations:
- What does it take to build this for real? (Architecture, tech stack, roadmap, sizing)
- What kind of data exercise needs to be done? (5 data domains, entity resolution, readiness audit)
- 16 Battle-tested Client Defense Q&As across 5 categories
- Interactive Data Readiness Calculator
- Prototype vs Production comparison matrix
Follows KONE light design system tokens with embedded logos.
"""

import json
import base64
import os
import sys

def build_tech_primer():
    # Load KONE logo and encode to base64
    logo_path = 'kone_logo.jpg'
    if not os.path.exists(logo_path):
        logo_path = '/Users/191561/.gemini/antigravity/brain/5f8deb25-0948-4c9b-8ee8-e5bf49f4b0cc/.user_uploaded/media_1794233681514_9cc72068.jpg'

    with open(logo_path, 'rb') as f:
        kone_logo_b64 = base64.b64encode(f.read()).decode('utf-8')

    # Load Cognizant Moment logo and encode to base64
    cognizant_path = 'cognizant_logo.png'
    if not os.path.exists(cognizant_path):
        cognizant_path = '/Users/191561/.gemini/antigravity/brain/5f8deb25-0948-4c9b-8ee8-e5bf49f4b0cc/.user_uploaded/media_1794236613020_7f5d883d.png'

    with open(cognizant_path, 'rb') as f:
        cognizant_logo_b64 = base64.b64encode(f.read()).decode('utf-8')

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Technical Architecture & Client Defense Guide | KONE Assisted Decisioning System</title>
  <link rel="icon" type="image/jpeg;base64,{kone_logo_b64}">
  <style>
    /* ============================================================================
       KONE DESIGN SYSTEM - LIGHT THEME (Extracted from kone.com/innovation)
       ========================================================================== */
    :root {{
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

      --font-heading: 'VideoJS', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-body: 'Inter Regular', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      --font-font-3: 'Inter SemiBold', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-font-4: 'KONE Information', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-font-5: 'Consolas', 'Monaco', 'Courier New', monospace;

      --radius-1: 2px;
      --radius-2: 3px;
      --radius-3: 4px;
      --radius-4: 8px;
      --radius-5: 15px;
      --radius-6: 24px;

      --shadow-1: 0 0 1em #fff;
      --shadow-2: 0 0 0 3px hsla(0,0%,100%,.7);
      --shadow-3: 0 0 3px rgba(0,0,0,.15);
      --shadow-4: 0 4px 10px rgba(0,0,0,.1);
      --shadow-5: 0 0 1px 0 rgba(20,20,20,.06),0 10px 15px -3px rgba(20,20,20,.08),0 4px 6px -2px rgba(20,20,20,.04);
      --shadow-6: 0 3px 5px rgba(0,0,0,.12);
      --shadow-blue: 0 8px 24px rgba(20, 80, 245, 0.18);

      --app-bg: #fafbfc;
      --card-bg: #ffffff;
      --card-border: var(--color-neutral-2);
      --text-high: #00061f;
      --text-medium: #323232;
      --text-dim: #575759;
      --text-muted: #73859f;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }}

    body {{
      background: var(--app-bg);
      background-image: 
        radial-gradient(circle at 10% 5%, rgba(20, 80, 245, 0.04) 0%, transparent 40%),
        radial-gradient(circle at 90% 95%, rgba(102, 168, 204, 0.05) 0%, transparent 45%),
        linear-gradient(180deg, #f7faff 0%, #fafbfc 100%);
      color: var(--text-high);
      font-family: var(--font-body);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      line-height: 1.55;
    }}

    /* Scrollbars */
    ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
    ::-webkit-scrollbar-track {{ background: var(--color-neutral-5); }}
    ::-webkit-scrollbar-thumb {{ background: var(--color-neutral-12); border-radius: var(--radius-3); }}
    ::-webkit-scrollbar-thumb:hover {{ background: var(--color-primary-1); }}

    /* Tabular numbers and utility badges */
    .num {{ font-variant-numeric: tabular-nums; font-feature-settings: "tnum"; }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 8px;
      border-radius: var(--radius-2);
      font-size: 11px;
      font-weight: 600;
      line-height: 1;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }}
    .badge-primary {{ background: var(--color-primary-7); color: var(--color-primary-1); border: 1px solid var(--color-primary-9); }}
    .badge-success {{ background: #eafaf1; color: #1e7e34; border: 1px solid #c3e6cb; }}
    .badge-warning {{ background: #fff8e6; color: #b78103; border: 1px solid #ffeeba; }}
    .badge-danger {{ background: #fdf2f2; color: #dc3545; border: 1px solid #f5c6cb; }}
    .badge-neutral {{ background: var(--color-neutral-5); color: var(--color-neutral-7); border: 1px solid var(--color-neutral-2); }}
    .badge-dark {{ background: var(--color-primary-2); color: #ffffff; }}

    /* ============================================================================
       TOP CHROME
       ========================================================================== */
    .top-chrome {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 64px;
      padding: 0 28px;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--color-neutral-2);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 8px rgba(0, 6, 31, 0.03);
    }}
    .top-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .brand-mark {{
      display: flex;
      align-items: center;
      cursor: pointer;
    }}
    .brand-logo-img {{
      height: 34px;
      width: auto;
      object-fit: contain;
      display: block;
      border-radius: var(--radius-2);
    }}
    .divider-vert {{
      width: 1px;
      height: 28px;
      background: var(--color-neutral-2);
    }}
    .system-title-wrap {{
      display: flex;
      flex-direction: column;
    }}
    .system-title {{
      font-size: 15px;
      font-family: var(--font-font-3);
      font-weight: 700;
      color: var(--color-primary-2);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .system-subtitle {{
      font-size: 11.5px;
      color: var(--color-neutral-6);
    }}

    .top-right {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .btn-return {{
      background: var(--color-primary-1);
      color: #ffffff;
      padding: 8px 16px;
      border-radius: var(--radius-3);
      font-size: 12.5px;
      font-family: var(--font-font-3);
      font-weight: 600;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 2px 8px rgba(20, 80, 245, 0.25);
      transition: all 0.2s ease;
    }}
    .btn-return:hover {{
      background: var(--color-primary-15);
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(20, 80, 245, 0.35);
    }}

    /* ============================================================================
       NAV TABS HEADER
       ========================================================================== */
    .nav-tabs-bar {{
      background: #ffffff;
      border-bottom: 1px solid var(--color-neutral-2);
      padding: 0 28px;
      display: flex;
      gap: 4px;
      position: sticky;
      top: 64px;
      z-index: 90;
      overflow-x: auto;
    }}
    .tab-btn {{
      padding: 14px 20px;
      background: transparent;
      border: none;
      border-bottom: 3px solid transparent;
      color: var(--color-neutral-7);
      font-size: 13.5px;
      font-family: var(--font-font-3);
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
      white-space: nowrap;
    }}
    .tab-btn:hover {{
      color: var(--color-primary-1);
      background: var(--color-primary-6);
    }}
    .tab-btn.active {{
      color: var(--color-primary-1);
      border-bottom-color: var(--color-primary-1);
      background: var(--color-primary-3);
    }}

    /* ============================================================================
       PAGE CONTAINER & LAYOUT
       ========================================================================== */
    .container {{
      max-width: 1360px;
      margin: 0 auto;
      padding: 32px 28px 80px 28px;
      width: 100%;
      flex: 1;
    }}

    .hero-banner {{
      background: linear-gradient(135deg, #ffffff 0%, #f5f8ff 100%);
      border: 1px solid var(--color-primary-8);
      border-radius: var(--radius-4);
      padding: 28px 32px;
      margin-bottom: 28px;
      box-shadow: var(--shadow-5);
      position: relative;
      overflow: hidden;
    }}
    .hero-banner::after {{
      content: "";
      position: absolute;
      top: -40px;
      right: -40px;
      width: 240px;
      height: 240px;
      background: radial-gradient(circle, rgba(20, 80, 245, 0.08) 0%, transparent 70%);
      pointer-events: none;
    }}
    .hero-title {{
      font-size: 24px;
      font-family: var(--font-font-3);
      color: var(--color-primary-2);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .hero-desc {{
      font-size: 14.5px;
      color: var(--color-neutral-7);
      max-width: 1050px;
      line-height: 1.6;
    }}
    .hero-meta-strip {{
      display: flex;
      align-items: center;
      gap: 24px;
      margin-top: 18px;
      padding-top: 16px;
      border-top: 1px solid var(--color-primary-8);
      font-size: 12.5px;
      color: var(--color-neutral-6);
      flex-wrap: wrap;
    }}
    .hero-meta-item {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .hero-meta-item strong {{
      color: var(--color-primary-2);
    }}

    /* TAB CONTENT PANES */
    .tab-pane {{
      display: none;
    }}
    .tab-pane.active {{
      display: block;
      animation: fadeIn 0.2s ease-in-out;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* CARDS & PANELS */
    .card {{
      background: #ffffff;
      border: 1px solid var(--color-neutral-2);
      border-radius: var(--radius-4);
      padding: 24px;
      box-shadow: var(--shadow-5);
      margin-bottom: 24px;
      transition: all 0.2s ease;
    }}
    .card:hover {{
      box-shadow: 0 6px 18px rgba(0, 6, 31, 0.06);
    }}
    .card-title {{
      font-size: 17px;
      font-family: var(--font-font-3);
      color: var(--color-primary-2);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .card-subtitle {{
      font-size: 13px;
      color: var(--color-neutral-6);
      margin-bottom: 18px;
    }}

    /* GRIDS */
    .grid-2 {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }}
    .grid-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }}

    @media (max-width: 1024px) {{
      .grid-2, .grid-3, .grid-4 {{ grid-template-columns: 1fr; }}
    }}

    /* ARCHITECTURE DIAGRAM / TIERS */
    .arch-tier {{
      background: #ffffff;
      border: 1px solid var(--color-neutral-2);
      border-radius: var(--radius-4);
      padding: 20px;
      margin-bottom: 16px;
      position: relative;
      border-left: 5px solid var(--color-primary-1);
      box-shadow: var(--shadow-5);
    }}
    .arch-tier-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }}
    .arch-tier-num {{
      font-size: 11px;
      font-weight: 700;
      color: var(--color-primary-1);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .arch-tier-name {{
      font-size: 16px;
      font-family: var(--font-font-3);
      color: var(--color-primary-2);
      font-weight: 700;
    }}
    .arch-pill-row {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-top: 10px;
    }}
    .arch-tech-pill {{
      background: var(--color-primary-3);
      border: 1px solid var(--color-primary-8);
      color: var(--color-primary-2);
      padding: 4px 10px;
      border-radius: var(--radius-2);
      font-size: 12px;
      font-family: var(--font-font-5);
      font-weight: 600;
    }}

    /* CALLOUT BOXES */
    .callout {{
      padding: 16px 20px;
      border-radius: var(--radius-3);
      font-size: 13.5px;
      line-height: 1.55;
      margin: 16px 0;
    }}
    .callout-info {{
      background: var(--color-primary-3);
      border-left: 4px solid var(--color-primary-1);
      color: var(--color-primary-2);
    }}
    .callout-warning {{
      background: #fff8e6;
      border-left: 4px solid #f59e0b;
      color: #78350f;
    }}
    .callout-success {{
      background: #eafaf1;
      border-left: 4px solid #10b981;
      color: #064e3b;
    }}

    /* TABLES */
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      margin-top: 12px;
    }}
    .data-table th {{
      text-align: left;
      padding: 10px 14px;
      background: var(--color-primary-3);
      color: var(--color-neutral-7);
      font-weight: 700;
      font-size: 11.5px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      border-bottom: 1px solid var(--color-primary-8);
    }}
    .data-table td {{
      padding: 12px 14px;
      border-bottom: 1px solid var(--color-neutral-2);
      color: var(--text-high);
      vertical-align: top;
    }}
    .data-table tr:hover td {{
      background: var(--color-primary-6);
    }}

    /* Q&A ACCORDIONS */
    .qa-controls {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }}
    .qa-search-box {{
      flex: 1;
      min-width: 260px;
      padding: 10px 16px;
      border: 1px solid var(--color-neutral-2);
      border-radius: var(--radius-3);
      font-size: 13.5px;
      background: #ffffff;
      outline: none;
      transition: all 0.2s ease;
    }}
    .qa-search-box:focus {{
      border-color: var(--color-primary-1);
      box-shadow: 0 0 0 3px rgba(20, 80, 245, 0.12);
    }}
    .filter-btn {{
      padding: 8px 14px;
      background: #ffffff;
      border: 1px solid var(--color-neutral-2);
      border-radius: var(--radius-3);
      font-size: 12px;
      font-family: var(--font-font-3);
      color: var(--color-neutral-7);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .filter-btn:hover {{
      border-color: var(--color-primary-1);
      color: var(--color-primary-1);
    }}
    .filter-btn.active {{
      background: var(--color-primary-1);
      border-color: var(--color-primary-1);
      color: #ffffff;
    }}

    .qa-card {{
      background: #ffffff;
      border: 1px solid var(--color-neutral-2);
      border-radius: var(--radius-4);
      margin-bottom: 14px;
      box-shadow: var(--shadow-5);
      overflow: hidden;
      transition: all 0.2s ease;
    }}
    .qa-card.open {{
      border-color: var(--color-primary-9);
      box-shadow: 0 8px 24px rgba(20, 80, 245, 0.08);
    }}
    .qa-header {{
      padding: 16px 20px;
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      cursor: pointer;
      background: #ffffff;
      gap: 14px;
      user-select: none;
    }}
    .qa-header:hover {{
      background: var(--color-primary-6);
    }}
    .qa-title-wrap {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .qa-category-tag {{
      font-size: 10.5px;
      font-weight: 700;
      color: var(--color-primary-1);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .qa-question {{
      font-size: 15px;
      font-family: var(--font-font-3);
      color: var(--color-primary-2);
      line-height: 1.4;
    }}
    .qa-toggle-icon {{
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: var(--color-primary-3);
      color: var(--color-primary-1);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      flex-shrink: 0;
      transition: transform 0.2s ease;
    }}
    .qa-card.open .qa-toggle-icon {{
      transform: rotate(180deg);
      background: var(--color-primary-1);
      color: #ffffff;
    }}
    .qa-body {{
      display: none;
      padding: 0 20px 22px 20px;
      border-top: 1px solid var(--color-neutral-2);
      background: #ffffff;
    }}
    .qa-card.open .qa-body {{
      display: block;
      animation: fadeIn 0.15s ease-out;
    }}
    .qa-block {{
      margin-top: 14px;
    }}
    .qa-subhead {{
      font-size: 11.5px;
      font-weight: 700;
      color: var(--color-neutral-6);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 4px;
    }}
    .qa-exec-pitch {{
      font-size: 14px;
      color: var(--color-primary-2);
      background: var(--color-primary-3);
      border-left: 3px solid var(--color-primary-1);
      padding: 12px 14px;
      border-radius: 0 var(--radius-2) var(--radius-2) 0;
      font-weight: 500;
      line-height: 1.5;
    }}
    .qa-deep-dive {{
      font-size: 13.5px;
      color: var(--text-medium);
      line-height: 1.6;
      margin-top: 8px;
    }}

    /* READINESS CALCULATOR */
    .calc-box {{
      background: linear-gradient(135deg, #ffffff 0%, var(--color-primary-3) 100%);
      border: 1px solid var(--color-primary-8);
      border-radius: var(--radius-4);
      padding: 24px;
      margin-bottom: 24px;
    }}
    .calc-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 24px;
      align-items: center;
    }}
    @media (max-width: 900px) {{
      .calc-grid {{ grid-template-columns: 1fr; }}
    }}
    .calc-items {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .calc-item {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 10px 14px;
      background: #ffffff;
      border: 1px solid var(--color-neutral-2);
      border-radius: var(--radius-3);
      cursor: pointer;
      user-select: none;
      transition: all 0.15s ease;
    }}
    .calc-item:hover {{
      border-color: var(--color-primary-9);
      background: var(--color-primary-6);
    }}
    .calc-item input[type="checkbox"] {{
      width: 18px;
      height: 18px;
      accent-color: var(--color-primary-1);
      cursor: pointer;
    }}
    .calc-label {{
      font-size: 13px;
      color: var(--text-high);
      flex: 1;
    }}
    .calc-score-display {{
      text-align: center;
      padding: 24px;
      background: #ffffff;
      border: 1px solid var(--color-primary-8);
      border-radius: var(--radius-4);
      box-shadow: var(--shadow-5);
    }}
    .calc-score-num {{
      font-size: 54px;
      font-family: var(--font-heading);
      font-weight: 700;
      color: var(--color-primary-1);
      line-height: 1;
      margin-bottom: 4px;
    }}
    .calc-score-sub {{
      font-size: 12px;
      color: var(--color-neutral-6);
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.05em;
    }}
    .calc-timeline-est {{
      margin-top: 14px;
      padding: 8px 12px;
      background: var(--color-primary-7);
      border-radius: var(--radius-2);
      font-size: 12.5px;
      color: var(--color-primary-2);
      font-weight: 600;
    }}

    /* BOTTOM FOOTER */
    .bottom-footer {{
      margin-top: auto;
      background: #ffffff;
      border-top: 1px solid var(--color-neutral-2);
      padding: 20px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12px;
      color: var(--color-neutral-6);
      flex-wrap: wrap;
      gap: 16px;
    }}
    .footer-left {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}
    .cognizant-logo-img {{
      height: 24px;
      width: auto;
      object-fit: contain;
      display: block;
    }}

    /* PRINT STYLES */
    @media print {{
      .top-chrome, .nav-tabs-bar, .qa-controls, .btn-return, .bottom-footer {{ display: none !important; }}
      .tab-pane {{ display: block !important; margin-bottom: 40px; page-break-after: always; }}
      body {{ background: #ffffff !important; }}
      .card, .arch-tier, .qa-card {{ box-shadow: none !important; border: 1px solid #ccc !important; }}
      .qa-body {{ display: block !important; }}
    }}
  </style>
</head>
<body>

  <!-- ============================================================================
       TOP CHROME
       ========================================================================== -->
  <header class="top-chrome">
    <div class="top-left">
      <div class="brand-mark" onclick="location.href='index.html'" title="Return to KONE Assisted Decisioning System">
        <img class="brand-logo-img" src="data:image/jpeg;base64,{kone_logo_b64}" alt="KONE">
      </div>
      <div class="divider-vert"></div>
      <div class="system-title-wrap">
        <div class="system-title">
          Assisted Decisioning System
          <span class="badge badge-primary">Technical Architecture & Client Defense</span>
        </div>
        <div class="system-subtitle">Enterprise Engineering Blueprint · Data Readiness Audit · Production Roadmap</div>
      </div>
    </div>

    <div class="top-right">
      <span class="badge badge-neutral" style="font-family:var(--font-font-5);">Confidential · KONE & Cognizant Moment</span>
      <a href="index.html" class="btn-return" title="Launch the Interactive 8-Stage Assisted Decisioning System">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
        Launch Live System (index.html)
      </a>
    </div>
  </header>

  <!-- ============================================================================
       NAV TABS BAR
       ========================================================================== -->
  <nav class="nav-tabs-bar" id="techNavTabs">
    <button class="tab-btn active" onclick="switchTab('exec')">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
      Executive Summary & Context
    </button>
    <button class="tab-btn" onclick="switchTab('poc')">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
      ⚡ Enterprise Pilot Blueprint & KONE Asks (16–20 Wks)
    </button>
    <button class="tab-btn" onclick="switchTab('deps')">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg>
      All System & Ops Dependencies
    </button>
    <button class="tab-btn" onclick="switchTab('arch')">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>
      Production Architecture & Stack
    </button>
    <button class="tab-btn" onclick="switchTab('data')">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>
      The Data Exercise & Readiness Audit
    </button>
    <button class="tab-btn" onclick="switchTab('roadmap')">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/><path d="M9 14l2 2 4-4"/></svg>
      What It Takes to Build (Roadmap & Cost)
    </button>
    <button class="tab-btn" onclick="switchTab('defense')">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
      Client Defense Guide (18 Technical Q&As)
    </button>
    <button class="tab-btn" onclick="switchTab('matrix')">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
      Prototype vs. Production Matrix
    </button>
  </nav>

  <!-- ============================================================================
       CONTAINER BODY
       ========================================================================== -->
  <main class="container">

    <!-- ========================================================================
         TAB 1: EXECUTIVE SUMMARY & STRATEGIC CONTEXT
         ======================================================================== -->
    <section class="tab-pane active" id="pane-exec">
      <div class="hero-banner">
        <div class="hero-title">
          <span>Executive Technical Briefing: The KONE Marketing Brain</span>
          <span class="badge badge-success">Target State Blueprint</span>
        </div>
        <p class="hero-desc">
          This technical reference prepares the delivery team for technical scrutiny by KONE’s Chief Technology Officer, 
          Head of Enterprise Architecture, VP of Data & IoT Platform, MarTech leadership, and Information Security. 
          It unpacks how the <strong>Assisted Decisioning System (ADS)</strong> evolves from the current standalone boardroom 
          prototype into an enterprise-grade closed-loop decision engine that connects 2.87M maintenance assets to real-time 
          commercial and field execution.
        </p>
        <div class="hero-meta-strip">
          <div class="hero-meta-item">
            <span>Primary Sponsors:</span> <strong>Petra (CMO) & Hans (Global Customer Marketing Director)</strong>
          </div>
          <div class="hero-meta-item">
            <span>Core Mantra:</span> <em>"If KONE only knew what KONE knows"</em>
          </div>
          <div class="hero-meta-item">
            <span>Key Business Focus:</span> <strong>One Week Modernization & Connected Asset Monetization</strong>
          </div>
        </div>
      </div>

      <!-- ========================================================================
           EXECUTIVE POC & DEPENDENCIES AT A GLANCE BANNER
           ======================================================================== -->
      <div class="card" style="margin-top:18px; margin-bottom:18px; background:linear-gradient(135deg, #ffffff 0%, var(--color-primary-3) 100%); border: 1.5px solid var(--color-primary-9); box-shadow:var(--shadow-5);">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
          <div>
            <div style="font-size:16px; font-weight:800; color:var(--color-primary-2); display:flex; align-items:center; gap:8px;">
              <span>⚡ Enterprise Pilot: 16 to 20 Weeks to Live Field Pilot in Iberia</span>
              <span class="badge badge-success">Production Ready</span>
            </div>
            <div style="font-size:13px; color:var(--text-medium); margin-top:4px;">
              De-risked 16-to-20 week enterprise flight plan anchored on KONE's flagship <strong>"Life, Upgraded in ONE Week" (ONE Week MOD)</strong> campaign across 9,039 addressable residential elevator assets in Italy & Iberia (ITIB).
            </div>
          </div>
          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <button class="btn-primary" onclick="switchTab('poc')" style="background:var(--color-primary-1); color:#ffffff; border:none; padding:8px 16px; border-radius:var(--radius-3); font-weight:700; font-size:12.5px; cursor:pointer; box-shadow:0 2px 6px rgba(20,80,245,0.25);">
              Explore 16–20 Wk Pilot & KONE Ask &rarr;
            </button>
            <button class="btn-primary" onclick="switchTab('deps')" style="background:#ffffff; color:var(--color-primary-1); border:1px solid var(--color-primary-1); padding:8px 16px; border-radius:var(--radius-3); font-weight:700; font-size:12.5px; cursor:pointer;">
              View All Dependencies &rarr;
            </button>
          </div>
        </div>
      </div>

      <div class="grid-3">
        <div class="card">
          <div class="card-title">
            <span>1. Beyond BI Dashboards</span>
            <span class="badge badge-primary">Decisions > Reports</span>
          </div>
          <div class="card-subtitle">Why traditional dashboards fail KONE leadership</div>
          <p style="font-size:13px; color:var(--text-medium); line-height:1.55;">
            Traditional BI (Tableau, Power BI) reports historical lagging indicators ("What happened last quarter in Iberia?"). 
            The Assisted Decisioning System is an <strong>action engine</strong> that recommends <em>where capital should be deployed next Monday</em>, 
            prescribes operational fixes (technician lead capture, 5-day disruption guarantees), and simulates the revenue and EBITDA yield before a single euro is committed.
          </p>
        </div>

        <div class="card">
          <div class="card-title">
            <span>2. The Connected Asset Advantage</span>
            <span class="badge badge-success">&gt;45% Connected Base</span>
          </div>
          <div class="card-subtitle">Unlocking latent telemetry for commercial growth</div>
          <p style="font-size:13px; color:var(--text-medium); line-height:1.55;">
            KONE maintains 2.87 million elevator and escalator contracts, with over 45% equipped with 
            <strong>KONE 24/7 Connected Services</strong>. This stream of door cycles, vibration anomalies, and controller 
            fault codes represents an unmatched commercial moat—if married to contract renewal dates and building owner profiles.
          </p>
        </div>

        <div class="card">
          <div class="card-title">
            <span>3. Scaling Across Markets</span>
            <span class="badge badge-warning">"If It Works in Germany..."</span>
          </div>
          <div class="card-subtitle">Solving organizational amnesia</div>
          <p style="font-size:13px; color:var(--text-medium); line-height:1.55;">
            When DACH achieves a 46% modernization conversion rate, the playbook must not die in local spreadsheets. 
            The ADS codifies what travels (bracket pre-assembly, guaranteed installation speed) versus what must adapt 
            (Spanish property administrator procurement channels), updating prior probabilities using Bayesian learning.
          </p>
        </div>
      </div>

      <div class="card">
        <div class="card-title">
          <span>The 8-Stage Closed-Loop Decision Flywheel</span>
          <span class="badge badge-neutral">Architecture Scope</span>
        </div>
        <div class="card-subtitle">How enterprise telemetry flows through the cognitive stages of the system</div>
        <div class="grid-4" style="margin-top:16px;">
          <div style="background:var(--color-primary-3); border:1px solid var(--color-primary-8); padding:14px; border-radius:var(--radius-3);">
            <div style="font-size:11px; font-weight:700; color:var(--color-primary-1); text-transform:uppercase;">Stage 1: Sense</div>
            <div style="font-size:13px; font-weight:700; color:var(--color-primary-2); margin:3px 0;">Portfolio Telemetry</div>
            <div style="font-size:12px; color:var(--color-neutral-7);">Continuous ingest of 2.87M contract signals, age distributions, and 90-day modernization activation anomalies.</div>
          </div>
          <div style="background:var(--color-primary-3); border:1px solid var(--color-primary-8); padding:14px; border-radius:var(--radius-3);">
            <div style="font-size:11px; font-weight:700; color:var(--color-primary-1); text-transform:uppercase;">Stage 2: Diagnose</div>
            <div style="font-size:13px; font-weight:700; color:var(--color-primary-2); margin:3px 0;">Variance Attribution</div>
            <div style="font-size:12px; color:var(--color-neutral-7);">Decomposing +22 pt conversion gap between DACH & Iberia into operational levers vs media spend.</div>
          </div>
          <div style="background:var(--color-primary-3); border:1px solid var(--color-primary-8); padding:14px; border-radius:var(--radius-3);">
            <div style="font-size:11px; font-weight:700; color:var(--color-primary-1); text-transform:uppercase;">Stage 3: Prioritise</div>
            <div style="font-size:13px; font-weight:700; color:var(--color-primary-2); margin:3px 0;">Bayesian Ranking</div>
            <div style="font-size:12px; color:var(--color-neutral-7);">Multi-objective optimization scoring EBITDA yield, feasibility match, and dynamic confidence priors.</div>
          </div>
          <div style="background:var(--color-primary-3); border:1px solid var(--color-primary-8); padding:14px; border-radius:var(--radius-3);">
            <div style="font-size:11px; font-weight:700; color:var(--color-primary-1); text-transform:uppercase;">Stage 4: Simulate</div>
            <div style="font-size:13px; font-weight:700; color:var(--color-primary-2); margin:3px 0;">Monte Carlo Allocation</div>
            <div style="font-size:12px; color:var(--color-neutral-7);">Interactive capital curve solver (€0M to €20M) predicting revenue, ROI, and payback frontier in real time.</div>
          </div>
          <div style="background:var(--color-primary-3); border:1px solid var(--color-primary-8); padding:14px; border-radius:var(--radius-3);">
            <div style="font-size:11px; font-weight:700; color:var(--color-primary-1); text-transform:uppercase;">Stage 5: Orchestrate</div>
            <div style="font-size:13px; font-weight:700; color:var(--color-primary-2); margin:3px 0;">Closed-Loop Dispatch</div>
            <div style="font-size:12px; color:var(--color-neutral-7);">Commits decision records to Salesforce, SAP FSM, and Adobe Content Supply Chain for field delivery.</div>
          </div>
          <div style="background:var(--color-primary-3); border:1px solid var(--color-primary-8); padding:14px; border-radius:var(--radius-3);">
            <div style="font-size:11px; font-weight:700; color:var(--color-primary-1); text-transform:uppercase;">Stage 6: Replicate</div>
            <div style="font-size:13px; font-weight:700; color:var(--color-primary-2); margin:3px 0;">Playbook Codification</div>
            <div style="font-size:12px; color:var(--color-neutral-7);">Exports verified plays (EcoDisc, UltraRope, DX Class, One Week Modernization) across peer markets.</div>
          </div>
          <div style="background:var(--color-primary-3); border:1px solid var(--color-primary-8); padding:14px; border-radius:var(--radius-3);">
            <div style="font-size:11px; font-weight:700; color:var(--color-primary-1); text-transform:uppercase;">Stage 7: Optimise</div>
            <div style="font-size:13px; font-weight:700; color:var(--color-primary-2); margin:3px 0;">Day-90 Outcomes</div>
            <div style="font-size:12px; color:var(--color-neutral-7);">Measures pilot delivery (38 quotes, 39.5% conversion, 151 days site downtime saved) and tunes levers.</div>
          </div>
          <div style="background:var(--color-primary-3); border:1px solid var(--color-primary-8); padding:14px; border-radius:var(--radius-3);">
            <div style="font-size:11px; font-weight:700; color:var(--color-primary-1); text-transform:uppercase;">Stage 8: Learn</div>
            <div style="font-size:13px; font-weight:700; color:var(--color-primary-2); margin:3px 0;">Institutional Memory</div>
            <div style="font-size:12px; color:var(--color-neutral-7);">Closes the loop by updating model priors from 0.62 to 0.84, eliminating corporate memory loss.</div>
          </div>
        </div>
      </div>
    </section>

<!-- ========================================================================
         TAB: ENTERPRISE PILOT BLUEPRINT & KONE PREREQUISITES (16-20 WEEKS)
         ======================================================================== -->
    <section class="tab-pane" id="pane-poc">
      <!-- Top Overview Banner -->
      <div class="card" style="background: linear-gradient(135deg, #ffffff 0%, var(--color-primary-3) 100%); border-left: 4px solid var(--color-primary-1);">
        <div class="card-title">
          <span>Enterprise Pilot Blueprint: 16 to 20 Weeks to Production-Grade Deployment</span>
          <span class="badge badge-success">De-risked Enterprise Flight Plan</span>
        </div>
        <div class="card-subtitle">Zero-disruption, governance-first implementation bridging industrial operational technology (OT) and enterprise IT</div>
        <p style="font-size:13.5px; color:var(--text-medium); line-height:1.6; margin-top:8px;">
          Initial estimates of 8 to 10 weeks for an enterprise IoT-to-ERP decisioning pilot are <strong>dangerously optimistic</strong> 
          in an industrial manufacturing and service giant like KONE. Real-world enterprise delivery must account for 
          <strong>Works Council (Betriebsrat §87 BetrVG) co-determination</strong>, <strong>SAP S/4HANA Clean Core transport governance</strong>, 
          <strong>IoT broker Avro schema alignment</strong>, and <strong>cross-system entity resolution</strong> across fragmented asset databases.
        </p>
        <p style="font-size:13.5px; color:var(--text-medium); line-height:1.6; margin-top:6px;">
          This <strong>16-to-20 week phased pilot</strong> is anchored around KONE’s flagship European campaign: 
          <strong>"Life, Upgraded in ONE Week" (ONE Week MOD)</strong>. Targeting <strong>600,000+ aging residential MonoSpace LIS units</strong> 
          across Europe, the pilot focuses on <strong>9,039 addressable units across 5,648 accounts in Italy and Iberia (ITIB)</strong> 
          operating within an isolated European cloud sandbox with <strong>zero modifications to core production ERP</strong>.
        </p>

        <!-- KPI Pill Highlights -->
        <div class="grid-4" style="margin-top:16px;">
          <div style="background:#ffffff; border:1px solid var(--color-primary-8); padding:14px; border-radius:var(--radius-3); text-align:center; box-shadow:0 2px 6px rgba(0,0,0,0.03);">
            <div style="font-size:26px; font-weight:800; color:var(--color-primary-1); font-family:var(--font-font-5);">16 – 20 Wks</div>
            <div style="font-size:11px; font-weight:700; color:var(--color-primary-2); text-transform:uppercase; margin-top:4px;">Enterprise Flight Plan</div>
          </div>
          <div style="background:#ffffff; border:1px solid var(--color-primary-8); padding:14px; border-radius:var(--radius-3); text-align:center; box-shadow:0 2px 6px rgba(0,0,0,0.03);">
            <div style="font-size:26px; font-weight:800; color:var(--color-primary-1); font-family:var(--font-font-5);">9,039 Units</div>
            <div style="font-size:11px; font-weight:700; color:var(--color-primary-2); text-transform:uppercase; margin-top:4px;">ITIB Pilot Cohort (MonoSpace LIS)</div>
          </div>
          <div style="background:#ffffff; border:1px solid var(--color-primary-8); padding:14px; border-radius:var(--radius-3); text-align:center; box-shadow:0 2px 6px rgba(0,0,0,0.03);">
            <div style="font-size:26px; font-weight:800; color:var(--color-primary-1); font-family:var(--font-font-5);">4 – 6 hrs/wk</div>
            <div style="font-size:11px; font-weight:700; color:var(--color-primary-2); text-transform:uppercase; margin-top:4px;">Blended KONE SME Ask</div>
          </div>
          <div style="background:#ffffff; border:1px solid var(--color-primary-8); padding:14px; border-radius:var(--radius-3); text-align:center; box-shadow:0 2px 6px rgba(0,0,0,0.03);">
            <div style="font-size:26px; font-weight:800; color:#10b981; font-family:var(--font-font-5);">Zero</div>
            <div style="font-size:11px; font-weight:700; color:var(--color-primary-2); text-transform:uppercase; margin-top:4px;">Core ERP Transport Risks</div>
          </div>
        </div>
      </div>

      <!-- ========================================================================
           WHY 8-10 WEEKS IS SUPER OPTIMISTIC: ENTERPRISE REALITY CHECK
           ======================================================================== -->
      <div class="card" style="margin-top:20px; border-left:4px solid #ef4444;">
        <div class="card-title">
          <span>Enterprise Reality Check: Why 8–10 Weeks Fails in Industrial IT/OT Environments</span>
          <span class="badge" style="background:#fee2e2; color:#991b1b;">Architectural Truth</span>
        </div>
        <div class="card-subtitle">Five critical enterprise bottlenecks that make 8–10 weeks an unrealistic risk for KONE</div>

        <div class="grid-2" style="margin-top:16px;">
          <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
            <div style="font-size:14px; font-weight:700; color:var(--color-primary-2); display:flex; align-items:center; gap:8px;">
              <span style="color:#ef4444;">&times;</span> Naive 8–10 Week SaaS Assumption
            </div>
            <ul style="font-size:12.5px; color:var(--text-medium); line-height:1.6; margin-top:10px; padding-left:18px;">
              <li>Assumes instant, self-service REST API access to SAP S/4HANA work orders and customer records.</li>
              <li>Assumes clean, standardized IoT telemetry with uniform schema across all 2.87M connected elevators.</li>
              <li>Ignores European labor laws and treats field technician telemetry as freely mineable productivity data.</li>
              <li>Assumes elevator serial numbers match 1:1 between maintenance contracts, telemetry gateways, and CRM accounts.</li>
              <li>Assumes local marketing frontlines immediately adopt auto-generated English marketing collateral.</li>
            </ul>
          </div>

          <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
            <div style="font-size:14px; font-weight:700; color:var(--color-primary-2); display:flex; align-items:center; gap:8px;">
              <span style="color:#10b981;">&#10003;</span> The 16–20 Week Enterprise Reality
            </div>
            <ul style="font-size:12.5px; color:var(--text-medium); line-height:1.6; margin-top:10px; padding-left:18px;">
              <li><strong>SAP Clean Core & Change Advisory Board (CAB):</strong> Extracting data via OData v4 / CDS views requires security reviews, Basis transports, and corporate firewall rules (Lead time: 4–6 weeks).</li>
              <li><strong>Heterogeneous IoT Gateways:</strong> Ingesting KONE 24/7 Connected Services Kafka/MQTT streams across KRM and 24/7 Connect boxes requires Avro schema registry access and timestamp de-jittering (Lead time: 4–6 weeks).</li>
              <li><strong>Works Council Co-Determination (§87 BetrVG):</strong> Strict legal protections prevent tracking technician dispatch. Requires certifying the <em>Technician Privacy Airlock</em> with union legal counsel (Lead time: 4–6 weeks).</li>
              <li><strong>Cadastral Entity Resolution:</strong> Merging fractured municipal address registers with SAP Functional Locations and Salesforce accounts across 9,039 assets requires iterative fuzzy linkage (Lead time: 3–4 weeks).</li>
              <li><strong>Adobe Content Supply Chain & Frontline Hub:</strong> Ingesting Tridion/AEM modular assets, localizing Spanish/Italian copy, and coordinating agency ad-ops (Omnicom/Virta) requires phased alignment (Lead time: 3–4 weeks).</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- ========================================================================
           SPOTLIGHT SAMPLE USE CASE: KONE "LIFE, UPGRADED IN ONE WEEK" (ONE WEEK MOD)
           ======================================================================== -->
      <div class="card" style="margin-top:20px; border-top:3px solid var(--color-primary-1);">
        <div class="card-title">
          <span>Sample Pilot Usecase: KONE "Life, Upgraded in ONE Week" (ONE Week MOD)</span>
          <span class="badge badge-primary">European Marketing Package</span>
        </div>
        <div class="card-subtitle">End-to-end alignment with KONE's residential partial modernization campaign charter (Owner: Lingkai Shao, PM: Phuong Dinh)</div>

        <!-- Campaign Strategic Context Grid -->
        <div class="grid-3" style="margin-top:16px;">
          <div style="background:var(--color-primary-3); border:1px solid var(--color-primary-8); border-radius:var(--radius-3); padding:16px;">
            <div style="font-size:12px; font-weight:700; color:var(--color-primary-1); text-transform:uppercase;">The Market Opportunity</div>
            <div style="font-size:18px; font-weight:800; color:var(--color-primary-2); margin-top:4px;">600,000+ Aging Units</div>
            <p style="font-size:12.5px; color:var(--text-medium); line-height:1.55; margin-top:8px;">
              Out of 10M+ aging elevators across Europe, over <strong>600k residential MonoSpace LIS (Lift in Shaft) units</strong> 
              are &gt;15 years old with &le;7 floors. The European campaign identifies <strong>20,061 addressable priority units</strong> across 6 frontlines.
            </p>
          </div>

          <div style="background:var(--color-primary-3); border:1px solid var(--color-primary-8); border-radius:var(--radius-3); padding:16px;">
            <div style="font-size:12px; font-weight:700; color:var(--color-primary-1); text-transform:uppercase;">The Customer Nightmare</div>
            <div style="font-size:18px; font-weight:800; color:var(--color-primary-2); margin-top:4px;">Months of Shutdown</div>
            <p style="font-size:12.5px; color:var(--text-medium); line-height:1.55; margin-top:8px;">
              Historically, full modernization leaves residents stranded for 4 to 8 weeks, dragging customer satisfaction down to a 
              <strong>49% baseline</strong>. The ONE Week MOD promise guarantees completion in <strong>&le; 7 days of downtime</strong>, targeting <strong>70% CSAT</strong>.
            </p>
          </div>

          <div style="background:var(--color-primary-3); border:1px solid var(--color-primary-8); border-radius:var(--radius-3); padding:16px;">
            <div style="font-size:12px; font-weight:700; color:var(--color-primary-1); text-transform:uppercase;">Core Verified Claims</div>
            <div style="font-size:18px; font-weight:800; color:var(--color-primary-2); margin-top:4px;">74% Energy &bull; 80% Issues</div>
            <p style="font-size:12.5px; color:var(--text-medium); line-height:1.55; margin-top:8px;">
              Anchored by KONE EcoDisc gearless drive (up to <strong>74% energy savings</strong>), 
              <strong>80% of faults detected proactively</strong> via KONE 24/7 Connected Services, and 
              <strong>+23% acoustic noise reduction</strong> for penthouse residents.
            </p>
          </div>
        </div>

        <!-- Frontline Opportunity Matrix & Media Budget -->
        <div style="margin-top:20px;">
          <div style="font-size:14px; font-weight:700; color:var(--color-primary-2); margin-bottom:10px;">
            Frontline Opportunity Sizing & Omnichannel Media Allocation (From Campaign Package)
          </div>
          <table class="data-table">
            <thead>
              <tr>
                <th>Frontline / Region</th>
                <th>Addressable MonoSpace Units</th>
                <th>Target Accounts</th>
                <th>Campaign Media Budget</th>
                <th>Pilot Scope & Strategic Focus</th>
              </tr>
            </thead>
            <tbody>
              <tr style="background:#eff6ff;">
                <td><strong>ITIB (Italy & Iberia)</strong></td>
                <td><span class="badge badge-primary">9,039 Units</span></td>
                <td>5,648 Accounts</td>
                <td><strong>€120,000</strong></td>
                <td><strong>Primary 16–20 Wk Pilot Cohort:</strong> High residential density, aging MonoSpace fleet in Madrid, Barcelona, Milan, and Rome.</td>
              </tr>
              <tr>
                <td><strong>DACH (Germany, Austria, Switzerland)</strong></td>
                <td>2,470 Units</td>
                <td>1,840 Accounts</td>
                <td>€125,000</td>
                <td>Phase 2 Scale-out: High commercial FM governance, stringent energy efficiency certification requirements.</td>
              </tr>
              <tr>
                <td><strong>GIN (Great Britain & Ireland)</strong></td>
                <td>4,804 Units</td>
                <td>3,120 Accounts</td>
                <td>€135,000</td>
                <td>Phase 2 Scale-out: Focus on pure lost accounts (+5 yrs lost service) in urban multi-family housing.</td>
              </tr>
              <tr>
                <td><strong>FBL (France, Belgium, Luxembourg)</strong></td>
                <td>2,070 Units</td>
                <td>1,450 Accounts</td>
                <td>€125,000</td>
                <td>Phase 2 Scale-out: Focus on condominium co-ownership boards (Syndics de copropriété).</td>
              </tr>
              <tr>
                <td><strong>NORD (Nordics)</strong></td>
                <td>938 Units</td>
                <td>680 Accounts</td>
                <td>€110,000</td>
                <td>Phase 3 Scale-out: 24/7 Connected Services penetration &gt;85%; focus on regenerative drive upgrade.</td>
              </tr>
              <tr>
                <td><strong>EEM (Eastern Europe & Mediterranean)</strong></td>
                <td>740 Units</td>
                <td>510 Accounts</td>
                <td>€90,000</td>
                <td>Phase 3 Scale-out: Focus on cost-sensitive residential cooperatives.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Omnichannel Activation & Target Personas -->
        <div class="grid-2" style="margin-top:20px;">
          <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
            <div style="font-size:14px; font-weight:700; color:var(--color-primary-2); margin-bottom:8px;">
              Dual Target Personas & Customer Journeys
            </div>
            <div style="margin-bottom:12px;">
              <div style="font-size:13px; font-weight:700; color:var(--color-primary-1);">1. Facility Managers & Professional Building Operators</div>
              <div style="font-size:12px; color:var(--text-medium); line-height:1.55; margin-top:2px;">
                <strong>Pain Points:</strong> Tenant complaint floods, unpredictable OPEX repair spikes, vendor accountability.<br>
                <strong>ADS Solution:</strong> Predicts breakdown probability before next maintenance cycle; generates tailored technical ROI brief comparing 5-year repair costs vs. ONE Week MOD CAPEX amortized with EcoDisc energy savings.
              </div>
            </div>
            <div>
              <div style="font-size:13px; font-weight:700; color:var(--color-primary-1);">2. Building Owners & Homeowners Associations (HOA / Condominium)</div>
              <div style="font-size:12px; color:var(--text-medium); line-height:1.55; margin-top:2px;">
                <strong>Pain Points:</strong> Fear of elderly residents climbing stairs during months of shutdown, budget disputes.<br>
                <strong>ADS Solution:</strong> Generates resident-friendly lobby battlecards highlighting guaranteed &le;7-day turnaround, safety compliance, and property valuation appreciation.
              </div>
            </div>
          </div>

          <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
            <div style="font-size:14px; font-weight:700; color:var(--color-primary-2); margin-bottom:8px;">
              Omnichannel Campaign Orchestration & Media Mix
            </div>
            <ul style="font-size:12.5px; color:var(--text-medium); line-height:1.6; padding-left:18px;">
              <li><strong>Meta (Facebook/Instagram):</strong> Advantage+ 1:1 feeds, 9:16 vertical video & stories highlighting homeowner relief and quick 1-week turnaround.</li>
              <li><strong>LinkedIn Ads:</strong> Sponsored Content & InMail targeting professional FMs and HOA board presidents.</li>
              <li><strong>YouTube VRC:</strong> 30s emotional narrative ("Life shouldn't pause for an elevator"), 15s core promise, 6s bumpers.</li>
              <li><strong>Spotify Audio:</strong> 8s, 12s, 30s spots targeting commuting apartment owners during morning drive-time.</li>
              <li><strong>Google PMAX & Paid Search:</strong> Intent capture for keywords like <em>elevator modernization cost</em>, <em>residential lift replacement</em>.</li>
              <li><strong>Account-Based Advertising (ABA):</strong> IP & domain targeting via Dun & Bradstreet / CRM lists for commercial real estate portfolios.</li>
              <li><strong>Field Technician Leave-Behinds:</strong> Physical door-hangers and customized lobby cards placed by technicians during routine maintenance on high-vulnerability units.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- ========================================================================
           THE 16-20 WEEK ENTERPRISE PILOT FLIGHT PLAN (4 PHASES / 8 SPRINTS)
           ======================================================================== -->
      <div class="card" style="margin-top:20px;">
        <div class="card-title">
          <span>The 16–20 Week Enterprise Pilot Flight Plan (4 Phased Horizons / 8 Sprints)</span>
          <span class="badge badge-primary">Battle-Tested Delivery Roadmap</span>
        </div>
        <div class="card-subtitle">Detailed breakdown of sprint objectives, technical activities, and milestone exit deliverables</div>

        <div style="position:relative; margin-top:24px;">

          <!-- PHASE 0: WEEKS 1-4 -->
          <div style="display:flex; gap:20px; margin-bottom:24px;">
            <div style="width:150px; flex-shrink:0; font-size:13px; font-weight:700; color:var(--color-primary-1); text-align:right;">
              Weeks 1 – 4<br>
              <span class="badge badge-neutral" style="margin-top:4px;">Phase 0: Sprints 1–2</span>
            </div>
            <div style="width:2px; background:var(--color-primary-9); position:relative;">
              <div style="position:absolute; top:0; left:-5px; width:12px; height:12px; border-radius:50%; background:var(--color-primary-1);"></div>
            </div>
            <div style="flex:1; background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="font-size:15px; font-weight:700; color:var(--color-primary-2);">Cloud Sandbox Tenancy, Works Council Privacy Airlock & Initial Ingestion</div>
                <span class="badge badge-neutral">Security & Legal Foundations</span>
              </div>
              <div style="font-size:12.5px; color:var(--color-neutral-6); margin:4px 0 10px 0;">Goal: Establish isolated EU cloud tenant, execute legal co-determination agreements, and ingest baseline data dumps.</div>
              <ul style="font-size:13px; color:var(--text-medium); line-height:1.6; padding-left:20px;">
                <li>Provision dedicated European cloud tenant in AWS Frankfurt (eu-central-1) or Azure West Europe with KMS envelope encryption.</li>
                <li>Execute GDPR Article 28 DPA and DPIA with KONE Data Privacy Officer.</li>
                <li>Formalize European Works Council (Betriebsrat §87 BetrVG) agreement: implement the <em>Technician Anonymization Airlock</em> stripping individual technician IDs and routing leads exclusively to branch depot pools.</li>
                <li>Receive initial batch data drops: 24 months of SAP PM work orders, 90-day IoT telemetry sample, and Salesforce CRM accounts for the 4,008 Iberian MonoSpace units.</li>
                <li>Establish data schema dictionary mapping KONE legacy tables to the canonical Golden Record schema.</li>
              </ul>
              <div style="margin-top:10px; padding:8px 12px; background:var(--color-primary-3); border-radius:var(--radius-2); font-size:12px; color:var(--color-primary-18);">
                <strong>Milestone 0 Deliverable:</strong> Provisioned sovereign cloud sandbox, signed GDPR & Works Council airlock agreements, and validated data drops for 4,008 Iberian pilot assets.
              </div>
            </div>
          </div>

          <!-- PHASE 1: WEEKS 5-8 -->
          <div style="display:flex; gap:20px; margin-bottom:24px;">
            <div style="width:150px; flex-shrink:0; font-size:13px; font-weight:700; color:var(--color-primary-1); text-align:right;">
              Weeks 5 – 8<br>
              <span class="badge badge-neutral" style="margin-top:4px;">Phase 1: Sprints 3–4</span>
            </div>
            <div style="width:2px; background:var(--color-primary-9); position:relative;">
              <div style="position:absolute; top:0; left:-5px; width:12px; height:12px; border-radius:50%; background:var(--color-primary-1);"></div>
            </div>
            <div style="flex:1; background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="font-size:15px; font-weight:700; color:var(--color-primary-2);">Entity Resolution, Cadastral Reconciliation & ONE Week MOD Eligibility</div>
                <span class="badge badge-neutral">Data Stitching Layer</span>
              </div>
              <div style="font-size:12.5px; color:var(--color-neutral-6); margin:4px 0 10px 0;">Goal: Reconcile fractured keys across IoT, SAP Plant Maintenance, and Salesforce CRM; filter ONE Week MOD candidate cohort.</div>
              <ul style="font-size:13px; color:var(--text-medium); line-height:1.6; padding-left:20px;">
                <li>Execute deterministic and fuzzy graph linkage: IoT Gateway MAC ↔ SAP Functional Location ↔ Salesforce Building Asset ID.</li>
                <li>Stitch building hierarchy: Building Cadastral ID ↔ Property Management Account ↔ Portfolio Parent across Madrid and Barcelona.</li>
                <li>Apply engineering eligibility filters for the <strong>ONE Week MOD</strong> campaign: MonoSpace LIS units, &ge;15 years old, &le;7 floors, residential shaft dimensions, and motor bedplate compatibility.</li>
                <li>Segment the 9,039 ITIB assets into active maintenance contracts nearing renewal vs. pure lost accounts (+5 yrs lost service).</li>
                <li>Quantify entity resolution match rate and flag edge cases for KONE SME validation.</li>
              </ul>
              <div style="margin-top:10px; padding:8px 12px; background:var(--color-primary-3); border-radius:var(--radius-2); font-size:12px; color:var(--color-primary-18);">
                <strong>Milestone 1 Deliverable:</strong> Unified Golden Record Entity Graph covering &ge;88% of target ITIB assets with verified ONE Week MOD engineering eligibility flags.
              </div>
            </div>
          </div>

          <!-- PHASE 2: WEEKS 9-12 -->
          <div style="display:flex; gap:20px; margin-bottom:24px;">
            <div style="width:150px; flex-shrink:0; font-size:13px; font-weight:700; color:var(--color-primary-1); text-align:right;">
              Weeks 9 – 12<br>
              <span class="badge badge-neutral" style="margin-top:4px;">Phase 2: Sprints 5–6</span>
            </div>
            <div style="width:2px; background:var(--color-primary-9); position:relative;">
              <div style="position:absolute; top:0; left:-5px; width:12px; height:12px; border-radius:50%; background:var(--color-primary-1);"></div>
            </div>
            <div style="flex:1; background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="font-size:15px; font-weight:700; color:var(--color-primary-2);">Predictive Modeling, Bayesian Variance Diagnosis & Monte Carlo Optimization</div>
                <span class="badge badge-neutral">Intelligence Layer</span>
              </div>
              <div style="font-size:12.5px; color:var(--color-neutral-6); margin:4px 0 10px 0;">Goal: Calibrate churn prediction, variance diagnostics, and multi-objective budget simulation with real frontline operational data.</div>
              <ul style="font-size:13px; color:var(--text-medium); line-height:1.6; padding-left:20px;">
                <li>Train Equipment Vulnerability Index (EVI) on historical breakdown patterns, door cycle wear, and ride vibration telemetry.</li>
                <li>Calibrate Commercial Churn Propensity (CCP) incorporating contract renewal dates, competitor pricing, and historical service callouts.</li>
                <li>Encode engineering and logistics constraints for the ONE Week MOD package: 7-day technician labor allocation, depot parts availability, and regional installation bandwidth.</li>
                <li>Calibrate Monte Carlo budget simulator to balance digital media spend (Meta, LinkedIn, YouTube, Spotify) vs. field technician leave-behinds.</li>
                <li>Conduct rigorous offline backtesting against 24 months of historical contract cancellations and modernization wins.</li>
              </ul>
              <div style="margin-top:10px; padding:8px 12px; background:var(--color-primary-3); border-radius:var(--radius-2); font-size:12px; color:var(--color-primary-18);">
                <strong>Milestone 2 Deliverable:</strong> Calibrated predictive model achieving ROC-AUC &ge; 0.84 on historical churn holdout and 10,000-run Monte Carlo simulation runtime under 2.5 seconds.
              </div>
            </div>
          </div>

          <!-- PHASE 3: WEEKS 13-16 -->
          <div style="display:flex; gap:20px; margin-bottom:24px;">
            <div style="width:150px; flex-shrink:0; font-size:13px; font-weight:700; color:var(--color-primary-1); text-align:right;">
              Weeks 13 – 16<br>
              <span class="badge badge-neutral" style="margin-top:4px;">Phase 3: Sprints 7–8</span>
            </div>
            <div style="width:2px; background:var(--color-primary-9); position:relative;">
              <div style="position:absolute; top:0; left:-5px; width:12px; height:12px; border-radius:50%; background:var(--color-primary-1);"></div>
            </div>
            <div style="flex:1; background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="font-size:15px; font-weight:700; color:var(--color-primary-2);">Adobe Content Supply Chain, CRM Webhooks & Closed-Loop Field Dispatch</div>
                <span class="badge badge-neutral">Experience & Action Layer</span>
              </div>
              <div style="font-size:12.5px; color:var(--color-neutral-6); margin:4px 0 10px 0;">Goal: Connect the decisioning UI to Adobe DAM modular assets, automated battlecard synthesis, and bi-directional CRM dispatch.</div>
              <ul style="font-size:13px; color:var(--text-medium); line-height:1.6; padding-left:20px;">
                <li>Deploy full glassmorphism Assisted Decisioning System UI connected to live sandbox REST API endpoints.</li>
                <li>Connect Adobe modular ingredients generator to synthesize tailored modernization battlecards (EcoDisc, DX Class, UltraRope) based on building asset age and vibration scores.</li>
                <li>Ingest ONE Week MOD modular creative components from SDL Tridion / AEM Assets with localized Spanish and Italian copy.</li>
                <li>Implement automated battlecard synthesis injecting verified engineering claims (74% energy savings, 70% satisfaction target, 80% proactive issue detection) with zero hallucinations.</li>
                <li>Configure Stage 5 bidirectional dispatch webhooks to Salesforce Opportunity staging and SAP FSM service tickets.</li>
                <li>Conduct frontline enablement workshops with 15 Iberian sales representatives and field service supervisors in Madrid and Barcelona.</li>
              </ul>
              <div style="margin-top:10px; padding:8px 12px; background:var(--color-primary-3); border-radius:var(--radius-2); font-size:12px; color:var(--color-primary-18);">
                <strong>Milestone 3 Deliverable:</strong> Fully operational interactive decisioning platform with live scenario modeling, automated asset generation, and outbound dispatch webhooks.
              </div>
            </div>
          </div>

          <!-- PHASE 4: WEEKS 17-20 -->
          <div style="display:flex; gap:20px;">
            <div style="width:150px; flex-shrink:0; font-size:13px; font-weight:700; color:#10b981; text-align:right;">
              Weeks 17 – 20<br>
              <span class="badge badge-success" style="margin-top:4px;">Phase 4: Live Activation</span>
            </div>
            <div style="width:2px; background:var(--color-primary-9); position:relative;">
              <div style="position:absolute; top:0; left:-5px; width:12px; height:12px; border-radius:50%; background:#10b981;"></div>
            </div>
            <div style="flex:1; background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="font-size:15px; font-weight:700; color:var(--color-primary-2);">Live Market Intervention, Value Proof & Executive C-Suite Readout</div>
                <span class="badge badge-success">Business Readout & Scale-Out</span>
              </div>
              <div style="font-size:12.5px; color:var(--color-neutral-6); margin:4px 0 10px 0;">Goal: Execute live field intervention across 50 prioritized accounts, measure pipeline conversion, and present ROI.</div>
              <ul style="font-size:13px; color:var(--text-medium); line-height:1.6; padding-left:20px;">
                <li>Launch 30-day live field intervention across 50 prioritized commercial and residential accounts in Madrid and Barcelona.</li>
                <li>Dispatch personalized ONE Week MOD proposals, digital ads (Meta, LinkedIn, YouTube, Spotify), and technician leave-behind cards.</li>
                <li>Track Day-30 leading indicators: quote request velocity, building manager engagement, and field technician lead capture rate.</li>
                <li>Compile Executive C-Suite Readout detailing verified pipeline generation, payback timeline, and scale-out business case for DACH and Nordics.</li>
                <li>Deliver final architecture blueprint and multi-year production roadmap to KONE Executive Committee.</li>
              </ul>
              <div style="margin-top:10px; padding:8px 12px; background:#ecfdf5; border:1px solid #10b981; border-radius:var(--radius-2); font-size:12px; color:#065f46;">
                <strong>Milestone 4 Deliverable:</strong> Executive C-Suite Readout presentation, verified pilot pipeline ROI report, and signed Phase 2 scale-out plan.
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Quantitative POC Exit Criteria Scorecard -->
      <div class="card" style="margin-top:20px;">
        <div class="card-title">
          <span>Enterprise Pilot Go / No-Go Decision Gate Scorecard</span>
          <span class="badge badge-neutral">Pre-Agreed Acceptance Criteria</span>
        </div>
        <div class="card-subtitle">Measurable, audit-ready benchmarks required to transition from pilot to pan-European production</div>

        <table class="data-table" style="margin-top:16px;">
          <thead>
            <tr>
              <th style="width:22%;">Success Dimension</th>
              <th style="width:30%;">Metric / KPI</th>
              <th style="width:18%;">Pilot Target Threshold</th>
              <th style="width:30%;">Verification Method</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Entity Resolution</strong></td>
              <td>Automated linkage of IoT MAC ↔ SAP Functional Location ↔ Salesforce Asset</td>
              <td><span class="badge badge-success">&ge; 88% Accuracy</span></td>
              <td>Audited sample of 500 equipment records verified against physical site registers.</td>
            </tr>
            <tr>
              <td><strong>Predictive Precision</strong></td>
              <td>Equipment Vulnerability Index (EVI) churn and breakdown prediction</td>
              <td><span class="badge badge-success">ROC-AUC &ge; 0.84</span></td>
              <td>Backtested against 24 months of historical unscheduled callouts and contract cancellations.</td>
            </tr>
            <tr>
              <td><strong>Simulation Latency</strong></td>
              <td>10,000-iteration Monte Carlo budget allocation with capacity constraints</td>
              <td><span class="badge badge-success">&lt; 2.5 Seconds</span></td>
              <td>Automated performance load test on Ray distributed compute cluster.</td>
            </tr>
            <tr>
              <td><strong>Content Personalization</strong></td>
              <td>Automated generation of localized building-specific modernization battlecards</td>
              <td><span class="badge badge-success">100% Citation Accuracy</span></td>
              <td>Deterministic schema validation preventing hallucinations; zero ungrounded safety specs.</td>
            </tr>
            <tr>
              <td><strong>Commercial Usability</strong></td>
              <td>Sales & Field Operations user satisfaction (CSAT)</td>
              <td><span class="badge badge-success">&ge; 4.3 / 5.0</span></td>
              <td>Structured post-pilot survey across 15 Iberian sales reps and service supervisors.</td>
            </tr>
            <tr>
              <td><strong>Governance & InfoSec</strong></td>
              <td>Works Council (Betriebsrat) and GDPR compliance sign-off</td>
              <td><span class="badge badge-success">100% Sign-Off</span></td>
              <td>Formal sign-off by KONE Data Privacy Officer and Works Council representatives.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- What is Required from KONE (The Comprehensive Ask Checklist) -->
      <div class="card" style="margin-top:20px; border-top: 3px solid var(--color-primary-1);">
        <div class="card-title">
          <span>What is Required from KONE: The 4-Pillar Prerequisite Checklist (16–20 Wk Horizon)</span>
          <span class="badge badge-primary">Client Commitments</span>
        </div>
        <div class="card-subtitle">Transparent inventory of data extracts, infrastructure access, SME time, and governance sign-offs needed from KONE</div>

        <div class="grid-2" style="margin-top:20px;">
          <!-- Pillar A: Data Assets -->
          <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:10px;">
              <div style="width:28px; height:28px; border-radius:6px; background:var(--color-primary-3); display:flex; align-items:center; justify-content:center; color:var(--color-primary-1); font-weight:700;">A</div>
              <div style="font-size:15px; font-weight:700; color:var(--color-primary-2);">Data Extracts & API Access Prerequisites</div>
            </div>
            <p style="font-size:12.5px; color:var(--color-neutral-6); margin-bottom:12px;">Delivered as static CSV/Parquet drops or read-only database views for pilot cohort:</p>
            <ul style="font-size:13px; color:var(--text-medium); line-height:1.6; padding-left:18px;">
              <li><strong>24-Month Maintenance Work Orders:</strong> Export from SAP PM/CS including Equipment ID, callout timestamps, failure reason codes, parts consumed, and downtime duration.</li>
              <li><strong>IoT Telemetry Sample (30–90 Days):</strong> Daily trip counts, door cycle counts, brake wear indicators, and leveling fault codes for ~5,000 units in pilot market.</li>
              <li><strong>Contract Master Data:</strong> SAP S/4HANA active maintenance contracts (contract tier, start/end date, annual fee, penalty SLA, equipment vintage).</li>
              <li><strong>Salesforce CRM Hierarchy:</strong> Account ID, parent holding company, facility manager contact title, and open modernization pipeline.</li>
              <li><strong>ONE Week MOD Campaign Collateral:</strong> Tridion / Adobe AEM modular assets, technical cut-sheets (MonoSpace LIS, EcoDisc, DX Class), and localized Spanish/Italian copy.</li>
            </ul>
          </div>

          <!-- Pillar B: Cloud & Environment -->
          <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:10px;">
              <div style="width:28px; height:28px; border-radius:6px; background:var(--color-primary-3); display:flex; align-items:center; justify-content:center; color:var(--color-primary-1); font-weight:700;">B</div>
              <div style="font-size:15px; font-weight:700; color:var(--color-primary-2);">Cloud & Infrastructure Prerequisites</div>
            </div>
            <p style="font-size:12.5px; color:var(--color-neutral-6); margin-bottom:12px;">Provisioned in dedicated, secure European zone:</p>
            <ul style="font-size:13px; color:var(--text-medium); line-height:1.6; padding-left:18px;">
              <li><strong>Cloud Sandbox Tenancy:</strong> Provisioning of a dedicated AWS resource group (Frankfurt eu-central-1) or Azure subscription (West Europe). Alternatively, Cognizant can host the sandbox in an isolated sovereign tenant.</li>
              <li><strong>Secure Transfer Mechanism:</strong> S3 bucket / Azure Blob container with KMS encryption and static IP whitelisting for automated batch data transfer.</li>
              <li><strong>SSO / SAML User Authentication:</strong> Configuration of KONE Azure AD (Entra ID) / Okta test user group for 15 named pilot users (commercial reps, service managers).</li>
              <li><strong>Network Egress Clearance:</strong> Whitelisting of secure outbound HTTPS webhooks from sandbox to Salesforce sandbox / SAP BTP test endpoints.</li>
            </ul>
          </div>

          <!-- Pillar C: SME Time Commitments -->
          <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:10px;">
              <div style="width:28px; height:28px; border-radius:6px; background:var(--color-primary-3); display:flex; align-items:center; justify-content:center; color:var(--color-primary-1); font-weight:700;">C</div>
              <div style="font-size:15px; font-weight:700; color:var(--color-primary-2);">KONE SME Team Time Commitments (16–20 Wk Sizing)</div>
            </div>
            <p style="font-size:12.5px; color:var(--color-neutral-6); margin-bottom:12px;">Sized to minimize burden on KONE business-as-usual operations:</p>
            <table style="width:100%; font-size:12px; border-collapse:collapse;">
              <thead>
                <tr style="border-bottom:1px solid var(--color-neutral-2); text-align:left; color:var(--color-neutral-7);">
                  <th style="padding:4px 0;">Role</th>
                  <th style="padding:4px 0;">Commitment</th>
                  <th style="padding:4px 0;">Key Involvement</th>
                </tr>
              </thead>
              <tbody style="color:var(--text-medium);">
                <tr style="border-bottom:1px solid #f0f0f0;">
                  <td style="padding:6px 0;"><strong>Executive Sponsor</strong> (VP Commercial)</td>
                  <td>1 hr / 2 weeks</td>
                  <td>Bi-weekly steering committee & milestone approvals</td>
                </tr>
                <tr style="border-bottom:1px solid #f0f0f0;">
                  <td style="padding:6px 0;"><strong>Lead Solution Architect</strong></td>
                  <td>2 hrs / week</td>
                  <td>Clean Core compliance, API governance, security</td>
                </tr>
                <tr style="border-bottom:1px solid #f0f0f0;">
                  <td style="padding:6px 0;"><strong>Data / IoT Platform Engineer</strong></td>
                  <td>4 hrs/wk (W1–4), 1.5 hrs/wk after</td>
                  <td>Data extract support, schema validation</td>
                </tr>
                <tr style="border-bottom:1px solid #f0f0f0;">
                  <td style="padding:6px 0;"><strong>Regional Marketing Lead</strong> (ITIB)</td>
                  <td>2 hrs / week</td>
                  <td>ONE Week MOD scenario calibration, localized copy</td>
                </tr>
                <tr style="border-bottom:1px solid #f0f0f0;">
                  <td style="padding:6px 0;"><strong>Field Service Manager</strong></td>
                  <td>2 hrs / week (W13–20)</td>
                  <td>Technician lead workflow review & pilot feedback</td>
                </tr>
                <tr>
                  <td style="padding:6px 0;"><strong>InfoSec / Privacy Officer</strong></td>
                  <td>4 hrs total (W2–4)</td>
                  <td>DPIA & Works Council anonymization sign-off</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Pillar D: Governance & Legal -->
          <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:10px;">
              <div style="width:28px; height:28px; border-radius:6px; background:var(--color-primary-3); display:flex; align-items:center; justify-content:center; color:var(--color-primary-1); font-weight:700;">D</div>
              <div style="font-size:15px; font-weight:700; color:var(--color-primary-2);">Governance, Legal & Works Council Alignment</div>
            </div>
            <p style="font-size:12.5px; color:var(--color-neutral-6); margin-bottom:12px;">Fast-tracked regulatory and labor compliance:</p>
            <ul style="font-size:13px; color:var(--text-medium); line-height:1.6; padding-left:18px;">
              <li><strong>GDPR Article 28 DPA:</strong> Execution of standard Data Processing Agreement designating Cognizant as processor for the pilot tenant.</li>
              <li><strong>Works Council (Betriebsrat) Charter:</strong> Formal approval of the <em>Technician Anonymization Airlock</em> confirming that technician IDs are stripped, individual performance monitoring is cryptographically blocked, and lead dispatch is assigned strictly to branch depot pools.</li>
              <li><strong>Data Retention & Destruction Agreement:</strong> Formal protocol specifying that all pilot extracts are permanently wiped upon completion of Phase 1 unless transitioned into production.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         TAB: ALL SYSTEM, INFRASTRUCTURE & OPS DEPENDENCIES
         ======================================================================== -->
    <section class="tab-pane" id="pane-deps">
      <!-- Top Overview Banner -->
      <div class="card" style="background: linear-gradient(135deg, #ffffff 0%, var(--color-primary-3) 100%); border-left: 4px solid var(--color-primary-1);">
        <div class="card-title">
          <span>Comprehensive System, Infrastructure & Organizational Dependencies</span>
          <span class="badge badge-primary">Enterprise Integration Blueprint</span>
        </div>
        <div class="card-subtitle">Exhaustive mapping of technical, upstream system, infrastructure, security, and human dependencies</div>
        <p style="font-size:13.5px; color:var(--text-medium); line-height:1.6; margin-top:8px;">
          Deploying the KONE Assisted Decisioning System requires orchestrated alignment across five enterprise boundaries: 
          <strong>upstream source systems, cloud data platforms, machine learning/LLM runtimes, network security perimeters, and organizational labor compliance</strong>. 
          The architecture employs decoupling patterns (event mesh, CDC, asynchronous message queues, and fallback caches) so that no single upstream dependency can block the decision engine.
        </p>
      </div>

      <!-- 4 Pillars of Dependencies -->
      <div class="grid-2" style="margin-top:20px;">
        <!-- Dependency Pillar 1 -->
        <div class="card">
          <div class="card-title">
            <span>1. Core Enterprise System Dependencies</span>
            <span class="badge badge-primary">Data Sources</span>
          </div>
          <div class="card-subtitle">Source of truth systems providing commercial, operational, and telemetry inputs</div>

          <table style="width:100%; font-size:12.5px; margin-top:12px; border-collapse:collapse;">
            <thead>
              <tr style="border-bottom:2px solid var(--color-neutral-2); text-align:left; color:var(--color-neutral-8);">
                <th style="padding:6px 0;">System</th>
                <th style="padding:6px 0;">Protocol / Interface</th>
                <th style="padding:6px 0;">Frequency</th>
                <th style="padding:6px 0;">Fallback If Unavailable</th>
              </tr>
            </thead>
            <tbody style="color:var(--text-medium);">
              <tr style="border-bottom:1px solid #f0f0f0;">
                <td style="padding:8px 0;"><strong>SAP S/4HANA / ECC</strong><br><span style="font-size:11px; color:var(--color-neutral-6);">PM, CS, SD Modules</span></td>
                <td>OData v4 / CDS Views via SAP BTP Event Mesh</td>
                <td>CDC / Hourly batch</td>
                <td>Cached Contract Master in PostgreSQL; delta sync on reconnect</td>
              </tr>
              <tr style="border-bottom:1px solid #f0f0f0;">
                <td style="padding:8px 0;"><strong>KONE 24/7 Connected Services</strong><br><span style="font-size:11px; color:var(--color-neutral-6);">AWS IoT Core / Azure IoT Hub</span></td>
                <td>Kafka Avro Streams / MQTT via TLS 1.3</td>
                <td>15-min rolling windows</td>
                <td>Imputation via equipment age decay curve & regional mean</td>
              </tr>
              <tr style="border-bottom:1px solid #f0f0f0;">
                <td style="padding:8px 0;"><strong>Salesforce CRM</strong><br><span style="font-size:11px; color:var(--color-neutral-6);">Sales & Service Cloud</span></td>
                <td>REST API v59.0 / Platform Events</td>
                <td>Real-time webhooks</td>
                <td>Asynchronous queueing in Redis with retry backoff</td>
              </tr>
              <tr style="border-bottom:1px solid #f0f0f0;">
                <td style="padding:8px 0;"><strong>SAP Field Service (FSM)</strong><br><span style="font-size:11px; color:var(--color-neutral-6);">Mobile Field Dispatch</span></td>
                <td>OData Service API / Webhook queues</td>
                <td>Daily work log sync</td>
                <td>Depot queue staging; prevents field tech blocking</td>
              </tr>
              <tr>
                <td style="padding:8px 0;"><strong>Adobe Experience Cloud</strong><br><span style="font-size:11px; color:var(--color-neutral-6);">AEM Assets & Workfront</span></td>
                <td>AEM OpenAPI / HTTP REST</td>
                <td>On-demand generation</td>
                <td>Pre-approved static PDF template library with variable text injection</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Dependency Pillar 2 -->
        <div class="card">
          <div class="card-title">
            <span>2. Cloud & Compute Stack Dependencies</span>
            <span class="badge badge-neutral">Infrastructure</span>
          </div>
          <div class="card-subtitle">Underlying hosting, compute engines, event brokers, and analytical stores</div>

          <div style="display:flex; flex-direction:column; gap:10px; margin-top:12px;">
            <div style="padding:10px 12px; background:var(--color-primary-3); border-radius:var(--radius-2); font-size:12.5px;">
              <strong style="color:var(--color-primary-1);">Data Lakehouse & Query Engine:</strong> Snowflake or Databricks running in AWS Frankfurt or Azure West Europe. Requires multi-cluster warehouse (Size M) for sub-second analytical queries across 2.87M asset histories.
            </div>
            <div style="padding:10px 12px; background:var(--color-primary-3); border-radius:var(--radius-2); font-size:12.5px;">
              <strong style="color:var(--color-primary-1);">Event Streaming Bus:</strong> Apache Kafka or Redpanda cluster with 3 brokers, partitioned by Geographic Depot ID, guaranteeing zero message loss and 7-day replay capability.
            </div>
            <div style="padding:10px 12px; background:var(--color-primary-3); border-radius:var(--radius-2); font-size:12.5px;">
              <strong style="color:var(--color-primary-1);">Distributed Simulation Cluster:</strong> Ray.io cluster (8 worker nodes, auto-scaling up to 32 vCPUs) dedicated to executing 10,000-run Monte Carlo budget allocations under 2.5 seconds.
            </div>
            <div style="padding:10px 12px; background:var(--color-primary-3); border-radius:var(--radius-2); font-size:12.5px;">
              <strong style="color:var(--color-primary-1);">Transactional & Vector Store:</strong> Managed PostgreSQL 16 with pgvector extension for Golden Record Entity Graph state and contract semantic embeddings.
            </div>
            <div style="padding:10px 12px; background:var(--color-primary-3); border-radius:var(--radius-2); font-size:12.5px;">
              <strong style="color:var(--color-primary-1);">In-Memory Cache & State:</strong> Redis Enterprise cluster (or AWS ElastiCache) for sub-100ms slider simulation state and live user session state caching.
            </div>
          </div>
        </div>

        <!-- Dependency Pillar 3 -->
        <div class="card">
          <div class="card-title">
            <span>3. Machine Learning & LLM Stack Dependencies</span>
            <span class="badge badge-success">Intelligence Stack</span>
          </div>
          <div class="card-subtitle">Statistical simulation packages, foundational models, and deterministic guardrails</div>

          <div style="display:flex; flex-direction:column; gap:10px; margin-top:12px;">
            <div style="padding:10px 12px; border:1px solid var(--color-neutral-2); border-radius:var(--radius-2); font-size:12.5px;">
              <strong style="color:var(--color-primary-2);">Foundational LLM Service:</strong> Azure OpenAI Private Endpoint (GPT-4o) or self-hosted open model (Llama-3-70B) in Frankfurt. Requires contract guaranteeing <strong>zero customer data retention (ZDR) and zero model training</strong>.
            </div>
            <div style="padding:10px 12px; border:1px solid var(--color-neutral-2); border-radius:var(--radius-2); font-size:12.5px;">
              <strong style="color:var(--color-primary-2);">Deterministic RAG Framework:</strong> LangGraph + Pydantic schema validation. Enforces strict JSON schemas for battlecard generation; rejects any response missing exact SAP catalog citations.
            </div>
            <div style="padding:10px 12px; border:1px solid var(--color-neutral-2); border-radius:var(--radius-2); font-size:12.5px;">
              <strong style="color:var(--color-primary-2);">Bayesian & Causal Analytics:</strong> PyMC5, ArviZ, and DoWhy for causal attribution, synthetic control modeling, and probabilistic variance decomposition.
            </div>
            <div style="padding:10px 12px; border:1px solid var(--color-neutral-2); border-radius:var(--radius-2); font-size:12.5px;">
              <strong style="color:var(--color-primary-2);">Vector Embeddings:</strong> OpenAI text-embedding-3-large (or multilingual BGE-M3) for dense indexing of equipment service manuals, technical bulletins, and customer contracts.
            </div>
          </div>
        </div>

        <!-- Dependency Pillar 4 -->
        <div class="card">
          <div class="card-title">
            <span>4. Network, Security & Compliance Dependencies</span>
            <span class="badge badge-danger">Governance & SecOps</span>
          </div>
          <div class="card-subtitle">Zero-trust network architecture, identity federation, and European labor compliance</div>

          <div style="display:flex; flex-direction:column; gap:10px; margin-top:12px;">
            <div style="padding:10px 12px; border:1px solid var(--color-neutral-2); border-radius:var(--radius-2); font-size:12.5px;">
              <strong style="color:var(--color-primary-2);">Network Perimeter:</strong> AWS PrivateLink / Azure ExpressRoute connecting KONE enterprise WAN to the decision cluster; no public ingress ports; all egress over static NAT gateways.
            </div>
            <div style="padding:10px 12px; border:1px solid var(--color-neutral-2); border-radius:var(--radius-2); font-size:12.5px;">
              <strong style="color:var(--color-primary-2);">Identity & Role-Based Access:</strong> SAML 2.0 / OIDC federation with KONE Microsoft Entra ID. Granular role-based permissions (Executive, Commercial Lead, Depot Dispatcher, Field Technician).
            </div>
            <div style="padding:10px 12px; border:1px solid var(--color-neutral-2); border-radius:var(--radius-2); font-size:12.5px;">
              <strong style="color:var(--color-primary-2);">Works Council (Betriebsrat) Airlock:</strong> Compliance with German BetrVG §87(1) Nr. 6. Cryptographic technician pseudonymization prevents tracking of individual worker speeds or routes.
            </div>
            <div style="padding:10px 12px; border:1px solid var(--color-neutral-2); border-radius:var(--radius-2); font-size:12.5px;">
              <strong style="color:var(--color-primary-2);">Data Residency & Encryption:</strong> Strict EU data residency (Germany/Ireland). AES-256 at rest with Customer-Managed Keys (AWS KMS / Azure Key Vault); TLS 1.3 with mTLS for microservices.
            </div>
          </div>
        </div>
      </div>

      <!-- Dependency Risk & Mitigation Matrix -->
      <div class="card" style="margin-top:20px;">
        <div class="card-title">
          <span>Top 6 Dependency Bottlenecks & Pre-Packaged Mitigation Strategies</span>
          <span class="badge badge-warning">Proactive Risk Management</span>
        </div>
        <div class="card-subtitle">Battle-tested mitigation playbooks addressing potential roadblocks before they impact delivery</div>

        <table class="data-table" style="margin-top:16px;">
          <thead>
            <tr>
              <th style="width:22%;">Dependency Risk</th>
              <th style="width:12%;">Probability</th>
              <th style="width:12%;">Impact</th>
              <th style="width:54%;">Pre-Packaged Mitigation Playbook</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>SAP Direct Access Delays</strong></td>
              <td><span class="badge badge-warning">Medium</span></td>
              <td><span class="badge badge-danger">High</span></td>
              <td><strong>CSV / Parquet Drop Sandbox:</strong> Begin Sprint 1 with read-only static file drops extracted by KONE IT. Enables complete entity graph construction without waiting for firewall/OData service provisioning.</td>
            </tr>
            <tr>
              <td><strong>Dirty / Missing IoT Telemetry</strong></td>
              <td><span class="badge badge-danger">High</span></td>
              <td><span class="badge badge-warning">Medium</span></td>
              <td><strong>Synthetic Bayesian Priors:</strong> Assets lacking live sensors are initialized with historical vintage curves (e.g., 18-year-old hydraulic units). Predictions update automatically as telemetry packets arrive.</td>
            </tr>
            <tr>
              <td><strong>Works Council Scrutiny</strong></td>
              <td><span class="badge badge-danger">High</span></td>
              <td><span class="badge badge-danger">Critical</span></td>
              <td><strong>Depot-Level Aggregation Airlock:</strong> Strip individual technician identifiers before ingestion. Leads are assigned to *depot dispatch pools* rather than named individuals, fully satisfying European co-determination laws.</td>
            </tr>
            <tr>
              <td><strong>Salesforce Schema Changes</strong></td>
              <td><span class="badge badge-warning">Medium</span></td>
              <td><span class="badge badge-primary">Low</span></td>
              <td><strong>Decoupled Webhook Staging:</strong> The system pushes to an external staging table or standard Salesforce Platform Event topic. Zero custom schema changes required in production Salesforce.</td>
            </tr>
            <tr>
              <td><strong>LLM Inference Latency / Limits</strong></td>
              <td><span class="badge badge-primary">Low</span></td>
              <td><span class="badge badge-warning">Medium</span></td>
              <td><strong>Semantic Caching & Modular Templates:</strong> Pre-generate and cache 90% of modernization collateral in Redis. LLM only performs parameter slot-filling, delivering sub-200ms document generation.</td>
            </tr>
            <tr>
              <td><strong>KONE SME Availability Bandwidth</strong></td>
              <td><span class="badge badge-warning">Medium</span></td>
              <td><span class="badge badge-warning">Medium</span></td>
              <td><strong>Autonomous Data Profilers:</strong> Pre-built automated profiling scripts run against sample extracts, reducing KONE engineer review time to under 4 hours total during the first 3 weeks.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- ========================================================================
         TAB 2: PRODUCTION ARCHITECTURE & TARGET TECH STACK
         ======================================================================== -->
    <section class="tab-pane" id="pane-arch">
      <div class="card">
        <div class="card-title">
          <span>Enterprise Target Architecture (The 6-Tier System Blueprint)</span>
          <span class="badge badge-primary">Cloud Native · Event Driven</span>
        </div>
        <div class="card-subtitle">
          How the Assisted Decisioning System deploys into KONE's corporate cloud infrastructure (AWS / Azure / Snowflake)
        </div>

        <!-- TIER 1 -->
        <div class="arch-tier">
          <div class="arch-tier-header">
            <div class="arch-tier-num">Tier 1: Telemetry & Ingestion Plane (Edge & Streaming)</div>
            <span class="badge badge-success">Sub-minute streaming & Batch connectors</span>
          </div>
          <div class="arch-tier-name">KONE 24/7 IoT Broker & Enterprise Source Ingestion</div>
          <p style="font-size:13px; color:var(--text-medium); margin-top:6px; line-height:1.5;">
            Ingests real-time telemetry from connected elevator controllers (KCE, TMS, DX Class) via MQTT/AMQP edge gateways. 
            Runs through Apache Kafka / Azure Event Hubs with schema registry validation to prevent breaking changes from edge firmware upgrades. 
            Batch connectors extract daily delta tables from SAP S/4HANA (Contract & Asset Master) and Salesforce CRM.
          </p>
          <div class="arch-pill-row">
            <span class="arch-tech-pill">KONE 24/7 IoT Gateway</span>
            <span class="arch-tech-pill">AWS IoT Core / Azure Event Hubs</span>
            <span class="arch-tech-pill">Apache Kafka</span>
            <span class="arch-tech-pill">Airbyte / Fivetran CDC</span>
            <span class="arch-tech-pill">Protobuf / Avro Schemas</span>
          </div>
        </div>

        <!-- TIER 2 -->
        <div class="arch-tier">
          <div class="arch-tier-header">
            <div class="arch-tier-num">Tier 2: Lakehouse & Semantic Knowledge Graph</div>
            <span class="badge badge-primary">The Asset-Centric Golden Record</span>
          </div>
          <div class="arch-tier-name">Unified Enterprise Entity Graph & Lakehouse Storage</div>
          <p style="font-size:13px; color:var(--text-medium); margin-top:6px; line-height:1.5;">
            Normalizes disparate corporate identifiers into a single unified Knowledge Graph:
            <code>Equipment UUID &harr; Shaft Geometry &harr; Building Cadastral ID &harr; Property Manager Account &harr; Maintenance Contract &harr; Sales Pipeline &harr; Technician Team</code>.
            Data transformations are orchestrated via dbt in Snowflake or Databricks Delta Lake, with Neo4j or Amazon Neptune resolving complex relational hierarchies.
          </p>
          <div class="arch-pill-row">
            <span class="arch-tech-pill">Snowflake / Databricks Delta Lake</span>
            <span class="arch-tech-pill">dbt Core (Semantic Layer)</span>
            <span class="arch-tech-pill">Neo4j / Amazon Neptune Graph</span>
            <span class="arch-tech-pill">Apache Iceberg Tables</span>
            <span class="arch-tech-pill">OpenMetadata Governance</span>
          </div>
        </div>

        <!-- TIER 3 -->
        <div class="arch-tier">
          <div class="arch-tier-header">
            <div class="arch-tier-num">Tier 3: Decision Intelligence & Simulation Cluster</div>
            <span class="badge badge-warning">Microsecond Simulation & Inference</span>
          </div>
          <div class="arch-tier-name">Bayesian Updating & Monte Carlo Capital Allocation Engine</div>
          <p style="font-size:13px; color:var(--text-medium); margin-top:6px; line-height:1.5;">
            A high-performance Python microservice cluster (FastAPI + gRPC). Houses the Bayesian belief engine (PyMC / Stan) 
            that continuously updates conversion probability posteriors from field evidence. The Monte Carlo simulation cluster 
            (Ray / Celery) runs 10,000 parameter sweeps across budget slices (€0M to €20M) in under 800ms, factoring in 
            technician capacity constraints, parts supply lead times, and regional margin profiles.
          </p>
          <div class="arch-pill-row">
            <span class="arch-tech-pill">Python 3.12 / FastAPI</span>
            <span class="arch-tech-pill">PyMC / Stan (Bayesian Inference)</span>
            <span class="arch-tech-pill">Ray Distributed Computing</span>
            <span class="arch-tech-pill">OR-Tools (Constraint Optimization)</span>
            <span class="arch-tech-pill">Redis Cache Cluster</span>
          </div>
        </div>

        <!-- TIER 4 -->
        <div class="arch-tier">
          <div class="arch-tier-header">
            <div class="arch-tier-num">Tier 4: Agentic Reasoning & Content Supply Chain</div>
            <span class="badge badge-primary">Deterministic Guardrails · No Hallucination</span>
          </div>
          <div class="arch-tier-name">Agentic Task Orchestration & Adobe Content Supply Chain Gateway</div>
          <p style="font-size:13px; color:var(--text-medium); margin-top:6px; line-height:1.5;">
            Executes multi-agent workflows using LangGraph and Semantic Kernel. Employs <strong>strict Pydantic schema validation</strong> 
            (function calling only) to synthesize executive diagnostics, generate technician briefing packets, and orchestrate with the 
            <strong>Adobe Content Supply Chain</strong> (Adobe Workfront, AEM Modular Ingredients, Firefly localized assets). Zero raw, 
            unconstrained text generation touches commercial or customer-facing channels.
          </p>
          <div class="arch-pill-row">
            <span class="arch-tech-pill">LangGraph / Semantic Kernel</span>
            <span class="arch-tech-pill">Azure OpenAI (GPT-4o) / Vertex AI</span>
            <span class="arch-tech-pill">Pydantic Schemas</span>
            <span class="arch-tech-pill">Adobe Workfront API</span>
            <span class="arch-tech-pill">Adobe Experience Manager (AEM Assets)</span>
          </div>
        </div>

        <!-- TIER 5 -->
        <div class="arch-tier">
          <div class="arch-tier-header">
            <div class="arch-tier-num">Tier 5: Bidirectional Dispatch & CRM/ERP Connectors</div>
            <span class="badge badge-success">Closed-Loop Operational Sync</span>
          </div>
          <div class="arch-tier-name">Enterprise Integration Bus & Field Execution Dispatcher</div>
          <p style="font-size:13px; color:var(--text-medium); margin-top:6px; line-height:1.5;">
            Pushes approved decisions directly into line-of-business software:
            Creates pre-qualified Opportunities and Tasks in <strong>Salesforce CRM</strong>, reserves bracket pre-assembly inventory 
            and pushes technician inspection work orders in <strong>SAP FSM</strong>, and dispatches localized campaign workflows in 
            <strong>Adobe Marketo / SFMC</strong>. Listens for downstream outcome webhooks to feed Stage 7 (Optimise).
          </p>
          <div class="arch-pill-row">
            <span class="arch-tech-pill">Salesforce REST & Bulk API</span>
            <span class="arch-tech-pill">SAP S/4HANA OData Connectors</span>
            <span class="arch-tech-pill">SAP Field Service Management (FSM)</span>
            <span class="arch-tech-pill">MuleSoft / Azure API Management</span>
            <span class="arch-tech-pill">Webhooks / EventSub</span>
          </div>
        </div>

        <!-- TIER 6 -->
        <div class="arch-tier">
          <div class="arch-tier-header">
            <div class="arch-tier-num">Tier 6: Executive Control Tower & Frontend Experience</div>
            <span class="badge badge-dark">Sub-second Reactive UI</span>
          </div>
          <div class="arch-tier-name">Next.js 15 / React 19 Single-Pane-of-Glass Workspace</div>
          <p style="font-size:13px; color:var(--text-medium); margin-top:6px; line-height:1.5;">
            The executive interface built with Next.js 15, TypeScript, Tailwind CSS, and KONE PocketUI design tokens. 
            Subscribed to live Server-Sent Events (SSE) for telemetry streaming and interactive simulation slider manipulations. 
            Features full WCAG 2.1 AA accessibility, offline fallback service workers, and enterprise SSO (Microsoft Entra ID / Okta).
          </p>
          <div class="arch-pill-row">
            <span class="arch-tech-pill">Next.js 15 / React 19</span>
            <span class="arch-tech-pill">TypeScript</span>
            <span class="arch-tech-pill">Tailwind CSS (KONE Tokens)</span>
            <span class="arch-tech-pill">Server-Sent Events (SSE)</span>
            <span class="arch-tech-pill">Microsoft Entra ID (SSO)</span>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================================================
         TAB 3: THE DATA EXERCISE & READINESS AUDIT
         ======================================================================== -->
    <section class="tab-pane" id="pane-data">
      <div class="card">
        <div class="card-title">
          <span>The Critical Data Exercise: Unifying the 5 Domains</span>
          <span class="badge badge-warning">Prerequisite Data Discovery</span>
        </div>
        <div class="card-subtitle">
          The exact data discovery, extraction, profiling, and entity reconciliation required to feed the Assisted Decisioning System
        </div>

        <p style="font-size:14px; color:var(--text-high); line-height:1.6;">
          To make the "Marketing Brain" operate in production, KONE does <strong>not</strong> need to embark on a 3-year data warehouse overhaul. 
          Instead, we execute a targeted <strong>Entity Resolution & Semantic Harmonization Sprint</strong> across five distinct operational domains:
        </p>

        <table class="data-table" style="margin-top:18px;">
          <thead>
            <tr>
              <th style="width:16%;">Data Domain</th>
              <th style="width:18%;">Source System at KONE</th>
              <th style="width:26%;">Key Data Fields Extracted</th>
              <th style="width:18%;">Refresh Latency</th>
              <th style="width:22%;">Common Data Quality Pitfalls</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1. Asset Telemetry & Health</strong></td>
              <td>KONE 24/7 Connected Services (AWS IoT Core)</td>
              <td>Door cycles, leveling errors, drive vibration RMS, temperature drift, emergency stop count, controller model (KCE/TMS).</td>
              <td><span class="badge badge-success">Near Real-Time (&lt;5 min)</span></td>
              <td>Older non-connected controllers (55% base); intermittent cellular signal in basement shafts.</td>
            </tr>
            <tr>
              <td><strong>2. Installed Base & Contract Master</strong></td>
              <td>SAP S/4HANA / SAP ECC (Plant Maintenance)</td>
              <td>Equipment Serial, installation year, modernization history, maintenance contract tier (Standard/Plus/24-7), customer legal entity.</td>
              <td><span class="badge badge-primary">Daily Batch (Delta CDC)</span></td>
              <td>Inconsistent building address strings; merged accounts across holding companies.</td>
            </tr>
            <tr>
              <td><strong>3. Commercial & Sales Pipeline</strong></td>
              <td>Salesforce CRM (Sales Cloud / CPQ)</td>
              <td>Active modernization opportunities, quote stage, bid value, lost reasons, competitor elevator brand displacement.</td>
              <td><span class="badge badge-primary">Hourly Sync / Webhooks</span></td>
              <td>Sales rep free-text notes; missing competitive replacement metadata; stale close dates.</td>
            </tr>
            <tr>
              <td><strong>4. Field Service & Technician Observations</strong></td>
              <td>SAP FSM / Salesforce Field Service</td>
              <td>Technician visit frequency, shaft dimension audits, hoistway clearances, customer verbal renewal intent, referral leads.</td>
              <td><span class="badge badge-primary">Daily Batch / Event Triggers</span></td>
              <td>Works Council (Betriebsrat) sensitivity in Germany; unstructured technician comments.</td>
            </tr>
            <tr>
              <td><strong>5. Customer & Marketing Engagement</strong></td>
              <td>Adobe Experience Platform / Marketo / Web</td>
              <td>Property manager portal logins, disruption calculator downloads, webinar attendance, modernization email open rates.</td>
              <td><span class="badge badge-primary">Hourly Batch</span></td>
              <td>Cookie deprecation; difficulty linking individual property manager emails to corporate SAP account IDs.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- ENTITY RESOLUTION DEEP DIVE -->
      <div class="card">
        <div class="card-title">
          <span>The "Golden Record" Entity Resolution Challenge</span>
          <span class="badge badge-danger">Core Technical Hurdle</span>
        </div>
        <div class="card-subtitle">Connecting physical elevator shafts to corporate contract buyers</div>

        <div class="callout callout-info">
          <strong>Why this is the #1 data exercise:</strong> At KONE, an elevator has an engineering serial number in the factory, 
          an equipment ID in SAP, an asset record in Salesforce, and a physical location known to municipal cadastral registers. 
          Meanwhile, the entity paying the bill might be an international asset manager (e.g. Blackstone), a national property firm 
          (e.g. Lar España), or a local homeowner association (Comunidad de Propietarios).
        </div>

        <div class="grid-3" style="margin-top:16px;">
          <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
            <div style="font-size:12px; font-weight:700; color:var(--color-primary-1); margin-bottom:4px;">STEP 1: Geospatial & Cadastral Normalization</div>
            <p style="font-size:12.5px; color:var(--color-neutral-7); line-height:1.5;">
              Use GIS reverse-geocoding to resolve disparate address strings ("Calle Gran Vía 28" vs "C. Gran Via, 28, 28013 Madrid") 
              into a canonical Building UUID linked to national land registers.
            </p>
          </div>
          <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
            <div style="font-size:12px; font-weight:700; color:var(--color-primary-1); margin-bottom:4px;">STEP 2: Probabilistic Graph Linking</div>
            <p style="font-size:12.5px; color:var(--color-neutral-7); line-height:1.5;">
              Apply deterministic keys (Serial + Postal Code) supplemented by Jaro-Winkler string distance on property manager names 
              to bind SAP Contract Numbers to Salesforce CRM Accounts with &gt;99.2% match accuracy.
            </p>
          </div>
          <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
            <div style="font-size:12px; font-weight:700; color:var(--color-primary-1); margin-bottom:4px;">STEP 3: The Shadow Pipeline Strategy</div>
            <p style="font-size:12.5px; color:var(--color-neutral-7); line-height:1.5;">
              Begin with synthetic telemetry seeds (as in this prototype) to test the mathematical decision model, while 
              concurrently running a 6-week "Shadow Pipeline" that incrementally replaces mock tables with live lakehouse feeds.
            </p>
          </div>
        </div>
      </div>

      <!-- INTERACTIVE READINESS CALCULATOR -->
      <div class="calc-box">
        <div class="calc-grid">
          <div>
            <div style="font-size:16px; font-family:var(--font-font-3); color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">
              Interactive Client Data Readiness Assessment
            </div>
            <div style="font-size:13px; color:var(--color-neutral-6); margin-bottom:14px;">
              Toggle the availability of KONE's corporate data feeds to compute current system readiness and expected delivery velocity:
            </div>
            <div class="calc-items">
              <label class="calc-item">
                <input type="checkbox" id="chk-telemetry" checked onchange="updateReadiness()">
                <div class="calc-label">
                  <strong>KONE 24/7 Connected Services Telemetry:</strong> Live door cycle & fault code stream from connected base (&gt;45%)
                </div>
                <span class="badge badge-success">+25 pts</span>
              </label>

              <label class="calc-item">
                <input type="checkbox" id="chk-sap" checked onchange="updateReadiness()">
                <div class="calc-label">
                  <strong>SAP S/4HANA Asset & Contract Master:</strong> Equipment age, contract type, and service billing history
                </div>
                <span class="badge badge-success">+25 pts</span>
              </label>

              <label class="calc-item">
                <input type="checkbox" id="chk-crm" checked onchange="updateReadiness()">
                <div class="calc-label">
                  <strong>Salesforce CRM Modernization Pipeline:</strong> Active deals, quote stages, win/loss attribution codes
                </div>
                <span class="badge badge-success">+20 pts</span>
              </label>

              <label class="calc-item">
                <input type="checkbox" id="chk-fsm" onchange="updateReadiness()">
                <div class="calc-label">
                  <strong>SAP FSM Technician Shaft Audits:</strong> Digital hoistway dimension logs & technician lead capture tags
                </div>
                <span class="badge badge-primary">+15 pts</span>
              </label>

              <label class="calc-item">
                <input type="checkbox" id="chk-adobe" onchange="updateReadiness()">
                <div class="calc-label">
                  <strong>Adobe Content Supply Chain (Workfront/AEM):</strong> Modular ingredient metadata & digital customer touchpoints
                </div>
                <span class="badge badge-primary">+15 pts</span>
              </label>
            </div>
          </div>

          <div class="calc-score-display">
            <div class="calc-score-num" id="calcScoreNum">70%</div>
            <div class="calc-score-sub" id="calcScoreLabel">Strong MVP Baseline</div>
            <p style="font-size:12px; color:var(--color-neutral-6); margin-top:8px;" id="calcScoreDesc">
              Ready to deploy Phase 1 MVP (Sense, Diagnose, Prioritise, and Simulate) with Iberian pilot cohort.
            </p>
            <div class="calc-timeline-est" id="calcTimeline">
              Estimated Discovery: <strong>4 Weeks</strong> · MVP Launch: <strong>12 Weeks</strong>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         TAB 4: WHAT IT TAKES TO BUILD (ROADMAP & COST)
         ======================================================================== -->
    <section class="tab-pane" id="pane-roadmap">
      <div class="card">
        <div class="card-title">
          <span>Production Delivery Roadmap (48-Week Enterprise Flight Plan)</span>
          <span class="badge badge-primary">Phased Agile Rollout</span>
        </div>
        <div class="card-subtitle">From proof-of-concept to global multi-market autonomous decisioning</div>

        <div style="margin-top:14px; padding:12px 16px; background:var(--color-primary-3); border-left:4px solid var(--color-primary-1); border-radius:var(--radius-2); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
          <div style="font-size:13px; color:var(--color-primary-18);">
            <strong>Fast-Track Option:</strong> For rapid executive validation, Phase 0 (Discovery) and Phase 1 (Iberia Pilot) can be executed as a focused 
            <strong>16-to-20 Week Enterprise Pilot</strong> anchored on the European <strong>ONE Week Modernization (MonoSpace LIS)</strong> campaign cohort in Italy & Iberia.
          </div>
          <button onclick="switchTab('poc')" style="background:var(--color-primary-1); color:#ffffff; border:none; padding:6px 12px; border-radius:var(--radius-3); font-weight:700; font-size:12px; cursor:pointer; flex-shrink:0;">
            View 16–20 Wk Pilot Plan &rarr;
          </button>
        </div>

        <div style="position:relative; margin-top:20px;">
          <!-- PHASE 0 -->
          <div style="display:flex; gap:20px; margin-bottom:24px;">
            <div style="width:130px; flex-shrink:0; font-size:13px; font-weight:700; color:var(--color-primary-1); text-align:right;">
              Weeks 1 – 6<br>
              <span class="badge badge-neutral" style="margin-top:4px;">Phase 0</span>
            </div>
            <div style="width:2px; background:var(--color-primary-9); position:relative;">
              <div style="position:absolute; top:0; left:-5px; width:12px; height:12px; border-radius:50%; background:var(--color-primary-1);"></div>
            </div>
            <div style="flex:1; background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
              <div style="font-size:15px; font-weight:700; color:var(--color-primary-2);">Architecture Blueprint & Data Discovery Audit</div>
              <div style="font-size:12.5px; color:var(--color-neutral-6); margin:4px 0 10px 0;">Target: Align enterprise architecture, profile 5 data sources, establish security boundaries.</div>
              <ul style="font-size:13px; color:var(--text-medium); line-height:1.6; padding-left:20px;">
                <li>Execute data schema profiling across SAP, Salesforce, and KONE 24/7 IoT streaming brokers.</li>
                <li>Design Entity Resolution algorithm for Spain & DACH elevator registers.</li>
                <li>Establish Information Security (InfoSec) clearance, GDPR data boundary, and Works Council compliance plan.</li>
                <li>Stand up cloud sandbox environment (Snowflake / AWS / Azure).</li>
              </ul>
            </div>
          </div>

          <!-- PHASE 1 -->
          <div style="display:flex; gap:20px; margin-bottom:24px;">
            <div style="width:130px; flex-shrink:0; font-size:13px; font-weight:700; color:var(--color-primary-1); text-align:right;">
              Weeks 7 – 18<br>
              <span class="badge badge-success" style="margin-top:4px;">Phase 1 (MVP)</span>
            </div>
            <div style="width:2px; background:var(--color-primary-9); position:relative;">
              <div style="position:absolute; top:0; left:-5px; width:12px; height:12px; border-radius:50%; background:var(--color-primary-1);"></div>
            </div>
            <div style="flex:1; background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
              <div style="font-size:15px; font-weight:700; color:var(--color-primary-2);">Pilot Market MVP (Iberia Modernization Flywheel)</div>
              <div style="font-size:12.5px; color:var(--color-neutral-6); margin:4px 0 10px 0;">Target: Operationalize Stages 1–5 for the 38-building Madrid & Barcelona cohort.</div>
              <ul style="font-size:13px; color:var(--text-medium); line-height:1.6; padding-left:20px;">
                <li>Deploy live ingestion for 34,500 aging units in Spain and Portugal.</li>
                <li>Implement Bayesian Variance Diagnosis decomposing the +22 pt gap between DACH & Iberia.</li>
                <li>Build interactive Monte Carlo simulation engine with live slider budget optimization.</li>
                <li>Establish bidirectional field dispatch to Iberian sales ops and field technician teams.</li>
              </ul>
            </div>
          </div>

          <!-- PHASE 2 -->
          <div style="display:flex; gap:20px; margin-bottom:24px;">
            <div style="width:130px; flex-shrink:0; font-size:13px; font-weight:700; color:var(--color-primary-1); text-align:right;">
              Weeks 19 – 32<br>
              <span class="badge badge-primary" style="margin-top:4px;">Phase 2</span>
            </div>
            <div style="width:2px; background:var(--color-primary-9); position:relative;">
              <div style="position:absolute; top:0; left:-5px; width:12px; height:12px; border-radius:50%; background:var(--color-primary-1);"></div>
            </div>
            <div style="flex:1; background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
              <div style="font-size:15px; font-weight:700; color:var(--color-primary-2);">European Scale-Out & Adobe Content Supply Chain Sync</div>
              <div style="font-size:12.5px; color:var(--color-neutral-6); margin:4px 0 10px 0;">Target: Expand to DACH, Benelux, UK&I, France, Nordics; integrate Adobe ecosystem.</div>
              <ul style="font-size:13px; color:var(--text-medium); line-height:1.6; padding-left:20px;">
                <li>Expand Knowledge Graph to encompass 2.87M contracts across 7 core operating units.</li>
                <li>Integrate Adobe Workfront & AEM Assets for automated, localized modernization collateral generation.</li>
                <li>Implement Stage 6 (Replicate) cross-market playbook sharing algorithms.</li>
                <li>Activate real-time technician lead capture mobile workflows.</li>
              </ul>
            </div>
          </div>

          <!-- PHASE 3 -->
          <div style="display:flex; gap:20px;">
            <div style="width:130px; flex-shrink:0; font-size:13px; font-weight:700; color:var(--color-primary-1); text-align:right;">
              Weeks 33 – 48<br>
              <span class="badge badge-dark" style="margin-top:4px;">Phase 3</span>
            </div>
            <div style="width:2px; background:var(--color-primary-9); position:relative;">
              <div style="position:absolute; top:0; left:-5px; width:12px; height:12px; border-radius:50%; background:var(--color-primary-1);"></div>
            </div>
            <div style="flex:1; background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px;">
              <div style="font-size:15px; font-weight:700; color:var(--color-primary-2);">Autonomous Bayesian Learning & Global Enterprise Rollout</div>
              <div style="font-size:12.5px; color:var(--color-neutral-6); margin:4px 0 10px 0;">Target: Automated Day-90 attribution loop (Stages 7 & 8) and worldwide rollout.</div>
              <ul style="font-size:13px; color:var(--text-medium); line-height:1.6; padding-left:20px;">
                <li>Activate Stage 7 & 8 closed-loop learning: automated posterior updating without manual intervention.</li>
                <li>Integrate with KONE global capital planning and financial ERP for quarterly budget recommendations.</li>
                <li>Roll out self-service executive mobile experience for Petra, Hans, and regional managing directors.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- SIZING & RESOURCING -->
      <div class="grid-2">
        <div class="card">
          <div class="card-title">
            <span>Engineering Pod Composition</span>
            <span class="badge badge-primary">Dedicated Pod</span>
          </div>
          <div class="card-subtitle">Recommended multi-disciplinary delivery squad</div>
          <table class="data-table">
            <thead>
              <tr>
                <th>Role</th>
                <th>Count</th>
                <th>Core Responsibilities</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Enterprise Solution Architect</strong></td>
                <td>1 FTE</td>
                <td>Cloud topology, API gateway, security posture, SAP/Salesforce integration governance.</td>
              </tr>
              <tr>
                <td><strong>Lead Data Engineers</strong></td>
                <td>2 FTE</td>
                <td>Kafka streaming, dbt lakehouse pipelines, entity resolution graph, IoT data contracts.</td>
              </tr>
              <tr>
                <td><strong>Decision Scientists / ML Eng</strong></td>
                <td>2 FTE</td>
                <td>Bayesian inference models, Monte Carlo distributed simulation cluster, optimization solvers.</td>
              </tr>
              <tr>
                <td><strong>SAP & Salesforce Integration Eng</strong></td>
                <td>1 FTE</td>
                <td>OData connectors, SAP FSM work order dispatch, Salesforce CPQ / Sales Cloud sync.</td>
              </tr>
              <tr>
                <td><strong>MarTech & Adobe Specialist</strong></td>
                <td>1 FTE</td>
                <td>Adobe Workfront, AEM Modular Ingredients, Firefly asset supply chain automation.</td>
              </tr>
              <tr>
                <td><strong>Senior Full-Stack UI Engineers</strong></td>
                <td>2 FTE</td>
                <td>Next.js 15, TypeScript, WebSockets/SSE live streams, KONE PocketUI design system.</td>
              </tr>
              <tr>
                <td><strong>Security & Governance Lead</strong></td>
                <td>0.5 FTE</td>
                <td>GDPR compliance, Works Council audits, encryption, SOC2/ISO 27001 validation.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="card">
          <div class="card-title">
            <span>Cloud Infrastructure Sizing & Cost Drivers</span>
            <span class="badge badge-success">Cost Predictability</span>
          </div>
          <div class="card-subtitle">Estimated production cloud footprint & annual OPEX drivers</div>
          
          <div style="font-size:13px; color:var(--text-medium); line-height:1.6;">
            <p style="margin-bottom:10px;">
              The system leverages serverless and auto-scaling components to maintain an efficient, predictable infrastructure footprint:
            </p>
            <div style="padding:10px 14px; background:var(--color-primary-3); border-radius:var(--radius-3); margin-bottom:8px;">
              <strong>1. Data Lakehouse & Graph Query (Snowflake / Databricks / Neo4j):</strong><br>
              <span style="font-size:12px; color:var(--color-neutral-7);">Compute scales dynamically during morning simulation hours; auto-suspends during non-peak windows (~€4,500 - €7,000 / mo).</span>
            </div>
            <div style="padding:10px 14px; background:var(--color-primary-3); border-radius:var(--radius-3); margin-bottom:8px;">
              <strong>2. Simulation Cluster (Ray on AWS EKS / Azure AKS):</strong><br>
              <span style="font-size:12px; color:var(--color-neutral-7);">Horizontal pod auto-scaling; spins up 32-core workers only during active boardroom or Monday morning planning sessions (~€1,200 - €2,000 / mo).</span>
            </div>
            <div style="padding:10px 14px; background:var(--color-primary-3); border-radius:var(--radius-3); margin-bottom:8px;">
              <strong>3. LLM Reasoning & Schema Gateways (Azure OpenAI / Vertex AI):</strong><br>
              <span style="font-size:12px; color:var(--color-neutral-7);">Strict schema-constrained token usage; zero free-form chatter (~€800 - €1,500 / mo).</span>
            </div>
            <div style="padding:10px 14px; background:var(--color-primary-3); border-radius:var(--radius-3);">
              <strong>4. Total Projected Cloud Infrastructure OPEX:</strong><br>
              <span style="font-size:14px; font-weight:700; color:var(--color-primary-1);">€7,500 – €11,500 per month</span> 
              <span style="font-size:12px; color:var(--color-neutral-6);">&bull; Yields &gt;18x ROI against Iberian modernization lift alone.</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         TAB 5: CLIENT DEFENSE GUIDE (16 TECHNICAL Q&AS)
         ======================================================================== -->
    <section class="tab-pane" id="pane-defense">
      <div class="card">
        <div class="card-title">
          <span>Client Technical Defense Guide (16 Battle-Tested Q&As)</span>
          <span class="badge badge-primary">Presenter Cheat Sheet</span>
        </div>
        <div class="card-subtitle">
          Prepare for tough, skeptical questions from KONE's CTO, Enterprise Architects, Data Officers, and MarTech leads
        </div>

        <!-- SEARCH & FILTER BAR -->
        <div class="qa-controls">
          <input type="text" id="qaSearchInput" class="qa-search-box" placeholder="Search technical questions (e.g., IoT, latency, hallucination, GDPR, SAP, Works Council)..." oninput="filterQA()">
          <button class="filter-btn active" onclick="setQACategory('all', this)">All (18)</button>
          <button class="filter-btn" onclick="setQACategory('iot', this)">IoT & Telemetry (3)</button>
          <button class="filter-btn" onclick="setQACategory('ai', this)">Data Science & AI (4)</button>
          <button class="filter-btn" onclick="setQACategory('enterprise', this)">SAP / Salesforce / Adobe (5)</button>
          <button class="filter-btn" onclick="setQACategory('governance', this)">GDPR & Compliance (3)</button>
          <button class="filter-btn" onclick="setQACategory('business', this)">Architecture & ROI (3)</button>
        </div>

        <div id="qaAccordionContainer">

          <!-- Q1 -->
          <div class="qa-card" data-cat="business">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">Architecture & Strategy</span>
                <div class="qa-question">1. "Isn't this just another BI dashboard like Power BI or Tableau? Why build a custom application?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "Dashboards are passive rearview mirrors that tell you where revenue was lost last quarter. 
                  The Assisted Decisioning System is an active steering wheel. It couples live IoT telemetry to forward-looking 
                  Monte Carlo simulation and closed-loop field dispatch. It doesn't ask leaders to read 50 charts—it asks them to 
                  commit capital and automatically triggers the field execution."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  BI tools cannot run dynamic 10,000-iteration Monte Carlo optimization across constrained parameters in under a second; 
                  they cannot update Bayesian posterior beliefs as field technicians complete shaft surveys; and they cannot push 
                  governed tasks bidirectionally into Salesforce, SAP FSM, and Adobe Workfront via REST webhooks. Tableau is a reporting 
                  layer; ADS is an operational decision and orchestration system.
                </div>
              </div>
            </div>
          </div>

          <!-- Q2 -->
          <div class="qa-card" data-cat="iot">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">IoT & Telemetry</span>
                <div class="qa-question">2. "How do you connect to 2.87M assets without overwhelming KONE 24/7 Connected Services or our IoT MQTT brokers?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "We never query the physical elevator controllers or IoT brokers directly from the user interface. 
                  We tap into the existing cloud data lake stream via an asynchronous message consumer. 
                  The elevator edge remains 100% decoupled and safe."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  The ADS architecture hooks into the downstream stream of KONE's AWS IoT Core / Azure Event Hub via an Apache Kafka 
                  consumer group. Raw telemetry (vibration, leveling, door cycles) is pre-aggregated into hourly health indices and 
                  stored in lakehouse delta tables. The front-end queries an in-memory Redis cluster populated by pre-computed 
                  anomaly aggregations. At no point does front-end traffic touch the MQTT command-and-control broker or the elevator's 
                  microcontroller bus.
                </div>
              </div>
            </div>
          </div>

          <!-- Q3 -->
          <div class="qa-card" data-cat="iot">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">IoT & Telemetry</span>
                <div class="qa-question">3. "What happens if a market or elevator has zero IoT connectivity (the 55% non-connected base)?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "The system uses connected units as 'sentinels' to infer health models for non-connected siblings. 
                  If a 32-year-old hydraulic unit in Madrid shows valve wear, the system scores all similar non-connected units 
                  in Madrid with a matching risk prior based on age, cycles, and building type."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  We implement Bayesian hierarchical clustering. Equipment with active KONE 24/7 telemetry informs the prior probability 
                  distribution for equivalent cohorts (same manufacturer, age bracket, controller type, and building typology in SAP). 
                  Furthermore, routine technician maintenance visits logged in SAP FSM provide manual calibration points that refine 
                  the non-connected asset's health score.
                </div>
              </div>
            </div>
          </div>

          <!-- Q4 -->
          <div class="qa-card" data-cat="ai">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">Data Science & AI</span>
                <div class="qa-question">4. "How does the Bayesian decisioning engine work mathematically? Does it use arbitrary weights?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "No black-box heuristics. We use classical Bayesian updating: prior belief multiplied by the likelihood of observed 
                  field evidence equals our updated posterior confidence. Every recommendation is mathematically traceable."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  For each modernization candidate, the initial confidence prior <code>P(&theta;)</code> is seeded from historical market 
                  conversion rates in SAP/Salesforce. When evidence vectors <code>x</code> land (e.g., technician confirms shaft clearance, 
                  property manager downloads One Week Modernization flyer, door faults exceed 3 per month), the posterior probability 
                  <code>P(&theta;|x) &prop; P(x|&theta;) &bull; P(&theta;)</code> is calculated. In our Iberian pilot, this updated confidence 
                  from 0.62 to 0.84 as 38 site audits confirmed standard shaft tolerances.
                </div>
              </div>
            </div>
          </div>

          <!-- Q5 -->
          <div class="qa-card" data-cat="ai">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">Data Science & AI</span>
                <div class="qa-question">5. "How does the Monte Carlo simulation handle real-world operational constraints like technician shortages?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "The simulator doesn't assume infinite capacity. It enforces hard physical boundaries: available certified technician 
                  hours per province, bracket manufacturing lead times, and sales quotation velocity."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  The simulation runs an optimization algorithm (Simplex / Interior Point via OR-Tools) subject to linear inequality constraints:
                  <code>&sum; (Units_i &times; TechHours_i) &le; Capacity_Regional</code> and <code>LeadTime_Brackets &le; MaxDisruption_SLA</code>. 
                  When the user moves the budget slider beyond €8.4M in Iberia, the curve flattens because Madrid and Barcelona 
                  technician teams hit 92% utilization—demonstrating diminishing marginal returns without hiring or overtime approval.
                </div>
              </div>
            </div>
          </div>

          <!-- Q6 -->
          <div class="qa-card" data-cat="ai">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">Data Science & AI</span>
                <div class="qa-question">6. "How do you distinguish correlation from causation in the 22-point conversion gap between DACH and Iberia?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "By running causal decomposition. We proved that increasing Iberian ad spend had zero statistical impact, 
                  whereas bundling the 5-Day Disruption Guarantee and technician lead bounties drove 88% of the conversion variance."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  We use Do-calculus and Shapley Value additive feature attribution (SHAP). In Stage 2 (Diagnose), the variance 
                  decomposition isolated three variables explaining the +22 pt gap: 
                  (1) Technician First-Touch Lead Capture (+11.4 pts), 
                  (2) One Week Disruption Guarantee backed by pre-assembled brackets (+7.8 pts), 
                  (3) Property Administrator Portal Quotation SLA (+2.8 pts). Creative branding and media mix spend showed a 
                  near-zero Shapley value (&lt;0.5 pts), directing Petra to reallocate budget from media to operational field enablement.
                </div>
              </div>
            </div>
          </div>

          <!-- Q7 -->
          <div class="qa-card" data-cat="ai">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">Data Science & AI</span>
                <div class="qa-question">7. "How do you prevent generative AI hallucinations when synthesizing executive diagnostics or field briefs?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "Generative models never invent numbers. The LLM is strictly an articulation engine that fills 
                  pre-validated schemas derived directly from our deterministic database and simulation models."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  All metrics, shaft dimensions, quote values, and conversion probabilities are calculated in deterministic Python 
                  services. We enforce strict JSON function calling via Pydantic schemas. If an LLM returns a field brief with a budget, 
                  shaft height, or elevator model not matching the verified Lakehouse record, the API gateway automatically rejects 
                  the response and re-prompts or falls back to hardcoded template strings. Hallucination risk is zero on numerical 
                  and commercial terms.
                </div>
              </div>
            </div>
          </div>

          <!-- Q8 -->
          <div class="qa-card" data-cat="enterprise">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">SAP / Salesforce / Adobe</span>
                <div class="qa-question">8. "We already have Salesforce and SAP. Does this replace them or sit on top?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "It sits on top. SAP remains the master of equipment and contracts. Salesforce remains the master of pipeline. 
                  ADS is the intelligence bridge that connects them so marketing and sales finally operate from the same brain."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  ADS acts as an intelligent orchestration plane. It reads from SAP and Salesforce via standard APIs, enriches 
                  records with IoT predictive risk and Bayesian priority, and writes back actionable tasks. Sales reps still live in 
                  Salesforce; technicians still live in SAP FSM; marketing still lives in Adobe Workfront. ADS eliminates the need for 
                  executives to manually reconcile spreadsheets across three disparate enterprise tools.
                </div>
              </div>
            </div>
          </div>

          <!-- Q9 -->
          <div class="qa-card" data-cat="enterprise">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">SAP / Salesforce / Adobe</span>
                <div class="qa-question">9. "How does this integrate with Adobe Content Supply Chain (Workfront, AEM, Firefly)?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "Better intelligence creates better content. When the ADS identifies a modernization cluster in Madrid, 
                  it triggers Adobe Workfront to assemble pre-approved modular assets—combining localized Spanish copy with verified 
                  hoistway disruption guarantees."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  ADS maps decision outputs to the Adobe Content Supply Chain through Workfront project templates. 
                  In Stage 6 (Replicate), approved growth ingredients (e.g., KONE One Week Modernization customer calculation widget, 
                  EcoDisc energy reduction proof point) are tagged with AEM metadata IDs. ADS pushes campaign briefs to Workfront, 
                  which orchestrates Adobe Firefly / Express to generate localized Spanish, German, or Dutch collateral without 
                  starting from a blank sheet or relying on external agencies.
                </div>
              </div>
            </div>
          </div>

          <!-- Q10 -->
          <div class="qa-card" data-cat="enterprise">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">SAP / Salesforce / Adobe</span>
                <div class="qa-question">10. "Will this require heavy modifications to our SAP S/4HANA or Salesforce CRM cores?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "Zero core modifications. We use out-of-the-box standard OData APIs for SAP and standard REST/Bulk APIs for Salesforce. 
                  We follow a clean core, side-by-side extension pattern."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  We adhere strictly to SAP's 'Clean Core' paradigm using SAP BTP / OData services (API_EQUIPMENT, API_MAINTCONTRACT). 
                  For Salesforce, we consume standard Enterprise REST and Pub/Sub APIs. All custom entity resolution, graph relationships, 
                  and Bayesian computations reside in the external Lakehouse and ADS microservices. No custom ABAP or complex Apex 
                  triggers are installed in KONE's transactional core.
                </div>
              </div>
            </div>
          </div>

          <!-- Q11 -->
          <div class="qa-card" data-cat="enterprise">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">SAP / Salesforce / Adobe</span>
                <div class="qa-question">11. "How does closed-loop technician attribution work without disrupting field workflows?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "Technicians don't fill out marketing surveys. We add a single 5-second checkmark in their existing mobile app 
                  during routine maintenance: 'Shaft suitable for One-Week Modernization (Y/N)'. That single tap triggers the entire 
                  commercial machine."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  In SAP FSM mobile, we enrich routine service work orders with a lightweight custom attribute screen containing 
                  two fields: Hoistway Fit Confirmed (Boolean) and Modernization Opportunity Lead (Check). When submitted, an SAP event 
                  webhook fires into ADS Stage 5 (Orchestrate), which immediately matches the asset to its Property Administrator in 
                  Salesforce and credits the technician's crew with a referral lead tag for attribution in Stage 7.
                </div>
              </div>
            </div>
          </div>

          <!-- Q12 -->
          <div class="qa-card" data-cat="governance">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">GDPR & Compliance</span>
                <div class="qa-question">12. "How do you address European Works Council (Betriebsrat) concerns regarding technician tracking?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "The system measures cohort enablement, not individual worker performance. 
                  Data is aggregated at the depot and branch level in strict accordance with German and European labor agreements."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  In Germany and Austria, Works Council agreements strictly prohibit individual technician KPI monitoring or automated 
                  incentive scoring. ADS implements differential privacy and depot-level aggregation: leads and attribution are scored 
                  by branch / service area (e.g., 'Frankfurt Central Depot', 'Madrid Sur'), never exposing individual technician IDs. 
                  Role-based access control (RBAC) ensures marketing and leadership dashboards only see anonymized cohort statistics.
                </div>
              </div>
            </div>
          </div>

          <!-- Q13 -->
          <div class="qa-card" data-cat="governance">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">GDPR & Compliance</span>
                <div class="qa-question">13. "What is the GDPR compliance posture regarding building tenant and property manager data?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "ADS operates strictly on B2B commercial entities and anonymized physical building assets. 
                  We do not collect, process, or store personal tenant ride histories or individual passenger identities."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  Elevator telemetry (accelerometer vibration, motor temperature, leveling variance) contains zero PII. 
                  Property management contact details imported from Salesforce CRM are processed under GDPR Article 6(1)(f) 
                  (Legitimate Interest for B2B commercial maintenance contracts). All data stays within the EU Data Boundary 
                  (AWS Frankfurt / Azure West Europe) with AES-256 encryption at rest and TLS 1.3 in transit.
                </div>
              </div>
            </div>
          </div>

          <!-- Q14 -->
          <div class="qa-card" data-cat="governance">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">GDPR & Compliance</span>
                <div class="qa-question">14. "What security certifications, SSO, and encryption standards are enforced?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "The production deployment complies with ISO 27001, SOC 2 Type II, and KONE's corporate cybersecurity baseline, 
                  integrated directly with Microsoft Entra ID (Azure AD) SSO."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  Authentication is managed via SAML 2.0 / OpenID Connect against KONE's Microsoft Entra ID with conditional access 
                  and MFA. API communications require mTLS and short-lived OAuth 2.0 bearer tokens. Audit logs capture all user 
                  actions, simulation runs, and decision commitments with immutable cryptographic hashing for enterprise compliance.
                </div>
              </div>
            </div>
          </div>

          <!-- Q15 -->
          <div class="qa-card" data-cat="business">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">Architecture & Strategy</span>
                <div class="qa-question">15. "How do we prove the financial ROI of the Assisted Decisioning System itself?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "Through synthetic control groups and randomized market holdouts. We compare modernization conversion lift 
                  in orchestrated cohorts against un-assisted control cohorts in identical geographic markets."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  Stage 7 (Optimise) runs continuous A/B holdout testing. In Madrid and Barcelona, the 38 pilot buildings were matched 
                  with 38 identical twin buildings (same asset age, contract tier, and building size) that received standard un-assisted 
                  sales follow-up. The pilot cohort delivered a 39.5% conversion rate versus 24.1% in the control cohort—yielding an 
                  incremental €1.24M in modernized order book value that directly attributes a 12x return on software build costs in the first 90 days.
                </div>
              </div>
            </div>
          </div>

          <!-- Q16 -->
          <div class="qa-card" data-cat="enterprise">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">SAP / Salesforce / Adobe</span>
                <div class="qa-question">16. "How does the system handle multi-tenant isolation across global vs regional operating companies?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "Row-level security ensures local country managing directors only see their own operating company's data, 
                  while Petra and Hans maintain a consolidated global control tower view."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  Data in Snowflake and the API layer enforces Row-Level Security (RLS) keyed to KONE's SAP Company Code (BUKRS). 
                  A user belonging to KONE Ibérica S.A. (Company Code 1200) cannot access German or Finnish pipeline or margin records. 
                  Global marketing leadership accounts hold cross-tenant analytical roles that aggregate anonymized regional performance 
                  without exposing restricted local customer contract terms.
                </div>
              </div>
            </div>
          </div>

          <!-- Q17 -->
          <div class="qa-card" data-cat="business">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">Architecture & Delivery</span>
                <div class="qa-question">17. "Why does an enterprise pilot take 16–20 weeks instead of 8–10 weeks? Can we execute faster?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "An 8-week timeline is a dangerous SaaS fallacy in an industrial multinational like KONE. 
                  It overlooks European Works Council (§87 BetrVG) co-determination on technician telemetry, 
                  SAP S/4HANA Clean Core CAB change windows, and cadastral entity resolution. A 16–20 week flight plan 
                  provides the exact legal, technical, and operational airlocks required to produce verified commercial 
                  pipeline without risking production systems or alienating field labor."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  In a real enterprise, provisioning SAP BTP Event Mesh or custom OData v4 CDS views requires Basis team change 
                  transports and security vetting (4–6 weeks lead time). Ingesting KONE 24/7 Connected Services streaming brokers 
                  (Kafka/MQTT across KRM and 24/7 Connect gateways) requires Avro schema registry access and sensor jitter de-biasing. 
                  Crucially, German and European Works Councils strictly prohibit algorithmic surveillance of field technicians; 
                  negotiating the <em>Technician Anonymization Airlock</em> takes 4–6 weeks of legal review. 
                  By staging static data in an isolated EU sandbox in Phase 0 (Weeks 1–4) and stitching the entity graph in Phase 1 (Weeks 5–8), 
                  we eliminate risk, guarantee compliance, and deliver rock-solid ROI by Week 20.
                </div>
              </div>
            </div>
          </div>

          <!-- Q18 -->
          <div class="qa-card" data-cat="enterprise">
            <div class="qa-header" onclick="toggleQA(this)">
              <div class="qa-title-wrap">
                <span class="qa-category-tag">SAP / Salesforce / Adobe</span>
                <div class="qa-question">18. "How does the Assisted Decisioning System specifically support our 'Life, Upgraded in ONE Week' (ONE Week MOD) campaign?"</div>
              </div>
              <div class="qa-toggle-icon">&darr;</div>
            </div>
            <div class="qa-body">
              <div class="qa-block">
                <div class="qa-subhead">Executive Pitch (30 Seconds)</div>
                <div class="qa-exec-pitch">
                  "ONE Week MOD is the ideal flagship use case. Out of 10M+ aging elevators across Europe, the system identifies 
                  the 20,061 addressable residential MonoSpace LIS units across our 6 frontlines (starting with 9,039 in Italy & Iberia). 
                  It flags units facing repeat door cycle faults, confirms engineering fitment (<= 7 floors, shaft dimensions), 
                  and automatically synthesizes localized Adobe battlecards guaranteeing <= 7 days downtime, 74% energy savings, 
                  and 80% proactive issue detection."
                </div>
              </div>
              <div class="qa-block">
                <div class="qa-subhead">Deep Technical Defense</div>
                <div class="qa-deep-dive">
                  The ADS engine operationalizes the campaign package charter end-to-end:
                  <ol style="margin-top:6px; padding-left:18px; line-height:1.55;">
                    <li><strong>Sense:</strong> Ingests door dwell cycles, leveling faults, and vibration telemetry from aging MonoSpace LIS units via KONE 24/7 Connected Services.</li>
                    <li><strong>Diagnose & Prioritise:</strong> Filters residential assets with &le;7 floors and 15+ year vintage. Distinguishes active maintenance accounts nearing renewal from pure lost accounts (+5 yrs lost service).</li>
                    <li><strong>Simulate:</strong> Monte Carlo optimizer evaluates technician labor capacity (7-day install SLA) and depot inventory availability against media response across Meta Advantage+, LinkedIn ABA, YouTube VRC, and Spotify.</li>
                    <li><strong>Act:</strong> Connects to SDL Tridion / Adobe AEM Assets to dynamically generate localized Spanish/Italian battlecards and dispatches closed-loop leads into Salesforce Opportunities and SAP FSM field service depot queues.</li>
                  </ol>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         TAB 6: PROTOTYPE VS PRODUCTION MATRIX
         ======================================================================== -->
    <section class="tab-pane" id="pane-matrix">
      <div class="card">
        <div class="card-title">
          <span>Prototype vs. Production Implementation Comparison</span>
          <span class="badge badge-primary">Technical Parity Audit</span>
        </div>
        <div class="card-subtitle">
          Transparent technical comparison between the current boardroom prototype and the full enterprise build
        </div>

        <table class="data-table">
          <thead>
            <tr>
              <th style="width:20%;">System Dimension</th>
              <th style="width:38%;">Current Boardroom Prototype (index.html)</th>
              <th style="width:42%;">Target Enterprise Production Build</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Architecture & Runtime</strong></td>
              <td>Standalone single-file HTML5/JS application running client-side with zero external runtime dependencies.</td>
              <td>Distributed microservice mesh (Next.js 15, FastAPI, Ray Cluster) deployed on AWS/Azure Kubernetes (EKS/AKS).</td>
            </tr>
            <tr>
              <td><strong>Data Layer & Persistence</strong></td>
              <td>In-memory synthetic dataset (<code>kone_synthetic_dataset.json</code>) with real-time browser session mutations.</td>
              <td>Snowflake / Databricks Lakehouse with dbt semantic layer and Neo4j / Neptune Entity Knowledge Graph.</td>
            </tr>
            <tr>
              <td><strong>IoT Telemetry Feed</strong></td>
              <td>Simulated incremental/decremental jitter across 38 Spanish pilot buildings with realistic vibration and door cycles.</td>
              <td>Live Kafka / Azure Event Hubs streaming from &gt;45% connected elevator base via AWS IoT Core.</td>
            </tr>
            <tr>
              <td><strong>Decision & Simulation Engine</strong></td>
              <td>Client-side Monte Carlo curve generator and Bayesian update calculator running in JavaScript Web Workers.</td>
              <td>Distributed Python PyMC / Stan Bayesian inference cluster and Ray multi-node Monte Carlo optimization solvers.</td>
            </tr>
            <tr>
              <td><strong>Enterprise Integrations</strong></td>
              <td>Interactive UI modals demonstrating mock JSON payload generation for Salesforce, SAP FSM, and Adobe Workfront.</td>
              <td>Production bidirectional REST/OData connectors with Salesforce CPQ, SAP S/4HANA Clean Core, and Adobe Workfront.</td>
            </tr>
            <tr>
              <td><strong>Content Supply Chain</strong></td>
              <td>Curated KONE growth ingredients (EcoDisc, UltraRope, DX Class, One Week Mod) and Madrid pilot asset previews.</td>
              <td>Direct integration with Adobe Experience Manager (AEM Assets) and Adobe Firefly / Express for automated localization.</td>
            </tr>
            <tr>
              <td><strong>Security & Auth</strong></td>
              <td>Local session state with client-side credential reset; no PII stored.</td>
              <td>Enterprise Microsoft Entra ID (SSO) with MFA, Row-Level Security (RLS) by SAP Company Code, ISO 27001 & GDPR audit logging.</td>
            </tr>
            <tr>
              <td><strong>Delivery Timeline</strong></td>
              <td><span class="badge badge-success">Completed & Ready to Demo</span></td>
              <td><span class="badge badge-primary">Phased 12-week MVP &bull; 48-week Global Rollout</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

  </main>

  <!-- ============================================================================
       BOTTOM FOOTER
       ========================================================================== -->
  <footer class="bottom-footer">
    <div class="footer-left">
      <img class="brand-logo-img" src="data:image/jpeg;base64,{kone_logo_b64}" alt="KONE" style="height:22px;">
      <span><strong>KONE Assisted Decisioning System (ADS)</strong> · Technical Architecture & Client Defense Reference</span>
    </div>
    <div style="display:flex; align-items:center; gap:16px;">
      <span>Prepared for KONE Global Marketing Leadership</span>
      <div class="divider-vert" style="height:20px;"></div>
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="font-size:11px; color:var(--color-neutral-6);">Designed & Engineered by</span>
        <img class="cognizant-logo-img" src="data:image/png;base64,{cognizant_logo_b64}" alt="Cognizant Moment">
      </div>
    </div>
  </footer>

  <!-- ============================================================================
       INTERACTIVE LOGIC SCRIPT
       ========================================================================== -->
  <script>
    // Tab switching logic
    function switchTab(tabId) {{
      const tabs = document.querySelectorAll('.tab-btn');
      const panes = document.querySelectorAll('.tab-pane');
      
      tabs.forEach(t => t.classList.remove('active'));
      panes.forEach(p => p.classList.remove('active'));
      
      const targetPane = document.getElementById('pane-' + tabId);
      if (targetPane) {{
        targetPane.classList.add('active');
      }}
      
      // Highlight matching tab
      const navBar = document.getElementById('techNavTabs');
      const buttons = navBar.querySelectorAll('.tab-btn');
      const tabIndexMap = {{
        'exec': 0,
        'arch': 1,
        'data': 2,
        'roadmap': 3,
        'defense': 4,
        'matrix': 5
      }};
      if (buttons[tabIndexMap[tabId]]) {{
        buttons[tabIndexMap[tabId]].classList.add('active');
      }}
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // Q&A Accordion toggle
    function toggleQA(headerEl) {{
      const card = headerEl.closest('.qa-card');
      card.classList.toggle('open');
    }}

    // Q&A Category Filter
    let currentCategory = 'all';
    function setQACategory(cat, btn) {{
      currentCategory = cat;
      const btns = document.querySelectorAll('.filter-btn');
      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterQA();
    }}

    // Search and filter combined
    function filterQA() {{
      const query = document.getElementById('qaSearchInput').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.qa-card');

      cards.forEach(card => {{
        const cat = card.getAttribute('data-cat');
        const text = card.innerText.toLowerCase();

        const matchesCat = (currentCategory === 'all' || cat === currentCategory);
        const matchesQuery = (query === '' || text.includes(query));

        if (matchesCat && matchesQuery) {{
          card.style.display = 'block';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    // Data Readiness Assessment Calculation
    function updateReadiness() {{
      const telemetry = document.getElementById('chk-telemetry').checked;
      const sap = document.getElementById('chk-sap').checked;
      const crm = document.getElementById('chk-crm').checked;
      const fsm = document.getElementById('chk-fsm').checked;
      const adobe = document.getElementById('chk-adobe').checked;

      let score = 0;
      if (telemetry) score += 25;
      if (sap) score += 25;
      if (crm) score += 20;
      if (fsm) score += 15;
      if (adobe) score += 15;

      const numEl = document.getElementById('calcScoreNum');
      const labelEl = document.getElementById('calcScoreLabel');
      const descEl = document.getElementById('calcScoreDesc');
      const timeEl = document.getElementById('calcTimeline');

      numEl.innerText = score + '%';

      if (score >= 90) {{
        numEl.style.color = '#10b981';
        labelEl.innerText = 'Enterprise Production Ready';
        descEl.innerText = 'All 5 data domains connected. Ready for full multi-market automated decisioning and closed-loop field dispatch.';
        timeEl.innerHTML = 'Estimated Discovery: <strong>3–4 Weeks</strong> &bull; Enterprise Pilot: <strong>16–20 Weeks</strong>';
      }} else if (score >= 70) {{
        numEl.style.color = 'var(--color-primary-1)';
        labelEl.innerText = 'Strong MVP Baseline';
        descEl.innerText = 'Core telemetry, ERP, and CRM connected. Ready for Phase 1 MVP (Sense, Diagnose, Prioritise, and Simulate) with Iberian pilot cohort.';
        timeEl.innerHTML = 'Estimated Discovery: <strong>4 Weeks</strong> &bull; MVP Launch: <strong>12 Weeks</strong>';
      }} else if (score >= 45) {{
        numEl.style.color = '#f59e0b';
        labelEl.innerText = 'Foundation in Progress';
        descEl.innerText = 'Basic ERP/CRM records present, but missing live telemetry or field feedback. System relies on synthetic prior models.';
        timeEl.innerHTML = 'Estimated Discovery: <strong>6 Weeks</strong> &bull; MVP Launch: <strong>16 Weeks</strong>';
      }} else {{
        numEl.style.color = '#dc3545';
        labelEl.innerText = 'High Data Fragmentation';
        descEl.innerText = 'Critical data gaps across telemetry and ERP. Requires Phase 0 Entity Resolution and Lakehouse foundational sprint.';
        timeEl.innerHTML = 'Estimated Discovery: <strong>8 Weeks</strong> &bull; Prerequisite Data Sprint Required';
      }}
    }}

    // Default open first 2 Q&As for immediate visual guidance
    document.addEventListener('DOMContentLoaded', () => {{
      const firstCards = document.querySelectorAll('.qa-card');
      if (firstCards.length > 0) firstCards[0].classList.add('open');
      if (firstCards.length > 1) firstCards[1].classList.add('open');
    }});
  </script>
</body>
</html>
"""

    output_path = 'tech-architecture.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✓ Created {output_path} ({len(html_content)} bytes)")

if __name__ == "__main__":
    build_tech_primer()
