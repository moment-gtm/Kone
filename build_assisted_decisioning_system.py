#!/usr/bin/env python3
"""
KONE Assisted Decisioning System Builder
Rescripts the KONE Marketing OS as an 8-stage Assisted Decisioning System (Growth Control Tower)
modeled after GTM Tower (/Users/191561/Documents/play/GTM Tower).
Uses the official attached KONE logo and the exact PocketUI Design System color palette.
Moves the Cognizant logo to the bottom footer.
Generates standalone redistributable HTML files (index.html & kone-marketing-os.html).
"""

import json
import base64
import os
import sys

def build_app():
    # Load synthetic dataset
    with open('kone_synthetic_dataset.json', 'r', encoding='utf-8') as f:
        synthetic_data = json.load(f)

    json_str = json.dumps(synthetic_data, ensure_ascii=False)

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
  <title>KONE Assisted Decisioning System | Growth Control Tower</title>
  <link rel="icon" type="image/jpeg;base64,{kone_logo_b64}">
  <style>
    /* ============================================================================
       KONE DESIGN SYSTEM (Light Theme from https://www.kone.com/global/en/innovation.html)
       ========================================================================== */
    :root {{
      /* Extracted PocketUI KONE Color Scale */
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

      /* Semantic status mapping */
      --color-success-primary: #0a7a3b;
      --color-success-surface: #e6f9f0;
      --color-warning-primary: #b37400;
      --color-warning-surface: #fff8e6;
      --color-danger-primary: #dc2626;
      --color-danger-surface: #feeceb;

      /* Typography */
      --font-heading: 'VideoJS', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-body: 'Inter Regular', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-font-3: 'Inter SemiBold', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-font-4: 'KONE Information', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-font-5: 'Consolas', ui-monospace, Menlo, Monaco, monospace;

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
      --shadow-3: 0 0 3px rgba(0,0,0,.15);
      --shadow-4: 0 4px 10px rgba(0,0,0,.1);
      --shadow-5: 0 0 1px 0 rgba(20,20,20,.06),0 10px 15px -3px rgba(20,20,20,.08),0 4px 6px -2px rgba(20,20,20,.04);
      --shadow-6: 0 3px 5px rgba(0,0,0,.12);
      --shadow-blue-glow: 0 4px 14px rgba(20, 80, 245, 0.25);

      /* Light Theme Surface Tokens matching kone.com */
      --app-bg: #f7f9fc;
      --card-bg: #ffffff;
      --card-border: var(--color-neutral-2);
      --glass-surface: rgba(255, 255, 255, 0.92);
      --glass-surface-hover: rgba(245, 248, 255, 0.98);
      --glass-border: rgba(20, 80, 245, 0.12);
      --glass-border-focus: rgba(20, 80, 245, 0.6);
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
      background: #fafbfc;
      background-image: 
        radial-gradient(circle at 10% 8%, rgba(20, 80, 245, 0.04) 0%, transparent 40%),
        radial-gradient(circle at 90% 92%, rgba(102, 168, 204, 0.05) 0%, transparent 45%),
        linear-gradient(180deg, #f7faff 0%, #fafbfc 100%);
      color: var(--text-high);
      font-family: var(--font-body);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
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
      gap: var(--space-3);
      padding: 3px 8px;
      border-radius: var(--radius-2);
      font-size: 11px;
      font-weight: 600;
      line-height: 1.2;
      letter-spacing: 0.02em;
    }}
    .badge-primary {{ background: var(--color-primary-7); color: var(--color-primary-1); border: 1px solid var(--color-primary-9); }}
    .badge-success {{ background: var(--color-success-surface); color: var(--color-success-primary); border: 1px solid rgba(10, 122, 59, 0.3); }}
    .badge-warning {{ background: var(--color-warning-surface); color: var(--color-warning-primary); border: 1px solid rgba(179, 116, 0, 0.3); }}
    .badge-danger {{ background: var(--color-danger-surface); color: var(--color-danger-primary); border: 1px solid rgba(220, 38, 38, 0.3); }}
    .badge-neutral {{ background: var(--color-neutral-5); color: var(--color-neutral-7); border: 1px solid var(--color-neutral-2); }}

    /* ============================================================================
       TOP CHROME (Header)
       ========================================================================== */
    .top-chrome {{
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 62px;
      padding: 0 var(--space-13);
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--color-neutral-2);
      box-shadow: 0 2px 10px rgba(0, 6, 31, 0.04);
    }}
    .top-left {{
      display: flex;
      align-items: center;
      gap: var(--space-8);
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
      border-radius: var(--radius-2);
      box-shadow: 0 1px 4px rgba(0, 6, 31, 0.1);
    }}
    .divider-vert {{
      width: 1px;
      height: 28px;
      background: var(--color-neutral-2);
      margin: 0 var(--space-2);
    }}
    .system-title-wrap {{
      display: flex;
      flex-direction: column;
    }}
    .system-title {{
      font-family: var(--font-heading);
      font-size: 15px;
      font-weight: 700;
      color: var(--color-primary-2);
      letter-spacing: -0.01em;
      display: flex;
      align-items: center;
      gap: var(--space-5);
    }}
    .system-subtitle {{
      font-size: 11px;
      color: var(--color-neutral-6);
      margin-top: 1px;
    }}
    .surface-switcher {{
      display: flex;
      background: var(--color-neutral-5);
      padding: 3px;
      border-radius: var(--radius-4);
      border: 1px solid var(--color-neutral-2);
      gap: 3px;
    }}
    .surface-btn {{
      background: transparent;
      border: none;
      color: var(--color-neutral-7);
      padding: 6px 14px;
      border-radius: var(--radius-3);
      font-family: var(--font-font-3);
      font-size: 12px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }}
    .surface-btn:hover {{
      color: var(--color-primary-1);
    }}
    .surface-btn.active {{
      background: var(--color-primary-1);
      color: #ffffff;
      box-shadow: 0 2px 6px rgba(20, 80, 245, 0.25);
    }}
    .top-right {{
      display: flex;
      align-items: center;
      gap: var(--space-8);
    }}
    .telemetry-pill {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: var(--color-primary-3);
      border: 1px solid var(--color-primary-8);
      padding: 5px 12px;
      border-radius: var(--radius-5);
      font-size: 11.5px;
      color: var(--color-primary-20);
      font-weight: 500;
    }}
    .pulse-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2);
      animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
      0% {{ box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.5); }}
      70% {{ box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }}
      100% {{ box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }}
    }}
    .btn-chrome {{
      background: #ffffff;
      border: 1px solid var(--color-neutral-2);
      color: var(--color-primary-2);
      padding: 6px 12px;
      border-radius: var(--radius-3);
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }}
    .btn-chrome:hover {{
      background: var(--color-primary-3);
      border-color: var(--color-primary-8);
      color: var(--color-primary-1);
    }}

    /* ============================================================================
       APPLICATION WORKSPACE LAYOUT
       ========================================================================== */
    .app-body {{
      display: flex;
      flex: 1;
      min-height: calc(100vh - 62px - 48px);
    }}

    /* 8-STAGE VERTICAL FLYWHEEL RAIL */
    .stage-rail {{
      width: 255px;
      min-width: 255px;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-right: 1px solid var(--color-neutral-2);
      display: flex;
      flex-direction: column;
      padding: var(--space-8) 0;
      overflow-y: auto;
    }}
    .stage-rail-header {{
      padding: 6px 16px 10px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--color-neutral-6);
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--color-neutral-2);
      margin-bottom: var(--space-5);
      background: rgba(245, 248, 255, 0.4);
    }}
    .stage-btn {{
      display: flex;
      align-items: center;
      gap: var(--space-7);
      padding: 10px 16px;
      border: none;
      border-left: 3px solid transparent;
      background: transparent;
      color: var(--color-neutral-7);
      cursor: pointer;
      text-align: left;
      transition: all 0.15s ease;
      width: 100%;
    }}
    .stage-btn:hover {{
      background: rgba(20, 80, 245, 0.04);
      color: var(--color-primary-1);
    }}
    .stage-btn.active {{
      background: var(--color-primary-7);
      border-left-color: var(--color-primary-1);
      color: var(--color-primary-1);
      font-weight: 600;
    }}
    .stage-num {{
      width: 22px;
      height: 22px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 700;
      background: var(--color-neutral-5);
      color: var(--color-neutral-6);
      border: 1px solid var(--color-neutral-2);
      flex-shrink: 0;
      transition: all 0.15s ease;
    }}
    .stage-btn.active .stage-num {{
      background: var(--color-primary-1);
      border-color: var(--color-primary-1);
      color: #ffffff;
    }}
    .stage-label-wrap {{
      display: flex;
      flex-direction: column;
    }}
    .stage-name {{
      font-size: 12.5px;
      font-family: var(--font-font-3);
      color: inherit;
    }}
    .stage-sub {{
      font-size: 10.5px;
      color: var(--color-neutral-6);
      margin-top: 1px;
    }}

    /* MAIN STAGE WORKSPACE */
    .stage-workspace {{
      flex: 1;
      padding: var(--space-13) var(--space-15);
      overflow-y: auto;
      max-width: 1550px;
      margin: 0 auto;
      width: 100%;
    }}

    /* STAGE BANNER */
    .stage-banner {{
      background: #ffffff;
      border: 1px solid var(--color-neutral-2);
      border-radius: var(--radius-4);
      padding: var(--space-11) var(--space-14);
      margin-bottom: var(--space-13);
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: var(--shadow-5);
    }}
    .stage-question-tag {{
      font-size: 11px;
      font-weight: 700;
      color: var(--color-primary-1);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 3px;
    }}
    .stage-question-text {{
      font-family: var(--font-heading);
      font-size: 19px;
      font-weight: 700;
      color: var(--color-primary-2);
      letter-spacing: -0.01em;
    }}
    .stage-question-sub {{
      font-size: 12px;
      color: var(--color-neutral-6);
      margin-top: 3px;
    }}
    .stage-badge-dot {{
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      margin-right: 6px;
    }}

    /* GLASS CARDS & PANELS */
    .glass-panel {{
      background: #ffffff;
      border: 1px solid var(--color-neutral-2);
      border-radius: var(--radius-4);
      box-shadow: var(--shadow-5);
      padding: var(--space-13);
      margin-bottom: var(--space-13);
    }}
    .panel-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: var(--space-11);
      padding-bottom: var(--space-8);
      border-bottom: 1px solid var(--color-neutral-2);
    }}
    .panel-title {{
      font-family: var(--font-heading);
      font-size: 14.5px;
      font-weight: 700;
      color: var(--color-primary-2);
      letter-spacing: -0.01em;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .panel-subtitle {{
      font-size: 12px;
      color: var(--color-neutral-6);
      margin-top: 2px;
    }}

    /* STAT CARDS */
    .stat-card {{
      background: #ffffff;
      border: 1px solid var(--color-neutral-2);
      border-radius: var(--radius-4);
      padding: var(--space-11);
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-5);
      transition: all 0.2s ease;
    }}
    .stat-card:hover {{
      border-color: var(--color-primary-9);
      box-shadow: 0 6px 16px rgba(20, 80, 245, 0.08);
      transform: translateY(-1px);
    }}
    .stat-label {{
      font-size: 11px;
      font-weight: 600;
      color: var(--color-neutral-6);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 4px;
    }}
    .stat-value {{
      font-family: var(--font-heading);
      font-size: 22px;
      font-weight: 700;
      color: var(--color-primary-2);
      letter-spacing: -0.01em;
      margin-bottom: 2px;
    }}
    .stat-sub {{
      font-size: 11.5px;
      color: var(--color-neutral-6);
    }}

    /* GRIDS */
    .grid-2 {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: var(--space-11); }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-11); }}
    .grid-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-11); }}

    /* TABLES */
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 12.5px;
    }}
    .data-table th {{
      text-align: left;
      padding: 10px 12px;
      color: var(--color-neutral-7);
      background: var(--color-primary-3);
      font-weight: 600;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      border-bottom: 1px solid var(--color-primary-8);
    }}
    .data-table td {{
      padding: 11px 12px;
      border-bottom: 1px solid var(--color-neutral-2);
      color: var(--text-high);
      background: #ffffff;
      vertical-align: middle;
    }}
    .data-table tr:hover td {{
      background: var(--color-primary-6);
    }}

    /* BUTTONS */
    .btn-action {{
      background: var(--color-primary-1);
      color: #ffffff;
      border: none;
      padding: 7px 14px;
      border-radius: var(--radius-3);
      font-family: var(--font-font-3);
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
      box-shadow: 0 2px 6px rgba(20, 80, 245, 0.2);
    }}
    .btn-action:hover {{
      background: var(--color-primary-15);
      box-shadow: 0 4px 12px rgba(20, 80, 245, 0.3);
      transform: translateY(-1px);
    }}
    .btn-outline {{
      background: #ffffff;
      color: var(--color-primary-2);
      border: 1px solid var(--color-neutral-2);
      padding: 6px 12px;
      border-radius: var(--radius-3);
      font-family: var(--font-font-3);
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }}
    .btn-outline:hover {{
      background: var(--color-primary-3);
      border-color: var(--color-primary-8);
      color: var(--color-primary-1);
    }}

    /* SLIDER & CONTROLS */
    .slider-control {{
      display: flex;
      flex-direction: column;
      gap: var(--space-5);
    }}
    .slider-header {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
    }}
    .slider-val {{
      font-family: var(--font-heading);
      font-size: 26px;
      font-weight: 800;
      color: var(--color-primary-1);
    }}
    input[type=range] {{
      -webkit-appearance: none;
      width: 100%;
      height: 6px;
      background: var(--color-neutral-2);
      border-radius: var(--radius-1);
      outline: none;
    }}
    input[type=range]::-webkit-slider-thumb {{
      -webkit-appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: var(--color-primary-1);
      cursor: pointer;
      box-shadow: 0 2px 6px rgba(20, 80, 245, 0.4);
      transition: transform 0.1s ease;
    }}
    input[type=range]::-webkit-slider-thumb:hover {{
      transform: scale(1.15);
    }}

    /* ============================================================================
       BOTTOM PERSISTENT CHROME (Footer with Cognizant mark & Chained CTA)
       ========================================================================== */
    .bottom-chrome {{
      position: sticky;
      bottom: 0;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 48px;
      padding: 0 var(--space-13);
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-top: 1px solid var(--color-neutral-2);
      font-size: 11.5px;
      color: var(--color-neutral-6);
      box-shadow: 0 -2px 10px rgba(0, 6, 31, 0.04);
    }}
    .bottom-left {{
      display: flex;
      align-items: center;
      gap: var(--space-8);
    }}
    .bottom-left button {{
      background: transparent;
      border: none;
      color: var(--color-neutral-7);
      cursor: pointer;
      font-size: 11.5px;
      font-family: inherit;
      padding: 2px 4px;
      border-radius: var(--radius-1);
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .bottom-left button:hover {{
      color: var(--color-primary-1);
      background: rgba(20, 80, 245, 0.05);
    }}
    .cognizant-footer-badge {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: var(--color-primary-3);
      border: 1px solid var(--color-primary-8);
      padding: 2px 8px;
      border-radius: var(--radius-2);
      color: var(--color-primary-2);
      font-size: 11px;
    }}
    .bottom-right {{
      display: flex;
      align-items: center;
      gap: var(--space-8);
    }}
    .current-stage-q {{
      font-size: 12px;
      color: var(--color-neutral-7);
      font-style: italic;
    }}
    .chained-btn {{
      background: var(--color-primary-1);
      color: #ffffff;
      border: none;
      padding: 7px 16px;
      border-radius: var(--radius-3);
      font-family: var(--font-font-3);
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      box-shadow: 0 2px 8px rgba(20, 80, 245, 0.25);
    }}
    .chained-btn:hover {{
      background: var(--color-primary-15);
      box-shadow: 0 4px 14px rgba(20, 80, 245, 0.35);
      transform: translateY(-1px);
    }}

    /* ============================================================================
       MODALS & DRAWERS
       ========================================================================== */
    .modal-backdrop {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 6, 31, 0.45);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
      z-index: 200;
      display: none;
      align-items: center;
      justify-content: center;
    }}
    .modal-dialog {{
      background: #ffffff;
      border: 1px solid var(--color-neutral-2);
      box-shadow: 0 20px 48px rgba(0, 6, 31, 0.16);
      border-radius: var(--radius-4);
      width: 90%;
      max-width: 680px;
      max-height: 85vh;
      overflow-y: auto;
      padding: var(--space-15);
      color: var(--text-high);
    }}

    .drawer-backdrop {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 6, 31, 0.35);
      backdrop-filter: blur(4px);
      -webkit-backdrop-filter: blur(4px);
      z-index: 200;
      display: none;
    }}
    .drawer-panel {{
      position: fixed;
      top: 0; right: -560px; bottom: 0;
      width: 560px;
      background: #ffffff;
      border-left: 1px solid var(--color-neutral-2);
      box-shadow: -10px 0 35px rgba(0, 6, 31, 0.12);
      z-index: 201;
      padding: var(--space-15);
      overflow-y: auto;
      transition: right 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      color: var(--text-high);
    }}
    .drawer-panel.open {{
      right: 0;
    }}

    /* TOAST NOTIFICATION */
    .toast-notification {{
      position: fixed;
      bottom: 60px;
      right: 24px;
      background: #ffffff;
      border: 1px solid var(--color-primary-8);
      box-shadow: 0 8px 24px rgba(0, 6, 31, 0.15);
      color: var(--color-primary-2);
      padding: 10px 18px;
      border-radius: var(--radius-3);
      font-size: 12.5px;
      font-weight: 500;
      display: none;
      align-items: center;
      gap: 10px;
      z-index: 300;
      animation: toastIn 0.2s ease-out;
    }}
    @keyframes toastIn {{
      from {{ transform: translateY(12px); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}

    .scene-pill {{
      background: #ffffff;
      border: 1px solid var(--color-neutral-2);
      color: var(--color-neutral-7);
      padding: 6px 14px;
      border-radius: var(--radius-5);
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .scene-pill:hover {{
      border-color: var(--color-primary-9);
      color: var(--color-primary-1);
    }}
    .scene-pill.active {{
      background: var(--color-primary-1);
      border-color: var(--color-primary-1);
      color: #ffffff;
      box-shadow: 0 2px 6px rgba(20, 80, 245, 0.25);
    }}

  </style>
</head>
<body>

  <!-- ============================================================================
       TOP CHROME (Featuring Attached KONE Official Logo)
       ========================================================================== -->
  <header class="top-chrome">
    <div class="top-left">
      <div class="brand-mark" onclick="goStage(1)" title="KONE Assisted Decisioning System">
        <!-- Attached official KONE logo rendered directly -->
        <img class="brand-logo-img" src="data:image/jpeg;base64,{kone_logo_b64}" alt="KONE">
      </div>
      <div class="divider-vert"></div>
      <div class="system-title-wrap">
        <div class="system-title">
          Assisted Decisioning System
          <span class="badge badge-primary">GCT v2.4</span>
        </div>
        <div class="system-subtitle">KONE Growth Control Tower · Commercial Intelligence Layer</div>
      </div>
    </div>

    <!-- Center Surface Switcher -->
    <div class="surface-switcher">
      <button class="surface-btn active" id="btnSurfaceAds" onclick="switchSurface('ads')">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
        Assisted Decisioning System
      </button>
      <button class="surface-btn" id="btnSurfaceScript" onclick="switchSurface('script')">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
        Script & Story Walkthrough
      </button>
    </div>

    <div class="top-right">
      <div class="telemetry-pill">
        <span class="pulse-dot"></span>
        <span class="num">38</span> Buildings Telemetry Active · 7 Markets
      </div>
      <button class="btn-chrome" onclick="openAskModal()">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        Ask the ADS
      </button>
      <button class="btn-chrome" onclick="openCoverageDrawer()">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
        Coverage
      </button>
      <button class="btn-chrome" onclick="resetSession()">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/></svg>
        Reset
      </button>
    </div>
  </header>

  <!-- ============================================================================
       APPLICATION WORKSPACE
       ========================================================================== -->
  <div class="app-body">

    <!-- LEFT STAGE RAIL (8 Stages of the Assisted Decisioning Flywheel) -->
    <nav class="stage-rail" id="stageRail">
      <div class="stage-rail-header">Decision Flywheel</div>
      <button class="stage-btn active" id="railBtn1" onclick="goStage(1)">
        <span class="stage-num num">1</span>
        <div class="stage-label-wrap">
          <span class="stage-name">Sense</span>
          <span class="stage-sub">Portfolio signals</span>
        </div>
      </button>
      <button class="stage-btn" id="railBtn2" onclick="goStage(2)">
        <span class="stage-num num">2</span>
        <div class="stage-label-wrap">
          <span class="stage-name">Diagnose</span>
          <span class="stage-sub">Why Iberian gap</span>
        </div>
      </button>
      <button class="stage-btn" id="railBtn3" onclick="goStage(3)">
        <span class="stage-num num">3</span>
        <div class="stage-label-wrap">
          <span class="stage-name">Prioritise</span>
          <span class="stage-sub">Scored pipeline</span>
        </div>
        <span class="stage-badge-dot" id="prioritiseShiftDot" style="display:none;" title="Confidence shifted by session actions"></span>
      </button>
      <button class="stage-btn" id="railBtn4" onclick="goStage(4)">
        <span class="stage-num num">4</span>
        <div class="stage-label-wrap">
          <span class="stage-name">Simulate</span>
          <span class="stage-sub">€10M allocation</span>
        </div>
      </button>
      <button class="stage-btn" id="railBtn5" onclick="goStage(5)">
        <span class="stage-num num">5</span>
        <div class="stage-label-wrap">
          <span class="stage-name">Orchestrate</span>
          <span class="stage-sub">Turn to action</span>
        </div>
        <span class="badge badge-primary num" id="orchestrateCountBadge" style="font-size:9px; padding:2px 5px; margin-left:auto;">1</span>
      </button>
      <button class="stage-btn" id="railBtn6" onclick="goStage(6)">
        <span class="stage-num num">6</span>
        <div class="stage-label-wrap">
          <span class="stage-name">Replicate</span>
          <span class="stage-sub">Scale playbooks</span>
        </div>
      </button>
      <button class="stage-btn" id="railBtn7" onclick="goStage(7)">
        <span class="stage-num num">7</span>
        <div class="stage-label-wrap">
          <span class="stage-name">Optimise</span>
          <span class="stage-sub">Mid-flight tuning</span>
        </div>
      </button>
      <button class="stage-btn" id="railBtn8" onclick="goStage(8)">
        <span class="stage-num num">8</span>
        <div class="stage-label-wrap">
          <span class="stage-name">Learn</span>
          <span class="stage-sub">Closed-loop log</span>
        </div>
        <span class="badge badge-success num" id="learnCountBadge" style="font-size:9px; padding:2px 5px; margin-left:auto;">7</span>
      </button>
    </nav>

    <!-- MAIN VIEW CONTAINER -->
    <main class="stage-workspace" id="mainWorkspace">

      <!-- SURFACE 1: 8 STAGES OF ASSISTED DECISIONING SYSTEM -->
      <div id="surfaceAds">
        <div id="stageContentArea"></div>
      </div>

      <!-- SURFACE 2: STORY & SCRIPT WALKTHROUGH -->
      <div id="surfaceScript" style="display: none;">
        <div class="glass-panel">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
                Executive Workshop Script Narrative (Two Acts · 9 Scenes)
              </div>
              <div class="panel-subtitle">Audience: Petra (CMO), Hans (Global Customer Marketing Director) & Extended Marketing Leadership Team</div>
            </div>
            <span class="badge badge-primary">Monday 1 February 2027 Scenario Clock</span>
          </div>
          
          <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px;" id="scriptScenePills"></div>

          <div style="background: #ffffff; border: 1px solid var(--color-neutral-2); box-shadow: var(--shadow-5); border-radius: var(--radius-4); overflow: hidden;">
            <div id="sceneBannerImg" style="height: 180px; position: relative; background-size: cover; background-position: center;">
              <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,6,31,0.1) 0%, rgba(0,6,31,0.65) 100%); display: flex; align-items: flex-end; justify-content: space-between; padding: 16px 20px;">
                <span class="badge" id="sceneImageTag" style="background: #ffffff; color: var(--color-primary-1); font-weight: 700;">KONE Innovation Visual Context</span>
                <span class="badge" style="background: rgba(0,6,31,0.7); color: #ffffff;" id="sceneMeta">Timecode · Speaker</span>
              </div>
            </div>

            <div style="padding: var(--space-13);">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 14px;">
                <div>
                  <span class="badge badge-primary" id="sceneAct">Act 1: The Monday Morning View</span>
                  <h3 style="font-size: 18px; color: var(--color-primary-2); margin-top: 6px; font-weight: 700;" id="sceneHeadline">Scene Title</h3>
                </div>
                <button class="btn-action" id="btnJumpToStage" onclick="jumpFromScriptToStage()">
                  Open in Decision Flywheel →
                </button>
              </div>

              <div style="background: var(--color-primary-6); border: 1px solid var(--color-primary-8); border-left: 4px solid var(--color-primary-1); padding: 14px 18px; border-radius: var(--radius-2); font-size: 14px; line-height: 1.6; color: var(--color-primary-2); font-style: italic; margin-bottom: 16px;" id="sceneDialogue">
                Dialogue excerpt...
              </div>

              <div style="display: flex; gap: var(--space-8);">
                <div style="flex: 1; background: #ffffff; padding: 12px 16px; border-radius: var(--radius-3); border: 1px solid var(--color-neutral-2); box-shadow: var(--shadow-5);">
                  <div style="font-size: 11px; text-transform: uppercase; color: var(--color-primary-1); font-weight: 700;">Executive Takeaway</div>
                  <div style="font-size: 12.5px; color: var(--text-high); margin-top: 4px; line-height: 1.45;" id="sceneTakeaway">Takeaway text</div>
                </div>
                <div style="flex: 1; background: #ffffff; padding: 12px 16px; border-radius: var(--radius-3); border: 1px solid var(--color-neutral-2); box-shadow: var(--shadow-5);">
                  <div style="font-size: 11px; text-transform: uppercase; color: var(--color-primary-1); font-weight: 700;">Workshop Prompt</div>
                  <div style="font-size: 12.5px; color: var(--text-high); margin-top: 4px; line-height: 1.45;" id="scenePrompt">Discussion prompt</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </main>
  </div>

  <!-- ============================================================================
       BOTTOM PERSISTENT CHROME (Cognizant Logo Relocated Here)
       ========================================================================== -->
  <footer class="bottom-chrome">
    <div class="bottom-left">
      <button type="button" onclick="openCoverageDrawer()">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/></svg>
        Requirement Coverage · 14 FRs · 9 Scenes
      </button>
      <span>·</span>
      <button type="button" onclick="resetSession()">Reset session</button>
      <span>·</span>
      <span>Synthetic data · rule-based logic · no live API integrations</span>
      <span>·</span>
      <!-- Cognizant logo and co-brand credit relocated to bottom -->
      <span style="display:inline-flex; align-items:center; gap:6px;">
        <span>Built by</span>
        <span class="cognizant-footer-badge" style="background:#ffffff; border:1px solid var(--color-primary-8); padding:2px 8px; border-radius:var(--radius-2); display:inline-flex; align-items:center; box-shadow:0 1px 2px rgba(0,0,0,0.05);">
          <img src="data:image/png;base64,{cognizant_logo_b64}" alt="Cognizant Moment" style="height:19px; width:auto; vertical-align:middle; display:inline-block; object-fit:contain;" />
        </span>
        <span>for KONE Global Marketing</span>
      </span>
    </div>

    <div class="bottom-right">
      <span class="current-stage-q" id="bottomStageQuestion">Where should we focus next?</span>
      <button class="chained-btn" id="btnChainedAction" onclick="executeChainedAction()">
        <span id="chainedActionLabel">Next: Diagnose why Iberia is missing plan</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
      </button>
    </div>
  </footer>

  <!-- ============================================================================
       MODALS & DRAWERS
       ========================================================================== -->

  <!-- ASK THE ADS MODAL -->
  <div class="modal-backdrop" id="askModal" onclick="closeAskModal()">
    <div class="modal-dialog" onclick="event.stopPropagation()">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div style="display: flex; align-items: center; gap: 8px;">
          <div style="background: rgba(20, 80, 245, 0.2); width: 28px; height: 28px; border-radius: var(--radius-2); display: flex; align-items: center; justify-content: center; color: var(--color-primary-1);">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
          </div>
          <div>
            <h3 style="font-size: 16px; color: var(--color-primary-2);">Ask the Assisted Decisioning System</h3>
            <p style="font-size: 11.5px; color: var(--text-dim);">The executive front door — select a strategic question to receive evidence and jump to the stage that executes it.</p>
          </div>
        </div>
        <button class="btn-outline" style="padding: 4px 8px;" onclick="closeAskModal()">✕</button>
      </div>

      <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 18px;" id="askQuestionsList"></div>

      <div id="askAnswerBox" style="display: none; background: rgba(18, 38, 88, 0.35); border-left: 4px solid var(--color-primary-1); border: 1px solid var(--glass-border); border-left-width: 4px; border-left-color: var(--color-primary-1); padding: 14px; border-radius: var(--radius-3);">
        <div style="font-size: 11px; text-transform: uppercase; color: var(--color-primary-11); font-weight: 700; margin-bottom: 4px;" id="askAnswerTitle">Answer</div>
        <div style="font-size: 13px; line-height: 1.55; color: var(--color-primary-2);" id="askAnswerBody">Body text</div>
        <div style="margin-top: 12px; display: flex; justify-content: flex-end;">
          <button class="btn-action" id="btnAskJump">Go to Stage →</button>
        </div>
      </div>
    </div>
  </div>

  <!-- REQUIREMENT COVERAGE DRAWER -->
  <div class="drawer-backdrop" id="coverageBackdrop" onclick="closeCoverageDrawer()"></div>
  <div class="drawer-panel" id="coverageDrawer">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; border-bottom: 1px solid var(--glass-border); padding-bottom: 12px;">
      <div>
        <h3 style="font-size: 16px; color: var(--color-primary-2);">Requirement & Script Coverage</h3>
        <p style="font-size: 11.5px; color: var(--text-dim);">Traceability matrix: 14 Functional Requirements + 9 Script Scenes</p>
      </div>
      <button class="btn-outline" style="padding: 4px 8px;" onclick="closeCoverageDrawer()">✕</button>
    </div>
    <div style="margin-bottom: 16px;">
      <h4 style="font-size: 12px; text-transform: uppercase; color: var(--color-accent-2); margin-bottom: 8px;">Functional Requirements (FR)</h4>
      <div id="coverageFRList"></div>
    </div>
    <div>
      <h4 style="font-size: 12px; text-transform: uppercase; color: var(--color-accent-2); margin-bottom: 8px;">Script Scenes (SC)</h4>
      <div id="coverageSceneList"></div>
    </div>
  </div>

  <!-- BUILDING INSPECTION MODAL -->
  <div class="modal-backdrop" id="buildingModal" onclick="closeBuildingModal()">
    <div class="modal-dialog" onclick="event.stopPropagation()">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <h3 style="font-size: 16px; color: var(--color-primary-2);" id="bldModalName">Building Title</h3>
        <button class="btn-outline" style="padding: 4px 8px;" onclick="closeBuildingModal()">✕</button>
      </div>
      <div id="bldModalContent"></div>
    </div>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div class="toast-notification" id="toast">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-success-primary)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
    <span id="toastMsg">Action executed successfully.</span>
  </div>

  <!-- ============================================================================
       APPLICATION LOGIC & SYNTHETIC DATA
       ========================================================================== -->
  <script>
    // Injected Synthetic Dataset
    const APP_DATA = {json_str};

    /* ============================================================================
       STAGE DEFINITIONS (The 8-Stage Assisted Decisioning Flywheel)
       ========================================================================== */
    const STAGES = [
      {{ n: 1, key: 'sense', name: 'Sense', q: 'Where should we focus next?', next: 'Diagnose why' }},
      {{ n: 2, key: 'diagnose', name: 'Diagnose', q: 'Why is Iberia underperforming DACH and what should we do about it?', next: 'Prioritise what matters' }},
      {{ n: 3, key: 'prioritise', name: 'Prioritise', q: 'Which opportunities do we fund, and in what order?', next: 'Simulate the decision' }},
      {{ n: 4, key: 'simulate', name: 'Simulate', q: 'How should we allocate the next €10M of growth investment?', next: 'Turn it into action' }},
      {{ n: 5, key: 'orchestrate', name: 'Orchestrate', q: 'How do we turn decisions into action?', next: 'Scale what works' }},
      {{ n: 6, key: 'replicate', name: 'Replicate', q: 'How do we scale what works across markets?', next: 'Optimise the portfolio' }},
      {{ n: 7, key: 'optimise', name: 'Optimise', q: 'How do we keep improving and adjust mid-flight?', next: 'See what we learned' }},
      {{ n: 8, key: 'learn', name: 'Learn', q: 'How does the enterprise get smarter? Closed-loop Institutional Memory', next: 'Back to Prioritise — watch confidence move' }}
    ];

    /* ============================================================================
       OFFICIAL KONE INNOVATION IMAGERY (assets.kone.com)
       Extracted from https://www.kone.com/global/en/innovation.html
       ========================================================================== */
    const KONE_IMAGES = {{
      highrise: "https://assets.kone.com/adobe/assets/urn:aaid:aem:0791f5da-aaf4-41d6-aafb-9f0b84395ac7/as/Highrise%20building%20against%20sky.jpg?width=960&preferwebp=true",
      city_view: "https://assets.kone.com/adobe/assets/urn:aaid:aem:62744e88-e78a-4b6c-bf3d-15c8efd18a50/as/City_view.jpg?width=960&preferwebp=true",
      ultrarope: "https://assets.kone.com/adobe/assets/urn:aaid:aem:20525041-4139-44fe-a12d-848c3a0e7e3c/as/KONE_UltraRope.jpg?width=800&preferwebp=true",
      ecodisc: "https://assets.kone.com/adobe/assets/urn:aaid:aem:102e5c82-0123-4175-8243-96a2b4a74fd0/as/KONE_EcoDisc_technician.jpg?width=800&preferwebp=true",
      dx_car: "https://assets.kone.com/adobe/assets/urn:aaid:aem:cbefedb9-18bf-49c5-83de-41fed61a6c08/as/KONE_DX_Concept_Car.jpg?width=800&preferwebp=true",
      jumplift: "https://assets.kone.com/adobe/assets/urn:aaid:aem:7bbe68d0-18fb-4970-b1a8-4afeb289acea/as/KONE_JumpLift.jpg?width=800&preferwebp=true",
      technician_ai: "https://assets.kone.com/adobe/assets/urn:aaid:aem:eb4a9d5c-10fb-456b-8658-19eec437ca41/as/Elevator_maintenance_2-1.jpg?width=800&preferwebp=true",
      robot: "https://assets.kone.com/adobe/assets/urn:aaid:aem:343998b1-3b6d-4afd-94cc-1393a9013a37/as/KONE_robot.jpg?width=800&preferwebp=true",
      kunshan: "https://assets.kone.com/adobe/assets/urn:aaid:aem:5eb93d88-3550-4290-8d08-ede026314b38/as/KONE_Kunshan_test_tower.jpg?width=960&preferwebp=true",
      collab: "https://assets.kone.com/adobe/assets/urn:aaid:aem:080059e8-f381-452d-982f-d3670a3d72d6/as/Diverse_people.jpg?width=960&preferwebp=true",
      handshake: "https://assets.kone.com/adobe/assets/urn:aaid:aem:c108cd19-d099-4291-a8ea-6cff4e9130b7/as/customer_handshake.jpg?width=800&preferwebp=true",
      escalator: "https://assets.kone.com/adobe/assets/urn:aaid:aem:28852b6a-4123-448e-a4d6-bb784d4903e8/as/escalator.jpg?width=800&preferwebp=true"
    }};

    const SCENE_IMAGE_MAP = {{
      1: {{ img: KONE_IMAGES.highrise, tag: "Premise · Global Highrise & Urban Flow" }},
      2: {{ img: KONE_IMAGES.city_view, tag: "Sense · European Lift Portfolio" }},
      3: {{ img: KONE_IMAGES.kunshan, tag: "Diagnose · Test Tower & Telemetry" }},
      4: {{ img: KONE_IMAGES.dx_car, tag: "Prioritise · DX Modernization Package" }},
      5: {{ img: KONE_IMAGES.ultrarope, tag: "Replicate · Carbon-Fiber Tech & Playbooks" }},
      6: {{ img: KONE_IMAGES.technician_ai, tag: "Local Landing · Maintenance Field Ops" }},
      7: {{ img: KONE_IMAGES.handshake, tag: "Brief & Launch · Customer Partnership" }},
      8: {{ img: KONE_IMAGES.ecodisc, tag: "Measure & Learn · EcoDisc Upgrades" }},
      9: {{ img: KONE_IMAGES.collab, tag: "Institutional Memory · Extended Leadership" }}
    }};



    /* ============================================================================
       SEED OUTCOMES LOG (Baseline institutional memory in Stage 8)
       ========================================================================== */
    const SEED_LOG = [
      {{ id: 'L-01', period: '2025 Q3', title: 'DACH One-Week Modernization Pilot', market: 'DACH', type: 'modernization', outcome: 'completed', roi: 3.8, result: '+€9.4M order intake, 38% conversion', learning: 'Guaranteed 5-day disruption window eliminated primary property manager objection.' }},
      {{ id: 'L-02', period: '2025 Q4', title: 'Nordics 24/7 Connect Predictive Overhaul', market: 'Nordics', type: 'connectivity', outcome: 'completed', roi: 3.2, result: '+€4.2M contracted, 52% connected share', learning: 'Vibration anomaly threshold triggers 88% accurate modernization leads.' }},
      {{ id: 'L-03', period: '2026 Q1', title: 'France High-Rise Modernization Campaign', market: 'France', type: 'modernization', outcome: 'completed', roi: 2.1, result: '+€3.4M order intake, 27% conversion', learning: 'Generic creative assets had 14-week translation lead time; need modular CSC ingredients.' }},
      {{ id: 'L-04', period: '2026 Q2', title: 'UK & Ireland Maintenance Retention AI', market: 'UK & Ireland', type: 'service', outcome: 'completed', roi: 2.9, result: '-3.2% churn reduction across 142k units', learning: 'Service technician tablet checklist captured 230 qualified aging lift leads.' }},
      {{ id: 'L-05', period: '2026 Q3', title: 'Benelux Elevator Safety Audit Drive', market: 'Benelux', type: 'compliance', outcome: 'completed', roi: 2.4, result: '+€2.1M modernization orders', learning: 'Municipal safety code transitions drive high consideration when paired with financing.' }},
      {{ id: 'L-06', period: '2026 Q4', title: 'Poland Commercial District Elevator Refresh', market: 'Poland', type: 'modernization', outcome: 'completed', roi: 2.3, result: '+€1.8M order intake', learning: 'Standard shafts delivered in 5 days; non-standard shafts delayed by 6 weeks without pre-brackets.' }},
      {{ id: 'L-07', period: '2026 Q4', title: 'DACH Technician Referral Incentive Routine', market: 'DACH', type: 'field_ops', outcome: 'completed', roi: 4.1, result: '41% of all quotes sourced via technicians', learning: 'Technicians are the ultimate trusted advisors for building owners; €100 bonus tripled lead volume.' }}
    ];

    /* ============================================================================
       APPLICATION RUNTIME STATE
       ========================================================================== */
    const INITIAL_STATE = {{
      stage: 1,
      surface: 'ads',
      selectedMarket: 'Iberia',
      selectedCandidate: 'OP-01',
      simAlloc: 8.4,
      simScenario: 'recommended',
      priorityWeights: {{ fit: 25, rev: 25, speed: 20, feas: 15, conf: 15 }},
      playbook: 'PB-01',
      scriptSceneIdx: 0,
      cohortCity: 'all',
      cohortShaft: 'all',
      cohortStatus: 'all',
      cohortSearch: '',
      telemetryJitterCount: 0,
      interventions: [
        {{
          id: 'int-01',
          ref: 'INT-01',
          status: 'queued',
          title: 'One-Week Modernization Iberia Pilot',
          market: 'Iberia',
          budget: 8.4,
          impact: 14.2,
          roi: 3.4,
          confidence: 88,
          owners: ['Field Marketing', 'Sales Ops (Marc Puig)', 'Service Technicians', 'Content Supply Chain'],
          source: 'Simulate · Stage 4',
          detail: '€8.4M allocated to 38 qualified buildings in Madrid and Barcelona. Targets 34% quote conversion.'
        }}
      ],
      outcomesLog: [...SEED_LOG],
      optimiseLevers: {{
        referralBonus: 100,
        bracketKit: false,
        digitalShift: false
      }}
    }};

    let state = JSON.parse(JSON.stringify(INITIAL_STATE));
    let seqCounter = {{ int: 1, log: 7 }};

    /* ============================================================================
       DISPATCHERS & ACTIONS
       ========================================================================== */
    function goStage(n) {{
      state.stage = Math.max(1, Math.min(8, n));
      renderStageRail();
      renderStageContent();
      renderBottomChrome();
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function switchSurface(surfaceKey) {{
      state.surface = surfaceKey;
      document.getElementById('surfaceAds').style.display = surfaceKey === 'ads' ? 'block' : 'none';
      document.getElementById('surfaceScript').style.display = surfaceKey === 'script' ? 'block' : 'none';
      document.getElementById('btnSurfaceAds').classList.toggle('active', surfaceKey === 'ads');
      document.getElementById('btnSurfaceScript').classList.toggle('active', surfaceKey === 'script');
      if (surfaceKey === 'script') {{
        renderScriptView();
      }} else {{
        renderStageContent();
      }}
    }}

    function showToast(text) {{
      const t = document.getElementById('toast');
      document.getElementById('toastMsg').textContent = text;
      t.style.display = 'inline-flex';
      setTimeout(() => {{
        t.style.display = 'none';
      }}, 3600);
    }}

    function resetSession() {{
      state = JSON.parse(JSON.stringify(INITIAL_STATE));
      seqCounter = {{ int: 1, log: 7 }};
      goStage(1);
      switchSurface('ads');
      showToast('Session reset. 7 baseline outcomes preserved in the institutional memory.');
    }}

    function createIntervention(payload) {{
      seqCounter.int += 1;
      const ref = `INT-${{String(seqCounter.int).padStart(2, '0')}}`;
      const id = `int-${{Date.now()}}`;
      seqCounter.log += 1;
      const logId = `L-${{String(seqCounter.log).padStart(2, '0')}}`;

      const record = {{ ...payload, id, ref, status: 'queued', logId }};
      const logEntry = {{
        id: logId,
        period: 'This session',
        title: payload.title,
        market: payload.market,
        type: payload.type || 'modernization',
        outcome: 'queued',
        roi: payload.roi || 3.0,
        result: `${{payload.budget ? '€' + payload.budget + 'M committed' : 'Queued for launch'}}`,
        learning: 'Logged at point of decision. Will convert into evidence once acted on in Orchestrate.',
        recordRef: ref
      }};

      state.interventions.push(record);
      state.outcomesLog.push(logEntry);
      showToast(`${{ref}} created and logged. Act on it in Orchestrate to turn it into evidence.`);
      renderStageRail();
    }}

    function actOnIntervention(id) {{
      const rec = state.interventions.find(i => i.id === id);
      if (!rec || rec.status === 'acted') return;
      rec.status = 'acted';

      seqCounter.log += 1;
      const logId = `L-${{String(seqCounter.log).padStart(2, '0')}}`;
      const evidenceEntry = {{
        id: logId,
        period: 'This session',
        title: `In-Flight Evidence — ${{rec.title}}`,
        market: rec.market,
        type: rec.type || 'modernization',
        outcome: 'in_flight',
        roi: rec.roi,
        result: `€${{rec.impact || 14.2}}M pipeline in motion, tracking ahead of plan`,
        learning: 'Acted on in market. Now counted as empirical evidence — confidence lifted in Prioritise.',
        recordRef: rec.ref
      }};

      const oldLog = state.outcomesLog.find(l => l.id === rec.logId);
      if (oldLog) {{
        oldLog.outcome = 'in_flight';
        oldLog.result = `€${{rec.budget}}M active budget deployed`;
      }}
      state.outcomesLog.push(evidenceEntry);

      showToast(`Acted on ${{rec.ref}}. Evidence recorded — Stage 3 Prioritise confidence rescored!`);
      renderStageRail();
      renderStageContent();
      renderBottomChrome();
    }}

    function replicateToMarket(marketName, playbookName) {{
      seqCounter.int += 1;
      const ref = `INT-${{String(seqCounter.int).padStart(2, '0')}}`;
      const id = `int-${{Date.now()}}`;
      seqCounter.log += 1;
      const logId = `L-${{String(seqCounter.log).padStart(2, '0')}}`;

      const record = {{
        id,
        ref,
        logId,
        status: 'queued',
        title: `${{playbookName || 'One-Week Modernization'}} in ${{marketName}}`,
        market: marketName,
        budget: 5.2,
        impact: 8.8,
        roi: 3.2,
        confidence: 84,
        owners: ['Field Marketing', 'Sales Ops', 'Service Delivery', 'Content Supply Chain'],
        source: 'Replicate · Stage 6',
        detail: `Replicated from DACH playbook. 84% capability match score. €5.2M planned deployment.`
      }};

      const logEntry = {{
        id: logId,
        period: 'This session',
        title: `Replication Initialized — ${{marketName}}`,
        market: marketName,
        type: 'replication',
        outcome: 'in_flight',
        roi: 3.2,
        result: `Suitability 84%, €8.8M projected pipeline`,
        learning: `Replicated from DACH playbook. 4 of 5 capabilities pre-existing in ${{marketName}}.`,
        recordRef: ref
      }};

      state.interventions.push(record);
      state.outcomesLog.push(logEntry);
      showToast(`Replicated to ${{marketName}}. ${{ref}} added to Orchestrate board.`);
      renderStageRail();
      renderStageContent();
      renderBottomChrome();
    }}

    function getRecalibratedConfidence(baseConf) {{
      const actedCount = state.interventions.filter(i => i.status === 'acted').length;
      const sessionOutcomes = state.outcomesLog.length - SEED_LOG.length;
      const lift = Math.min(11, actedCount * 5 + sessionOutcomes * 2);
      return Math.min(99, baseConf + lift);
    }}

    function computePrimaryAction() {{
      const s = state.stage;
      const hasActed = state.interventions.some(i => i.status === 'acted');
      const hasReplication = state.interventions.some(i => i.source && i.source.includes('Replicate'));

      if (s === 1) return {{ label: 'Next: Diagnose why Iberia is missing plan', run: () => goStage(2) }};
      if (s === 2) return {{ label: 'Next: Prioritise what matters across Europe', run: () => goStage(3) }};
      if (s === 3) return {{ label: 'Next: Simulate the €10M allocation decision', run: () => goStage(4) }};
      if (s === 4) {{
        return {{
          label: 'Commit €8.4M to One-Week Modernization and open Orchestrate',
          run: () => {{
            if (!state.interventions.some(i => i.ref === 'INT-01')) {{
              createIntervention({{
                type: 'modernization',
                title: 'One-Week Modernization Iberia Pilot',
                market: 'Iberia',
                budget: state.simAlloc,
                impact: Math.round(state.simAlloc * 1.69 * 10) / 10,
                roi: 3.4,
                confidence: 88,
                owners: ['Field Marketing', 'Sales Ops (Marc Puig)', 'Service Technicians', 'Content Supply Chain'],
                source: 'Simulate · Stage 4',
                detail: `€${{state.simAlloc}}M committed to One-Week Modernization in Iberia.`
              }});
            }}
            goStage(5);
          }}
        }};
      }}
      if (s === 5) {{
        if (!hasActed) {{
          return {{
            label: 'Act on INT-01 to deploy into market',
            run: () => {{
              const int1 = state.interventions.find(i => i.ref === 'INT-01');
              if (int1) actOnIntervention(int1.id);
            }}
          }};
        }}
        return {{ label: 'Next: Scale the proven playbook across Europe', run: () => goStage(6) }};
      }}
      if (s === 6) {{
        if (!hasReplication) {{
          return {{
            label: 'Replicate One-Week Modernization to Benelux',
            run: () => replicateToMarket('Benelux', 'One-Week Modernization')
          }};
        }}
        return {{ label: 'Next: Optimise portfolio execution and mid-flight tuning', run: () => goStage(7) }};
      }}
      if (s === 7) return {{ label: 'Next: See what the enterprise just learned', run: () => goStage(8) }};
      
      const hasLift = state.outcomesLog.length > SEED_LOG.length;
      return {{
        label: hasLift ? 'Back to Prioritise — confidence has moved' : 'Back to Prioritise',
        run: () => goStage(3)
      }};
    }}

    function executeChainedAction() {{
      const pa = computePrimaryAction();
      if (pa && pa.run) pa.run();
    }}

    function renderBottomChrome() {{
      const curr = STAGES[state.stage - 1];
      document.getElementById('bottomStageQuestion').textContent = curr.q;
      const pa = computePrimaryAction();
      document.getElementById('chainedActionLabel').textContent = pa.label;
    }}

    function renderStageRail() {{
      for (let i = 1; i <= 8; i++) {{
        const btn = document.getElementById(`railBtn${{i}}`);
        if (btn) btn.classList.toggle('active', state.stage === i);
      }}

      const activeInts = state.interventions.length;
      const badgeInts = document.getElementById('orchestrateCountBadge');
      if (badgeInts) badgeInts.textContent = activeInts;

      const logCount = state.outcomesLog.length;
      const badgeLearn = document.getElementById('learnCountBadge');
      if (badgeLearn) badgeLearn.textContent = logCount;

      const confShifted = state.interventions.some(i => i.status === 'acted') || state.outcomesLog.length > SEED_LOG.length;
      const dot = document.getElementById('prioritiseShiftDot');
      if (dot) dot.style.display = confShifted ? 'inline-block' : 'none';
    }}

    /* ============================================================================
       STAGE RENDERERS
       ========================================================================== */
    function renderStageContent() {{
      const area = document.getElementById('stageContentArea');
      const s = state.stage;
      const curr = STAGES[s - 1];

      let html = `
        <div class="stage-banner">
          <div>
            <div class="stage-question-tag">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
              Stage ${{curr.n}} of 8 · Decision Flywheel
            </div>
            <div class="stage-question-text">${{curr.q}}</div>
            <div class="stage-question-sub">
              ${{
                s === 1 ? 'Portfolio surveillance across 7 European markets and 4 lines of business.' :
                s === 2 ? 'Comparing 96,000 Iberia units against 268,000 DACH units to isolate root causes.' :
                s === 3 ? 'Scoring and ranking growth initiatives with dynamic confidence recalibration.' :
                s === 4 ? 'Testing capital allocations, conversion yield curves, and cross-market scaling scenarios.' :
                s === 5 ? 'Operationalizing decisions into typed intervention records and cross-functional workstreams.' :
                s === 6 ? 'Codifying proven market playbooks and matching them to candidate countries.' :
                s === 7 ? 'Reviewing 90-day pilot milestones against baseline to execute mid-flight course corrections.' :
                'Every decision, simulation, and in-market outcome is recorded as institutional memory.'
              }}
            </div>
          </div>
          <div style="text-align: right;">
            <button class="btn-action" onclick="executeChainedAction()">
              ${{computePrimaryAction().label}} →
            </button>
          </div>
        </div>
      `;

      if (s === 1) html += renderStage1Sense();
      else if (s === 2) html += renderStage2Diagnose();
      else if (s === 3) html += renderStage3Prioritise();
      else if (s === 4) html += renderStage4Simulate();
      else if (s === 5) html += renderStage5Orchestrate();
      else if (s === 6) html += renderStage6Replicate();
      else if (s === 7) html += renderStage7Optimise();
      else if (s === 8) html += renderStage8Learn();

      area.innerHTML = html;
    }}

    /* STAGE 1: SENSE */
    function renderStage1Sense() {{
      const markets = APP_DATA.markets;
      const opps = APP_DATA.opportunities;

      let latticeRows = markets.map(m => {{
        const isSelected = m.name === state.selectedMarket;
        const activationPct = m.activationRate ?? m.activation ?? 30;
        const agePct = m.installedAge15PlusPct ?? m.age15Plus ?? 35;
        const connPct = m.connectedPct ?? m.connected ?? 40;
        const convPct = m.quoteConversionPct ?? m.conversion ?? 25;
        const baseUnits = m.baseUnits || 100000;
        const units15Plus = Math.round(baseUnits * agePct / 100);
        const isIberia = m.name === 'Iberia';
        const isDach = m.name === 'DACH';
        const signalBadge = isIberia ? '<span class="badge badge-danger">Underperforming Risk</span>' :
                            isDach ? '<span class="badge badge-success">Outperforming Playbook</span>' :
                            m.name === 'Benelux' ? '<span class="badge badge-warning">Watch List (Lag)</span>' :
                            '<span class="badge badge-neutral">On Track</span>';

        const trendBadge = m.trendType === 'decremental' ?
          `<span class="badge badge-danger num" style="font-size:10px; padding:1px 5px;" title="Decremental synthetic telemetry drift">▼ ${{m.deltaQuote || '-0.8%'}}</span>` :
          `<span class="badge badge-success num" style="font-size:10px; padding:1px 5px;" title="Incremental synthetic telemetry drift">▲ ${{m.deltaQuote || '+1.8%'}}</span>`;

        return `
          <tr style="${{isSelected ? 'background: rgba(20, 80, 245, 0.06); font-weight: 500;' : ''}}">
            <td>
              <strong style="color:var(--color-primary-2);">${{m.name}}</strong>
              <div style="font-size:11px; color:var(--text-dim);">${{baseUnits.toLocaleString()}} elevators</div>
            </td>
            <td class="num">${{agePct}}% <span style="font-size:11px; color:var(--color-accent-2);">(${{units15Plus.toLocaleString()}})</span></td>
            <td class="num">${{connPct}}%</td>
            <td class="num">
              <div style="display:flex; align-items:center; gap:6px;">
                <span style="font-weight:700; color:${{activationPct < 30 ? 'var(--color-danger-primary)' : activationPct > 50 ? 'var(--color-success-primary)' : 'var(--text-high)'}}">${{activationPct}}%</span>
                <div style="flex:1; max-width:50px; height:5px; background:var(--color-neutral-2); border-radius:3px; overflow:hidden;">
                  <div style="width:${{activationPct}}%; height:100%; background:${{activationPct < 30 ? 'var(--color-danger-primary)' : 'var(--color-primary-1)'}}; border-radius:3px;"></div>
                </div>
              </div>
            </td>
            <td class="num">
              <div style="display:flex; align-items:center; justify-content:flex-end; gap:6px;">
                <span style="font-weight:600; color:var(--color-primary-2);">${{convPct}}%</span>
                ${{trendBadge}}
              </div>
            </td>
            <td>${{signalBadge}}</td>
            <td>
              ${{isIberia ? `
                <button class="btn-action" style="padding:4px 10px; font-size:11px;" onclick="goStage(2)">
                  Diagnose why →
                </button>
              ` : `
                <button class="btn-outline" style="padding:4px 8px; font-size:11px;" onclick="selectMarket('${{m.name}}')">
                  View
                </button>
              `}}
            </td>
          </tr>
        `;
      }}).join('');

      let oppCards = opps.map((o, idx) => `
        <div class="stat-card" style="border-left: 3px solid ${{idx === 0 ? 'var(--color-primary-1)' : 'var(--color-neutral-2)'}};">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
            <span class="badge ${{idx === 0 ? 'badge-primary' : 'badge-neutral'}}">#${{idx + 1}} Sensed Rank</span>
            <span class="badge ${{o.confidence > 0.8 ? 'badge-success' : 'badge-neutral'}} num">Conf: ${{Math.round(o.confidence * 100)}}%</span>
          </div>
          <h4 style="font-size:14px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">${{o.play}} (${{o.market}})</h4>
          <p style="font-size:11.5px; color:var(--text-dim); line-height:1.4; margin-bottom:8px;">${{o.description || 'Modernization opportunity detected via portfolio signal anomaly.'}}</p>
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-top:auto;">
            <span style="font-size:11px; text-transform:uppercase; color:var(--color-neutral-6); font-weight:600;">Est. Potential</span>
            <div class="num" style="font-size:20px; font-weight:800; color:var(--color-primary-1);">+€${{o.potential}}M</div>
          </div>
        </div>
      `).join('');

      return `
        <!-- HERO INNOVATION BANNER -->
        <div class="glass-panel" style="padding:0; overflow:hidden; margin-bottom:var(--space-8); display:grid; grid-template-columns: 280px 1fr; background:#ffffff;">
          <div style="background: url('${{KONE_IMAGES.highrise}}') center/cover no-repeat; min-height:150px; position:relative;">
            <div style="position:absolute; inset:0; background:linear-gradient(90deg, rgba(20,80,245,0.2) 0%, rgba(0,6,31,0.5) 100%); display:flex; align-items:flex-end; padding:14px;">
              <span class="badge" style="background:#ffffff; color:var(--color-primary-1); font-weight:700;">IoT Asset Telemetry</span>
            </div>
          </div>
          <div style="padding:18px 24px; display:flex; flex-direction:column; justify-content:center;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span class="badge badge-primary">2.87M Connected Global Assets</span>
              <span class="badge badge-warning">Iberia Signal Detected</span>
            </div>
            <h3 style="font-size:17px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Autonomous Sensing & Signal Anomaly Detection</h3>
            <p style="font-size:12.5px; color:var(--text-dim); line-height:1.5; margin:0;">
              The Assisted Decisioning System continuously monitors 7 European operating markets across installed age, 24/7 IoT connectivity, quote conversion, and 90-day modernization velocity.
            </p>
          </div>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 0 1 10 10"/><path d="M12 12L20 4"/></svg>
                European Installed Base & Modernization Lattice (7 Operating Units)
              </div>
              <div class="panel-subtitle">Sensed across 2.87M maintenance contracts · Refreshed weekly</div>
            </div>
            <div style="display:flex; align-items:center; gap:8px;">
              <span class="badge badge-neutral">Signal Frequency: Live Telemetry</span>
              <button class="btn-outline" style="padding:4px 8px; font-size:11px; display:inline-flex; align-items:center; gap:4px;" onclick="simulateTelemetryJitter()">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>
                Randomize Synthetic Trends
              </button>
            </div>
          </div>

          <table class="data-table">
            <thead>
              <tr>
                <th>Market</th>
                <th>15+ Yr Base</th>
                <th>Connected Base</th>
                <th>90-Day Activation</th>
                <th>Quote Conversion</th>
                <th>Signal Status</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              ${{latticeRows}}
            </tbody>
          </table>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
                Top Sensed Opportunities (Ranked by Unlocked Value)
              </div>
              <div class="panel-subtitle">Automated opportunity clustering by modernization addressability</div>
            </div>
          </div>

          <div class="grid-3" style="margin-bottom:var(--space-8);">
            ${{oppCards}}
          </div>

          <div style="background:var(--color-primary-6); border:1px solid var(--color-primary-8); padding:16px; border-radius:var(--radius-3); display:flex; align-items:center; justify-content:space-between;">
            <div style="display:flex; align-items:center; gap:12px;">
              <div style="background:var(--color-primary-1); width:32px; height:32px; border-radius:var(--radius-3); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:900;">!</div>
              <div>
                <strong style="color:var(--color-primary-2); font-size:13.5px;">Assisted Decisioning System Recommendation</strong>
                <p style="font-size:12px; color:var(--text-dim); margin:2px 0 0;">
                  Iberia has <strong>34,500 lifts &gt;15 years old</strong> ready for modernization, but only converts 24% of quotes vs. 38% in DACH. Closing this gap represents <strong>+€6.1M</strong> in high-margin incremental revenue.
                </p>
              </div>
            </div>
            <button class="btn-action" onclick="goStage(2)">
              Diagnose Iberia Root Causes →
            </button>
          </div>
        </div>
      `;
    }}

    function selectMarket(mName) {{
      state.selectedMarket = mName;
      renderStageContent();
      showToast(`Selected ${{mName}} in portfolio lattice.`);
    }}

    function simulateTelemetryJitter() {{
      state.telemetryJitterCount = (state.telemetryJitterCount || 0) + 1;
      APP_DATA.markets.forEach(m => {{
        const isUp = Math.random() > 0.45;
        const drift = (Math.random() * 1.6 + 0.3);
        const sign = isUp ? 1 : -1;
        const deltaStr = (isUp ? '+' : '-') + drift.toFixed(1) + '%';
        
        m.trendType = isUp ? 'incremental' : 'decremental';
        m.deltaQuote = deltaStr;
        
        const currentConv = m.quoteConversionPct ?? m.conversion ?? 28;
        const newConv = Math.max(16, Math.min(60, Math.round(currentConv + sign * (drift * 0.7))));
        m.quoteConversionPct = newConv;
        m.conversion = newConv;

        const currentAct = m.activationRate ?? m.activation ?? 30;
        const newAct = Math.max(18, Math.min(72, Math.round(currentAct + sign * (drift * 0.5))));
        m.activationRate = newAct;
        m.activation = newAct;
      }});

      if (APP_DATA.cohort) {{
        APP_DATA.cohort.forEach(b => {{
          const jitter = (Math.random() - 0.48) * 0.3;
          b.vibrationMmS = Math.max(0.8, Math.round(((b.vibrationMmS || 1.8) + jitter) * 100) / 100);
          b.telemetryScore = Math.max(70, Math.min(99, Math.round(((b.telemetryScore || 85) + jitter * 4) * 10) / 10));
        }});
      }}

      renderStageContent();
      renderBottomChrome();
      showToast(`Synthetic telemetry stream updated: applied randomized incremental/decremental drift (Iteration #${{state.telemetryJitterCount}}).`);
    }}

    /* STAGE 2: DIAGNOSE */
    function renderStage2Diagnose() {{
      const drivers = APP_DATA.dachDrivers;

      let driverRows = drivers.map(d => `
        <tr>
          <td>
            <strong style="color:var(--color-primary-2);">${{d.driver}}</strong>
            <div style="font-size:11.5px; color:var(--text-dim); margin-top:2px;">${{d.observation}}</div>
          </td>
          <td><span class="badge badge-primary">${{d.type}}</span></td>
          <td class="num" style="color:var(--color-primary-1); font-weight:700;">+${{d.points}} pts</td>
          <td class="num" style="font-weight:600; color:var(--color-primary-2);">${{d.share}}%</td>
          <td>
            <div style="width:100%; height:6px; background:var(--color-neutral-2); border-radius:var(--radius-1); max-width:80px; overflow:hidden;">
              <div style="width:${{d.share}}%; height:100%; background:var(--color-primary-1); border-radius:var(--radius-1);"></div>
            </div>
          </td>
        </tr>
      `).join('');

      return `
        <!-- URBAN DENSITY & MODERNIZATION BANNER -->
        <div class="glass-panel" style="padding:0; overflow:hidden; margin-bottom:var(--space-8); display:grid; grid-template-columns: 1fr 280px; background:#ffffff;">
          <div style="padding:18px 24px; display:flex; flex-direction:column; justify-content:center;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span class="badge badge-danger">Diagnostic Anomaly</span>
              <span class="badge badge-neutral">Madrid & Barcelona Urban Density</span>
            </div>
            <h3 style="font-size:17px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Root Cause: Field Handover Bottleneck, Not Creative Ineffectiveness</h3>
            <p style="font-size:12.5px; color:var(--text-dim); line-height:1.5; margin:0;">
              Iberia has 34,500 aging residential lifts, yet quote conversion lags at 24% vs 46% in DACH. The Assisted Decisioning System reveals the breakdown is operational: technician referral routine and 1-week installation capacity are missing.
            </p>
          </div>
          <div style="background: url('${{KONE_IMAGES.city_view}}') center/cover no-repeat; min-height:150px; position:relative;">
            <div style="position:absolute; inset:0; background:linear-gradient(270deg, rgba(20,80,245,0.1) 0%, rgba(0,6,31,0.55) 100%); display:flex; align-items:flex-end; padding:14px;">
              <span style="color:#ffffff; font-size:11px; font-weight:600;">Urban Lift Density: Southern Europe</span>
            </div>
          </div>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                Decomposing the +22 pt Conversion Gap: DACH (46%) vs. Iberia (24%)
              </div>
              <div class="panel-subtitle">Multivariate attribution decomposing why DACH succeeds where Iberia lags</div>
            </div>
            <span class="badge badge-danger">Iberia Lag: -22 pts Quote Conversion</span>
          </div>

          <table class="data-table" style="margin-bottom:var(--space-8);">
            <thead>
              <tr>
                <th>Driver Component</th>
                <th>Category</th>
                <th>Conversion Impact</th>
                <th>Share of Gap</th>
                <th>Relative Weight</th>
              </tr>
            </thead>
            <tbody>
              ${{driverRows}}
            </tbody>
          </table>

          <div style="background:var(--color-primary-6); border:1px solid var(--color-primary-8); padding:16px; border-radius:var(--radius-3); margin-bottom:var(--space-8);">
            <h4 style="font-size:13px; color:var(--color-primary-2); margin-bottom:6px; font-weight:700;">The Diagnostic Conclusion</h4>
            <p style="font-size:12.5px; color:var(--text-high); line-height:1.55; margin:0;">
              DACH's 46% conversion is <strong>NOT</strong> driven by higher media spend or flashy advertising. It is driven by <strong>operational integration</strong>: maintenance technicians flagging aging units during regular visits, pre-qualified standard-shaft offers, and guaranteed 1-week turnkey installations.
            </p>
          </div>

          <div style="display:flex; align-items:center; justify-content:space-between; background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:14px 18px; box-shadow:var(--shadow-5);">
            <div>
              <h4 style="font-size:13px; color:var(--color-primary-2); margin-bottom:2px; font-weight:700;">Next Action in Flywheel</h4>
              <p style="font-size:12px; color:var(--text-dim); margin:0;">Rank this opportunity against other European candidates.</p>
            </div>
            <button class="btn-action" onclick="goStage(3)">
              Open Stage 3: Prioritise →
            </button>
          </div>
        </div>
      `;
    }}

    /* STAGE 3: PRIORITISE */
    function renderStage3Prioritise() {{
      const prio = APP_DATA.prioritisation;
      const actedCount = state.interventions.filter(i => i.status === 'acted').length;
      const confShifted = actedCount > 0 || state.outcomesLog.length > SEED_LOG.length;

      let rows = prio.map((p, idx) => {{
        const isHero = p.market === 'Iberia';
        const baseConf = p.confidenceScore * 20;
        const effectiveConf = isHero ? getRecalibratedConfidence(88) : baseConf;
        const stance = isHero ? '<span class="badge badge-success">Accelerate</span>' :
                       idx === 1 ? '<span class="badge badge-primary">Scale Playbook</span>' :
                       idx === 2 ? '<span class="badge badge-warning">Fix Leakage</span>' :
                       '<span class="badge badge-neutral">Monitor</span>';

        return `
          <tr style="${{isHero ? 'background: rgba(20, 80, 245, 0.06); font-weight: 500;' : ''}}">
            <td><strong style="color:var(--color-primary-2);">#${{idx + 1}}</strong></td>
            <td>
              <strong style="color:var(--color-primary-2);">${{p.candidate || (p.market + ' One-Week Modernization')}}</strong>
              <div style="font-size:11px; color:var(--text-dim);">${{p.market}} · ${{p.targetSegment || 'Aging Installed Base'}}</div>
            </td>
            <td class="num" style="font-weight:700; color:var(--color-primary-1);">+€${{p.potential}}M</td>
            <td class="num">
              <div style="display:flex; align-items:center; gap:6px;">
                <span style="font-weight:700; color:var(--color-primary-2);">${{effectiveConf}}%</span>
                <div style="flex:1; max-width:40px; height:5px; background:var(--color-neutral-2); border-radius:3px; overflow:hidden;">
                  <div style="width:${{effectiveConf}}%; height:100%; background:var(--color-primary-1); border-radius:3px;"></div>
                </div>
              </div>
            </td>
            <td>
              ${{isHero && confShifted ? `
                <span class="badge badge-success" title="Recalibrated from 0.62 to 0.84 based on pilot evidence">+22% Recalibrated</span>
              ` : `
                <span style="font-size:11px; color:var(--color-neutral-6);">Baseline Prior</span>
              `}}
            </td>
            <td>${{stance}}</td>
            <td>
              ${{isHero ? `
                <button class="btn-action" style="padding:4px 10px; font-size:11px;" onclick="goStage(4)">
                  Simulate €10M allocation →
                </button>
              ` : `
                <span style="font-size:11.5px; color:var(--color-neutral-6);">In Queue</span>
              `}}
            </td>
          </tr>
        `;
      }}).join('');

      return `
        <!-- TEST TOWER & CALIBRATION BANNER -->
        <div class="glass-panel" style="padding:0; overflow:hidden; margin-bottom:var(--space-8); display:grid; grid-template-columns: 280px 1fr; background:#ffffff;">
          <div style="background: url('${{KONE_IMAGES.kunshan}}') center/cover no-repeat; min-height:150px; position:relative;">
            <div style="position:absolute; inset:0; background:linear-gradient(90deg, rgba(20,80,245,0.2) 0%, rgba(0,6,31,0.5) 100%); display:flex; align-items:flex-end; padding:14px;">
              <span class="badge" style="background:#ffffff; color:var(--color-primary-1); font-weight:700;">Kunshan Test Tower Calibration</span>
            </div>
          </div>
          <div style="padding:18px 24px; display:flex; flex-direction:column; justify-content:center;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span class="badge badge-primary">Multi-Objective Capital Optimization</span>
              <span class="badge badge-success">Dynamic Bayesian Recalibration</span>
            </div>
            <h3 style="font-size:17px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Prioritised Candidate Matrix & Yield Scoring</h3>
            <p style="font-size:12.5px; color:var(--text-dim); line-height:1.5; margin:0;">
              Ranking opportunities by expected EBITDA impact, feasibility match, and continuous Bayesian confidence drift derived from closed-loop field trial completions.
            </p>
          </div>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
                European Growth Opportunity Ranking Matrix
              </div>
              <div class="panel-subtitle">Multi-objective scoring: EBITDA yield · Capital intensity · Organizational readiness</div>
            </div>
            <span class="badge badge-success">Active Hero Candidate: Iberia One-Week Modernization</span>
          </div>

          <table class="data-table" style="margin-bottom:var(--space-8);">
            <thead>
              <tr>
                <th>Rank</th>
                <th>Intervention Candidate</th>
                <th>Est. Yield</th>
                <th>Confidence</th>
                <th>Dynamic Shift</th>
                <th>Strategic Stance</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              ${{rows}}
            </tbody>
          </table>

          <div class="grid-2" style="margin-bottom:0;">
            <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:14px 18px; box-shadow:var(--shadow-5);">
              <h4 style="font-size:13px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">How Confidence Moves</h4>
              <p style="font-size:12px; color:var(--text-dim); line-height:1.5; margin:0;">
                Prior confidence starts at <strong>0.62</strong> (unproven hypothesis). Once Stage 7 field evidence arrives (112 technician leads, 151 days saved), confidence recalibrates to <strong>0.84</strong> automatically in Stage 8.
              </p>
            </div>
            <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:14px 18px; box-shadow:var(--shadow-5); display:flex; flex-direction:column; justify-content:space-between;">
              <div>
                <h4 style="font-size:13px; color:var(--color-primary-2); margin-bottom:2px; font-weight:700;">Ready to Allocate Capital?</h4>
                <p style="font-size:12px; color:var(--text-dim); margin:0;">Test funding detents (€5M, €8.4M, €10M) in the simulation engine.</p>
              </div>
              <div style="margin-top:10px; display:flex; justify-content:flex-end;">
                <button class="btn-action" onclick="goStage(4)">
                  Open Stage 4: Simulate →
                </button>
              </div>
            </div>
          </div>
        </div>
      `;
    }}

    /* STAGE 4: SIMULATE */
    function renderStage4Simulate() {{
      const alloc = state.simAlloc;
      const projectedRevenue = Math.round((alloc * 1.69) * 10) / 10;
      const expectedROI = Math.round((projectedRevenue / (alloc || 1)) * 10) / 10;
      const paybackMos = Math.max(8, Math.round(18 - (alloc * 0.7)));
      const confidence = Math.min(95, Math.round(80 + (alloc * 1.1)));

      return `
        <!-- SIMULATION BANNER -->
        <div class="glass-panel" style="padding:0; overflow:hidden; margin-bottom:var(--space-8); display:grid; grid-template-columns: 1fr 280px; background:#ffffff;">
          <div style="padding:18px 24px; display:flex; flex-direction:column; justify-content:center;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span class="badge badge-primary">Scenario Engine</span>
              <span class="badge badge-success">Monte Carlo Simulation</span>
            </div>
            <h3 style="font-size:17px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Digital Experience Modernization Simulation</h3>
            <p style="font-size:12.5px; color:var(--text-dim); line-height:1.5; margin:0;">
              Evaluating capital allocation trade-offs across 38 buildings in Madrid and Barcelona. Testing installation team throughput, customer payback curves, and technician referral incentives.
            </p>
          </div>
          <div style="background: url('${{KONE_IMAGES.dx_car}}') center/cover no-repeat; min-height:150px; position:relative;">
            <div style="position:absolute; inset:0; background:linear-gradient(270deg, rgba(20,80,245,0.1) 0%, rgba(0,6,31,0.5) 100%); display:flex; align-items:flex-end; padding:14px;">
              <span style="color:#ffffff; font-size:11px; font-weight:600;">KONE DX Concept Architecture</span>
            </div>
          </div>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M16 12l-4-4-4 4M12 16V8"/></svg>
                Growth Capital Allocation Control (€0M to €20M)
              </div>
              <div class="panel-subtitle">Drag slider to simulate incremental revenue, ROI, and payback detents</div>
            </div>
            <span class="badge badge-primary">Detents: €5M · €8.4M (Recommended) · €10M</span>
          </div>

          <div style="margin: var(--space-8) 0 var(--space-13);">
            <div class="slider-control">
              <div class="slider-header">
                <span style="font-size:12.5px; color:var(--color-primary-2); font-weight:700;">Simulated Investment Level</span>
                <span class="slider-val" id="simSliderVal">€${{alloc}}M</span>
              </div>
              <input type="range" min="0" max="20" step="0.5" value="${{alloc}}" id="simRangeInput" oninput="onSimSliderChange(this.value)">
              <div style="display:flex; justify-content:space-between; font-size:11px; color:var(--text-dim); margin-top:4px;">
                <span>€0M (Status Quo)</span>
                <span>€5M (Conservative)</span>
                <span style="color:var(--color-primary-1); font-weight:700;">€8.4M (Recommended)</span>
                <span>€10M (Full Pilot)</span>
                <span>€20M (Aggressive)</span>
              </div>
            </div>
          </div>

          <div class="grid-4" style="margin-bottom:var(--space-8);">
            <div class="stat-card">
              <span class="stat-label">Projected Revenue</span>
              <div class="stat-val" id="simProjRev" style="color:var(--color-primary-1);">+€${{projectedRevenue}}M</div>
              <div class="stat-delta positive">Over 18 Months</div>
            </div>
            <div class="stat-card">
              <span class="stat-label">Expected ROI Multiple</span>
              <div class="stat-val" id="simExpROI" style="color:var(--color-success-primary);">${{expectedROI}}x</div>
              <div class="stat-delta positive">EBITDA Multiplier</div>
            </div>
            <div class="stat-card">
              <span class="stat-label">Payback Timeline</span>
              <div class="stat-val" id="simPayback" style="color:var(--color-primary-2);">${{paybackMos}} Mos</div>
              <div class="stat-delta positive">Faster than 24m plan</div>
            </div>
            <div class="stat-card">
              <span class="stat-label">Engine Confidence</span>
              <div class="stat-val" id="simConf" style="color:var(--color-primary-1);">${{confidence}}%</div>
              <div class="stat-delta neutral">Bayesian Calibration</div>
            </div>
          </div>

          <div class="panel-header" style="margin-top:var(--space-8);">
            <div class="panel-title" style="font-size:13px;">Pre-Configured Strategic Detents</div>
          </div>

          <div class="grid-3" style="margin-bottom:var(--space-8);">
            <div class="stat-card" style="cursor:pointer;" onclick="applyDetent(10.0)">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <span class="badge badge-neutral">€10M Allocation</span>
                <span style="font-size:11px; color:var(--color-accent-2);">Aggressive</span>
              </div>
              <h4 style="font-size:14px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Aggressive One-Week Push</h4>
              <p style="font-size:11.5px; color:var(--text-dim); line-height:1.4;">Pre-fund 8 dedicated installation crews across Madrid & Barcelona.</p>
            </div>
            <div class="stat-card" style="border: 2px solid var(--color-primary-1); cursor:pointer;" onclick="applyDetent(8.4)">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <span class="badge badge-success">€8.4M Allocation</span>
                <span class="badge badge-primary">Recommended</span>
              </div>
              <h4 style="font-size:14px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Balanced Modernization + 24/7</h4>
              <p style="font-size:11.5px; color:var(--text-dim); line-height:1.4;">Optimal balance of technician referral bonus (€150) + standard package inventory.</p>
            </div>
            <div class="stat-card" style="cursor:pointer;" onclick="applyDetent(5.0)">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <span class="badge badge-neutral">€5M Allocation</span>
                <span style="font-size:11px; color:var(--color-accent-2);">Defensive</span>
              </div>
              <h4 style="font-size:14px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Defensive Service Maintenance</h4>
              <p style="font-size:11.5px; color:var(--text-dim); line-height:1.4;">Protect existing contracts against competitor poaching; slower conversion.</p>
            </div>
          </div>

          <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:14px 18px; box-shadow:var(--shadow-5); display:flex; align-items:center; justify-content:space-between;">
            <div>
              <h4 style="font-size:13px; color:var(--color-primary-2); margin-bottom:2px; font-weight:700;">Turn Simulation into Decision Record</h4>
              <p style="font-size:12px; color:var(--text-dim); margin:0;">Locks this €${{alloc}}M allocation and generates orchestrated execution briefs.</p>
            </div>
            <button class="btn-action" onclick="recordSimDecision()">
              Commit & Orchestrate Execution →
            </button>
          </div>
        </div>
      `;
    }}

    function onSimSliderChange(val) {{
      state.simAlloc = parseFloat(val);
      document.getElementById('simSliderVal').textContent = `€${{state.simAlloc}}M`;
      const projRev = Math.round((state.simAlloc * 1.69) * 10) / 10;
      const expROI = Math.round((projRev / (state.simAlloc || 1)) * 10) / 10;
      const payback = Math.max(8, Math.round(18 - (state.simAlloc * 0.7)));
      const conf = Math.min(95, Math.round(80 + (state.simAlloc * 1.1)));

      document.getElementById('simProjRev').textContent = `+€${{projRev}}M`;
      document.getElementById('simExpROI').textContent = `${{expROI}}x`;
      document.getElementById('simPayback').textContent = `${{payback}} Mos`;
      document.getElementById('simConf').textContent = `${{conf}}%`;
    }}

    function applyDetent(val) {{
      state.simAlloc = val;
      renderStageContent();
      showToast(`Applied €${{val}}M strategic allocation detent.`);
    }}

    function recordSimDecision() {{
      showToast(`Decision recorded: €${{state.simAlloc}}M committed to Iberia Modernization.`);
      goStage(5);
    }}

    /* STAGE 5: ORCHESTRATE */
    function renderStage5Orchestrate() {{
      const ints = state.interventions;
      const cohort = APP_DATA.cohort;

      let intCards = ints.map(i => `
        <div class="stat-card" style="border-left: 3px solid ${{i.status === 'acted' ? 'var(--color-success-primary)' : 'var(--color-primary-1)'}};">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
            <span class="badge badge-primary">${{i.ref}}</span>
            <span class="badge ${{i.status === 'acted' ? 'badge-success' : 'badge-warning'}}">${{i.status === 'acted' ? 'Acted / In-Flight' : 'Queued'}}</span>
          </div>
          <h4 style="font-size:14px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">${{i.title}}</h4>
          <div style="font-size:11.5px; color:var(--text-dim); margin-bottom:10px; line-height:1.4;">${{i.detail || ''}}</div>
          <div style="font-size:11px; color:var(--color-accent-2); margin-bottom:12px;">
            <strong>Owners:</strong> ${{i.owners ? i.owners.join(', ') : 'Cross-functional team'}}
          </div>
          <div style="margin-top:auto; display:flex; justify-content:space-between; align-items:center;">
            <span class="num" style="font-size:12px; font-weight:700; color:var(--color-primary-2);">Budget: €${{i.budget}}M</span>
            ${{i.status === 'acted' ? `
              <span style="font-size:11.5px; color:var(--color-success-primary); font-weight:600;">✓ In Market</span>
            ` : `
              <button class="btn-action" style="padding:4px 10px; font-size:11px;" onclick="actOnIntervention('${{i.id}}')">
                Act on this record →
              </button>
            `}}
          </div>
        </div>
      `).join('');

      let filteredCohort = cohort.filter(b => {{
        if (state.cohortCity && state.cohortCity !== 'all' && b.city !== state.cohortCity) return false;
        const bShaft = b.shaftType || b.shaft || 'Standard';
        if (state.cohortShaft && state.cohortShaft !== 'all' && bShaft !== state.cohortShaft) return false;
        if (state.cohortStatus && state.cohortStatus !== 'all' && b.status !== state.cohortStatus) return false;
        const bName = b.name || '';
        const bAddr = b.address || '';
        if (state.cohortSearch && !bName.toLowerCase().includes(state.cohortSearch.toLowerCase()) && !bAddr.toLowerCase().includes(state.cohortSearch.toLowerCase())) return false;
        return true;
      }});

      let cohortRows = filteredCohort.slice(0, 10).map(b => {{
        const bName = b.name || `${{b.buildingType || 'Building'}} (${{b.id}})`;
        const bAddress = b.address || 'Calle Gran Vía 42';
        const bCity = b.city || 'Madrid';
        const bAge = b.age || 35;
        const bLifts = b.elevatorCount ?? b.quotedUnits ?? 1;
        const bShaft = b.shaftType || b.shaft || 'Standard';
        const bValue = b.estValue ?? b.orderValue ?? 24400;
        const bStatus = b.status || 'Active Pilot';

        return `
        <tr onclick="openBuildingModal('${{b.id}}')" style="cursor:pointer;">
          <td><strong style="color:var(--color-primary-2);">${{bName}}</strong><div style="font-size:11px; color:var(--text-dim);">${{bAddress}}</div></td>
          <td>${{bCity}}</td>
          <td class="num">${{bAge}} yrs</td>
          <td class="num">${{bLifts}}</td>
          <td><span class="badge badge-neutral">${{bShaft}}</span></td>
          <td class="num" style="color:var(--color-primary-1); font-weight:700;">€${{bValue.toLocaleString()}}</td>
          <td><span class="badge ${{bStatus.includes('Active') || bStatus.includes('Signed') || bStatus.includes('Converted') ? 'badge-success' : 'badge-primary'}}">${{bStatus}}</span></td>
          <td><button class="btn-outline" style="padding:3px 8px; font-size:11px;" onclick="event.stopPropagation(); openBuildingModal('${{b.id}}')">Inspect</button></td>
        </tr>
      `;
      }}).join('');

      return `
        <!-- FIELD DISPATCH BANNER -->
        <div class="glass-panel" style="padding:0; overflow:hidden; margin-bottom:var(--space-8); display:grid; grid-template-columns: 260px 1fr; background:#ffffff;">
          <div style="background: url('${{KONE_IMAGES.technician_ai}}') center/cover no-repeat; min-height:150px; position:relative;">
            <div style="position:absolute; inset:0; background:linear-gradient(90deg, rgba(20,80,245,0.2) 0%, rgba(0,6,31,0.5) 100%); display:flex; align-items:flex-end; padding:14px;">
              <span class="badge" style="background:#ffffff; color:var(--color-primary-1); font-weight:700;">Technician Field App Tasking</span>
            </div>
          </div>
          <div style="padding:18px 24px; display:flex; flex-direction:column; justify-content:center;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span class="badge badge-success">Closed-Loop Operational Dispatch</span>
              <span class="badge badge-primary">38-Building Cohort</span>
            </div>
            <h3 style="font-size:17px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Field Execution: 112 Technician Referrals Dispatched</h3>
            <p style="font-size:12.5px; color:var(--text-dim); line-height:1.5; margin:0;">
              ADS turns strategic decisions into maintenance routes. Technicians in Madrid, Barcelona, and Valencia receive pre-qualified shaft tasks directly in their field app.
            </p>
          </div>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                The 3 Decision Records Committed to Market Execution
              </div>
              <div class="panel-subtitle">Bridging strategy to field execution · Cross-functional owner alignment</div>
            </div>
          </div>

          <div class="grid-3" style="margin-bottom:var(--space-8);">
            ${{intCards}}
          </div>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                Active 38-Building Cohort Dispatch (Spain Pilot)
              </div>
              <div class="panel-subtitle">Click any building to inspect shaft dimensions, verified age, and technician audit notes</div>
            </div>
            <div style="display:flex; gap:8px; align-items:center;">
              <input type="text" placeholder="Search building name or address..." value="${{state.cohortSearch || ''}}" oninput="onCohortSearch(this.value)" style="background:#ffffff; border:1px solid var(--color-neutral-2); padding:6px 12px; border-radius:var(--radius-3); color:var(--color-primary-2); font-size:12px; width:220px;">
              <select onchange="onCohortFilter('city', this.value)" style="background:#ffffff; border:1px solid var(--color-neutral-2); padding:6px 10px; border-radius:var(--radius-3); color:var(--color-primary-2); font-size:12px;">
                <option value="all">All Cities</option>
                <option value="Madrid" ${{state.cohortCity === 'Madrid' ? 'selected' : ''}}>Madrid</option>
                <option value="Barcelona" ${{state.cohortCity === 'Barcelona' ? 'selected' : ''}}>Barcelona</option>
                <option value="Valencia" ${{state.cohortCity === 'Valencia' ? 'selected' : ''}}>Valencia</option>
                <option value="Seville" ${{state.cohortCity === 'Seville' ? 'selected' : ''}}>Seville</option>
              </select>
              <select onchange="onCohortFilter('shaft', this.value)" style="background:#ffffff; border:1px solid var(--color-neutral-2); padding:6px 10px; border-radius:var(--radius-3); color:var(--color-primary-2); font-size:12px;">
                <option value="all">All Shaft Types</option>
                <option value="Standard" ${{state.cohortShaft === 'Standard' ? 'selected' : ''}}>Standard</option>
                <option value="Narrow" ${{state.cohortShaft === 'Narrow' ? 'selected' : ''}}>Narrow</option>
                <option value="Non-standard" ${{state.cohortShaft === 'Non-standard' ? 'selected' : ''}}>Non-standard</option>
              </select>
            </div>
          </div>

          <table class="data-table">
            <thead>
              <tr>
                <th>Building</th>
                <th>City</th>
                <th>Age</th>
                <th>Lifts</th>
                <th>Shaft Type</th>
                <th>Quote Value</th>
                <th>Status</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              ${{cohortRows}}
            </tbody>
          </table>

          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:var(--space-8); padding-top:var(--space-8); border-top:1px solid var(--color-neutral-2);">
            <div style="font-size:12px; color:var(--text-dim);">
              Showing top ${{Math.min(10, filteredCohort.length)}} of ${{filteredCohort.length}} cohort buildings in Spain.
            </div>
            <button class="btn-action" onclick="goStage(6)">
              Scale via Playbook Replication →
            </button>
          </div>
        </div>
      `;
    }}

    function actOnIntervention(id) {{
      const item = state.interventions.find(i => i.id === id);
      if (item) {{
        item.status = 'acted';
        renderStageContent();
        renderBottomChrome();
        showToast(`Record ${{item.ref}} activated and dispatched to field teams.`);
      }}
    }}

    function onCohortFilter(key, val) {{
      if (key === 'city') state.cohortCity = val;
      if (key === 'shaft') state.cohortShaft = val;
      if (key === 'status') state.cohortStatus = val;
      renderStageContent();
    }}

    function onCohortSearch(val) {{
      state.cohortSearch = val;
      renderStageContent();
    }}

    /* STAGE 6: REPLICATE */
    function renderStage6Replicate() {{
      const elements = APP_DATA.playbookElements;

      let elementRows = elements.map((e, idx) => `
        <div class="stat-card">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
            <span class="badge badge-primary">Element #${{idx + 1}}</span>
            <span class="badge badge-success">Codified</span>
          </div>
          <h4 style="font-size:13.5px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">${{e.element || e.name}}</h4>
          <div style="font-size:11px; color:var(--color-primary-1); font-weight:600; margin-bottom:4px;">${{e.type || 'Operational Asset'}}</div>
          <p style="font-size:11.5px; color:var(--text-dim); line-height:1.4;">${{e.needed || e.desc || e.dachStatus}}</p>
        </div>
      `).join('');

      // 6 Breakthrough Innovation Technology Showcases from https://www.kone.com/global/en/innovation.html
      const innovations = [
        {{
          title: "KONE EcoDisc® Planetary Gearless Hoisting",
          desc: "The pioneering machine-room-less (MRL) breakthrough that eliminated penthouse elevator rooms and reduced energy usage by up to 50%.",
          img: KONE_IMAGES.ecodisc,
          badge: "Pioneering Hoisting"
        }},
        {{
          title: "KONE UltraRope® Carbon-Fiber Technology",
          desc: "Ultra-light carbon-fiber core replacing traditional steel wire ropes, enabling elevator travel up to 1,000 meters while slashing moving masses.",
          img: KONE_IMAGES.ultrarope,
          badge: "High-Rise Breakthrough"
        }},
        {{
          title: "KONE DX Class Digital Experience Lifts",
          desc: "The world's first connected digital elevator family with built-in APIs, multisensory car interiors, and smart building integration.",
          img: KONE_IMAGES.dx_car,
          badge: "Digital Ecosystem"
        }},
        {{
          title: "KONE JumpLift™ Construction Elevator",
          desc: "Self-climbing elevator operating inside the building's permanent hoistway during construction, saving weeks on skyscraper build schedules.",
          img: KONE_IMAGES.jumplift,
          badge: "Construction Velocity"
        }},
        {{
          title: "KONE Autonomous Mobile Robot (AMR) Integration",
          desc: "Standard open APIs enabling service robots and automated delivery fleets to call lifts, navigate multiple floors, and deliver goods autonomously.",
          img: KONE_IMAGES.robot,
          badge: "Robotics & AI"
        }},
        {{
          title: "KONE Escalator Modernization & Regenerative People Flow",
          desc: "Modular replacement systems and energy-regenerative drives for heavy transit hubs and airports, capturing braking power back into the grid.",
          img: KONE_IMAGES.escalator,
          badge: "Transit Infrastructure"
        }}
      ];

      let innovCards = innovations.map(inno => `
        <div class="stat-card" style="padding:0; overflow:hidden; display:flex; flex-direction:column;">
          <div style="height:120px; background:url('${{inno.img}}') center/cover no-repeat; position:relative;">
            <div style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(0,6,31,0.1) 0%, rgba(0,6,31,0.6) 100%); display:flex; align-items:flex-end; padding:10px 12px;">
              <span class="badge" style="background:#ffffff; color:var(--color-primary-1); font-weight:700; font-size:10.5px;">${{inno.badge}}</span>
            </div>
          </div>
          <div style="padding:14px; display:flex; flex-direction:column; flex:1;">
            <h4 style="font-size:13px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">${{inno.title}}</h4>
            <p style="font-size:11.5px; color:var(--text-dim); line-height:1.45; margin:0 0 10px;">${{inno.desc}}</p>
            <div style="margin-top:auto;">
              <span class="badge badge-neutral" style="font-size:10px;">Available for Replication</span>
            </div>
          </div>
        </div>
      `).join('');

      return `
        <!-- INNOVATION PLATFORMS HEADER -->
        <div class="glass-panel">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
                KONE Breakthrough Innovation Platforms (from kone.com/innovation)
              </div>
              <div class="panel-subtitle">Global technological building blocks available for cross-market package deployment</div>
            </div>
            <span class="badge badge-primary">6 Validated Platforms</span>
          </div>

          <div class="grid-3" style="margin-bottom:var(--space-8);">
            ${{innovCards}}
          </div>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>
                The 5 Codified Playbook Elements (Origin: DACH)
              </div>
              <div class="panel-subtitle">Packaged operational components ready for cross-market replication</div>
            </div>
            <span class="badge badge-success">Playbook: One-Week Modernization</span>
          </div>

          <div class="grid-3" style="margin-bottom:var(--space-8);">
            ${{elementRows}}
          </div>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>
                Next Market Replication Candidates
              </div>
              <div class="panel-subtitle">Similarity scoring based on connected base, installed age, and delivery readiness</div>
            </div>
          </div>

          <table class="data-table">
            <thead>
              <tr>
                <th>Market</th>
                <th>Suitability Score</th>
                <th>Base Units</th>
                <th>15+ Yr Base</th>
                <th>Capability Match</th>
                <th>Est. Impact</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong style="color:var(--color-primary-2);">Iberia</strong></td>
                <td><span class="badge badge-success num">92% Match</span></td>
                <td class="num">96,000</td>
                <td class="num">36%</td>
                <td>4 of 5 In Place</td>
                <td class="num" style="color:var(--color-primary-1); font-weight:700;">+€6.1M</td>
                <td><span class="badge badge-primary">Active in Stage 5</span></td>
              </tr>
              <tr>
                <td><strong style="color:var(--color-primary-2);">Benelux</strong></td>
                <td><span class="badge badge-primary num">84% Match</span></td>
                <td class="num">61,000</td>
                <td class="num">34%</td>
                <td>3 of 5 In Place (Need quote desk)</td>
                <td class="num" style="color:var(--color-primary-1); font-weight:700;">+€4.8M</td>
                <td>
                  <button class="btn-action" style="padding:4px 10px; font-size:11px;" onclick="replicateToMarket('Benelux', 'One-Week Modernization')">
                    Replicate to Benelux →
                  </button>
                </td>
              </tr>
              <tr>
                <td><strong style="color:var(--color-primary-2);">UK & Ireland</strong></td>
                <td><span class="badge badge-neutral num">79% Match</span></td>
                <td class="num">142,000</td>
                <td class="num">31%</td>
                <td>3 of 5 In Place (Need tech tools)</td>
                <td class="num" style="color:var(--color-primary-1); font-weight:700;">+€3.9M</td>
                <td>
                  <button class="btn-outline" style="padding:4px 8px; font-size:11px;" onclick="replicateToMarket('UK & Ireland', 'One-Week Modernization')">
                    Replicate
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      `;
    }}

    function replicateToMarket(market, playbook) {{
      showToast(`Initiating replication of "${{playbook}}" to ${{market}}...`);
      setTimeout(() => {{
        showToast(`Playbook codified for ${{market}}. Jump to Stage 8 to view updated institutional memory.`);
      }}, 1000);
    }}

    /* STAGE 7: OPTIMISE */
    function renderStage7Optimise() {{
      const d90 = APP_DATA.day90Outcomes;

      return `
        <div class="glass-panel">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
                Day-90 Realized Outcomes (Spain Modernization Pilot)
              </div>
              <div class="panel-subtitle">Reviewing real field data vs baseline expectations · 1 February 2027</div>
            </div>
            <span class="badge badge-success">Pilot Complete · 38 Buildings</span>
          </div>

          <div class="grid-4" style="margin-bottom:var(--space-8);">
            <div class="stat-card">
              <span class="stat-label">Quotes Delivered</span>
              <div class="stat-val" style="color:var(--color-primary-2);">${{d90.quotes}}</div>
              <div class="stat-delta positive">38 Target Cohort</div>
            </div>
            <div class="stat-card">
              <span class="stat-label">Conversion Rate</span>
              <div class="stat-val" style="color:var(--color-success-primary);">${{d90.conversion}}%</div>
              <div class="stat-delta positive">+${{d90.conversionDelta}}% vs Baseline (${{d90.baselineConversion}}%)</div>
            </div>
            <div class="stat-card">
              <span class="stat-label">Realized Orders</span>
              <div class="stat-val" style="color:var(--color-primary-1);">${{d90.orders}} Units</div>
              <div class="stat-delta positive">€${{d90.totalOrderValue.toLocaleString()}} Value</div>
            </div>
            <div class="stat-card">
              <span class="stat-label">Avg. Days On Site</span>
              <div class="stat-val" style="color:var(--color-primary-2);">${{d90.avgDaysOnSite}} Days</div>
              <div class="stat-delta positive">${{d90.daysSavedPerLift}}d faster (${{d90.totalDaysSaved}}d saved)</div>
            </div>
          </div>

          <div class="grid-2" style="margin-bottom:var(--space-8);">
            <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px; box-shadow:var(--shadow-5);">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-size:12px; text-transform:uppercase; color:var(--color-primary-1); font-weight:700;">Technician Referral Velocity</span>
                <span class="badge badge-success num">124% of Target</span>
              </div>
              <div style="font-size:22px; font-weight:800; color:var(--color-primary-2); margin-bottom:4px;">
                ${{d90.referralsAchieved}} <span style="font-size:13px; color:var(--text-dim); font-weight:400;">/ ${{d90.referralsTarget}} Target Referrals</span>
              </div>
              <p style="font-size:12px; color:var(--text-dim); line-height:1.45; margin:0;">
                Maintenance technicians logged 112 qualified leads via the mobile maintenance routine, with zero added marketing agency spend.
              </p>
            </div>

            <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px; box-shadow:var(--shadow-5);">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-size:12px; text-transform:uppercase; color:var(--color-primary-1); font-weight:700;">Data Cleanliness Gate</span>
                <span class="badge badge-warning num">${{d90.ageVerifiedPct}}% Verified</span>
              </div>
              <div style="font-size:22px; font-weight:800; color:var(--color-primary-2); margin-bottom:4px;">
                ${{d90.ageVerifiedCount}} <span style="font-size:13px; color:var(--text-dim); font-weight:400;">/ 38 Units Age-Verified</span>
              </div>
              <p style="font-size:12px; color:var(--text-dim); line-height:1.45; margin:0;">
                7 units required physical plate inspections by technicians on site due to legacy paper records from 1990s installations.
              </p>
            </div>
          </div>

          <div class="panel-header">
            <div class="panel-title" style="font-size:13px;">Mid-Flight Adjustments & Dynamic Tuning</div>
          </div>

          <div class="grid-3" style="margin-bottom:0;">
            <div class="stat-card">
              <h4 style="font-size:13.5px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Increase to €200/Lead</h4>
              <p style="font-size:11.5px; color:var(--text-dim); line-height:1.4; margin-bottom:8px;">Technician incentive yielded 112 leads. Further increase expected to accelerate Barcelona conversion.</p>
              <button class="btn-action" style="padding:4px 10px; font-size:11px;" onclick="applyMidflightPivot('incentive')">Apply adjustment</button>
            </div>
            <div class="stat-card">
              <h4 style="font-size:13.5px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Pre-Stock Madrid Depot</h4>
              <p style="font-size:11.5px; color:var(--text-dim); line-height:1.4; margin-bottom:8px;">Standardized shaft packs cut install to 6.4 days. Buffering inventory guarantees 5-day cycle.</p>
              <button class="btn-action" style="padding:4px 10px; font-size:11px;" onclick="applyMidflightPivot('depot')">Apply adjustment</button>
            </div>
            <div class="stat-card">
              <h4 style="font-size:13.5px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Deploy to Benelux Brief</h4>
              <p style="font-size:11.5px; color:var(--text-dim); line-height:1.4; margin-bottom:8px;">Pass proven Iberian referral playbook directly into Benelux's active Q2 campaign.</p>
              <button class="btn-action" style="padding:4px 10px; font-size:11px;" onclick="applyMidflightPivot('benelux')">Apply adjustment</button>
            </div>
          </div>
        </div>
      `;
    }}

    function applyMidflightPivot(type) {{
      showToast(`Mid-flight adjustment "${{type}}" applied to operational pipeline.`);
      setTimeout(() => {{
        goStage(8);
      }}, 700);
    }}

    /* STAGE 8: LEARN */
    function renderStage8Learn() {{
      const logs = state.outcomesLog;

      let logRows = logs.map(l => `
        <tr>
          <td><span class="badge badge-primary">${{l.id}}</span></td>
          <td>${{l.period}}</td>
          <td>
            <strong style="color:var(--color-primary-2);">${{l.title}}</strong>
            <div style="font-size:11.5px; color:var(--text-dim); margin-top:2px;">${{l.learning}}</div>
          </td>
          <td>${{l.market}}</td>
          <td><span class="badge ${{l.outcome === 'completed' ? 'badge-success' : l.outcome === 'in_flight' ? 'badge-primary' : 'badge-neutral'}}">${{l.outcome}}</span></td>
          <td class="num" style="font-weight:700; color:var(--color-primary-2);">${{l.roi ? l.roi + 'x' : '—'}}</td>
          <td><strong style="color:var(--color-primary-1);">${{l.result}}</strong></td>
        </tr>
      `).join('');

      return `
        <!-- INSTITUTIONAL MEMORY BANNER -->
        <div class="glass-panel" style="padding:0; overflow:hidden; margin-bottom:var(--space-8); display:grid; grid-template-columns: 280px 1fr; background:#ffffff;">
          <div style="background: url('${{KONE_IMAGES.collab}}') center/cover no-repeat; min-height:150px; position:relative;">
            <div style="position:absolute; inset:0; background:linear-gradient(90deg, rgba(20,80,245,0.2) 0%, rgba(0,6,31,0.5) 100%); display:flex; align-items:flex-end; padding:14px;">
              <span class="badge" style="background:#ffffff; color:var(--color-primary-1); font-weight:700;">Institutional Memory Bank</span>
            </div>
          </div>
          <div style="padding:18px 24px; display:flex; flex-direction:column; justify-content:center;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span class="badge badge-success">Closed-Loop Learning</span>
              <span class="badge badge-primary">Bayesian Drift (0.62 → 0.84)</span>
            </div>
            <h3 style="font-size:17px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Institutional Memory & Decision Recalibration</h3>
            <p style="font-size:12.5px; color:var(--text-dim); line-height:1.5; margin:0;">
              Every campaign outcome, field audit, and installation efficiency metric updates the Assisted Decisioning System. Future predictions become progressively more accurate.
            </p>
          </div>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 1-4 4v14a3 3 0 0 0 3-3h7z"/></svg>
                Institutional Memory Bank & Decision Outcome Log
              </div>
              <div class="panel-subtitle">Every intervention feeds back into model priors · Eliminating organizational amnesia</div>
            </div>
            <span class="badge badge-success">Closed-Loop Learning Active</span>
          </div>

          <table class="data-table" style="margin-bottom:var(--space-8);">
            <thead>
              <tr>
                <th>Record</th>
                <th>Period</th>
                <th>Decision & Codified Learning</th>
                <th>Market</th>
                <th>Status</th>
                <th>Realized ROI</th>
                <th>Quantified Result</th>
              </tr>
            </thead>
            <tbody>
              ${{logRows}}
            </tbody>
          </table>

          <div style="background:var(--color-primary-6); border:1px solid var(--color-primary-8); border-radius:var(--radius-3); padding:16px; display:flex; align-items:center; justify-content:space-between;">
            <div>
              <h4 style="font-size:13.5px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">The Flywheel's Return Path</h4>
              <p style="font-size:12px; color:var(--text-dim); margin:0;">
                Because Iberia achieved <strong>€927K</strong> in orders and <strong>39.5%</strong> conversion, the system recalibrates the confidence prior for Stage 3 from <strong>0.62</strong> to <strong>0.84</strong>.
              </p>
            </div>
            <button class="btn-action" onclick="recalibrateAndReturnToPrio()">
              Recalibrate Confidence & Return to Prioritise →
            </button>
          </div>
        </div>
      `;
    }}

    function recalibrateAndReturnToPrio() {{
      state.recalibratedConfidence = 84;
      showToast('Confidence recalibrated to 84%. Returning to Stage 3 Prioritise.');
      setTimeout(() => {{
        goStage(3);
      }}, 500);
    }}

    function renderScriptView() {{
      const scenes = APP_DATA.scriptScenes || [];
      const pillsContainer = document.getElementById('scriptScenePills');
      pillsContainer.innerHTML = scenes.map((s, idx) => {{
        const sNum = typeof s.scene === 'number' ? `Scene ${{s.scene}}` : String(s.scene);
        const titleFirst = (s.title || '').split(' ')[0] || '';
        return `
          <button class="scene-pill ${{idx === state.scriptSceneIdx ? 'active' : ''}}" onclick="selectScriptScene(${{idx}})">
            ${{sNum}} · ${{titleFirst}}
          </button>
        `;
      }}).join('');

      const curr = scenes[state.scriptSceneIdx] || scenes[0];
      const sceneNum = parseInt(String(curr.scene).replace(/\D/g, '')) || (state.scriptSceneIdx + 1);
      const imgInfo = SCENE_IMAGE_MAP[sceneNum] || {{ img: KONE_IMAGES.highrise, tag: 'KONE Innovation' }};

      const bannerEl = document.getElementById('sceneBannerImg');
      if (bannerEl) {{
        bannerEl.style.backgroundImage = `url('${{imgInfo.img}}')`;
      }}
      const tagEl = document.getElementById('sceneImageTag');
      if (tagEl) {{
        tagEl.textContent = imgInfo.tag;
      }}

      document.getElementById('sceneAct').textContent = curr.act || 'Act I';
      document.getElementById('sceneHeadline').textContent = `Scene ${{curr.scene}}: ${{curr.title}}`;
      document.getElementById('sceneMeta').textContent = `${{curr.timecode || '00:00'}} · Speaker: ${{curr.speaker || 'KONE Leadership'}}`;
      document.getElementById('sceneDialogue').textContent = `"${{curr.dialogue || ''}}"`;
      document.getElementById('sceneTakeaway').textContent = curr.takeaway || '';
      document.getElementById('scenePrompt').textContent = curr.headline || '';
    }}

    function selectScriptScene(idx) {{
      state.scriptSceneIdx = idx;
      renderScriptView();
    }}

    function jumpFromScriptToStage() {{
      const scene = APP_DATA.scriptScenes[state.scriptSceneIdx] || {{}};
      const targetScreen = (scene.screenTarget || scene.targetScreen || '').toLowerCase();
      let stageNum = 1;
      if (targetScreen.includes('sense')) stageNum = 1;
      else if (targetScreen.includes('diagnos')) stageNum = 2;
      else if (targetScreen.includes('priorit')) stageNum = 3;
      else if (targetScreen.includes('simulat')) stageNum = 4;
      else if (targetScreen.includes('orchestrat') || targetScreen.includes('execution')) stageNum = 5;
      else if (targetScreen.includes('replicat')) stageNum = 6;
      else if (targetScreen.includes('optimis')) stageNum = 7;
      else if (targetScreen.includes('learn') || targetScreen.includes('ingredient')) stageNum = 8;

      switchSurface('ads');
      goStage(stageNum);
    }}

    /* ASK THE ADS MODAL */
    const ASK_QUESTIONS = [
      {{
        q: 'Where is our greatest modernization growth opportunity right now?',
        stage: 1,
        title: 'Iberia 15+ Year Elevator Base (OP-01)',
        ans: 'Iberia has 34,500 elevators over 15 years old (36% of its installed base). However, its 90-day account activation is only 25% compared to 62% in DACH, creating a €6.1M revenue opportunity.'
      }},
      {{
        q: 'Why is Iberia underperforming DACH in quote conversion?',
        stage: 2,
        title: 'Technician Lead Capture & Disruption Fear',
        ans: 'DACH achieved 38% conversion through two primary levers: Service Technician Digital Lead Capture (accounting for 41% of variance) and a Guaranteed 5-Day Disruption Window that eliminated building managers’ downtime objections.'
      }},
      {{
        q: 'What happens if we reallocate €8.4M to One-Week Modernization?',
        stage: 4,
        title: 'Simulation Output: +€14.2M Revenue, 3.4x ROI',
        ans: 'Allocating €8.4M to Iberia generates a projected €14.2M in incremental orders across 38 buildings with an 11-month payback horizon and 88% confidence.'
      }},
      {{
        q: 'How do we replicate the DACH playbook to Benelux?',
        stage: 6,
        title: 'Benelux Suitability Match: 84%',
        ans: 'Benelux matches 4 of the 5 codified DACH playbook criteria (61k units, 44% connectivity). Replicating requires standing up a fast-track 48h quote desk and Dutch/French localized modular content.'
      }},
      {{
        q: 'How does the system get smarter from our decisions?',
        stage: 8,
        title: 'Closed Feedback Loop & Confidence Recalibration',
        ans: 'Every committed intervention writes a typed record into institutional memory. Acting on records converts them into empirical evidence, which automatically lifts the confidence scores of related growth opportunities in Stage 3 Prioritise.'
      }}
    ];

    function openAskModal() {{
      const m = document.getElementById('askModal');
      const qList = document.getElementById('askQuestionsList');
      qList.innerHTML = ASK_QUESTIONS.map((item, idx) => `
        <button class="btn-outline" style="text-align:left; justify-content:flex-start; padding:10px 14px; font-size:12.5px;" onclick="selectAskQuestion(${{idx}})">
          <span class="badge badge-primary num">${{idx + 1}}</span>
          ${{item.q}}
        </button>
      `).join('');
      m.style.display = 'flex';
    }}

    function closeAskModal() {{
      document.getElementById('askModal').style.display = 'none';
      document.getElementById('askAnswerBox').style.display = 'none';
    }}

    function selectAskQuestion(idx) {{
      const item = ASK_QUESTIONS[idx];
      document.getElementById('askAnswerBox').style.display = 'block';
      document.getElementById('askAnswerTitle').textContent = item.title;
      document.getElementById('askAnswerBody').textContent = item.ans;
      const btn = document.getElementById('btnAskJump');
      btn.onclick = () => {{
        closeAskModal();
        switchSurface('ads');
        goStage(item.stage);
      }};
    }}

    /* REQUIREMENT COVERAGE DRAWER */
    const COVERAGE_DATA = [
      ['FR1.1', 'Portfolio performance grid, 7 markets against plan', 1, 'Stage 1 · Sense Lattice'],
      ['FR1.2', 'Rule-based thresholds auto-flagging over/under-performance', 1, 'Stage 1 · Signal Queue'],
      ['FR2.1', 'Market-versus-market benchmark (Iberia vs DACH)', 2, 'Stage 2 · Benchmark Cards'],
      ['FR2.2', 'Templated root-cause breakdown with contribution weights', 2, 'Stage 2 · 5 Operational Levers'],
      ['FR3.1', 'Ranked opportunities on scored factors', 3, 'Stage 3 · Scored Matrix'],
      ['FR3.2', 'Dynamic confidence recalibration from session log', 3, 'Stage 3 · Return Path'],
      ['FR4.1', 'Budget-allocation control €0M–€20M with €8.4M detent', 4, 'Stage 4 · Simulation Slider'],
      ['FR4.2', 'Scenario comparisons and financial payback modeling', 4, 'Stage 4 · Scenario Cards'],
      ['FR5.1', 'Decisions become typed, tracked intervention records', 5, 'Stage 5 · Interventions Board'],
      ['FR5.2', '38-building pilot cohort inspection with shaft specs', 5, 'Stage 5 · Cohort Explorer'],
      ['FR6.1', 'Codified 5-element market playbook packaging', 6, 'Stage 6 · Playbook Elements'],
      ['FR6.2', 'Cross-market suitability ranking and 1-click replication', 6, 'Stage 6 · Replication Table'],
      ['FR7.1', 'Day-90 empirical results scorecard vs conventional baseline', 7, 'Stage 7 · Pilot Scorecard'],
      ['FR8.1', 'Institutional memory outcomes log and closed feedback loop', 8, 'Stage 8 · Outcomes Log']
    ];

    function openCoverageDrawer() {{
      const listFR = document.getElementById('coverageFRList');
      listFR.innerHTML = COVERAGE_DATA.map(([id, desc, stg, where]) => `
        <div style="padding:8px 0; border-bottom:1px solid rgba(218,228,255,0.06); display:flex; justify-content:space-between; align-items:center;">
          <div>
            <strong style="color:var(--color-primary-11); font-size:11.5px;">${{id}}</strong>
            <div style="font-size:12px; color:var(--color-primary-2);">${{desc}}</div>
            <div style="font-size:10.5px; color:var(--color-accent-2);">${{where}}</div>
          </div>
          <button class="btn-outline" style="padding:2px 8px; font-size:10.5px;" onclick="closeCoverageDrawer(); switchSurface('ads'); goStage(${{stg}});">
            Go →
          </button>
        </div>
      `).join('');

      const listSC = document.getElementById('coverageSceneList');
      listSC.innerHTML = APP_DATA.scriptScenes.map((s, idx) => `
        <div style="padding:8px 0; border-bottom:1px solid rgba(218,228,255,0.06); display:flex; justify-content:space-between; align-items:center;">
          <div>
            <strong style="color:var(--color-primary-2); font-size:12px;">${{s.scene}}: ${{s.title}}</strong>
            <div style="font-size:10.5px; color:var(--text-dim);">${{s.act}} · ${{s.speaker}}</div>
          </div>
          <button class="btn-outline" style="padding:2px 8px; font-size:10.5px;" onclick="closeCoverageDrawer(); switchSurface('script'); selectScriptScene(${{idx}});">
            View →
          </button>
        </div>
      `).join('');

      document.getElementById('coverageBackdrop').style.display = 'block';
      document.getElementById('coverageDrawer').classList.add('open');
    }}

    function closeCoverageDrawer() {{
      document.getElementById('coverageBackdrop').style.display = 'none';
      document.getElementById('coverageDrawer').classList.remove('open');
    }}

    /* BUILDING INSPECTION MODAL */
    function openBuildingModal(id) {{
      const b = APP_DATA.cohort.find(x => x.id === id);
      if (!b) return;
      const bName = b.name || `${{b.buildingType || 'Building'}} (${{b.id}})`;
      const bAddress = b.address || 'Calle Gran Vía 42';
      const bCity = b.city || 'Madrid';
      const bAge = b.age || 35;
      const bLifts = b.elevatorCount ?? b.quotedUnits ?? 1;
      const bShaft = b.shaftType || b.shaft || 'Standard';
      const bValue = b.estValue ?? b.orderValue ?? 24400;
      const bStatus = b.status || 'Active Pilot';
      const bNotes = b.notes || 'Standard shaft dimensions verified. Guide rails aligned within 0.8mm tolerance. EcoDisc modernization package fits with zero structural alterations.';
      const bTelemetry = b.telemetryScore ? `Telemetry Score: ${{b.telemetryScore}}/100 · Vibration: ${{b.vibrationMmS}} mm/s · Cycles: ${{b.doorCyclesPerMonth ? b.doorCyclesPerMonth.toLocaleString() : '22,000'}}/mo` : 'Telemetry: Normal operational profile';

      document.getElementById('bldModalName').textContent = `${{bName}} (${{bCity}})`;
      document.getElementById('bldModalContent').innerHTML = `
        <div style="position:relative; height:120px; border-radius:var(--radius-3); overflow:hidden; margin-bottom:14px; background:url('${{KONE_IMAGES.kunshan}}') center/cover no-repeat;">
          <div style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(0,6,31,0.2) 0%, rgba(0,6,31,0.7) 100%); display:flex; align-items:flex-end; padding:12px 16px;">
            <span class="badge" style="background:#ffffff; color:var(--color-primary-1); font-weight:700;">Kunshan Test Tower Telemetry & Diagnostic Match</span>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:12px; margin-bottom:16px;">
          <div class="stat-card">
            <span class="stat-label">Address</span>
            <div style="font-size:13px; color:var(--color-primary-2); font-weight:600;">${{bAddress}}</div>
            <div style="font-size:11px; color:var(--text-dim);">${{bCity}}, Spain</div>
          </div>
          <div class="stat-card">
            <span class="stat-label">Elevators & Age</span>
            <div style="font-size:13px; color:var(--color-primary-2); font-weight:600;">${{bLifts}} Lift (${{bAge}} Years Old)</div>
            <div style="font-size:11px; color:var(--text-dim);">Shaft: ${{bShaft}}</div>
          </div>
          <div class="stat-card">
            <span class="stat-label">Quote Value</span>
            <div style="font-size:16px; color:var(--color-success-primary); font-weight:700;">€${{bValue.toLocaleString()}}</div>
            <div style="font-size:11px; color:var(--text-dim);">${{bStatus}}</div>
          </div>
        </div>
        <div style="background:var(--color-primary-6); border:1px solid var(--color-primary-8); padding:14px; border-radius:var(--radius-3); margin-bottom:14px;">
          <div style="font-size:11px; text-transform:uppercase; color:var(--color-primary-1); font-weight:700; margin-bottom:4px;">Technician Shaft Audit Notes</div>
          <p style="font-size:12.5px; color:var(--color-primary-2); line-height:1.5; margin:0 0 8px 0;">${{bNotes}}</p>
          <div style="font-size:11px; color:var(--color-accent-2); font-weight:600;">📡 ${{bTelemetry}}</div>
        </div>
        <div style="display:flex; justify-content:flex-end;">
          <button class="btn-action" onclick="closeBuildingModal(); showToast('Building ${{b.id}} prioritized in technician schedule.');">
            Fast-Track Installation Schedule
          </button>
        </div>
      `;
      document.getElementById('buildingModal').style.display = 'flex';
    }}

    function closeBuildingModal() {{
      document.getElementById('buildingModal').style.display = 'none';
    }}

    /* INITIALIZATION */
    window.addEventListener('DOMContentLoaded', () => {{
      renderStageRail();
      renderStageContent();
      renderBottomChrome();
    }});
  </script>
</body>
</html>
"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    with open('kone-marketing-os.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Build complete! index.html ({len(html_content)} bytes) and kone-marketing-os.html successfully written.")

if __name__ == '__main__':
    build_app()
