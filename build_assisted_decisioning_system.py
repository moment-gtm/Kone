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
      <a href="tech-architecture.html" class="btn-chrome" style="text-decoration:none; color:var(--color-primary-1); font-weight:700; border-color:var(--color-primary-9); background:var(--color-primary-3);" title="Technical Deep-Dive: Architecture, Roadmap, Data Audit & Client Defense Q&A">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
        Tech Architecture & Client Prep ↗
      </a>
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
      {{ n: 2, key: 'diagnose', name: 'Diagnose', q: 'Why is ITIB outperforming other European Frontlines in ONE Week MOD conversion?', next: 'Prioritise what matters' }},
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
      {{ id: 'L-01', period: '2025 Q3', title: 'DACH ONE Week MOD Benchmark', market: 'DACH', type: 'modernization', outcome: 'completed', roi: 3.8, result: '+€9.4M order intake, 38% conversion', learning: 'Guaranteed <=7-day disruption window and technician referral routine eliminated property manager objections.' }},
      {{ id: 'L-02', period: '2025 Q4', title: 'Nordics 24/7 Connect Predictive Overhaul', market: 'Nordics', type: 'connectivity', outcome: 'completed', roi: 3.2, result: '+€4.2M contracted, 52% connected share', learning: 'Vibration anomaly threshold triggers 88% accurate modernization leads.' }},
      {{ id: 'L-03', period: '2026 Q1', title: 'France High-Rise Modernization Campaign', market: 'France', type: 'modernization', outcome: 'completed', roi: 2.1, result: '+€3.4M order intake, 27% conversion', learning: 'Generic creative assets had 14-week translation lead time; need modular CSC ingredients.' }},
      {{ id: 'L-04', period: '2026 Q2', title: 'UK & Ireland Maintenance Retention AI', market: 'UK & Ireland', type: 'service', outcome: 'completed', roi: 2.9, result: '-3.2% churn reduction across 142k units', learning: 'Service technician tablet checklist captured 230 qualified aging lift leads.' }},
      {{ id: 'L-05', period: '2026 Q3', title: 'Benelux Elevator Safety Audit Drive', market: 'Benelux', type: 'compliance', outcome: 'completed', roi: 2.4, result: '+€2.1M modernization orders', learning: 'Municipal safety code transitions drive high consideration when paired with financing.' }},
      {{ id: 'L-06', period: '2026 Q4', title: 'European ONE Week MOD Campaign (DEA Package)', market: 'Europe (6 Frontlines)', type: 'campaign', outcome: 'completed', roi: 4.2, result: '20,061 addressable MonoSpace LIS units sized across 6 frontlines', learning: 'Focusing on residential MonoSpace LIS assets (<=7 floors) with standard shafts yields 2.4x higher quote conversion.' }},
      {{ id: 'L-07', period: '2026 Q4', title: 'DACH Technician Referral Incentive Routine', market: 'DACH', type: 'field_ops', outcome: 'completed', roi: 4.1, result: '41% of all quotes sourced via technicians', learning: 'Technicians are the ultimate trusted advisors for building owners; €100 bonus tripled lead volume.' }}
    ];

    /* ============================================================================
       APPLICATION RUNTIME STATE
       ========================================================================== */
    const INITIAL_STATE = {{
      stage: 1,
      surface: 'ads',
      selectedMarket: 'ITIB (Italy & Iberia)',
      selectedCandidate: 'OP-02',
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
          title: 'ONE Week MOD Pilot (MonoSpace LIS)',
          market: 'ITIB (Italy & Iberia)',
          budget: 8.4,
          impact: 14.2,
          roi: 3.4,
          confidence: 88,
          owners: ['Field Marketing', 'Sales Ops (Marc Puig)', 'Service Technicians', 'Operations Lead'],
          source: 'Simulate · Stage 4',
          detail: '€8.4M allocated to 38 qualified residential buildings in Spain & Italy. Targets 31%+ quote conversion with guaranteed <=7d install window.'
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

      if (s === 1) return {{ label: 'Next: Diagnose why ITIB is missing plan', run: () => goStage(2) }};
      if (s === 2) return {{ label: 'Next: Prioritise what matters across Europe', run: () => goStage(3) }};
      if (s === 3) return {{ label: 'Next: Simulate the ONE Week MOD pilot allocation', run: () => goStage(4) }};
      if (s === 4) {{
        return {{
          label: 'Commit €8.4M to ONE Week MOD and open Orchestrate',
          run: () => {{
            if (!state.interventions.some(i => i.ref === 'INT-01')) {{
              createIntervention({{
                type: 'modernization',
                title: 'ONE Week MOD Pilot (MonoSpace LIS)',
                market: 'ITIB (Italy & Iberia)',
                budget: state.simAlloc,
                impact: Math.round(state.simAlloc * 1.69 * 10) / 10,
                roi: 3.4,
                confidence: 88,
                owners: ['Field Marketing', 'Sales Ops (Marc Puig)', 'Service Technicians', 'Operations Lead'],
                source: 'Simulate · Stage 4',
                detail: `€${{state.simAlloc}}M committed to ONE Week MOD in Spain & Italy.`
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
            label: 'Replicate ONE Week MOD to GIN (Great Britain & Ireland)',
            run: () => replicateToMarket('GIN (Great Britain & Ireland)', 'ONE Week MOD')
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

        /* STAGE 1: SENSE - MARKETING CAMPAIGN & MARKET NEED RADAR */
    function renderStage1Sense() {{
      const markets = APP_DATA.markets || [];
      const channels = APP_DATA.campaignChannels || [];
      const opps = APP_DATA.opportunities || [];
      const selectedM = markets.find(m => m.name === state.selectedMarket) || markets[0];

      // Top priority growth opportunities (GTM Tower style)
      const priorityOpportunities = [
        {{
          rank: 1,
          name: 'ITIB (Italy & Iberia)',
          sub: 'Phase 1 Awareness Surge → Phase 2 Need-ID Pilot',
          value: '€341.6k',
          area: 'Madrid, Barcelona & Milan (9,039 addressable units, 5,648 HOA accounts)',
          action: 'Diagnose',
          tone: 'growth',
          targetMarket: 'ITIB (Italy & Iberia)'
        }},
        {{
          rank: 2,
          name: 'GIN (Great Britain & Ireland)',
          sub: 'Retargeting Pool & Interactive Assessment Unlock',
          value: '€185.0k',
          area: 'London & Midlands (4,804 addressable units, 3,120 property managers)',
          action: 'Diagnose',
          tone: 'replicate',
          targetMarket: 'GIN (Great Britain & Ireland)'
        }},
        {{
          rank: 3,
          name: 'DACH (Germany, Austria, Switzerland)',
          sub: 'CPL Optimization & Property Manager Account Match',
          value: '€120.0k',
          area: 'Munich, Frankfurt & Vienna (2,470 addressable units, 1,840 accounts)',
          action: 'Diagnose',
          tone: 'watch',
          targetMarket: 'DACH'
        }}
      ];

      // Assisted Decisioning Recommendations (GTM Tower style next moves)
      const recommendations = [
        {{
          text: 'Diagnose why ITIB converts 31.1% on Meta Advantage+ while GIN lags at 18.4%',
          stageName: 'Diagnose',
          stageNum: 2,
          run: () => {{ selectMarket('ITIB (Italy & Iberia)'); goStage(2); }}
        }},
        {{
          text: 'Simulate €120k marketing reallocation from Search into LinkedIn & YouTube VRC',
          stageName: 'Simulate',
          stageNum: 4,
          run: () => {{ goStage(4); }}
        }},
        {{
          text: 'Orchestrate D&B ABA audience feeds & Salesforce CPQ 1-Click quotes for 9,039 ITIB assets',
          stageName: 'Orchestrate',
          stageNum: 5,
          run: () => {{ goStage(5); }}
        }},
        {{
          text: 'Replicate the winning ITIB ONE Week MOD awareness playbook into Great Britain & Ireland',
          stageName: 'Replicate',
          stageNum: 6,
          run: () => {{ goStage(6); }}
        }}
      ];

      // European Frontlines Campaign Table Rows
      let marketRows = markets.map(m => {{
        const isSelected = m.name === state.selectedMarket;
        const budgetDisplay = m.mediaBudget ? `€${{Math.round(m.mediaBudget / 1000)}}k` : '€110k';
        const reachActual = m.reachActual ? m.reachActual.toLocaleString() : '842,000';
        const reachPct = m.reachPct || 100;
        const retargetingPool = m.retargetingPool ? m.retargetingPool.toLocaleString() : '64,800';
        const mqls = m.mqls || 140;
        const convPct = m.mqlToSqlConv || m.conversion || 24;
        const cpl = m.cpl ? `€${{m.cpl}}` : '€48';
        
        let statusBadge = '<span class="badge badge-neutral">On Track</span>';
        if (m.campaignStatus === 'Growth Surge') statusBadge = '<span class="badge badge-success">Growth Surge</span>';
        else if (m.campaignStatus === 'Need-ID Friction') statusBadge = '<span class="badge badge-danger">Need-ID Friction</span>';
        else if (m.campaignStatus === 'Benchmark') statusBadge = '<span class="badge badge-primary">Benchmark</span>';
        else if (m.campaignStatus === 'Adapt & Test') statusBadge = '<span class="badge badge-warning">Adapt & Test</span>';
        else if (m.campaignStatus === 'High Potential') statusBadge = '<span class="badge badge-primary">High Potential</span>';

        return `
          <tr style="${{isSelected ? 'background: rgba(20, 80, 245, 0.06); font-weight: 500;' : ''}}">
            <td>
              <strong style="color:var(--color-primary-2);">${{m.name}}</strong>
              <div style="font-size:11px; color:var(--text-dim);">${{m.submarkets || 'European Frontline'}}</div>
            </td>
            <td>
              <span style="font-size:11.5px; font-weight:600; color:var(--color-primary-2);">${{m.campaignPhase || 'Phase 1: Awareness'}}</span>
            </td>
            <td class="num"><span class="badge badge-neutral num">${{budgetDisplay}}</span></td>
            <td class="num">
              <span style="font-weight:700; color:var(--color-primary-1);">${{reachActual}}</span>
              <span style="font-size:10.5px; color:${{reachPct >= 100 ? 'var(--color-success-primary)' : 'var(--color-danger-primary)'}}"> (${{reachPct}}%)</span>
            </td>
            <td class="num" style="font-weight:600;">${{retargetingPool}}</td>
            <td class="num" style="font-weight:700; color:var(--color-primary-2);">${{mqls}}</td>
            <td class="num">
              <span style="font-weight:700; color:${{convPct >= 30 ? 'var(--color-success-primary)' : convPct < 20 ? 'var(--color-danger-primary)' : 'var(--color-primary-1)'}}">${{convPct}}%</span>
            </td>
            <td class="num" style="font-weight:600; color:var(--color-primary-2);">${{cpl}}</td>
            <td>${{statusBadge}}</td>
            <td>
              ${{m.name === 'ITIB (Italy & Iberia)' ? `
                <button class="btn-action" style="padding:4px 10px; font-size:11px;" onclick="selectMarket('${{m.name}}'); goStage(2);">
                  Diagnose why →
                </button>
              ` : `
                <button class="btn-outline" style="padding:4px 8px; font-size:11px;" onclick="selectMarket('${{m.name}}');">
                  Select
                </button>
              `}}
            </td>
          </tr>
        `;
      }}).join('');

      return `
        <!-- QUESTION HEADER (GTM TOWER STYLE) -->
        <div style="margin-bottom:var(--space-6);">
          <div style="display:flex; align-items:center; gap:8px; margin-bottom:4px;">
            <span class="badge badge-primary">Stage 1 of 8</span>
            <span class="badge badge-neutral">European Modernization Campaign Radar</span>
            <span class="badge badge-success">600,000+ European Units In Scope</span>
          </div>
          <h2 style="font-size:24px; font-weight:800; color:var(--color-primary-2); letter-spacing:-0.03em; margin:0 0 6px;">
            Where should we focus next?
          </h2>
          <p style="font-size:13px; color:var(--text-dim); margin:0; max-width:980px; line-height:1.5;">
            Residential building managers and HOA boards have <strong>very low awareness of elevator modernization</strong>, often assuming older units only need continuous repairs or that KONE cannot upgrade non-KONE equipment. The <em>"Life, upgraded in ONE week"</em> campaign activates <strong>Phase 1 Awareness & Storytelling</strong> to break the perceived 4–8 week disruption barrier, funneling high-intent leads into <strong>Phase 2 Consideration & Need-Identification</strong> across 6 European Frontlines.
          </p>
        </div>

        <!-- TOP TWO PANELS (GTM TOWER LAYOUT) -->
        <div style="display:grid; grid-template-columns: 1.15fr 1fr; gap:var(--space-6); margin-bottom:var(--space-6);">
          
          <!-- LEFT: PRIORITY GROWTH OPPORTUNITIES -->
          <div class="glass-panel" style="margin-bottom:0; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div class="panel-header" style="margin-bottom:12px;">
                <div>
                  <div class="panel-title" style="color:var(--color-primary-1);">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>
                    Priority Modernization Campaign Opportunities
                  </div>
                  <div class="panel-subtitle">Focus on these three frontline markets first based on high-intent pipeline value.</div>
                </div>
                <span class="badge badge-primary">Active Prioritization</span>
              </div>

              ${{priorityOpportunities.map(p => `
                <div onclick="selectMarket('${{p.targetMarket}}'); goStage(2);" style="cursor:pointer; display:flex; align-items:center; justify-content:space-between; padding:10px 14px; margin-bottom:8px; background:#ffffff; border:1px solid var(--color-neutral-2); border-left:4px solid ${{p.tone === 'growth' ? 'var(--color-success-primary)' : p.tone === 'replicate' ? 'var(--color-primary-1)' : 'var(--color-warning-primary)'}}; border-radius:var(--radius-3); transition:all 0.15s ease;" onmouseover="this.style.borderColor='var(--color-primary-1)';" onmouseout="this.style.borderColor='var(--color-neutral-2)';">
                  <div style="display:flex; align-items:center; gap:12px;">
                    <span style="font-size:12px; font-weight:800; color:var(--text-dim); width:20px;">#${{p.rank}}</span>
                    <div>
                      <div style="display:flex; align-items:center; gap:6px;">
                        <strong style="font-size:13px; color:var(--color-primary-2);">${{p.name}}</strong>
                        <span class="badge badge-${{p.tone === 'growth' ? 'success' : p.tone === 'replicate' ? 'primary' : 'warning'}}" style="font-size:10px; padding:1px 6px;">${{p.action}}</span>
                      </div>
                      <div style="font-size:11.5px; color:var(--text-dim); margin-top:2px;">${{p.area}}</div>
                    </div>
                  </div>
                  <div style="text-align:right;">
                    <div style="font-size:18px; font-weight:800; color:${{p.tone === 'growth' ? 'var(--color-success-primary)' : 'var(--color-primary-1)'}}; letter-spacing:-0.03em;">+${{p.value}}</div>
                    <div style="font-size:10.5px; color:var(--text-dim);">Immediate Pipeline</div>
                  </div>
                </div>
              `).join('')}}
            </div>

            <div style="font-size:11.5px; color:var(--text-dim); margin-top:8px; padding-top:8px; border-top:1px dashed var(--color-neutral-2); display:flex; justify-content:space-between; align-items:center;">
              <span><strong>€646.6k</strong> total pipeline across top three frontlines.</span>
              <span style="color:var(--color-primary-1); font-weight:600;">Click any row to diagnose campaign levers →</span>
            </div>
          </div>

          <!-- RIGHT: ASSISTED DECISIONING RECOMMENDATIONS -->
          <div class="glass-panel" style="margin-bottom:0; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div class="panel-header" style="margin-bottom:12px;">
                <div>
                  <div class="panel-title" style="color:var(--color-primary-2);">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
                    Assisted Decisioning System Recommendations
                  </div>
                  <div class="panel-subtitle">The next four operational marketing moves, each one click from the stage that acts on it.</div>
                </div>
                <span class="badge badge-success">Automated Flighting</span>
              </div>

              ${{recommendations.map((r, i) => `
                <div style="display:flex; align-items:center; justify-content:space-between; padding:9px 12px; margin-bottom:7px; background:var(--color-primary-6); border:1px solid var(--color-primary-8); border-radius:var(--radius-3);">
                  <div style="display:flex; align-items:flex-start; gap:8px; max-width:80%;">
                    <span style="color:var(--color-primary-1); font-weight:700; font-size:12px; margin-top:1px;">${{i + 1}}.</span>
                    <span style="font-size:12px; color:var(--color-primary-2); line-height:1.4; font-weight:500;">${{r.text}}</span>
                  </div>
                  <button class="btn-action" style="padding:4px 10px; font-size:11px; white-space:nowrap;" onclick="runRecommendation(${{i}})">
                    ${{r.stageName}} →
                  </button>
                </div>
              `).join('')}}
            </div>

            <div style="font-size:11.5px; color:var(--text-dim); margin-top:8px; padding-top:8px; border-top:1px dashed var(--color-primary-8); display:flex; justify-content:space-between; align-items:center;">
              <span>Continuous marketing flight optimization powered by closed-loop learning.</span>
              <span class="badge badge-neutral">Auto-Sync</span>
            </div>
          </div>
        </div>

        <!-- CAMPAIGN CHANNELS RADAR (REPLACING IOT ASSET TELEMETRY) -->
        <div class="glass-panel" style="margin-bottom:var(--space-6);">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"/><line x1="7" y1="2" x2="7" y2="22"/><line x1="17" y1="2" x2="17" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="2" y1="7" x2="7" y2="7"/><line x1="2" y1="17" x2="7" y2="17"/><line x1="17" y1="17" x2="22" y2="17"/><line x1="17" y1="7" x2="22" y2="7"/></svg>
                Digital Engagement & Media Activation Signals (ONE Week MOD DEA Package)
              </div>
              <div class="panel-subtitle">Real-time media flighting and audience engagement across Phase 1 Awareness & Phase 2 Consideration channels</div>
            </div>
            <div style="display:flex; align-items:center; gap:8px;">
              <span class="badge badge-neutral">Media Signal: Omnichannel API</span>
              <button class="btn-outline" style="padding:4px 8px; font-size:11px; display:inline-flex; align-items:center; gap:4px;" onclick="simulateTelemetryJitter()">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>
                Refresh Channel Signals
              </button>
            </div>
          </div>

          <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap:var(--space-4); margin-bottom:var(--space-4);">
            
            <!-- META ADVANTAGE+ -->
            <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-top:3px solid var(--color-primary-1); border-radius:var(--radius-3); padding:14px;">
              <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px;">
                <span style="font-size:11px; font-weight:700; color:var(--color-primary-1); text-transform:uppercase;">Meta Advantage+</span>
                <span class="badge badge-success" style="font-size:10px;">108% Reach</span>
              </div>
              <div style="font-size:22px; font-weight:800; color:var(--color-primary-2); margin-bottom:2px;">842,000</div>
              <div style="font-size:11px; color:var(--text-dim); margin-bottom:8px;">Awareness Reach (Reels & Feed)</div>
              <div style="font-size:11.5px; color:var(--text-high); line-height:1.4; border-top:1px solid var(--color-neutral-5); padding-top:6px;">
                <div><strong>34.2%</strong> 3-sec hook rate (Emotional #1)</div>
                <div style="color:var(--text-dim); font-size:11px; margin-top:2px;">€6.40 CPM · 64,800 Retargeting Pool</div>
              </div>
            </div>

            <!-- LINKEDIN INMAIL & FEED -->
            <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-top:3px solid #0077b5; border-radius:var(--radius-3); padding:14px;">
              <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px;">
                <span style="font-size:11px; font-weight:700; color:#0077b5; text-transform:uppercase;">LinkedIn Sponsored</span>
                <span class="badge badge-primary" style="font-size:10px;">B2B Verified</span>
              </div>
              <div style="font-size:22px; font-weight:800; color:var(--color-primary-2); margin-bottom:2px;">184,000</div>
              <div style="font-size:11px; color:var(--text-dim); margin-bottom:8px;">Property & Facility Managers</div>
              <div style="font-size:11.5px; color:var(--text-high); line-height:1.4; border-top:1px solid var(--color-neutral-5); padding-top:6px;">
                <div><strong>1.84%</strong> CTR · 68 Qualified MQLs</div>
                <div style="color:var(--text-dim); font-size:11px; margin-top:2px;">€112 CPL · High-Intent Decision Makers</div>
              </div>
            </div>

            <!-- YOUTUBE VRC -->
            <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-top:3px solid #ff0000; border-radius:var(--radius-3); padding:14px;">
              <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px;">
                <span style="font-size:11px; font-weight:700; color:#ff0000; text-transform:uppercase;">YouTube VRC</span>
                <span class="badge badge-success" style="font-size:10px;">+14.8% Recall</span>
              </div>
              <div style="font-size:22px; font-weight:800; color:var(--color-primary-2); margin-bottom:2px;">480,000</div>
              <div style="font-size:11px; color:var(--text-dim); margin-bottom:8px;">Video Views (Skippable & Shorts)</div>
              <div style="font-size:11.5px; color:var(--text-high); line-height:1.4; border-top:1px solid var(--color-neutral-5); padding-top:6px;">
                <div><strong>46.2%</strong> View-Through Rate (VTR)</div>
                <div style="color:var(--text-dim); font-size:11px; margin-top:2px;">€0.028 CPV · Strong Emotional Storytelling</div>
              </div>
            </div>

            <!-- GOOGLE PMAX & D&B ABA -->
            <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-top:3px solid #0f9d58; border-radius:var(--radius-3); padding:14px;">
              <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px;">
                <span style="font-size:11px; font-weight:700; color:#0f9d58; text-transform:uppercase;">PMAX & D&B ABA</span>
                <span class="badge badge-primary" style="font-size:10px;">High Intent</span>
              </div>
              <div style="font-size:22px; font-weight:800; color:var(--color-primary-2); margin-bottom:2px;">159,000</div>
              <div style="font-size:11px; color:var(--text-dim); margin-bottom:8px;">Targeted HOA / Search Demand</div>
              <div style="font-size:11.5px; color:var(--text-high); line-height:1.4; border-top:1px solid var(--color-neutral-5); padding-top:6px;">
                <div><strong>4.12%</strong> CTR · 130 Assessment Starts</div>
                <div style="color:var(--text-dim); font-size:11px; margin-top:2px;">€52 CPL · "Elevator downtime" queries</div>
              </div>
            </div>

          </div>
        </div>

        <!-- EUROPEAN FRONTLINES CAMPAIGN PERFORMANCE MATRIX -->
        <div class="glass-panel" style="margin-bottom:var(--space-6);">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 0 1 10 10"/><path d="M12 12L20 4"/></svg>
                European Frontlines Campaign Performance Matrix (20,061 Addressable Residential Units · €705k Media)
              </div>
              <div class="panel-subtitle">Sensed across Phase 1 Awareness and Phase 2 Consideration activations in 6 European Frontline markets</div>
            </div>
            <span class="badge badge-primary">Frontline Portfolio</span>
          </div>

          <table class="data-table">
            <thead>
              <tr>
                <th>Frontline Market</th>
                <th>Campaign Phase</th>
                <th>Media Budget</th>
                <th>Awareness Reach</th>
                <th>Retargeting Pool</th>
                <th>MQLs (Leads)</th>
                <th>Quote Conv. %</th>
                <th>Cost per Lead</th>
                <th>Campaign Status</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              ${{marketRows}}
            </tbody>
          </table>
        </div>

        <!-- SELECTED FRONTLINE CAMPAIGN FOCUS CARD -->
        <div class="glass-panel" style="background:#ffffff; border-left:4px solid var(--color-primary-1); margin-bottom:0;">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
            <div style="max-width:75%;">
              <div style="display:flex; align-items:center; gap:8px; margin-bottom:4px;">
                <span class="badge badge-primary">${{selectedM.name}}</span>
                <span class="badge badge-success">${{selectedM.campaignStatus || 'Active Campaign'}}</span>
                <span class="badge badge-neutral">€${{Math.round((selectedM.mediaBudget || 120000)/1000)}}k Media Budget</span>
              </div>
              <h3 style="font-size:16px; font-weight:700; color:var(--color-primary-2); margin:0 0 4px;">
                Campaign Diagnosis Opportunity: ${{selectedM.name}} (${{selectedM.baseUnits ? selectedM.baseUnits.toLocaleString() : '9,039'}} target residential units)
              </h3>
              <p style="font-size:12.5px; color:var(--text-dim); margin:0; line-height:1.5;">
                In ${{selectedM.name}}, Phase 1 awareness reaches <strong>${{selectedM.reachActual ? selectedM.reachActual.toLocaleString() : '842,000'}} potential customers</strong>. The top performing creative is <em>${{selectedM.topCreative || 'Emotional #1 ("Take the fast-track to a better day")'}}</em>. Converting these into Phase 2 qualified quotes unlocks <strong>+€${{selectedM.potential || 6.1}}M</strong> in incremental modernization pipeline.
              </p>
            </div>
            <button class="btn-action" style="padding:10px 18px; font-size:13px;" onclick="goStage(2)">
              Diagnose Campaign Levers & Bottlenecks →
            </button>
          </div>
        </div>
      `;
    }}


        /* STAGE 2: DIAGNOSE - MARKETING ATTRIBUTION & DRIVER DECOMPOSITION */
    function renderStage2Diagnose() {{
      const selectedM = APP_DATA.markets.find(m => m.name === state.selectedMarket) || APP_DATA.markets[0];
      const isITIB = selectedM.name === 'ITIB (Italy & Iberia)' || selectedM.id === 'itib';
      const marketingDrivers = APP_DATA.dachDrivers || [];
      const channels = APP_DATA.campaignChannels || [];
      const creativeAngles = APP_DATA.creativeAngles || [];

      // Marketing driver rows (GTM Tower style driver decomposition)
      let driverRows = marketingDrivers.map(d => `
        <tr>
          <td>
            <strong style="color:var(--color-primary-2); font-size:13px;">${{d.driver}}</strong>
            <div style="font-size:11.5px; color:var(--text-dim); margin-top:3px; line-height:1.4;">${{d.observation}}</div>
          </td>
          <td><span class="badge badge-primary">${{d.type}}</span></td>
          <td class="num" style="color:var(--color-primary-1); font-weight:800; font-size:13px;">+${{d.points}} pts</td>
          <td class="num" style="font-weight:700; color:var(--color-primary-2);">${{d.share}}%</td>
          <td>
            <div style="width:100%; height:6px; background:var(--color-neutral-2); border-radius:var(--radius-1); max-width:80px; overflow:hidden;">
              <div style="width:${{d.share}}%; height:100%; background:var(--color-primary-1); border-radius:var(--radius-1);"></div>
            </div>
          </td>
        </tr>
      `).join('');

      // Channel performance rows
      let channelRows = channels.map(c => `
        <tr>
          <td>
            <strong style="color:var(--color-primary-2);">${{c.channel}}</strong>
            <div style="font-size:11px; color:var(--text-dim);">${{c.format}}</div>
          </td>
          <td class="num" style="font-weight:700; color:var(--color-primary-1);">${{c.reach.toLocaleString()}}</td>
          <td class="num">${{c.vtr || 'N/A'}}</td>
          <td class="num" style="font-weight:600;">${{c.ctr}}</td>
          <td class="num" style="font-weight:700; color:var(--color-primary-2);">${{c.mqls}}</td>
          <td class="num"><span class="badge badge-neutral num">€${{c.cpl}}</span></td>
          <td style="font-size:11.5px; color:var(--text-dim); max-width:200px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${{c.topCopy}}</td>
        </tr>
      `).join('');

      return `
        <!-- QUESTION HEADER (GTM TOWER STYLE) -->
        <div style="margin-bottom:var(--space-6);">
          <div style="display:flex; align-items:center; gap:8px; margin-bottom:4px;">
            <span class="badge badge-primary">Stage 2 of 8</span>
            <span class="badge badge-danger">Marketing Performance Diagnostic</span>
            <span class="badge badge-success">ONE Week MOD Campaign</span>
          </div>
          <h2 style="font-size:24px; font-weight:800; color:var(--color-primary-2); letter-spacing:-0.03em; margin:0 0 6px;">
            Why is ${{selectedM.name}} outperforming other European Frontlines in ONE Week MOD Lead Conversion?
          </h2>
          <p style="font-size:13px; color:var(--text-dim); margin:0; max-width:980px; line-height:1.5;">
            ${{selectedM.name}} campaign index <strong>118 vs 100 target</strong>, with €${{Math.round((selectedM.mediaBudget || 120000)/1000)}}k media budget across ${{selectedM.baseUnits ? selectedM.baseUnits.toLocaleString() : '9,039'}} target residential assets. Driver contributions are multivariate-attributed from audience reach, emotional creative hook rates, landing page self-assessment completion, and field technician referrals. The screen ends in an actionable marketing intervention, not just a data finding.
          </p>
        </div>

        <!-- HERO NUMBER READOUT STRIP (GTM TOWER STYLE) -->
        <div class="glass-panel" style="padding:14px 20px; margin-bottom:var(--space-6); background:#ffffff; border-left:6px solid var(--color-primary-1); display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:18px;">
          <div style="display:flex; align-items:center; gap:16px;">
            <div>
              <div style="font-size:11.5px; font-weight:700; color:var(--text-dim); text-transform:uppercase; letter-spacing:0.04em;">Campaign Performance Index</div>
              <div style="display:flex; align-items:baseline; gap:8px;">
                <span style="font-size:46px; font-weight:900; color:var(--color-primary-1); letter-spacing:-0.04em; line-height:1;">118</span>
                <span style="font-size:12px; color:var(--color-success-primary); font-weight:700;">+18% vs European Target</span>
              </div>
            </div>
          </div>

          <div style="display:flex; align-items:center; gap:28px; flex-wrap:wrap;">
            <div>
              <div style="font-size:11px; color:var(--text-dim); font-weight:600;">Sales Quotes Generated</div>
              <div style="font-size:22px; font-weight:800; color:var(--color-primary-2);">45 <span style="font-size:11px; font-weight:400; color:var(--text-dim);">quotes</span></div>
              <div style="font-size:10.5px; color:var(--color-success-primary); font-weight:600;">Target: 32 (+40.6%)</div>
            </div>

            <div style="border-left:1px solid var(--color-neutral-2); padding-left:24px;">
              <div style="font-size:11px; color:var(--text-dim); font-weight:600;">MQL-to-Quote Conversion</div>
              <div style="font-size:22px; font-weight:800; color:var(--color-success-primary);">31.1%</div>
              <div style="font-size:10.5px; color:var(--text-dim);">+7.1 pt uplift vs baseline (24%)</div>
            </div>

            <div style="border-left:1px solid var(--color-neutral-2); padding-left:24px;">
              <div style="font-size:11px; color:var(--text-dim); font-weight:600;">Cost per Qualified Lead (CPL)</div>
              <div style="font-size:22px; font-weight:800; color:var(--color-primary-1);">€48</div>
              <div style="font-size:10.5px; color:var(--color-success-primary); font-weight:600;">Portfolio benchmark: €72 (-33%)</div>
            </div>

            <div style="border-left:1px solid var(--color-neutral-2); padding-left:24px;">
              <div style="font-size:11px; color:var(--text-dim); font-weight:600;">Aided Brand Recall Lift</div>
              <div style="font-size:22px; font-weight:800; color:var(--color-primary-2);">+18.4%</div>
              <div style="font-size:10.5px; color:var(--color-success-primary); font-weight:600;">YouTube VRC + Meta Reels</div>
            </div>
          </div>
        </div>

        <!-- MARKETING DRIVER DECOMPOSITION WATERFALL -->
        <div class="glass-panel" style="margin-bottom:var(--space-6);">
          <div class="panel-header">
            <div>
              <div class="panel-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                Decomposing the Marketing Conversion Delta (+22 pt Gap: Benchmark vs Lagging Frontlines)
              </div>
              <div class="panel-subtitle">Multivariate attribution isolating the 5 marketing growth levers in the ONE Week MOD European package</div>
            </div>
            <span class="badge badge-success">5 Verified Marketing Levers</span>
          </div>

          <table class="data-table" style="margin-bottom:var(--space-4);">
            <thead>
              <tr>
                <th>Marketing Driver Component</th>
                <th>Category</th>
                <th>Conversion Impact</th>
                <th>Share of Gap</th>
                <th>Attribution Weight</th>
              </tr>
            </thead>
            <tbody>
              ${{driverRows}}
            </tbody>
          </table>

          <div style="background:var(--color-primary-6); border:1px solid var(--color-primary-8); padding:14px 18px; border-radius:var(--radius-3);">
            <div style="display:flex; align-items:flex-start; gap:10px;">
              <div style="background:var(--color-primary-1); color:#fff; width:22px; height:22px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:11px; flex-shrink:0; margin-top:1px;">i</div>
              <div>
                <strong style="color:var(--color-primary-2); font-size:12.5px;">Diagnostic Root Cause Analysis</strong>
                <p style="font-size:12px; color:var(--text-high); line-height:1.5; margin:3px 0 0;">
                  The +22 pt conversion advantage is <strong>not caused by elevator machinery or generic brand spend</strong>. It is driven by <strong>breaking the customer disruption barrier</strong>: 69% of B2B property managers make emotionally-driven decisions and feared a 4–8 week shutdown. The combination of <em>Emotional Copy #1 ("Take the fast-track to a better day")</em>, <em>Account-Based Advertising (D&B ABA) targeting verified property managers</em>, and the <em>Interactive Online Need-Identifier</em> dismantled the fear of disruption and lifted conversion from 24% to 31.1%.
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- CHANNEL ATTRIBUTION & CREATIVE A/B TESTING -->
        <div style="display:grid; grid-template-columns: 1.25fr 1fr; gap:var(--space-6); margin-bottom:var(--space-6);">
          
          <!-- CHANNEL ATTRIBUTION TABLE -->
          <div class="glass-panel" style="margin-bottom:0;">
            <div class="panel-header">
              <div>
                <div class="panel-title">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
                  Cross-Channel Media Performance & CPL
                </div>
                <div class="panel-subtitle">Performance breakdown across Phase 1 awareness and Phase 2 retargeting channels</div>
              </div>
            </div>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Channel & Format</th>
                  <th>Reach</th>
                  <th>VTR</th>
                  <th>CTR</th>
                  <th>MQLs</th>
                  <th>CPL</th>
                  <th>Top Creative Asset</th>
                </tr>
              </thead>
              <tbody>
                ${{channelRows}}
              </tbody>
            </table>
          </div>

          <!-- CREATIVE A/B TESTING (EMOTIONAL VS RATIONAL) -->
          <div class="glass-panel" style="margin-bottom:0;">
            <div class="panel-header">
              <div>
                <div class="panel-title">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg>
                  Creative Angle A/B Testing (VML Insights)
                </div>
                <div class="panel-subtitle">Comparing Approach 1 (Emotional) vs Approach 2 (Rational)</div>
              </div>
              <span class="badge badge-primary">A/B Flight</span>
            </div>

            ${{creativeAngles.map(cr => `
              <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-left:4px solid ${{cr.id === 'CR-EMO-01' ? 'var(--color-primary-1)' : 'var(--color-success-primary)'}}; border-radius:var(--radius-3); padding:12px 14px; margin-bottom:10px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                  <strong style="font-size:12.5px; color:var(--color-primary-2);">${{cr.angle}}</strong>
                  <span class="badge badge-${{cr.id === 'CR-EMO-01' ? 'primary' : 'success'}}" style="font-size:10px;">CTR: ${{cr.ctr}}</span>
                </div>
                <div style="font-size:13px; font-weight:700; color:var(--color-primary-1); margin-bottom:4px;">"${{cr.headline}}"</div>
                <div style="font-size:11.5px; color:var(--text-dim); margin-bottom:6px; line-height:1.4;">${{cr.subtext}}</div>
                <div style="font-size:11px; color:var(--text-high); background:var(--color-primary-6); padding:6px 8px; border-radius:var(--radius-2); line-height:1.4;">
                  <strong>Audience Impact:</strong> ${{cr.vmlInsight}}
                </div>
              </div>
            `).join('')}}

            <div style="font-size:11px; color:var(--text-dim); line-height:1.4; margin-top:4px;">
              * <em>Strategic rule:</em> Use Emotional Copy on Meta Reels & YouTube Shorts for top-of-funnel reach; swap to Rational Copy on Landing Page for lead-gen conversion.
            </div>
          </div>
        </div>

        <!-- ACTIONS IN FLYWHEEL (GTM TOWER STYLE) -->
        <div style="display:flex; align-items:center; justify-content:space-between; background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:14px 20px; box-shadow:var(--shadow-5);">
          <div>
            <h4 style="font-size:13.5px; color:var(--color-primary-2); margin:0 0 2px; font-weight:700;">Prescriptive Campaign Interventions</h4>
            <p style="font-size:12px; color:var(--text-dim); margin:0;">
              Scale the winning ITIB emotional-to-rational creative mix across the €705k European budget or rank candidate frontlines in Stage 3.
            </p>
          </div>
          <div style="display:flex; align-items:center; gap:10px;">
            <button class="btn-outline" style="padding:8px 14px; font-size:12px;" onclick="goStage(4)">
              Simulate Budget Reallocation (Stage 4) →
            </button>
            <button class="btn-action" style="padding:8px 16px; font-size:12px;" onclick="goStage(3)">
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
        const isHero = p.market.includes('ITIB') || p.market === 'Iberia';
        const baseConf = Math.round(p.confidenceScore * 20);
        const effectiveConf = isHero ? getRecalibratedConfidence(88) : baseConf;
        const stance = isHero ? '<span class="badge badge-success">Accelerate Hero</span>' :
                       idx === 1 ? '<span class="badge badge-primary">Fast Follower</span>' :
                       idx === 2 ? '<span class="badge badge-warning">Adapt & Test</span>' :
                       '<span class="badge badge-neutral">Predictive Linkage</span>';

        return `
          <tr style="${{isHero ? 'background: rgba(20, 80, 245, 0.06); font-weight: 500;' : ''}}">
            <td><strong style="color:var(--color-primary-2);">#${{idx + 1}}</strong></td>
            <td>
              <strong style="color:var(--color-primary-2);">${{p.candidate || (p.market + ' ONE Week Modernization')}}</strong>
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
                  Simulate €8.4M allocation →
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
            <span class="badge badge-success">Active Hero Candidate: ITIB ONE-Week Modernization (MonoSpace LIS)</span>
          </div>

          <table class="data-table" style="margin-bottom:var(--space-8);">
            <thead>
              <tr>
                <th>Rank</th>
                <th>Candidate Playbook & Target</th>
                <th>EBITDA Potential</th>
                <th>Model Confidence</th>
                <th>Bayesian Drift</th>
                <th>Stance</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              ${{rows}}
            </tbody>
          </table>

          <div style="background:var(--color-primary-6); border:1px solid var(--color-primary-8); padding:16px; border-radius:var(--radius-3); display:flex; align-items:center; justify-content:space-between;">
            <div>
              <strong style="color:var(--color-primary-2); font-size:13.5px;">Candidate Selection Locked: ITIB One-Week Modernization (MonoSpace LIS)</strong>
              <p style="font-size:12px; color:var(--text-dim); margin:2px 0 0;">
                Highest strategic fit (86% weighted match), €6.1M pipeline potential, and highest organizational readiness across Spain & Italy.
              </p>
            </div>
            <button class="btn-action" onclick="goStage(4)">
              Proceed to Scenario Simulation →
            </button>
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
            <h3 style="font-size:17px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">ONE Week MOD Pilot Simulation & Capital Control</h3>
            <p style="font-size:12.5px; color:var(--text-dim); line-height:1.5; margin:0;">
              Evaluating capital allocation trade-offs across 38 qualified residential buildings in Madrid, Barcelona, and Milan with €120k media budget air cover. Testing installation team throughput, customer payback curves, and technician referral incentives.
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
                <span style="color:var(--color-primary-1); font-weight:700;">€8.4M (Recommended ONE Week MOD)</span>
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
              <p style="font-size:11.5px; color:var(--text-dim); line-height:1.4;">Pre-fund 8 dedicated installation crews across Madrid, Barcelona, and Milan.</p>
            </div>
            <div class="stat-card" style="border: 2px solid var(--color-primary-1); cursor:pointer;" onclick="applyDetent(8.4)">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <span class="badge badge-success">€8.4M Allocation</span>
                <span class="badge badge-primary">Recommended</span>
              </div>
              <h4 style="font-size:14px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Balanced ONE Week MOD + 24/7</h4>
              <p style="font-size:11.5px; color:var(--text-dim); line-height:1.4;">Optimal balance of technician referral bonus (€150), standardized EcoDisc package inventory, and €120k media budget.</p>
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
      showToast(`Decision recorded: €${{state.simAlloc}}M committed to ONE Week MOD.`);
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
        const bShaft = b.shaft || (b.shaftType && b.shaftType.includes('Standard') ? 'Standard' : 'Narrow');
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
        const bFloors = b.floors || 6;
        const bShaft = b.shaftType || 'Standard (1.65m x 1.82m)';
        const bValue = b.estValue ?? b.orderValue ?? 24400;
        const bStatus = b.status || 'Active Pilot';
        const bLeaveBehind = b.technicianLeaveBehind || 'Delivered to HOA Board';

        return `
        <tr onclick="openBuildingModal('${{b.id}}')" style="cursor:pointer;">
          <td>
            <strong style="color:var(--color-primary-2);">${{bName}}</strong>
            <div style="font-size:11px; color:var(--text-dim);">${{bAddress}}</div>
          </td>
          <td>${{bCity}}</td>
          <td>
            <span class="badge badge-primary" style="font-size:10.5px;">MonoSpace LIS</span>
            <span style="font-size:11px; color:var(--text-dim);">${{bFloors}} fl</span>
          </td>
          <td><span class="badge badge-neutral">${{bShaft}}</span></td>
          <td><span class="badge badge-success" style="font-size:10.5px;">${{bLeaveBehind}}</span></td>
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
              ADS turns strategic decisions into maintenance routes. Technicians in Madrid, Barcelona, Milan, Seville, and Valencia receive pre-qualified shaft tasks directly in their field app with lobby leave-behind kits.
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
                Active 38-Building Cohort Dispatch (Spain & Italy Pilot)
              </div>
              <div class="panel-subtitle">Click any building to inspect shaft dimensions, verified age, and technician audit notes</div>
            </div>
            <div style="display:flex; gap:8px; align-items:center;">
              <input type="text" placeholder="Search building name or address..." value="${{state.cohortSearch || ''}}" oninput="onCohortSearch(this.value)" style="background:#ffffff; border:1px solid var(--color-neutral-2); padding:6px 12px; border-radius:var(--radius-3); color:var(--color-primary-2); font-size:12px; width:220px;">
              <select onchange="onCohortFilter('city', this.value)" style="background:#ffffff; border:1px solid var(--color-neutral-2); padding:6px 10px; border-radius:var(--radius-3); color:var(--color-primary-2); font-size:12px;">
                <option value="all">All Cities</option>
                <option value="Madrid" ${{state.cohortCity === 'Madrid' ? 'selected' : ''}}>Madrid</option>
                <option value="Barcelona" ${{state.cohortCity === 'Barcelona' ? 'selected' : ''}}>Barcelona</option>
                <option value="Milan" ${{state.cohortCity === 'Milan' ? 'selected' : ''}}>Milan</option>
                <option value="Valencia" ${{state.cohortCity === 'Valencia' ? 'selected' : ''}}>Valencia</option>
                <option value="Seville" ${{state.cohortCity === 'Seville' ? 'selected' : ''}}>Seville</option>
              </select>
              <select onchange="onCohortFilter('shaft', this.value)" style="background:#ffffff; border:1px solid var(--color-neutral-2); padding:6px 10px; border-radius:var(--radius-3); color:var(--color-primary-2); font-size:12px;">
                <option value="all">All Shaft Types</option>
                <option value="Standard" ${{state.cohortShaft === 'Standard' ? 'selected' : ''}}>Standard</option>
                <option value="Narrow" ${{state.cohortShaft === 'Narrow' ? 'selected' : ''}}>Narrow</option>
              </select>
            </div>
          </div>

          <table class="data-table">
            <thead>
              <tr>
                <th>Building</th>
                <th>City</th>
                <th>Model & Floors</th>
                <th>Shaft Dimensions</th>
                <th>Leave-Behind Card</th>
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
              Showing top ${{Math.min(10, filteredCohort.length)}} of ${{filteredCohort.length}} cohort buildings in Spain & Italy.
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
          desc: "The pioneering machine-room-less (MRL) breakthrough delivering up to 74% energy savings and whisper-quiet ride comfort.",
          img: KONE_IMAGES.ecodisc,
          badge: "Up to 74% Energy Savings"
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
                The 5 Codified ONE Week MOD Playbook Elements
              </div>
              <div class="panel-subtitle">Packaged operational components ready for cross-market replication</div>
            </div>
            <span class="badge badge-success">Playbook: ONE Week MOD (MonoSpace LIS)</span>
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
                Next European Frontline Replication Candidates
              </div>
              <div class="panel-subtitle">Sized from the European Campaign Package across 20,061 addressable elevator assets</div>
            </div>
          </div>

          <table class="data-table">
            <thead>
              <tr>
                <th>Frontline Market</th>
                <th>Suitability Score</th>
                <th>Addressable Units</th>
                <th>Media Budget</th>
                <th>Capability Match</th>
                <th>Est. Pipeline</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong style="color:var(--color-primary-2);">ITIB (Italy & Iberia)</strong></td>
                <td><span class="badge badge-success num">92% Match</span></td>
                <td class="num">9,039 units</td>
                <td class="num">€120k</td>
                <td>4 of 5 In Place</td>
                <td class="num" style="color:var(--color-primary-1); font-weight:700;">+€6.1M</td>
                <td><span class="badge badge-primary">Active in Stage 5</span></td>
              </tr>
              <tr>
                <td><strong style="color:var(--color-primary-2);">GIN (Great Britain & Ireland)</strong></td>
                <td><span class="badge badge-primary num">88% Match</span></td>
                <td class="num">4,804 units</td>
                <td class="num">€135k</td>
                <td>4 of 5 In Place (Need tech tools)</td>
                <td class="num" style="color:var(--color-primary-1); font-weight:700;">+€5.8M</td>
                <td>
                  <button class="btn-action" style="padding:4px 10px; font-size:11px;" onclick="replicateToMarket('GIN (Great Britain & Ireland)', 'ONE Week MOD')">
                    Replicate to GIN →
                  </button>
                </td>
              </tr>
              <tr>
                <td><strong style="color:var(--color-primary-2);">FBL (France, Belgium, Lux)</strong></td>
                <td><span class="badge badge-primary num">82% Match</span></td>
                <td class="num">2,070 units</td>
                <td class="num">€125k</td>
                <td>3 of 5 In Place (Energy subsidy audit)</td>
                <td class="num" style="color:var(--color-primary-1); font-weight:700;">+€4.2M</td>
                <td>
                  <button class="btn-outline" style="padding:4px 8px; font-size:11px;" onclick="replicateToMarket('FBL (France, Belgium, Lux)', 'ONE Week MOD')">
                    Replicate
                  </button>
                </td>
              </tr>
              <tr>
                <td><strong style="color:var(--color-primary-2);">NORD (Nordics)</strong></td>
                <td><span class="badge badge-neutral num">76% Match</span></td>
                <td class="num">938 units</td>
                <td class="num">€110k</td>
                <td>3 of 5 In Place (24/7 telemetry)</td>
                <td class="num" style="color:var(--color-primary-1); font-weight:700;">+€2.1M</td>
                <td>
                  <button class="btn-outline" style="padding:4px 8px; font-size:11px;" onclick="replicateToMarket('NORD (Nordics)', 'ONE Week MOD')">
                    Replicate
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      `;
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
                Day-90 Realized Outcomes (Spain & Italy Pilot Cohort)
              </div>
              <div class="panel-subtitle">Reviewing real field data vs baseline expectations · 1 February 2027</div>
            </div>
            <span class="badge badge-success">Pilot Complete · 38 Buildings</span>
          </div>

          <div class="grid-4" style="margin-bottom:var(--space-8);">
            <div class="stat-card">
              <span class="stat-label">Quotes Delivered</span>
              <div class="stat-val" style="color:var(--color-primary-2);">${{d90.quotes}} Quotes</div>
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
              <div class="stat-delta positive">${{d90.daysSavedPerLift}}d faster (100% &le;7d SLA)</div>
            </div>
          </div>

          <div class="grid-4" style="margin-bottom:var(--space-8);">
            <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px; box-shadow:var(--shadow-5);">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-size:12px; text-transform:uppercase; color:var(--color-primary-1); font-weight:700;">EcoDisc Energy Savings</span>
                <span class="badge badge-success num">Verified</span>
              </div>
              <div style="font-size:22px; font-weight:800; color:var(--color-primary-2); margin-bottom:4px;">
                ${{d90.energySavingsPct || 74}}% <span style="font-size:13px; color:var(--text-dim); font-weight:400;">Power Reduction</span>
              </div>
              <p style="font-size:12px; color:var(--text-dim); line-height:1.45; margin:0;">
                KONE EcoDisc gearless hoisting achieved 74% energy drop across all 14 modernized buildings, beating conventional geared drives.
              </p>
            </div>

            <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px; box-shadow:var(--shadow-5);">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-size:12px; text-transform:uppercase; color:var(--color-primary-1); font-weight:700;">24/7 Predictive Care</span>
                <span class="badge badge-success num">80% Proactive</span>
              </div>
              <div style="font-size:22px; font-weight:800; color:var(--color-primary-2); margin-bottom:4px;">
                ${{d90.predictiveDetectionPct || 80}}% <span style="font-size:13px; color:var(--text-dim); font-weight:400;">Issues Solved</span>
              </div>
              <p style="font-size:12px; color:var(--text-dim); line-height:1.45; margin:0;">
                80% of leveling and vibration anomalies detected and fixed before resident disruption occurred.
              </p>
            </div>

            <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px; box-shadow:var(--shadow-5);">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-size:12px; text-transform:uppercase; color:var(--color-primary-1); font-weight:700;">HOA & Owner CSAT</span>
                <span class="badge badge-success num">Target Beaten</span>
              </div>
              <div style="font-size:22px; font-weight:800; color:var(--color-primary-2); margin-bottom:4px;">
                ${{d90.csatActual || 72}}% <span style="font-size:13px; color:var(--text-dim); font-weight:400;">(vs 49% Base)</span>
              </div>
              <p style="font-size:12px; color:var(--text-dim); line-height:1.45; margin:0;">
                Customer satisfaction surged from 49% baseline to 72%, surpassing the 70% DEA charter objective.
              </p>
            </div>

            <div style="background:#ffffff; border:1px solid var(--color-neutral-2); border-radius:var(--radius-3); padding:16px; box-shadow:var(--shadow-5);">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-size:12px; text-transform:uppercase; color:var(--color-primary-1); font-weight:700;">Technician Velocity</span>
                <span class="badge badge-success num">124% Target</span>
              </div>
              <div style="font-size:22px; font-weight:800; color:var(--color-primary-2); margin-bottom:4px;">
                ${{d90.referralsAchieved}} <span style="font-size:13px; color:var(--text-dim); font-weight:400;">/ ${{d90.referralsTarget}} Referrals</span>
              </div>
              <p style="font-size:12px; color:var(--text-dim); line-height:1.45; margin:0;">
                Maintenance technicians logged 112 qualified leads and placed lobby cards with zero added agency media cost.
              </p>
            </div>
          </div>

          <div class="panel-header">
            <div class="panel-title" style="font-size:13px;">Mid-Flight Adjustments & Dynamic Tuning</div>
          </div>

          <div class="grid-3" style="margin-bottom:0;">
            <div class="stat-card">
              <h4 style="font-size:13.5px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Increase to €200/Lead</h4>
              <p style="font-size:11.5px; color:var(--text-dim); line-height:1.4; margin-bottom:8px;">Technician incentive yielded 112 leads. Further increase expected to accelerate Barcelona & Milan conversion.</p>
              <button class="btn-action" style="padding:4px 10px; font-size:11px;" onclick="applyMidflightPivot('incentive')">Apply adjustment</button>
            </div>
            <div class="stat-card">
              <h4 style="font-size:13.5px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Pre-Stock Madrid & Milan Depots</h4>
              <p style="font-size:11.5px; color:var(--text-dim); line-height:1.4; margin-bottom:8px;">Standardized MonoSpace LIS packs cut install to 6.4 days. Buffering inventory guarantees 5-day cycle.</p>
              <button class="btn-action" style="padding:4px 10px; font-size:11px;" onclick="applyMidflightPivot('depot')">Apply adjustment</button>
            </div>
            <div class="stat-card">
              <h4 style="font-size:13.5px; color:var(--color-primary-2); margin-bottom:4px; font-weight:700;">Deploy to GIN (UK&I) Brief</h4>
              <p style="font-size:11.5px; color:var(--text-dim); line-height:1.4; margin-bottom:8px;">Pass proven technician referral & 7-day install SLA directly into GIN's active Q2 campaign.</p>
              <button class="btn-action" style="padding:4px 10px; font-size:11px;" onclick="applyMidflightPivot('gin')">Apply adjustment</button>
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
              Every campaign outcome, field audit, and installation efficiency metric updates the Assisted Decisioning System. Future predictions become progressively more accurate across Europe.
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
                Because the ITIB pilot achieved <strong>€341,600</strong> in orders, <strong>6.4 days on site</strong>, and <strong>31.1%</strong> conversion, the system recalibrates the confidence prior for Stage 3 from <strong>0.62</strong> to <strong>0.84</strong>.
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
        q: 'Why is ITIB outperforming other European Frontlines in ONE Week MOD conversion?',
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
      const bFloors = b.floors || 6;
      const bLifts = b.elevatorCount ?? b.quotedUnits ?? 1;
      const bShaft = b.shaftType || 'Standard (1.65m x 1.82m)';
      const bValue = b.estValue ?? b.orderValue ?? 24400;
      const bStatus = b.status || 'Active Pilot';
      const bNotes = b.notes || 'Standard shaft dimensions verified. Guide rails aligned within 0.8mm tolerance. EcoDisc modernization package fits with zero structural alterations.';
      const bTelemetry = `Vibration: ${{b.vibrationMmS || 1.4}} mm/s · Cycles: ${{b.doorCyclesPerMonth ? b.doorCyclesPerMonth.toLocaleString() : '18,000'}}/mo · Score: ${{b.telemetryScore || 82}}/100`;
      const bLeaveBehind = b.technicianLeaveBehind || 'Delivered to HOA Board';

      document.getElementById('bldModalName').textContent = `${{bName}} (${{bCity}})`;
      document.getElementById('bldModalContent').innerHTML = `
        <div style="position:relative; height:120px; border-radius:var(--radius-3); overflow:hidden; margin-bottom:14px; background:url('${{KONE_IMAGES.kunshan}}') center/cover no-repeat;">
          <div style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(0,6,31,0.2) 0%, rgba(0,6,31,0.7) 100%); display:flex; align-items:flex-end; padding:12px 16px;">
            <span class="badge" style="background:#ffffff; color:var(--color-primary-1); font-weight:700;">KONE MonoSpace LIS Modernization Profile</span>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:10px; margin-bottom:16px;">
          <div class="stat-card">
            <span class="stat-label">Address</span>
            <div style="font-size:12.5px; color:var(--color-primary-2); font-weight:600;">${{bAddress}}</div>
            <div style="font-size:11px; color:var(--text-dim);">${{bCity}}, Spain / Italy</div>
          </div>
          <div class="stat-card">
            <span class="stat-label">Equipment & Height</span>
            <div style="font-size:12.5px; color:var(--color-primary-2); font-weight:600;">MonoSpace LIS</div>
            <div style="font-size:11px; color:var(--text-dim);">${{bFloors}} Floors (${{bAge}} Yrs Old)</div>
          </div>
          <div class="stat-card">
            <span class="stat-label">Shaft & EcoDisc</span>
            <div style="font-size:12.5px; color:var(--color-primary-2); font-weight:600;">${{bShaft.split(' ')[0]}} Shaft</div>
            <div style="font-size:11px; color:var(--color-success-primary); font-weight:600;">74% Energy Savings</div>
          </div>
          <div class="stat-card">
            <span class="stat-label">Quote Value & SLA</span>
            <div style="font-size:15px; color:var(--color-success-primary); font-weight:700;">€${{bValue.toLocaleString()}}</div>
            <div style="font-size:11px; color:var(--color-primary-1); font-weight:600;">&le;7d Installation SLA</div>
          </div>
        </div>
        <div style="background:var(--color-primary-6); border:1px solid var(--color-primary-8); padding:14px; border-radius:var(--radius-3); margin-bottom:14px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
            <div style="font-size:11px; text-transform:uppercase; color:var(--color-primary-1); font-weight:700;">Technician Shaft Audit Notes</div>
            <span class="badge badge-success" style="font-size:10.5px;">Card: ${{bLeaveBehind}}</span>
          </div>
          <p style="font-size:12.5px; color:var(--color-primary-2); line-height:1.5; margin:0 0 8px 0;">${{bNotes}}</p>
          <div style="font-size:11px; color:var(--color-accent-2); font-weight:600;">📡 ${{bTelemetry}} · KONE 24/7 Connected Services Active</div>
        </div>
        <div style="display:flex; justify-content:flex-end; gap:8px;">
          <button class="btn-outline" onclick="closeBuildingModal()">Close</button>
          <button class="btn-action" onclick="closeBuildingModal(); showToast('Building ${{b.id}} prioritized in 1-week installation schedule.');">
            Fast-Track 1-Week Installation Schedule
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
