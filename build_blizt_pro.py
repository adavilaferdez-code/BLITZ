import json
import os

data_path = r'C:/Users/Adfgd/Desktop/MIPAGINAWEB/blizt_data.json'
with open(data_path, encoding='utf-8') as f:
    clients_data = json.load(f)

json_payload = json.dumps(clients_data, ensure_ascii=False, separators=(',', ':'))

html_template = r"""<!DOCTYPE html>
<html lang="es">
<head>
    <script>
        // CACHE-BUSTER & AUTO-PURGE FOR MOBILE PHONES & IPADS
        (function() {
            var CURRENT_BUILD = "2026.10.03.v2";
            var lastBuild = localStorage.getItem("__BLIZT_BUILD_VER__");
            
            // Unregister legacy Service Workers that block updates
            if ('serviceWorker' in navigator) {
                navigator.serviceWorker.getRegistrations().then(function(regs) {
                    for (var i = 0; i < regs.length; i++) {
                        regs[i].update();
                    }
                }).catch(function(){});
            }

            // Clear legacy cache storages
            if ('caches' in window && lastBuild !== CURRENT_BUILD) {
                caches.keys().then(function(names) {
                    for (var i = 0; i < names.length; i++) {
                        caches.delete(names[i]);
                    }
                }).catch(function(){});
                localStorage.setItem("__BLIZT_BUILD_VER__", CURRENT_BUILD);
            }
        })();
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="theme-color" content="#090b10">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <link rel="manifest" href="manifest.json">
    <link rel="apple-touch-icon" href="logo_antonio.png">
    <title>BLIZT Pro - Preventa, Cajas & Cartera de Clientes</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <script src="xlsx.full.min.js"></script>
    <script>
        if (typeof XLSX === 'undefined') {
            document.write('<script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"><\\/script>');
        }
    </script>
    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        :root {
            --bg-body: #090b10;
            --bg-surface: #0f131d;
            --bg-card: #141926;
            --bg-card-hover: #1c2236;
            --bg-elevated: #1a2238;
            --border: rgba(255, 255, 255, 0.08);
            --border-subtle: rgba(255, 255, 255, 0.04);
            --border-focus: #0284c7;
            --primary: #0284c7;
            --primary-glow: rgba(2, 132, 199, 0.35);
            --accent-cyan: #38bdf8;
            --accent-green: #10b981;
            --accent-green-bg: rgba(16, 185, 129, 0.12);
            --accent-gold: #f59e0b;
            --accent-gold-bg: rgba(245, 158, 11, 0.12);
            --accent-silver: #94a3b8;
            --accent-silver-bg: rgba(148, 163, 184, 0.12);
            --accent-bronze: #d97706;
            --accent-bronze-bg: rgba(217, 119, 6, 0.12);
            --accent-red: #ef4444;
            --accent-red-bg: rgba(239, 68, 68, 0.14);
            --accent-pink: #f43f5e;
            --text-main: #f8fafc;
            --text-muted: #8e9bb0;
            --text-dim: #64748b;
            --radius-sm: 8px;
            --radius-md: 12px;
            --radius-lg: 18px;
            --radius-pill: 9999px;
            --font-main: 'Outfit', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --shadow-card: 0 4px 20px rgba(0,0,0,0.25);
            --shadow-elevated: 0 10px 30px rgba(0,0,0,0.4);
        }

        html, body {
            height: 100%;
            background-color: var(--bg-body);
            color: var(--text-main);
            font-family: var(--font-main);
            -webkit-tap-highlight-color: transparent;
            overscroll-behavior: none;
            line-height: 1.4;
        }

        .app-bg {
            position: fixed;
            inset: 0;
            z-index: -1;
            background: 
                radial-gradient(circle at 15% 10%, rgba(2, 132, 199, 0.1) 0%, transparent 45%),
                radial-gradient(circle at 85% 90%, rgba(16, 185, 129, 0.06) 0%, transparent 50%);
            pointer-events: none;
        }

        #storageWarningBanner {
            display: none;
            background: linear-gradient(135deg, #b91c1c, #991b1b);
            color: #fff;
            padding: 12px 18px;
            font-size: 0.82rem;
            font-weight: 800;
            line-height: 1.4;
            border-bottom: 2px solid #ef4444;
            position: sticky;
            top: 0;
            z-index: 9999;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }

        .app-shell {
            max-width: 1050px;
            margin: 0 auto;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            padding-bottom: 90px;
        }

        /* TOP APP HEADER */
        .app-header {
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(9, 11, 16, 0.92);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border-bottom: 1px solid var(--border);
            padding: 12px 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
        }
        .header-left {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .btn-nav-back {
            background: rgba(255,255,255,0.06);
            border: 1px solid var(--border);
            color: var(--text-main);
            width: 38px;
            height: 38px;
            border-radius: var(--radius-md);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.1rem;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.2s;
        }
        .btn-nav-back:hover { background: rgba(255,255,255,0.12); }
        
        .brand-title-box {
            display: flex;
            flex-direction: column;
        }
        .brand-title-row {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .brand-title {
            font-size: 1.22rem;
            font-weight: 900;
            letter-spacing: 0.5px;
            color: #ffffff;
        }
        .brand-badge {
            background: linear-gradient(135deg, #0284c7, #2563eb);
            color: #ffffff;
            font-size: 0.62rem;
            font-weight: 800;
            padding: 3px 7px;
            border-radius: var(--radius-sm);
            letter-spacing: 1px;
            text-transform: uppercase;
        }
        .brand-subtitle {
            font-size: 0.72rem;
            color: var(--text-muted);
            font-weight: 600;
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .hdr-icon-btn {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border);
            color: var(--text-main);
            height: 38px;
            padding: 0 12px;
            border-radius: var(--radius-md);
            font-size: 0.78rem;
            font-weight: 700;
            font-family: var(--font-main);
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
        }
        .hdr-icon-btn:hover {
            background: rgba(255, 255, 255, 0.12);
            border-color: rgba(255, 255, 255, 0.2);
            transform: translateY(-1px);
        }
        .hdr-icon-btn.sync-btn {
            background: linear-gradient(135deg, rgba(2, 132, 199, 0.25), rgba(14, 165, 233, 0.3));
            border-color: rgba(56, 189, 248, 0.5);
            color: #38bdf8;
            box-shadow: 0 0 10px rgba(56, 189, 248, 0.15);
        }
        .hdr-icon-btn.sync-btn:hover {
            background: linear-gradient(135deg, rgba(2, 132, 199, 0.4), rgba(14, 165, 233, 0.5));
            border-color: #38bdf8;
            color: #ffffff;
            box-shadow: 0 0 14px rgba(56, 189, 248, 0.3);
        }
        .hdr-icon-btn.excel-btn {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(5, 150, 105, 0.25));
            border-color: rgba(16, 185, 129, 0.4);
            color: #34d399;
        }
        .hdr-icon-btn.excel-btn:hover {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.35), rgba(5, 150, 105, 0.4));
            border-color: #10b981;
            color: #fff;
        }

        /* KPI METRICS BAR (6 CHIPS SCROLLER) */
        .kpi-scroller {
            padding: 10px 16px 6px;
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 8px;
        }
        @media (max-width: 850px) {
            .kpi-scroller {
                display: flex;
                overflow-x: auto;
                padding-bottom: 10px;
                scrollbar-width: none;
            }
            .kpi-scroller::-webkit-scrollbar { display: none; }
            .kpi-chip {
                flex: 0 0 auto;
                min-width: 130px;
            }
        }
        .kpi-chip {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 8px 12px;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
            position: relative;
            overflow: hidden;
        }
        .kpi-chip::before {
            content: '';
            position: absolute;
            top: 0; left: 0; bottom: 0;
            width: 3px;
        }
        .kpi-chip.k-all::before { background: #3b82f6; }
        .kpi-chip.k-risk::before { background: #ef4444; }
        .kpi-chip.k-growth::before { background: #10b981; }
        .kpi-chip.k-cajas::before { background: #38bdf8; }
        .kpi-chip.k-rutero::before { background: #c084fc; }
        .kpi-chip.k-mail::before { background: #a855f7; }

        .kpi-chip:hover {
            background: var(--bg-card);
            border-color: rgba(255, 255, 255, 0.2);
            transform: translateY(-1px);
        }
        .kpi-chip-info {
            display: flex;
            flex-direction: column;
        }
        .kpi-chip-title {
            font-size: 0.65rem;
            font-weight: 700;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .kpi-chip-value {
            font-size: 1.15rem;
            font-weight: 900;
            color: #ffffff;
            line-height: 1.1;
        }
        .kpi-chip-icon {
            font-size: 1.2rem;
            opacity: 0.8;
        }

        /* SEARCH BAR & FILTER PILLS */
        .search-section {
            padding: 6px 14px 4px;
            position: relative;
            z-index: 10;
            background: transparent;
        }
        .search-bar-wrap {
            position: relative;
            display: flex;
            align-items: center;
        }
        .search-icon-svg {
            position: absolute;
            left: 14px;
            color: var(--text-dim);
            font-size: 1rem;
            pointer-events: none;
        }
        .search-input {
            width: 100%;
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-pill);
            padding: 11px 40px 11px 42px;
            color: #ffffff;
            font-size: 0.92rem;
            font-family: var(--font-main);
            font-weight: 500;
            outline: none;
            transition: all 0.25s;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.3);
        }
        .search-input:focus {
            border-color: var(--border-focus);
            background: var(--bg-card);
            box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.25);
        }
        .search-input::placeholder {
            color: var(--text-dim);
            font-size: 0.86rem;
        }
        .search-clear-btn {
            position: absolute;
            right: 12px;
            background: rgba(255,255,255,0.1);
            border: none;
            color: var(--text-muted);
            width: 24px;
            height: 24px;
            border-radius: 50%;
            display: none;
            align-items: center;
            justify-content: center;
            font-size: 0.75rem;
            cursor: pointer;
        }
        .search-clear-btn:hover { background: rgba(255,255,255,0.2); color: #fff; }

        .filter-scroller {
            display: flex;
            gap: 5px;
            overflow-x: auto;
            padding: 8px 0 6px;
            scrollbar-width: none;
            -webkit-overflow-scrolling: touch;
        }
        .filter-scroller::-webkit-scrollbar { display: none; }
        .filter-pill {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            color: var(--text-muted);
            padding: 5px 9px;
            border-radius: 8px;
            font-size: 0.74rem;
            font-weight: 800;
            font-family: var(--font-main);
            white-space: nowrap;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            flex-shrink: 0;
            height: 30px;
        }
        .filter-pill:hover {
            background: rgba(255, 255, 255, 0.1);
            color: #ffffff;
            border-color: rgba(255, 255, 255, 0.2);
        }
        .filter-pill.active {
            background: var(--primary);
            border-color: var(--primary);
            color: #ffffff;
            box-shadow: 0 2px 10px rgba(2, 132, 199, 0.4);
        }
        .filter-pill.pill-red.active {
            background: #ef4444;
            border-color: #ef4444;
            color: #ffffff;
            box-shadow: 0 2px 10px rgba(239, 68, 68, 0.4);
        }
        .filter-pill.pill-emerald.active {
            background: #10b981;
            border-color: #10b981;
            color: #000000;
            box-shadow: 0 2px 10px rgba(16, 185, 129, 0.4);
        }
        .filter-pill.pill-amber.active {
            background: #f59e0b;
            border-color: #f59e0b;
            color: #000000;
            box-shadow: 0 2px 10px rgba(245, 158, 11, 0.4);
        }
        .filter-pill.pill-pink.active {
            background: #f43f5e;
            border-color: #f43f5e;
            color: #ffffff;
        }
        .filter-pill.pill-cyan.active {
            background: #0284c7;
            border-color: #0284c7;
            color: #ffffff;
        }
        .filter-pill.pill-gold.active {
            background: var(--accent-gold);
            border-color: var(--accent-gold);
            color: #000;
        }

        /* HEALTH TRAFFIC LIGHT BADGES */
        .badge-health-risk {
            background: rgba(239, 68, 68, 0.15);
            border: 1px solid rgba(239, 68, 68, 0.45);
            color: #f87171;
            font-weight: 800;
        }
        .badge-health-growth {
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.45);
            color: #34d399;
            font-weight: 800;
        }
        .badge-health-stable {
            background: rgba(245, 158, 11, 0.15);
            border: 1px solid rgba(245, 158, 11, 0.35);
            color: #fbbf24;
            font-weight: 800;
        }
        .badge-health-nuevo {
            background: linear-gradient(135deg, #ec4899, #f43f5e);
            color: #ffffff;
            font-weight: 900;
            box-shadow: 0 2px 8px rgba(244, 63, 94, 0.4);
            border: 1px solid rgba(255,255,255,0.3);
        }

        /* CLIENT CARDS */
        .client-stream {
            padding: 8px 16px 30px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .client-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 14px 16px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            cursor: pointer;
            transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
            box-shadow: var(--shadow-card);
        }
        .client-card:hover {
            background: var(--bg-card-hover);
            border-color: rgba(255, 255, 255, 0.18);
            transform: translateY(-2px);
            box-shadow: var(--shadow-elevated);
        }
        .client-card::before {
            content: '';
            position: absolute;
            left: 0; top: 0; bottom: 0;
            width: 4px;
            background: transparent;
        }
        .client-card.is-risk::before { background: #ef4444; }
        .client-card.is-growth::before { background: #10b981; }
        .client-card.is-stable::before { background: #f59e0b; }
        .client-card.is-oro::before { background: #f59e0b; }
        .client-card.is-plata::before { background: #94a3b8; }
        .client-card.is-bronce::before { background: #d97706; }
        .client-card.is-rutero-card::before { background: #10b981; }
        .client-card.is-nuevo-card::before { background: #f43f5e; }

        .card-top-row {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 10px;
        }
        .card-name-group {
            display: flex;
            align-items: center;
            gap: 10px;
            min-width: 0;
        }
        .card-avatar {
            width: 38px;
            height: 38px;
            border-radius: var(--radius-md);
            background: linear-gradient(135deg, rgba(2, 132, 199, 0.2), rgba(37, 99, 235, 0.25));
            color: #38bdf8;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;
            font-weight: 800;
            flex-shrink: 0;
            border: 1px solid rgba(56, 189, 248, 0.3);
        }
        .card-title-box {
            min-width: 0;
        }
        .card-title {
            font-size: 1.02rem;
            font-weight: 800;
            color: #ffffff;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            line-height: 1.25;
        }
        .card-code-sub {
            font-size: 0.74rem;
            color: var(--text-muted);
            font-family: monospace;
            display: flex;
            align-items: center;
            gap: 6px;
            margin-top: 2px;
        }
        .badge-cluster {
            display: flex;
            align-items: center;
            gap: 5px;
            flex-shrink: 0;
            flex-wrap: wrap;
            justify-content: flex-end;
        }
        .badge-chip {
            font-size: 0.65rem;
            font-weight: 800;
            padding: 2px 7px;
            border-radius: var(--radius-sm);
            letter-spacing: 0.3px;
            display: inline-flex;
            align-items: center;
            gap: 3px;
        }
        .badge-rutero {
            background: var(--accent-green-bg);
            color: #34d399;
            border: 1px solid rgba(16, 185, 129, 0.3);
        }
        .badge-oro {
            background: var(--accent-gold-bg);
            color: #fbbf24;
            border: 1px solid rgba(245, 158, 11, 0.3);
        }
        .badge-plata {
            background: var(--accent-silver-bg);
            color: #cbd5e1;
            border: 1px solid rgba(148, 163, 184, 0.3);
        }
        .badge-bronce {
            background: var(--accent-bronze-bg);
            color: #f97316;
            border: 1px solid rgba(217, 119, 6, 0.3);
        }
        .badge-cajas-top {
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid rgba(56, 189, 248, 0.35);
            color: #38bdf8;
            font-weight: 800;
        }

        .card-meta-row {
            font-size: 0.78rem;
            color: var(--text-muted);
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 6px 12px;
            padding-left: 48px;
        }
        .meta-item.loc {
            color: #cbd5e1;
            font-weight: 600;
        }

        /* BOXES / CONSUMPTION STRIP */
        .card-boxes-strip {
            margin-left: 48px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: var(--radius-md);
            padding: 8px 12px;
            display: grid;
            grid-template-columns: 1.3fr 1fr 1fr 1fr;
            gap: 8px;
            align-items: center;
        }
        @media (max-width: 500px) {
            .card-meta-row, .card-boxes-strip, .card-actions-bar {
                padding-left: 0;
                margin-left: 0;
            }
            .card-boxes-strip {
                grid-template-columns: 1.2fr 1fr 1fr 1fr;
                padding: 6px 8px;
                gap: 4px;
            }
        }
        .box-col {
            display: flex;
            flex-direction: column;
        }
        .box-lbl {
            font-size: 0.62rem;
            font-weight: 800;
            color: var(--text-dim);
            text-transform: uppercase;
            letter-spacing: 0.3px;
        }
        .box-num {
            font-size: 0.88rem;
            font-weight: 900;
            color: #cbd5e1;
            font-family: monospace;
            white-space: nowrap;
        }
        .box-col.highlight .box-lbl { color: #38bdf8; }
        .box-col.highlight .box-num { color: #38bdf8; font-size: 0.95rem; }

        .card-actions-bar {
            padding-left: 48px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .btn-action-email {
            flex: 1;
            background: linear-gradient(135deg, #0284c7, #2563eb);
            color: #ffffff;
            font-size: 0.82rem;
            font-weight: 800;
            padding: 9px 14px;
            border-radius: var(--radius-md);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            border: none;
            cursor: pointer;
            box-shadow: 0 3px 12px rgba(2, 132, 199, 0.3);
            transition: all 0.2s;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .btn-action-email:hover { filter: brightness(1.15); transform: translateY(-1px); }

        .btn-action-addemail {
            width: 100%;
            background: rgba(2, 132, 199, 0.08);
            border: 1.5px dashed rgba(56, 189, 248, 0.45);
            color: #38bdf8;
            font-size: 0.8rem;
            font-weight: 800;
            padding: 9px 12px;
            border-radius: var(--radius-md);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .btn-action-addemail:hover {
            background: rgba(2, 132, 199, 0.22);
            border-color: #38bdf8;
            color: #ffffff;
        }

        .mini-btn {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border);
            color: var(--text-muted);
            width: 36px;
            height: 36px;
            border-radius: var(--radius-md);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 0.95rem;
            cursor: pointer;
            transition: all 0.2s;
            text-decoration: none;
            flex-shrink: 0;
        }
        .mini-btn:hover {
            background: rgba(255, 255, 255, 0.14);
            color: #ffffff;
        }
        .mini-btn.del:hover {
            background: rgba(239, 68, 68, 0.2);
            border-color: #ef4444;
            color: #f87171;
        }

        /* MODAL DOSSIER */
        .modal-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.78);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            z-index: 999;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.25s ease;
        }
        .modal-overlay.open {
            opacity: 1;
            pointer-events: auto;
        }
        .modal-panel {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: 24px 24px 0 0;
            width: 100%;
            max-width: 720px;
            max-height: 90vh;
            display: flex;
            flex-direction: column;
            transform: translateY(100%);
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            overflow-y: auto;
            -webkit-overflow-scrolling: touch;
        }
        .modal-overlay.open .modal-panel {
            transform: translateY(0);
        }
        .modal-drag-handle {
            width: 40px;
            height: 4px;
            background: rgba(255,255,255,0.2);
            border-radius: 2px;
            margin: 10px auto 4px;
        }

        .dossier-top-bar {
            padding: 14px 20px;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 12px;
        }
        .dossier-top-left {
            display: flex;
            align-items: center;
            gap: 14px;
            min-width: 0;
        }
        .dossier-avatar-large {
            width: 48px;
            height: 48px;
            border-radius: var(--radius-md);
            background: linear-gradient(135deg, #0284c7, #2563eb);
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            font-weight: 900;
            flex-shrink: 0;
            box-shadow: 0 4px 15px rgba(2, 132, 199, 0.35);
        }
        .dossier-name {
            font-size: 1.25rem;
            font-weight: 900;
            color: #fff;
            line-height: 1.2;
        }
        .dossier-loc-sub {
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-top: 2px;
        }
        .btn-modal-close {
            background: rgba(255,255,255,0.08);
            border: 1px solid var(--border);
            color: #fff;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
        }

        /* HEALTH DIAGNOSTIC CARD INSIDE DOSSIER */
        .dossier-health-banner {
            margin: 12px 18px 4px;
            padding: 14px 16px;
            border-radius: var(--radius-md);
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .dossier-health-banner.is-risk {
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(185, 28, 28, 0.08));
            border-color: rgba(239, 68, 68, 0.4);
        }
        .dossier-health-banner.is-growth {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(5, 150, 105, 0.08));
            border-color: rgba(16, 185, 129, 0.4);
        }
        .dossier-health-banner.is-stable {
            background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(217, 119, 6, 0.06));
            border-color: rgba(245, 158, 11, 0.35);
        }
        .dossier-health-banner.is-nuevo {
            background: linear-gradient(135deg, rgba(244, 63, 94, 0.12), rgba(225, 29, 72, 0.08));
            border-color: rgba(244, 63, 94, 0.4);
        }
        .health-banner-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
        }
        .health-status-badge {
            font-size: 0.76rem;
            font-weight: 800;
            padding: 3px 9px;
            border-radius: var(--radius-sm);
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }
        .health-summary-text {
            font-size: 0.82rem;
            color: #cbd5e1;
            line-height: 1.35;
        }
        .health-action-box {
            background: rgba(0, 0, 0, 0.25);
            border-radius: var(--radius-sm);
            padding: 8px 10px;
            font-size: 0.78rem;
            line-height: 1.35;
            border-left: 3px solid #38bdf8;
        }

        .dossier-contact-hub {
            margin: 12px 18px 4px;
            background: rgba(2, 132, 199, 0.06);
            border: 1px solid rgba(56, 189, 248, 0.25);
            border-radius: var(--radius-md);
            padding: 14px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .hub-title-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .hub-title {
            font-size: 0.78rem;
            font-weight: 800;
            color: #38bdf8;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .hub-badge {
            font-size: 0.65rem;
            font-weight: 800;
            background: rgba(56, 189, 248, 0.15);
            color: #38bdf8;
            padding: 2px 7px;
            border-radius: var(--radius-pill);
        }
        .contact-active-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 10px 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
        }
        .contact-val-large {
            font-size: 1.05rem;
            font-weight: 800;
            color: #fff;
            word-break: break-all;
        }
        .contact-actions-cluster {
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .manual-input-box {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        .manual-input-label {
            font-size: 0.72rem;
            font-weight: 700;
            color: var(--text-muted);
        }
        .manual-input-bar {
            display: flex;
            gap: 6px;
        }
        .manual-input-bar input {
            flex: 1;
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 9px 12px;
            color: #fff;
            font-family: var(--font-main);
            font-size: 0.88rem;
            outline: none;
        }
        .manual-input-bar input:focus {
            border-color: var(--border-focus);
        }
        .manual-input-bar button {
            background: #0284c7;
            border: none;
            color: #fff;
            font-weight: 800;
            font-size: 0.8rem;
            padding: 0 14px;
            border-radius: var(--radius-md);
            cursor: pointer;
        }
        .btn-clipboard-big {
            width: 100%;
            background: linear-gradient(135deg, rgba(2, 132, 199, 0.2), rgba(37, 99, 235, 0.25));
            border: 1px solid rgba(56, 189, 248, 0.4);
            color: #38bdf8;
            font-size: 0.84rem;
            font-weight: 800;
            padding: 11px;
            border-radius: var(--radius-md);
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            transition: all 0.2s;
        }
        .btn-clipboard-big:hover {
            background: linear-gradient(135deg, #0284c7, #2563eb);
            color: #fff;
        }

        .web-links-grid {
            padding: 6px 18px;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 6px;
        }
        @media (max-width: 500px) {
            .web-links-grid { grid-template-columns: 1fr 1fr; }
        }
        .web-link-btn {
            background: rgba(255,255,255,0.04);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 8px 10px;
            color: var(--text-muted);
            font-size: 0.75rem;
            font-weight: 700;
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            transition: all 0.2s;
        }
        .web-link-btn:hover {
            background: rgba(255,255,255,0.1);
            color: #fff;
        }

        .dossier-section-title {
            padding: 14px 18px 4px;
            font-size: 0.72rem;
            font-weight: 800;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .dossier-grid {
            padding: 4px 18px 12px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }
        @media (max-width: 500px) {
            .dossier-grid { grid-template-columns: 1fr; }
        }
        .dossier-cell {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: var(--radius-md);
            padding: 8px 10px;
            display: flex;
            flex-direction: column;
        }
        .dossier-cell.full {
            grid-column: 1 / -1;
        }
        .cell-label {
            font-size: 0.62rem;
            font-weight: 800;
            color: var(--text-dim);
            text-transform: uppercase;
        }
        .cell-value {
            font-size: 0.88rem;
            font-weight: 700;
            color: #cbd5e1;
            margin-top: 2px;
        }
        .cell-value.highlight-blue { color: #38bdf8; font-weight: 800; }
        .cell-value.highlight-green { color: #34d399; font-weight: 800; }
        .cell-value.highlight-gold { color: #fbbf24; font-weight: 800; }
        .cell-value.highlight-red { color: #f87171; font-weight: 800; }

        .dossier-footer-bar {
            padding: 12px 18px 24px;
            display: flex;
            gap: 8px;
            border-top: 1px solid var(--border);
            margin-top: 10px;
        }
        .btn-full-edit {
            flex: 1;
            background: rgba(255,255,255,0.08);
            border: 1px solid var(--border);
            color: #fff;
            padding: 12px;
            border-radius: var(--radius-md);
            font-size: 0.85rem;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.2s;
        }
        .btn-full-edit:hover { background: rgba(255,255,255,0.15); }

        /* EDIT FORM MODAL */
        .form-layout {
            padding: 14px 18px 24px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .form-group {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
        .form-group label {
            font-size: 0.72rem;
            font-weight: 800;
            color: var(--text-muted);
            text-transform: uppercase;
        }
        .form-group input, .form-group select, .form-group textarea {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 10px 12px;
            color: #fff;
            font-family: var(--font-main);
            font-size: 0.88rem;
            outline: none;
        }
        .form-group input:focus, .form-group select:focus, .form-group textarea:focus {
            border-color: var(--border-focus);
        }
        .form-row-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }

        /* TOAST */
        .toast-msg {
            position: fixed;
            bottom: 24px;
            left: 50%;
            transform: translateX(-50%) translateY(100px);
            background: #1e293b;
            color: #fff;
            border: 1px solid rgba(255,255,255,0.15);
            padding: 10px 20px;
            border-radius: var(--radius-pill);
            font-size: 0.85rem;
            font-weight: 700;
            z-index: 10000;
            opacity: 0;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            pointer-events: none;
        }
        .toast-msg.show {
            transform: translateX(-50%) translateY(0);
            opacity: 1;
        }
        .toast-msg.success { background: #065f46; border-color: #10b981; }
        .toast-msg.error { background: #991b1b; border-color: #ef4444; }

        /* FAB ADD */
        .fab-add {
            position: fixed;
            bottom: 24px;
            right: 24px;
            width: 54px;
            height: 54px;
            border-radius: 50%;
            background: linear-gradient(135deg, #0284c7, #2563eb);
            color: #fff;
            border: none;
            box-shadow: 0 8px 24px rgba(2, 132, 199, 0.5);
            font-size: 1.6rem;
            font-weight: 900;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 80;
            transition: all 0.2s;
        }
        .fab-add:hover {
            transform: scale(1.08);
            box-shadow: 0 10px 30px rgba(2, 132, 199, 0.65);
        }

        .empty-box {
            text-align: center;
            padding: 60px 20px;
            color: var(--text-muted);
        }
        .empty-box .icon {
            font-size: 3rem;
            margin-bottom: 12px;
            opacity: 0.6;
        }
    
        /* =========================================================================
           VIEW SWITCHER & EXECUTIVE DASHBOARD CSS
           ========================================================================= */
        .view-switcher-bar {
            display: flex;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 4px;
            margin: 12px 16px 8px 16px;
            gap: 6px;
        }
        .nav-view-btn {
            flex: 1;
            padding: 10px 16px;
            border-radius: var(--radius-md);
            border: none;
            background: transparent;
            color: var(--text-muted);
            font-family: var(--font-main);
            font-size: 0.88rem;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.25s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        .nav-view-btn:hover {
            color: #ffffff;
            background: rgba(255, 255, 255, 0.05);
        }
        .nav-view-btn.active {
            background: linear-gradient(135deg, #0284c7, #0369a1);
            color: #ffffff;
            box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
        }

        .dashboard-container {
            padding: 10px 16px 60px 16px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .dash-section-title {
            font-size: 1.05rem;
            font-weight: 900;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 12px;
        }
        .dash-section-title span.badge {
            font-size: 0.72rem;
            padding: 2px 8px;
            border-radius: 6px;
            font-weight: 800;
            background: rgba(255,255,255,0.08);
            color: var(--text-muted);
        }

        /* Multi-Year Volume Card */
        .dash-multi-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 18px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        .year-bars-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 12px;
            margin-top: 14px;
        }
        .year-bar-item {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            padding: 12px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        .year-bar-item.y2026 {
            border-color: rgba(56, 189, 248, 0.4);
            background: linear-gradient(180deg, rgba(2,132,199,0.15), rgba(2,132,199,0.05));
        }
        .year-bar-label {
            font-size: 0.75rem;
            color: var(--text-muted);
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .year-bar-value {
            font-size: 1.25rem;
            font-weight: 900;
            color: #ffffff;
            margin: 6px 0;
            font-variant-numeric: tabular-nums;
        }
        .year-bar-item.y2026 .year-bar-value {
            color: #38bdf8;
        }
        .year-progress-track {
            height: 6px;
            background: rgba(255,255,255,0.08);
            border-radius: 3px;
            overflow: hidden;
            margin-top: 6px;
        }
        .year-progress-fill {
            height: 100%;
            border-radius: 3px;
            transition: width 0.8s ease;
        }

        /* Top Rankings Grid */
        .rankings-dual-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 20px;
        }
        .ranking-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 18px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        .rank-list {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .rank-item {
            display: flex;
            align-items: center;
            gap: 12px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            padding: 10px 14px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .rank-item:hover {
            background: rgba(255, 255, 255, 0.06);
            border-color: rgba(255, 255, 255, 0.15);
            transform: translateX(3px);
        }
        .rank-num-badge {
            width: 28px;
            height: 28px;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.06);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;
            font-weight: 900;
            color: var(--text-muted);
            flex-shrink: 0;
        }
        .rank-num-badge.gold { background: linear-gradient(135deg, #d97706, #f59e0b); color: #000; box-shadow: 0 0 10px rgba(245,158,11,0.4); }
        .rank-num-badge.silver { background: linear-gradient(135deg, #64748b, #94a3b8); color: #000; }
        .rank-num-badge.bronze { background: linear-gradient(135deg, #b45309, #d97706); color: #fff; }
        .rank-num-badge.rescue { background: linear-gradient(135deg, #dc2626, #ef4444); color: #fff; box-shadow: 0 0 10px rgba(239,68,68,0.4); }

        .rank-info {
            flex: 1;
            min-width: 0;
        }
        .rank-name {
            font-size: 0.9rem;
            font-weight: 800;
            color: #ffffff;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .rank-sub {
            font-size: 0.75rem;
            color: var(--text-muted);
            display: flex;
            gap: 6px;
            margin-top: 2px;
        }
        .rank-stat-box {
            text-align: right;
            flex-shrink: 0;
        }
        .rank-stat-main {
            font-size: 0.95rem;
            font-weight: 900;
            font-variant-numeric: tabular-nums;
        }
        .rank-stat-sub {
            font-size: 0.72rem;
            color: var(--text-muted);
        }

        /* Health Distribution strip */
        .health-dist-strip {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 10px;
        }
        .health-dist-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 12px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .health-dist-card:hover {
            transform: translateY(-2px);
            border-color: rgba(255,255,255,0.2);
        }
        .health-dist-title { font-size: 0.75rem; font-weight: 800; color: var(--text-muted); margin-bottom: 4px; }
        .health-dist-val { font-size: 1.35rem; font-weight: 900; }
        .health-dist-pct { font-size: 0.72rem; color: var(--text-muted); margin-top: 2px; }

    
        /* DANGER & RED INACTIVITY BADGES */
        .badge-red-2-12 {
            background: rgba(239, 68, 68, 0.22) !important;
            border: 1px solid rgba(239, 68, 68, 0.6) !important;
            color: #fca5a5 !important;
            font-weight: 800 !important;
        }
        .badge-danger-peligro {
            background: linear-gradient(135deg, #7f1d1d, #b91c1c) !important;
            border: 1px solid #ef4444 !important;
            color: #ffffff !important;
            font-weight: 900 !important;
            box-shadow: 0 0 10px rgba(239, 68, 68, 0.5) !important;
            letter-spacing: 0.3px !important;
            animation: dangerPulse 2s infinite alternate;
        }
        @keyframes dangerPulse {
            0% { box-shadow: 0 0 6px rgba(239, 68, 68, 0.4); }
            100% { box-shadow: 0 0 14px rgba(239, 68, 68, 0.85); }
        }
        .client-card.is-peligro-card {
            border-color: rgba(239, 68, 68, 0.55);
            background: linear-gradient(180deg, rgba(127, 29, 29, 0.15), var(--bg-card));
        }
        .client-card.is-red-card {
            border-color: rgba(239, 68, 68, 0.35);
        }

    
        /* ROUTE DAY PLANNER BAR */
        .route-day-planner {
            display: flex;
            align-items: center;
            gap: 6px;
            margin-bottom: 12px;
            overflow-x: auto;
            scrollbar-width: none;
            -webkit-overflow-scrolling: touch;
            padding: 2px 2px;
        }
        .route-day-planner::-webkit-scrollbar { display: none; }
        
        .day-btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            color: var(--text-muted);
            border-radius: var(--radius-md);
            padding: 7px 12px;
            font-size: 0.8rem;
            font-weight: 800;
            font-family: var(--font-main);
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }
        .day-btn:hover {
            background: rgba(255, 255, 255, 0.1);
            color: #ffffff;
            border-color: rgba(255, 255, 255, 0.2);
        }
        .day-btn.active {
            background: linear-gradient(135deg, #0284c7, #026597);
            border-color: #38bdf8;
            color: #ffffff;
            box-shadow: 0 0 10px rgba(56, 189, 248, 0.35);
        }
        .day-btn.day-today {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(5, 150, 105, 0.3));
            border-color: rgba(16, 185, 129, 0.5);
            color: #34d399;
        }
        .day-btn.day-today.active {
            background: linear-gradient(135deg, #10b981, #059669);
            border-color: #34d399;
            color: #ffffff;
            box-shadow: 0 0 12px rgba(16, 185, 129, 0.45);
        }
        .badge-secuencia {
            background: rgba(2, 132, 199, 0.25) !important;
            border: 1px solid #38bdf8 !important;
            color: #7dd3fc !important;
            font-weight: 900 !important;
        }

    
        /* EXACT DATE ROUTE PLANNER */
        .route-date-picker-bar {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 8px 10px;
            margin-bottom: 8px;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        .route-date-header-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            flex-wrap: wrap;
        }
        .route-date-label {
            font-size: 0.84rem;
            font-weight: 800;
            color: #38bdf8;
            display: flex;
            align-items: center;
            gap: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .route-date-select {
            background: #111522;
            border: 1px solid rgba(56, 189, 248, 0.4);
            color: #ffffff;
            font-family: var(--font-main);
            font-size: 0.85rem;
            font-weight: 700;
            padding: 8px 12px;
            border-radius: var(--radius-md);
            cursor: pointer;
            outline: none;
            flex: 1;
            min-width: 260px;
            max-width: 100%;
        }
        .route-date-select:focus {
            border-color: #38bdf8;
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.35);
        }
        .route-date-pills-row {
            display: flex;
            align-items: center;
            gap: 6px;
            overflow-x: auto;
            scrollbar-width: none;
            -webkit-overflow-scrolling: touch;
            padding: 2px 0;
        }
        .route-date-pills-row::-webkit-scrollbar { display: none; }
        
        .date-quick-btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            color: var(--text-muted);
            border-radius: var(--radius-md);
            padding: 6px 12px;
            font-size: 0.78rem;
            font-weight: 800;
            font-family: var(--font-main);
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }
        .date-quick-btn:hover {
            background: rgba(255, 255, 255, 0.1);
            color: #ffffff;
            border-color: rgba(255, 255, 255, 0.25);
        }
        .date-quick-btn.active {
            background: linear-gradient(135deg, #0284c7, #0369a1);
            border-color: #38bdf8;
            color: #ffffff;
            box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
        }
        .date-banner-info {
            background: linear-gradient(90deg, rgba(2,132,199,0.2), rgba(16,185,129,0.15));
            border: 1px solid rgba(56,189,248,0.3);
            border-radius: var(--radius-md);
            padding: 10px 14px;
            margin-bottom: 12px;
            font-size: 0.85rem;
            font-weight: 800;
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
        }

    </style>
</head>
<body>
    <!-- GITHUB / IPAD AUTO UPDATE BANNER -->
    <div id="updateAvailableBanner" style="display:none; background: linear-gradient(90deg, #0284c7, #10b981); color: #ffffff; text-align: center; padding: 12px 16px; font-weight: 700; font-size: 0.9rem; cursor: pointer; position: sticky; top: 0; z-index: 99999; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" onclick="forceAppUpdate()">
        ✨ ¡Nueva versión detectada en GitHub! Toca aquí para actualizar en 1 segundo ⚡
    </div>

<div class="app-bg"></div>

<div id="storageWarningBanner">
    ⚠️ Tu navegador está en Modo Incógnito estricto. Los datos guardados podrían no persistir si cierras Safari. Utiliza el botón ⚙️ -> Paquete iPad para exportar tus copias.
</div>

<div class="app-shell">

    <!-- TOP HEADER -->
    <header class="app-header">
        <div class="header-left">
            <a href="index.html" class="btn-nav-back" title="Volver al inicio">←</a>
            <div class="brand-title-box">
                <div class="brand-title-row">
                    <span class="brand-title">⚡ BLIZT</span>
                    <span class="brand-badge">PRO</span>
                </div>
                <span class="brand-subtitle">Preventa, Cajas & Cartera de Clientes</span>
            </div>
        </div>
        <div class="header-actions">
            <button class="hdr-icon-btn sync-btn" onclick="forceAppUpdate()" title="Sincronizar y actualizar con GitHub al instante">
                🔄 <span>Actualizar Web</span>
            </button>
            <input type="file" id="excelUploadInput" accept=".xlsx, .xls" style="display:none;" onchange="processMonthlyExcel(this.files[0])">
            <button class="hdr-icon-btn excel-btn" onclick="document.getElementById('excelUploadInput').click()" title="Subir Excel mensual para actualizar datos sin perder correos">
                ☁️ <span>Excel</span>
            </button>
            <button class="hdr-icon-btn" onclick="openSettingsModal()" title="Sincronización con iPad y copias de seguridad">
                ⚙️
            </button>
        </div>
    </header>

    <!-- EXECUTIVE METRICS CHIPS (6 CHIPS SCROLLER) -->
    
    <!-- MAIN VIEW SWITCHER -->
    <div class="view-switcher-bar">
        <button id="btnViewClients" class="nav-view-btn active" onclick="switchMainView('clients')">
            👥 Cartera de Clientes (<span id="switchTotalCount">1.104</span>)
        </button>
        <button id="btnViewDashboard" class="nav-view-btn" onclick="switchMainView('dashboard')">
            📊 Dashboard & Foco Comercial
        </button>
    </div>

    <div id="clientsViewSection">
    <div class="kpi-scroller">
        <div class="kpi-chip k-all" onclick="selectFilterTab('all')">
            <div class="kpi-chip-info">
                <span class="kpi-chip-title">Total Base</span>
                <span class="kpi-chip-value" id="kpiTotal">1.104</span>
            </div>
            <div class="kpi-chip-icon">👥</div>
        </div>
        <div class="kpi-chip k-risk" onclick="selectFilterTab('riesgo')">
            <div class="kpi-chip-info">
                <span class="kpi-chip-title" style="color:#f87171;">🔴 En Riesgo</span>
                <span class="kpi-chip-value" id="kpiRisk" style="color:#ef4444;">0</span>
            </div>
            <div class="kpi-chip-icon">🚨</div>
        </div>
        <div class="kpi-chip k-growth" onclick="selectFilterTab('creciendo')">
            <div class="kpi-chip-info">
                <span class="kpi-chip-title" style="color:#34d399;">🟢 Creciendo</span>
                <span class="kpi-chip-value" id="kpiGrowth" style="color:#10b981;">0</span>
            </div>
            <div class="kpi-chip-icon">📈</div>
        </div>
        <div class="kpi-chip k-cajas" onclick="selectFilterTab('con_cajas')">
            <div class="kpi-chip-info">
                <span class="kpi-chip-title">Cajas 2026 (YTD)</span>
                <span class="kpi-chip-value" id="kpiCajas" style="color:#38bdf8;">0 CJ</span>
            </div>
            <div class="kpi-chip-icon">📦</div>
        </div>
        <div class="kpi-chip k-rutero" onclick="selectFilterTab('rutero')">
            <div class="kpi-chip-info">
                <span class="kpi-chip-title">Rutero BDB</span>
                <span class="kpi-chip-value" id="kpiRutero" style="color:#c084fc;">353</span>
            </div>
            <div class="kpi-chip-icon">🚚</div>
        </div>
        <div class="kpi-chip k-penalizan" onclick="selectFilterTab('penalizan_baja')" style="border-color:rgba(239,68,68,0.45); background:linear-gradient(135deg, rgba(127,29,29,0.3), rgba(220,38,38,0.1)); cursor:pointer;" title="Clientes en tu rutero que POGO marca para quitar o están de baja (penalizan tus visitas y frecuencia)">
            <div class="kpi-chip-info">
                <span class="kpi-chip-title" style="color:#f87171;">⚠️ Bajas</span>
                <span class="kpi-chip-value" id="kpiPenalizan" style="color:#ef4444;">89</span>
            </div>
            <div class="kpi-chip-icon">🚨</div>
        </div>
    </div>

    <!-- SEARCH & FILTER SECTION -->
    <div class="search-section">
                <!-- EXACT DATE ROUTE PLANNER BAR -->
        <div class="route-date-picker-bar">
            <div class="route-date-header-row">
                <span class="route-date-label">
                    <span>📅 RUTA POR FECHA EXACTA:</span>
                </span>
                <select id="routeExactDateSelect" class="route-date-select" onchange="selectExactRouteDate(this.value)">
                    <option value="all">Todas las Fechas (Ver Cartera Completa)</option>
                    <optgroup label="Semana 1 (05 al 09 Octubre)">
                        <option value="05/10/2026">Lunes 05/10/2026 — 17 clientes (Paradas #10 a #232)</option>
                        <option value="06/10/2026">Martes 06/10/2026 — 18 clientes (Paradas #30 a #280)</option>
                        <option value="07/10/2026">Miércoles 07/10/2026 — 18 clientes (Paradas #10 a #210)</option>
                        <option value="08/10/2026">Jueves 08/10/2026 — 18 clientes (Paradas #10 a #223)</option>
                        <option value="09/10/2026">Viernes 09/10/2026 — 18 clientes (Paradas #10 a #280)</option>
                    </optgroup>
                    <optgroup label="Semana 2 (12 al 16 Octubre)">
                        <option value="12/10/2026">Lunes 12/10/2026 — 19 clientes (Paradas #10 a #221)</option>
                        <option value="13/10/2026">Martes 13/10/2026 — 18 clientes (Paradas #10 a #260)</option>
                        <option value="14/10/2026">Miércoles 14/10/2026 — 18 clientes (Paradas #10 a #212)</option>
                        <option value="15/10/2026">Jueves 15/10/2026 — 17 clientes (Paradas #70 a #240)</option>
                        <option value="16/10/2026">Viernes 16/10/2026 — 18 clientes (Paradas #10 a #456)</option>
                    </optgroup>
                    <optgroup label="Semana 3 (19 al 23 Octubre)">
                        <option value="19/10/2026">Lunes 19/10/2026 — 17 clientes (Paradas #20 a #898)</option>
                        <option value="20/10/2026">Martes 20/10/2026 — 17 clientes (Paradas #10 a #240)</option>
                        <option value="21/10/2026">Miércoles 21/10/2026 — 18 clientes (Paradas #10 a #200)</option>
                        <option value="22/10/2026">Jueves 22/10/2026 — 17 clientes (Paradas #10 a #233)</option>
                        <option value="23/10/2026">Viernes 23/10/2026 — 18 clientes (Paradas #30 a #347)</option>
                    </optgroup>
                    <optgroup label="Semana 4 (26 al 30 Octubre)">
                        <option value="26/10/2026">Lunes 26/10/2026 — 18 clientes (Paradas #10 a #200)</option>
                        <option value="27/10/2026">Martes 27/10/2026 — 18 clientes (Paradas #10 a #210)</option>
                        <option value="28/10/2026">Miércoles 28/10/2026 — 17 clientes (Paradas #10 a #787)</option>
                        <option value="29/10/2026">Jueves 29/10/2026 — 17 clientes (Paradas #30 a #578)</option>
                        <option value="30/10/2026">Viernes 30/10/2026 — 17 clientes (Paradas #10 a #343)</option>
                    </optgroup>
                </select>
            </div>
            <!-- QUICK LUNES & WEEK BUTTONS -->
            <div class="route-date-pills-row">
                <span style="font-size:0.75rem; font-weight:800; color:var(--text-muted); margin-right:4px;">Lunes:</span>
                <button class="date-quick-btn" id="qBtn_05_10" onclick="selectExactRouteDate('05/10/2026')">05/10 (17)</button>
                <button class="date-quick-btn" id="qBtn_12_10" onclick="selectExactRouteDate('12/10/2026')">12/10 (19)</button>
                <button class="date-quick-btn" id="qBtn_19_10" onclick="selectExactRouteDate('19/10/2026')">19/10 (17)</button>
                <button class="date-quick-btn" id="qBtn_26_10" onclick="selectExactRouteDate('26/10/2026')">26/10 (18)</button>
                <button class="date-quick-btn active all-btn" id="qBtn_all" onclick="selectExactRouteDate('all')">Ver Todas</button>
            </div>
        </div>
        <!-- ROUTE INFO BANNER -->
        <div id="routeExactDateBanner" style="display:none;" class="date-banner-info"></div>
        <div class="search-bar-wrap">
            <span class="search-icon-svg">🔍</span>
            <input type="text" id="searchInput" class="search-input" placeholder="Buscar por cliente, cajas, código, pueblo, ruta o correo..." oninput="handleSearchInput(this)">
            <button class="search-clear-btn" id="btnSearchClear" onclick="clearSearchInput()">✕</button>
        </div>
        <div class="filter-scroller">
            <button class="filter-pill active" id="pill_all" onclick="selectFilterTab('all')">Todos (1.104)</button>
            <button class="filter-pill pill-red" id="pill_riesgo" onclick="selectFilterTab('riesgo')">🔴 En Riesgo (<span id="pillCountRisk">0</span>)</button>
            <button class="filter-pill" id="pill_penalizan_baja" onclick="selectFilterTab('penalizan_baja')" style="background:rgba(127,29,29,0.6); border-color:#ef4444; color:#ffffff; font-weight:900; box-shadow:0 0 10px rgba(239,68,68,0.4);">⚠️ Bajas (<span id="pillCountPenalizan">234</span>)</button>
            <button class="filter-pill" id="pill_baja_cierre" onclick="selectFilterTab('baja_cierre')" style="background:rgba(127,29,29,0.5); border-color:#ef4444; color:#fca5a5; font-weight:900;">🏚️ Cierres (<span id="pillCountCierre">0</span>)</button>
            <button class="filter-pill" id="pill_baja_temporal" onclick="selectFilterTab('baja_temporal')" style="background:rgba(245,158,11,0.25); border-color:#f59e0b; color:#fbbf24; font-weight:800;">⏳ Temporal (<span id="pillCountTemporal">0</span>)</button>
            <button class="filter-pill" id="pill_sin_compras_dudosos" onclick="selectFilterTab('sin_compras_dudosos')" style="background:rgba(2,132,199,0.25); border-color:#38bdf8; color:#7dd3fc; font-weight:800;">❓ Dudosos (<span id="pillCountDudosos">0</span>)</button>
            <button class="filter-pill pill-red" id="pill_sin_compra_2_12" onclick="selectFilterTab('sin_compra_2_12')">🔴 2-12M (<span id="pillCount2_12">0</span>)</button>
            <button class="filter-pill" id="pill_sin_compra_12_plus" onclick="selectFilterTab('sin_compra_12_plus')" style="background:rgba(127,29,29,0.4); border-color:#ef4444; color:#fca5a5; font-weight:800;">🚨 +12M Peligro (<span id="pillCount12Plus">0</span>)</button>
            <button class="filter-pill pill-red" id="pill_sin_compra_duda" onclick="selectFilterTab('sin_compra_duda')">🚫 0 Cajas (<span id="pillCountDudaBaja">0</span>)</button>
            <button class="filter-pill pill-emerald" id="pill_creciendo" onclick="selectFilterTab('creciendo')">🟢 Creciendo (<span id="pillCountGrowth">0</span>)</button>
            <button class="filter-pill pill-amber" id="pill_estables" onclick="selectFilterTab('estables')">🟡 Estables (<span id="pillCountStable">0</span>)</button>
            <button class="filter-pill pill-pink" id="pill_nuevos" onclick="selectFilterTab('nuevos')" style="display:none;">🆕 Nuevos (<span id="pillCountNuevos">0</span>)</button>
            <button class="filter-pill pill-cyan" id="pill_con_cajas" onclick="selectFilterTab('con_cajas')">📦 Con Cajas 2026</button>
            <button class="filter-pill pill-gold" id="pill_top_cajas" onclick="selectFilterTab('top_cajas')">🔥 Top +500 Cajas</button>
            <button class="filter-pill" id="pill_rutero" onclick="selectFilterTab('rutero')">🚚 Mi Rutero (353)</button>
            <button class="filter-pill pill-cyan" id="pill_con_mail" onclick="selectFilterTab('con_mail')">✉️ Con Email (<span id="pillCountMail">0</span>)</button>
            <button class="filter-pill" id="pill_sin_mail" onclick="selectFilterTab('sin_mail')">⚠️ Sin Email</button>
            <button class="filter-pill pill-gold" id="pill_oro" onclick="selectFilterTab('oro')">🥇 Oro</button>
            <button class="filter-pill pill-plata" id="pill_plata" onclick="selectFilterTab('plata')">🥈 Plata</button>
            <button class="filter-pill pill-bronce" id="pill_bronce" onclick="selectFilterTab('bronce')">🥉 Bronce</button>
            <button class="filter-pill" id="pill_mantener" onclick="selectFilterTab('mantener')">✅ Mantener</button>
            <button class="filter-pill" id="pill_incluir" onclick="selectFilterTab('incluir')">➕ Incluir</button>
            <button class="filter-pill" id="pill_quitar" onclick="selectFilterTab('quitar')">❌ Quitar</button>
            <button class="filter-pill" id="pill_hosteleria" onclick="selectFilterTab('hosteleria')">🍺 Hostelería</button>
            <button class="filter-pill" id="pill_restaurante" onclick="selectFilterTab('restaurante')">🍽️ Restaurante</button>
            <button class="filter-pill" id="pill_retail" onclick="selectFilterTab('retail')">🛒 Retail</button>
        </div>
    </div>

    <!-- CLIENT STREAM -->
    <div class="client-stream" id="clientStream"></div>

    <!-- EMPTY VIEW -->
    <div class="empty-box" id="emptyNotice" style="display:none;">
        <div class="icon">🔍</div>
        <h3 style="color:#ffffff; margin-bottom:4px;">Sin resultados coincidentes</h3>
        <p>Prueba con otro término de búsqueda o selecciona otra pestaña.</p>
    </div>

</div>

</div><!-- /#clientsViewSection -->

<!-- EXECUTIVE DASHBOARD VIEW -->
<div id="dashboardViewSection" class="dashboard-container" style="display:none;"></div>

    <!-- FAB ADD CLIENT -->
<button class="fab-add" onclick="openNewClientModal()" title="Dar de alta nuevo cliente">+</button>

<!-- =========================================================================
     MODAL DOSSIER & PROFILE
     ========================================================================= -->
<div class="modal-overlay" id="detailModal" onclick="if(event.target===this) closeDetailModal()">
    <div class="modal-panel">
        <div class="modal-drag-handle"></div>

        <div class="dossier-top-bar">
            <div class="dossier-top-left">
                <div class="dossier-avatar-large" id="dosAvatar">CL</div>
                <div class="dossier-title-box">
                    <div class="dossier-name" id="dosName">Nombre del Local</div>
                    <div class="dossier-loc-sub" id="dosCity">Localidad · Dirección</div>
                    <div class="badge-cluster" id="dosTags" style="margin-top:5px;"></div>
                </div>
            </div>
            <button class="btn-modal-close" onclick="closeDetailModal()">✕</button>
        </div>

        <!-- HEALTH & RISK DIAGNOSTIC CARD -->
        <div id="dosHealthBanner" class="dossier-health-banner"></div>

        <!-- CONTACT HUB (EMAIL FIRST) -->
        <div class="dossier-contact-hub" id="dosContactHub"></div>

        <!-- WEB RESEARCH BUTTONS -->
        <div style="padding: 10px 20px 4px; font-size:0.75rem; font-weight:800; color:var(--text-muted); text-transform:uppercase;">
            🌐 Buscar en Internet (Ficha del local)
        </div>
        <div class="web-links-grid">
            <a href="#" class="web-link-btn" id="btnWebEmail" target="_blank">✉️ Buscar Email</a>
            <a href="#" class="web-link-btn" id="btnWebGoogle" target="_blank">🔍 Google</a>
            <a href="#" class="web-link-btn" id="btnWebMaps" target="_blank">📍 Maps</a>
            <a href="#" class="web-link-btn" id="btnWebAmarillas" target="_blank">📒 Páginas Amarillas</a>
            <a href="#" class="web-link-btn" id="btnWebPhone" target="_blank">📞 Buscar Teléfono</a>
        </div>

        <!-- SECTIONS -->
        <div class="dossier-section-title">📦 Histórico de Consumo (Cajas Físicas)</div>
        <div class="dossier-grid" id="gridConsumo"></div>

        <div class="dossier-section-title">🚚 Logística y Rutero Preventa</div>
        <div class="dossier-grid" id="gridLogistica"></div>

        <div class="dossier-section-title">📊 Propuesta Comercial POGO</div>
        <div class="dossier-grid" id="gridComercial"></div>

        <div class="dossier-section-title">🏢 Establecimiento y Clasificación</div>
        <div class="dossier-grid" id="gridLocal"></div>

        <!-- FOOTER BUTTONS -->
        <div class="dossier-footer-bar">
            <button class="btn-full-edit" onclick="editCurrentClient()">✏️ Modificar Ficha</button>
            <button class="btn-full-edit" onclick="deleteCurrentClient()" style="flex:0 0 50px; background:rgba(239,68,68,0.15); border-color:rgba(239,68,68,0.3); color:#f87171;" title="Eliminar">🗑️</button>
        </div>

    </div>
</div>

<!-- =========================================================================
     MODAL EDIT / ADD CLIENT
     ========================================================================= -->
<div class="modal-overlay" id="editModal" onclick="if(event.target===this) closeEditModal()">
    <div class="modal-panel">
        <div class="modal-drag-handle"></div>
        <div class="dossier-top-bar">
            <h2 id="editModalTitle" style="font-size:1.1rem; font-weight:800; color:#fff;">Editar Cliente</h2>
            <button class="btn-modal-close" onclick="closeEditModal()">✕</button>
        </div>
        <div class="form-layout">
            
            <!-- INSTANT GITHUB REFRESH -->
            <div style="background:rgba(56,189,248,0.12); border:1px solid rgba(56,189,248,0.35); border-radius:var(--radius-md); padding:14px; text-align:center;">
                <div style="font-size:0.9rem; font-weight:800; color:#38bdf8; margin-bottom:6px;">🔄 Sincronización Inmediata con GitHub</div>
                <p style="font-size:0.8rem; color:var(--text-muted); line-height:1.4; margin-bottom:12px;">
                    ¿Has subido cambios a GitHub y el iPad no los muestra? Pulsa aquí para forzar la descarga de la última versión en 1 segundo:
                </p>
                <button onclick="forceAppUpdate()" class="btn-clipboard-big" style="background:#0284c7; width:100%; font-size:0.88rem;">
                    ⚡ FORZAR DESCARGA ÚLTIMA VERSIÓN GITHUB
                </button>
            </div>
            <div class="form-group">
                <label>Nombre del Establecimiento *</label>
                <input type="text" id="inpName" placeholder="Ej: Bar Central">
            </div>
            <div class="form-row-2">
                <div class="form-group">
                    <label>Código Solicitante *</label>
                    <input type="text" id="inpCode" placeholder="Ej: 0012345678" oninput="this.value=this.value.toUpperCase()">
                </div>
                <div class="form-group">
                    <label>Tipo de Local</label>
                    <select id="inpType">
                        <option value="hosteleria">Hostelería / Bar</option>
                        <option value="restaurante">Restaurante</option>
                        <option value="retail">Retail / Tienda</option>
                        <option value="otro">Otro</option>
                    </select>
                </div>
            </div>
            <div class="form-group">
                <label style="color:#38bdf8;">✉️ Correo Electrónico (Principal)</label>
                <input type="email" id="inpEmail" placeholder="correo@ejemplo.com" style="border-color:rgba(56,189,248,0.4);">
            </div>
            <div class="form-group">
                <label>Teléfono (Opcional)</label>
                <input type="text" id="inpPhone" placeholder="600 000 000">
            </div>
            <div class="form-group">
                <label>Dirección</label>
                <input type="text" id="inpAddress" placeholder="Calle, número...">
            </div>
            <div class="form-row-2">
                <div class="form-group">
                    <label>Localidad / Pueblo</label>
                    <input type="text" id="inpCity" placeholder="Localidad">
                </div>
                <div class="form-group">
                    <label>Ruta Preventa</label>
                    <input type="text" id="inpRutaPrev" placeholder="Ej: P01">
                </div>
            </div>
            <div class="form-row-2">
                <div class="form-group">
                    <label>Distribuidor</label>
                    <input type="text" id="inpDistributor" placeholder="Distribuidor">
                </div>
                <div class="form-group">
                    <label>Medalla</label>
                    <select id="inpMedal">
                        <option value="Oro">Oro</option>
                        <option value="Plata">Plata</option>
                        <option value="Bronce">Bronce</option>
                        <option value="Hierro">Hierro</option>
                    </select>
                </div>
            </div>
            <div class="form-group">
                <label>Notas Comerciales</label>
                <textarea id="inpNotes" rows="3" placeholder="Observaciones, acuerdos, horario de visita..."></textarea>
            </div>
            <button class="btn-clipboard-big" onclick="submitClientForm()" style="margin-top:6px;">
                💾 GUARDAR CAMBIOS
            </button>
        </div>
    </div>
</div>

<!-- =========================================================================
     MODAL SETTINGS & IPAD SYNC HUB
     ========================================================================= -->
<div class="modal-overlay" id="settingsModal" onclick="if(event.target===this) closeSettingsModal()">
    <div class="modal-panel">
        <div class="modal-drag-handle"></div>
        <div class="dossier-top-bar">
            <h2 style="font-size:1.1rem; font-weight:800; color:#fff;">📱 Sincronización iPad & Copias</h2>
            <button class="btn-modal-close" onclick="closeSettingsModal()">✕</button>
        </div>
        <div class="form-layout">
            
            <!-- EXPORT PACK TO IPAD -->
            <div style="background:rgba(2,132,199,0.12); border:1px solid rgba(56,189,248,0.3); border-radius:var(--radius-md); padding:12px;">
                <div style="font-size:0.85rem; font-weight:800; color:#38bdf8; margin-bottom:4px;">1️⃣ Pasar todo del Ordenador al iPad (Cero pérdidas)</div>
                <p style="font-size:0.78rem; color:var(--text-muted); line-height:1.4; margin-bottom:10px;">
                    Genera un paquete único con todos tus clientes actualizados, cajas y todos los correos que hayas escrito:
                </p>
                <button onclick="downloadFullSyncPackage()" class="btn-clipboard-big" style="background:#0284c7;">
                    📦 Descargar Paquete Completo para iPad
                </button>
            </div>

            <!-- IMPORT PACK ON IPAD -->
            <div style="background:rgba(16,185,129,0.1); border:1px solid rgba(16,185,129,0.3); border-radius:var(--radius-md); padding:12px;">
                <div style="font-size:0.85rem; font-weight:800; color:#34d399; margin-bottom:4px;">2️⃣ Cargar Paquete en el iPad</div>
                <p style="font-size:0.78rem; color:var(--text-muted); line-height:1.4; margin-bottom:8px;">
                    En tu iPad, abre este menú y selecciona el archivo que te pasaste (por AirDrop, WhatsApp o iCloud):
                </p>
                <input type="file" id="syncPackageFileInput" accept=".json" style="display:none;" onchange="importSyncPackageFile(this.files[0])">
                <button onclick="document.getElementById('syncPackageFileInput').click()" class="btn-clipboard-big" style="background:#10b981; color:#000;">
                    📥 Seleccionar Archivo de Sincronización (.json)
                </button>
            </div>

            <!-- EXCEL CSV BACKUP -->
            <button onclick="exportFullCSV()" class="btn-full-edit" style="background:rgba(255,255,255,0.06); margin-top:4px;">
                📤 Exportar Toda la Cartera en Excel (CSV)
            </button>

            <!-- PASTE JSON MANUAL -->
            <div style="margin-top:6px; padding-top:10px; border-top:1px solid var(--border);">
                <label style="font-size:0.72rem; font-weight:800; color:var(--text-muted); text-transform:uppercase;">O restaurar texto JSON directo</label>
                <textarea id="jsonRestoreBox" rows="2" placeholder="Pega aquí el contenido JSON si prefieres..." style="width:100%; margin-top:4px; background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius-md); padding:8px; color:#fff; font-family:monospace; font-size:0.75rem;"></textarea>
                <button onclick="restoreContactsFromJSON()" class="btn-full-edit" style="margin-top:6px; width:100%; padding:9px;">
                    🔄 Restaurar Texto JSON
                </button>
            </div>
        </div>
    </div>
</div>

<!-- TOAST MESSAGE -->
<div class="toast-msg" id="toastBox"></div>

<script>
// =========================================================================
//  BLIZT PRO - HEALTH ENGINE, ZERO DATA LOSS & CLIENT TRACKING CORE
// =========================================================================

const BLIZT_BASE_CATALOG = __JSON_PAYLOAD_PLACEHOLDER__;

// =========================================================================
//  GLOBAL UTILITY HELPERS
// =========================================================================
function parseNum(v) {
    if (!v && v !== 0) return 0;
    const n = parseFloat(String(v).replace(',', '.'));
    return isNaN(n) ? 0 : n;
}

function fmtNum(n) {
    return Math.round(n).toLocaleString('es-ES');
}

function getTodayDayCode() {
    const day = new Date().getDay();
    if (day === 0 || day === 6) return '1';
    return String(day);
}

function getMesesSinCompra(c) {
    if (!c || !c.meses_sin_compra) return 0;
    const s = String(c.meses_sin_compra).toUpperCase().replace('M', '').trim();
    const n = parseInt(s, 10);
    return isNaN(n) ? 0 : n;
}

const USER_EDITS_KEY = 'BLIZT_USER_EDITS';
const BASE_UPDATES_KEY = 'BLIZT_BASE_UPDATES';
const NEW_CLIENTS_KEY = 'BLIZT_NEW_CLIENTS_LOG';

let clients = [];
let userEdits = {};
let newClientsLog = {};
let activeDetailId = null;
let editingClientId = null;
let currentTab = 'all';
let searchQuery = '';

// =========================================================================
//  INSTANT GITHUB / IPAD AUTO-UPDATE ENGINE
// =========================================================================

async function forceAppUpdate() {
    showToast('🔄 Descargando última versión de GitHub...', 'info');
    try {
        if ('caches' in window) {
            const keys = await caches.keys();
            await Promise.all(keys.map(k => caches.delete(k)));
        }
        if ('serviceWorker' in navigator) {
            const regs = await navigator.serviceWorker.getRegistrations();
            for (let reg of regs) {
                await reg.unregister();
            }
        }
    } catch(e) {
        console.warn('Cache clear error:', e);
    }
    const cleanUrl = window.location.origin + window.location.pathname;
    window.location.href = cleanUrl + '?t=' + Date.now();
}

function initAutoUpdater() {
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('sw.js?v=' + Date.now()).then(reg => {
            reg.onupdatefound = () => {
                const installingWorker = reg.installing;
                if (installingWorker) {
                    installingWorker.onstatechange = () => {
                        if (installingWorker.state === 'installed' && navigator.serviceWorker.controller) {
                            showUpdateBanner();
                        }
                    };
                }
            };
        }).catch(() => {});
    }

    document.addEventListener('visibilitychange', () => {
        if (document.visibilityState === 'visible') {
            checkRemoteVersion();
        }
    });

    setTimeout(checkRemoteVersion, 3000);
}

function checkRemoteVersion() {
    if (!navigator.onLine) return;
    fetch(window.location.pathname + '?check=' + Date.now(), { cache: 'no-store', method: 'HEAD' })
        .then(res => {
            const etag = res.headers.get('etag') || res.headers.get('last-modified');
            if (etag) {
                const lastSeen = localStorage.getItem('__blizt_app_etag__');
                if (lastSeen && lastSeen !== etag) {
                    showUpdateBanner();
                }
                localStorage.setItem('__blizt_app_etag__', etag);
            }
        })
        .catch(() => {});
}

function showUpdateBanner() {
    const b = document.getElementById('updateAvailableBanner');
    if (b) b.style.display = 'block';
}

function startApp() {
    initAutoUpdater();
    checkStorageHealth();
    initDatabase();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', startApp);
} else {
    startApp();
}

function checkStorageHealth() {
    let ok = false;
    try {
        const k = '__blizt_store_test__';
        localStorage.setItem(k, '1');
        ok = localStorage.getItem(k) === '1';
        localStorage.removeItem(k);
    } catch(e) {
        ok = false;
    }

    const banner = document.getElementById('storageWarningBanner');
    if (!ok && banner) {
        banner.style.display = 'block';
    }
}

function initDatabase() {
    // 1. Load User Edits
    try {
        const raw = localStorage.getItem(USER_EDITS_KEY);
        if (raw) {
            userEdits = JSON.parse(raw) || {};
        }
    } catch(e) {
        userEdits = {};
    }

    // 2. Load New Clients Tracker
    try {
        const rawNew = localStorage.getItem(NEW_CLIENTS_KEY);
        if (rawNew) {
            newClientsLog = JSON.parse(rawNew) || {};
        }
    } catch(e) {
        newClientsLog = {};
    }

    // 3. Scan legacy keys
    const legacyKeys = ['blizt_clients_v3', 'blizt_clients_v2', 'blizt_clients'];
    legacyKeys.forEach(k => {
        try {
            const raw = localStorage.getItem(k);
            if (raw) {
                const arr = JSON.parse(raw);
                if (Array.isArray(arr)) {
                    arr.forEach(item => {
                        if (item.code && (item.email || item.phone || item.notes)) {
                            const cKey = String(item.code).trim().toUpperCase();
                            if (!userEdits[cKey]) userEdits[cKey] = {};
                            if (item.email && !userEdits[cKey].email) userEdits[cKey].email = item.email.trim();
                            if (item.phone && !userEdits[cKey].phone) userEdits[cKey].phone = item.phone.trim();
                            if (item.notes && !userEdits[cKey].notes) userEdits[cKey].notes = item.notes.trim();
                        }
                    });
                }
            }
        } catch(e) {}
    });

    saveUserEditsToStorage();
    rebuildClientList();
    renderStream();
}

function rebuildClientList() {
    let baseData = BLIZT_BASE_CATALOG;
    try {
        const storedBase = localStorage.getItem(BASE_UPDATES_KEY);
        if (storedBase) {
            const parsed = JSON.parse(storedBase);
            if (Array.isArray(parsed) && parsed.length > 50) {
                baseData = parsed;
            }
        }
    } catch(e) {}

    clients = baseData.filter(b => b && (b.name || b.code)).map(base => {
        const cKey = String(base.code).trim().toUpperCase();
        const edit = userEdits[cKey];
        const isNewFromExcel = Boolean(newClientsLog[cKey] || base.is_nuevo_excel);

        let item = { ...base, is_nuevo_excel: isNewFromExcel };

        if (edit) {
            item = {
                ...item,
                email: edit.email !== undefined ? edit.email : (base.email || ''),
                phone: edit.phone !== undefined ? edit.phone : (base.phone || ''),
                notes: edit.notes !== undefined ? edit.notes : (base.notes || ''),
                status: edit.status || base.status || 'active',
                name: edit.name || base.name,
                address: edit.address || base.address,
                city: edit.city || base.city,
                updatedAt: edit.updatedAt || base.updatedAt
            };
        }
        return item;
    });

    Object.keys(userEdits).forEach(cKey => {
        const edit = userEdits[cKey];
        if (edit && edit.isNew && edit.status !== 'deleted' && !clients.some(x => String(x.code).toUpperCase() === cKey)) {
            clients.unshift(edit);
        }
    });
}

function saveUserEditsToStorage() {
    try {
        localStorage.setItem(USER_EDITS_KEY, JSON.stringify(userEdits));
    } catch(e) {
        console.error('Storage error:', e);
    }
}

// =========================================================================
//  HEALTH & RISK TRAFFIC LIGHT ALGORITHM (SEMÁFORO DE SALUD)
// =========================================================================

function getClientHealth(c) {
    const cu26 = parseFloat(String(c.cu2026 || '0').replace(',', '.')) || 0;
    const cu25 = parseFloat(String(c.cu2025 || '0').replace(',', '.')) || 0;
    const cu24 = parseFloat(String(c.cu2024 || '0').replace(',', '.')) || 0;
    const cu23 = parseFloat(String(c.cu2023 || '0').replace(',', '.')) || 0;
    const maxPast = Math.max(cu25, cu24, cu23);
    const propuesta = (c.propuesta || '').toLowerCase();
    const mesesSinCompra = parseInt(c.meses_sin_compra || '0', 10) || 0;
    const isNuevo = Boolean(c.is_nuevo_excel);

    // 1. NUEVO CLIENTE
    if (isNuevo) {
        return {
            status: 'nuevo',
            badgeClass: 'badge-health-nuevo',
            badgeText: '🆕 Nuevo',
            icon: '🆕',
            color: '#f43f5e',
            title: 'Nuevo Cliente Incorporado',
            summary: 'Cliente dado de alta recientemente. Sin histórico previo consolidado.',
            recommendation: 'Realizar visita de bienvenida, asegurar pedidos semanales y verificar datos de contacto.',
            trendPercent: null
        };
    }

    // 2. PROPUESTA DE BAJA / QUITAR
    if (propuesta.includes('quitar')) {
        return {
            status: 'riesgo',
            badgeClass: 'badge-health-risk',
            badgeText: '🔴 En Riesgo (Baja)',
            icon: '🔴',
            color: '#ef4444',
            title: 'Propuesta de Salida / Baja en Cartera',
            summary: 'El sistema POGO marca este cliente con propuesta "Quitar" o baja de rutero.',
            recommendation: '🚨 Evaluar con el supervisor si se puede reactivar con condiciones especiales o liberar hueco en ruta.',
            trendPercent: -100
        };
    }

    // 3. EN RIESGO: Fuga de volumen o cliente con histórico a 0 en 2026
    if (maxPast >= 25 && cu26 === 0) {
        return {
            status: 'riesgo',
            badgeClass: 'badge-health-risk',
            badgeText: '🔴 En Riesgo (0 CJ)',
            icon: '🔴',
            color: '#ef4444',
            title: 'Alerta Crítica: Sin Consumo en 2026',
            summary: `Compró ${Math.round(maxPast)} cajas en años previos pero lleva 0 cajas en 2026. Riesgo inminente de fuga a la competencia.`,
            recommendation: '🚨 Visita urgente de rescate: auditar servicio, revisar precios y ofrecer paquete de reactivación.',
            trendPercent: -100
        };
    }

    // 4. COMPARATIVA 2026 vs 2025
    if (cu25 > 0 && cu26 > 0) {
        const ratio = cu26 / cu25;
        const diffPercent = Math.round((ratio - 1) * 100);

        if (ratio >= 0.70 || cu26 >= cu25) {
            const pctText = diffPercent > 0 ? `+${diffPercent}%` : `${diffPercent}%`;
            return {
                status: 'creciendo',
                badgeClass: 'badge-health-growth',
                badgeText: `🟢 Creciendo (${pctText})`,
                icon: '🟢',
                color: '#10b981',
                title: 'Cliente en Expansión / Crecimiento',
                summary: `Ritmo de compras excelente (${cu26} CJ en 2026 frente a ${cu25} CJ en 2025). Evolución positiva.`,
                recommendation: '🌟 Cliente prioritario: premiar fidelidad, proponer ampliación de gama y acuerdos de volumen.',
                trendPercent: diffPercent
            };
        } else if (ratio <= 0.35 && maxPast >= 40) {
            return {
                status: 'riesgo',
                badgeClass: 'badge-health-risk',
                badgeText: `🔴 En Riesgo (${diffPercent}%)`,
                icon: '🔴',
                color: '#ef4444',
                title: 'Caída Significativa de Volumen',
                summary: `El ritmo de pedidos ha disminuido un ${Math.abs(diffPercent)}% respecto a 2025 (${cu26} CJ vs ${cu25} CJ).`,
                recommendation: '⚠️ Contactar de inmediato para detectar causas del descenso antes de que se consolide la pérdida.',
                trendPercent: diffPercent
            };
        } else {
            const sign = diffPercent > 0 ? '+' : '';
            return {
                status: 'estable',
                badgeClass: 'badge-health-stable',
                badgeText: `🟡 Estable (${sign}${diffPercent}%)`,
                icon: '🟡',
                color: '#fbbf24',
                title: 'Consumo Estable / En Ritmo',
                summary: `Nivel de compra regular acorde al histórico comercial (${cu26} CJ vs ${cu25} CJ en 2025).`,
                recommendation: 'Mantener frecuencia de visita programada y asegurar correcta reposición en lineales.',
                trendPercent: diffPercent
            };
        }
    }

    // 5. MESES SIN COMPRA
    if (mesesSinCompra >= 3 && maxPast >= 15) {
        return {
            status: 'riesgo',
            badgeClass: 'badge-health-risk',
            badgeText: `🔴 Alerta (${mesesSinCompra}M sin compra)`,
            icon: '🔴',
            color: '#ef4444',
            title: `Inactividad Prolongada (${mesesSinCompra} meses)`,
            summary: `El local acumula ${mesesSinCompra} meses sin cursar pedidos tras un histórico de ${Math.round(maxPast)} cajas.`,
            recommendation: '📞 Llamar o visitar esta semana para reactivar la cuenta antes del cierre contable del mes.',
            trendPercent: -50
        };
    }

    // 6. NUEVA ACTIVACIÓN CON CAJAS
    if (cu26 > 0 && cu25 === 0) {
        return {
            status: 'creciendo',
            badgeClass: 'badge-health-growth',
            badgeText: '🟢 Nueva Activación',
            icon: '🟢',
            color: '#10b981',
            title: 'Nueva Cuenta Activada en 2026',
            summary: `Primera activación registrada con ${cu26} cajas en 2026 sin compras el año anterior.`,
            recommendation: 'Consolidar la cuenta, fijar frecuencia fija de visita y afianzar la relación de servicio.',
            trendPercent: 100
        };
    }

    // 7. POR DEFECTO ESTABLE
    return {
        status: 'estable',
        badgeClass: 'badge-health-stable',
        badgeText: '🟡 Estable',
        icon: '🟡',
        color: '#94a3b8',
        title: 'Cuenta Normalizada',
        summary: 'Sin alertas críticas en el histórico de consumo.',
        recommendation: 'Seguimiento estándar de preventa según calendario de visitas.',
        trendPercent: 0
    };
}

// =========================================================================
//  MONTHLY EXCEL MERGE & NEW CLIENTS DETECTION
// =========================================================================

function processMonthlyExcel(file) {
    if (!file) return;
    if (typeof XLSX === 'undefined') {
        alert('⚠️ La librería Excel está cargando. Espera un momento y vuelve a intentar.');
        return;
    }

    showToast('⏳ Analizando archivo Excel mensual...', 'success');

    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const data = new Uint8Array(e.target.result);
            const wb = XLSX.read(data, { type: 'array' });

            const pogoSheetName = wb.SheetNames.find(s => s.toLowerCase().includes('pogo') || s.toLowerCase().includes('recomendaciones'));
            const ruteroSheetName = wb.SheetNames.find(s => s.toLowerCase().includes('rutero'));

            if (!pogoSheetName && !ruteroSheetName) {
                alert('⚠️ No se encontraron las hojas "Recomendaciones POGO" o "Rutero" en este Excel.');
                return;
            }

            let updatedCount = 0;
            let newCount = 0;
            const newlyAddedNames = [];

            if (pogoSheetName) {
                const sheet = wb.Sheets[pogoSheetName];
                const rows = XLSX.utils.sheet_to_json(sheet, { header: 1 });
                if (rows && rows.length > 1) {
                    const headers = rows[0].map(h => String(h || '').trim().toLowerCase());
                    const colCode = headers.findIndex(h => h.includes('solicitante') || h.includes('cliente'));
                    const colName = headers.findIndex(h => h.includes('cliente') && !h.includes('solicitante')) >= 0 ? 
                                    headers.findIndex(h => h.includes('cliente') && !h.includes('solicitante')) : 
                                    headers.findIndex(h => h.includes('nombre'));
                    const colTrans = headers.findIndex(h => h.includes('transporte') || h.includes('distribuidor'));
                    const colRuta = headers.findIndex(h => h.includes('ruta dm') || h === 'ruta');
                    const colPrev = headers.findIndex(h => h.includes('prev'));
                    const colDia = headers.findIndex(h => h.includes('dia') || h.includes('día'));
                    const colDir = headers.findIndex(h => h.includes('direcci'));
                    const colLoc = headers.findIndex(h => h.includes('localidad') || h.includes('ciudad') || h.includes('pueblo'));
                    const colMed = headers.findIndex(h => h.includes('medalla') && !h.includes('potencial'));
                    const colMedPot = headers.findIndex(h => h.includes('potencial'));
                    const colProp = headers.findIndex(h => h.includes('propuesta'));
                    const colCU26 = headers.findIndex(h => h.includes('2026'));
                    const colCU25 = headers.findIndex(h => h.includes('2025'));
                    const colCU24 = headers.findIndex(h => h.includes('2024'));
                    const colCU23 = headers.findIndex(h => h.includes('2023'));
                    const colPuntos = headers.findIndex(h => h.includes('puntos'));
                    const colMeses = headers.findIndex(h => h.includes('meses'));

                    for (let i = 1; i < rows.length; i++) {
                        const r = rows[i];
                        if (!r || r.length === 0) continue;
                        const codeVal = r[colCode >= 0 ? colCode : 2];
                        const nameVal = r[colName >= 0 ? colName : 3];
                        if (!codeVal || !nameVal) continue;

                        const code = String(codeVal).split('.')[0].trim().toUpperCase();
                        let existing = clients.find(c => String(c.code).toUpperCase() === code);

                        const pogoData = {
                            name: String(nameVal).trim(),
                            code: code,
                            distributor: colTrans >= 0 && r[colTrans] ? String(r[colTrans]).trim() : (existing ? existing.distributor : ''),
                            ruta: colRuta >= 0 && r[colRuta] ? String(r[colRuta]).trim() : (existing ? existing.ruta : 'BDB'),
                            ruta_prev: colPrev >= 0 && r[colPrev] ? String(r[colPrev]).trim() : (existing ? existing.ruta_prev : ''),
                            dia_visita: colDia >= 0 && r[colDia] ? formatDiaVisita(r[colDia]) : (existing ? existing.dia_visita : ''),
                            address: colDir >= 0 && r[colDir] ? String(r[colDir]).trim() : (existing ? existing.address : ''),
                            city: colLoc >= 0 && r[colLoc] ? String(r[colLoc]).trim() : (existing ? existing.city : 'Extremadura'),
                            medal: colMed >= 0 && r[colMed] ? String(r[colMed]).trim() : (existing ? existing.medal : 'Bronce'),
                            medal_potencial: colMedPot >= 0 && r[colMedPot] ? String(r[colMedPot]).trim() : (existing ? existing.medal_potencial : ''),
                            propuesta: colProp >= 0 && r[colProp] ? String(r[colProp]).trim() : (existing ? existing.propuesta : 'Mantener'),
                            cu2026: colCU26 >= 0 && r[colCU26] !== undefined ? String(r[colCU26]).trim() : (existing ? existing.cu2026 : '0'),
                            cu2025: colCU25 >= 0 && r[colCU25] !== undefined ? String(r[colCU25]).trim() : (existing ? existing.cu2025 : '0'),
                            cu2024: colCU24 >= 0 && r[colCU24] !== undefined ? String(r[colCU24]).trim() : (existing ? existing.cu2024 : '0'),
                            cu2023: colCU23 >= 0 && r[colCU23] !== undefined ? String(r[colCU23]).trim() : (existing ? existing.cu2023 : '0'),
                            puntos_pogo: colPuntos >= 0 && r[colPuntos] ? String(r[colPuntos]).trim() : (existing ? existing.puntos_pogo : '0'),
                            meses_sin_compra: colMeses >= 0 && r[colMeses] ? String(r[colMeses]).trim() : (existing ? existing.meses_sin_compra : '0'),
                            fecha_alta: new Date().toISOString().slice(0, 7)
                        };

                        if (existing) {
                            Object.assign(existing, pogoData);
                            updatedCount++;
                        } else {
                            pogoData.id = 'client_' + code.toLowerCase() + '_' + Date.now().toString(36);
                            pogoData.is_nuevo_excel = true;
                            pogoData.email = '';
                            pogoData.phone = '';
                            pogoData.notes = '🆕 Nuevo cliente añadido en actualización mensual.';
                            clients.push(pogoData);
                            newClientsLog[code] = true;
                            newlyAddedNames.push(pogoData.name);
                            newCount++;
                        }
                    }
                }
            }

            // Scan rutero sheet if present
            if (ruteroSheetName) {
                const rSheet = wb.Sheets[ruteroSheetName];
                const rRows = XLSX.utils.sheet_to_json(rSheet, { header: 1 });
                if (rRows && rRows.length > 1) {
                    const rHeaders = rRows[0].map(h => String(h || '').trim().toLowerCase());
                    const rColCode = rHeaders.findIndex(h => h.includes('solicitante') || h.includes('cliente') || h.includes('codigo'));
                    const rColFrec = rHeaders.findIndex(h => h.includes('frecuencia') || h.includes('frec'));
                    const rColSec = rHeaders.findIndex(h => h.includes('secuencia') || h.includes('sec'));
                    const rColProx = rHeaders.findIndex(h => h.includes('prox') || h.includes('próx'));

                    for (let j = 1; j < rRows.length; j++) {
                        const row = rRows[j];
                        if (!row || row.length === 0) continue;
                        const codeVal = row[rColCode >= 0 ? rColCode : 0];
                        if (!codeVal) continue;
                        const code = String(codeVal).split('.')[0].trim().toUpperCase();
                        let target = clients.find(c => String(c.code).toUpperCase() === code);
                        if (target) {
                            target.en_rutero = true;
                            if (rColFrec >= 0 && row[rColFrec]) target.frecuencia = String(row[rColFrec]).trim();
                            if (rColSec >= 0 && row[rColSec]) target.secuencia = String(row[rColSec]).trim();
                            if (rColProx >= 0 && row[rColProx]) target.fecha_visita = formatExcelDate(row[rColProx]);
                        }
                    }
                }
            }

            try {
                localStorage.setItem(BASE_UPDATES_KEY, JSON.stringify(clients));
                localStorage.setItem(NEW_CLIENTS_KEY, JSON.stringify(newClientsLog));
            } catch(e) {}

            rebuildClientList();
            renderStream();

            let msg = `✅ ¡Actualización Excel completada!\n\n` +
                      `• Clientes actualizados: ${updatedCount}\n` +
                      `• 🆕 Nuevos clientes detectados: ${newCount}\n` +
                      `• Tus correos guardados: ${Object.keys(userEdits).length} (intactos al 100%)`;
            if (newCount > 0) {
                msg += `\n\nNuevos clientes:\n${newlyAddedNames.slice(0, 5).map(n => '• ' + n).join('\n')}${newCount > 5 ? '\n...y ' + (newCount - 5) + ' más' : ''}`;
            }
            alert(msg);
            showToast(`✅ ${updatedCount} actualizados, ${newCount} nuevos clientes`, 'success');

        } catch(err) {
            console.error(err);
            alert('❌ Error al procesar el Excel: ' + (err.message || 'Verifica el formato del archivo.'));
        }
    };
    reader.readAsArrayBuffer(file);
}

function formatDiaVisita(v) {
    const s = String(v).trim();
    const map = { '1':'Lunes (1)', '2':'Martes (2)', '3':'Miércoles (3)', '4':'Jueves (4)', '5':'Viernes (5)', '6':'Sábado (6)' };
    return map[s] || s;
}

function formatExcelDate(v) {
    if (!v) return '';
    if (v instanceof Date) {
        return v.toLocaleDateString('es-ES');
    }
    return String(v).split('T')[0];
}

// =========================================================================
//  STREAM RENDERING & KPI UPDATER
// =========================================================================

function updateKPIs() {
    const total = clients.length;
    const rutero = clients.filter(c => c.en_rutero).length;
    const emails = clients.filter(c => c.email && c.email.trim()).length;
    const nuevos = clients.filter(c => c.is_nuevo_excel).length;
    
    let sumCajas2026 = 0;
    let countRisk = 0;
    let countGrowth = 0;
    let countStable = 0;
    let countDudaBaja = 0;
    let count2_12 = 0;
    let countCierre = 0;
    let countPenalizan = 0;
    let countTemporal = 0;
    let countDudosos = 0;
    let count12Plus = 0;

    clients.forEach(c => {
        if (c.cu2026) {
            const num = parseFloat(String(c.cu2026).replace(',', '.'));
            if (!isNaN(num)) sumCajas2026 += num;
        }
        const h = getClientHealth(c);
        const c26Val = parseNum(c.cu2026);
        const cK = String(c.code).trim().toUpperCase();
        const aud = userEdits[cK] ? userEdits[cK].bajaAudit : null;
        if (c26Val === 0 || aud === 'baja') countDudaBaja++;
        const mCount = getMesesSinCompra(c);
        if (mCount >= 2 && mCount <= 12) count2_12++;
        const bloqLower = (c.bloqueo || '').toLowerCase();
        if (bloqLower.includes('cierre')) countCierre++;
        if (c26Val === 0 && (bloqLower.includes('baja') || bloqLower.includes('cierre') || bloqLower.includes('juridico') || bloqLower.includes('jurídico'))) countPenalizan++;
        else if (bloqLower.includes('temporal')) countTemporal++;
        if (c26Val === 0 && bloqLower.includes('sin asignar')) countDudosos++;
        if (mCount > 12) count12Plus++;
        if (h.status === 'riesgo') countRisk++;
        else if (h.status === 'creciendo') countGrowth++;
        else if (h.status === 'estable') countStable++;
    });

    const setVal = (id, val) => {
        const el = document.getElementById(id);
        if (el) el.textContent = val;
    };

    setVal('kpiTotal', total.toLocaleString());
    setVal('kpiRisk', countRisk.toLocaleString());
    setVal('kpiGrowth', countGrowth.toLocaleString());
    setVal('kpiCajas', Math.round(sumCajas2026).toLocaleString() + ' CJ');
    setVal('kpiRutero', rutero.toLocaleString());
    setVal('kpiMail', emails.toLocaleString());

    setVal('pillCountRisk', countRisk);
    setVal('pillCountGrowth', countGrowth);
    setVal('pillCountStable', countStable);
    setVal('pillCountDudaBaja', countDudaBaja);
    setVal('pillCount2_12', count2_12);
    setVal('pillCountCierre', countCierre);
    setVal('kpiPenalizan', countPenalizan);
    setVal('pillCountPenalizan', countPenalizan);

    // Calculate day counts
    const todayCode = getTodayDayCode();
    const countToday = clients.filter(c => c.en_rutero && String(c.dia_visita || '').includes(todayCode)).length;
    const countD1 = clients.filter(c => c.en_rutero && String(c.dia_visita || '').includes('1')).length;
    const countD2 = clients.filter(c => c.en_rutero && String(c.dia_visita || '').includes('2')).length;
    const countD3 = clients.filter(c => c.en_rutero && String(c.dia_visita || '').includes('3')).length;
    const countD4 = clients.filter(c => c.en_rutero && String(c.dia_visita || '').includes('4')).length;
    const countD5 = clients.filter(c => c.en_rutero && String(c.dia_visita || '').includes('5')).length;

    setVal('dayCountToday', countToday);
    setVal('dayCount1', countD1);
    setVal('dayCount2', countD2);
    setVal('dayCount3', countD3);
    setVal('dayCount4', countD4);
    setVal('dayCount5', countD5);
    setVal('pillCountTemporal', countTemporal);
    setVal('pillCountDudosos', countDudosos);
    setVal('pillCount12Plus', count12Plus);
    setVal('pillCountMail', emails);

    const pillNuevos = document.getElementById('pill_nuevos');
    const pillCountNuevos = document.getElementById('pillCountNuevos');
    if (pillNuevos && pillCountNuevos) {
        pillCountNuevos.textContent = nuevos;
        pillNuevos.style.display = nuevos > 0 ? 'inline-flex' : 'none';
    }
}

function renderStream() {
    updateKPIs();
    const stream = document.getElementById('clientStream');
    const emptyNotice = document.getElementById('emptyNotice');
    if (!stream) return;

    const filtered = getFilteredList();

    if (filtered.length === 0) {
        stream.innerHTML = '';
        if (emptyNotice) emptyNotice.style.display = 'block';
        return;
    }

    if (emptyNotice) emptyNotice.style.display = 'none';

    const limit = searchQuery ? 250 : 100;
    const itemsToShow = filtered.slice(0, limit);

    let html = itemsToShow.map(c => renderCardHTML(c)).join('');

    if (filtered.length > limit) {
        html += `<div style="text-align:center; padding:18px; font-size:0.85rem; font-weight:700; color:var(--text-muted); background:rgba(255,255,255,0.03); border-radius:var(--radius-md); margin-top:8px;">
            Mostrando ${limit} de ${filtered.length} clientes. Usa el buscador superior para encontrar cualquier cliente al instante.
        </div>`;
    }

    stream.innerHTML = html;
}

function renderCardHTML(c) {
    const initials = (c.name || '?').slice(0, 2).toUpperCase();
    const medalLower = (c.medal || '').toLowerCase();
    const health = getClientHealth(c);
    
    let medalClass = '';
    let medalIcon = '🎖️';
    let cardMedalClass = '';
    if (medalLower.includes('oro')) {
        medalClass = 'badge-oro';
        medalIcon = '🥇';
        cardMedalClass = 'is-oro';
    } else if (medalLower.includes('plata')) {
        medalClass = 'badge-plata';
        medalIcon = '🥈';
        cardMedalClass = 'is-plata';
    } else if (medalLower.includes('bronce')) {
        medalClass = 'badge-bronce';
        medalIcon = '🥉';
        cardMedalClass = 'is-bronce';
    }

    if (health.status === 'riesgo') cardMedalClass += ' is-risk';
    else if (health.status === 'creciendo') cardMedalClass += ' is-growth';
    else if (health.status === 'estable') cardMedalClass += ' is-stable';

    if (c.en_rutero) cardMedalClass += ' is-rutero-card';
    if (c.is_nuevo_excel) cardMedalClass += ' is-nuevo-card';

    const hasEmail = c.email && c.email.trim();
    const hasPhone = c.phone && c.phone.trim();
    const cleanDigits = hasPhone ? c.phone.replace(/\D/g, '') : '';

    const cu26 = c.cu2026 && c.cu2026 !== '0' && c.cu2026 !== '0.0' ? c.cu2026 : '';
    const cu25 = c.cu2025 && c.cu2025 !== '0' && c.cu2025 !== '0.0' ? c.cu2025 : '';
    const cu24 = c.cu2024 && c.cu2024 !== '0' && c.cu2024 !== '0.0' ? c.cu2024 : '';
    const cu23 = c.cu2023 && c.cu2023 !== '0' && c.cu2023 !== '0.0' ? c.cu2023 : '';

    const bestVolumeBadge = cu26 ? `📦 ${cu26} CJ (26)` : cu25 ? `📦 ${cu25} CJ (25)` : '';
    const seqNum = c.secuencia ? parseInt(String(c.secuencia), 10) : null;
    const seqBadge = (seqNum && c.en_rutero) ? '<span class="badge-chip badge-secuencia">📍 Parada #' + seqNum + '</span>' : '';
    
    const cKey = String(c.code).trim().toUpperCase();
    const auditStatus = userEdits[cKey] ? userEdits[cKey].bajaAudit : null;
    const mSinCompra = parseInt(String(c.meses_sin_compra || '0'), 10) || 0;
    const isQuitar = (c.propuesta || '').toLowerCase().includes('quitar');
    const bloq = (c.bloqueo || '').toLowerCase();
    const pLow = (c.propuesta || '').toLowerCase();
    const isPenaliza = c.en_rutero && (pLow.includes('quitar') || bloq.includes('baja') || bloq.includes('cierre'));
    
    let bloqBadge = '';
    if (bloq.includes('cierre')) {
        bloqBadge = '<span class="badge-chip" style="background:rgba(127,29,29,0.35); border:1px solid #ef4444; color:#fca5a5; font-weight:900;">🏚️ CIERRE NEGOCIO</span>';
        cardMedalClass += ' is-peligro-card';
    } else if (bloq.includes('temporal')) {
        bloqBadge = '<span class="badge-chip" style="background:rgba(245,158,11,0.25); border:1px solid #f59e0b; color:#fbbf24; font-weight:800;">⏳ BAJA TEMPORAL</span>';
    } else if (parseNum(c.cu2026) === 0 && bloq.includes('sin asignar')) {
        bloqBadge = '<span class="badge-chip" style="background:rgba(2,132,199,0.25); border:1px solid #38bdf8; color:#7dd3fc; font-weight:800;">❓ CERO CAJAS (AUDITAR)</span>';
    }

    let auditBadge = '';
    if (auditStatus === 'activo') {
        auditBadge = '<span class="badge-chip" style="background:rgba(16,185,129,0.2); border:1px solid rgba(16,185,129,0.5); color:#34d399; font-weight:800;">✅ Sigue Activo</span>';
    } else if (auditStatus === 'baja') {
        auditBadge = '<span class="badge-chip" style="background:rgba(239,68,68,0.25); border:1px solid rgba(239,68,68,0.6); color:#fca5a5; font-weight:800;">❌ Confirmado Baja</span>';
    } else if (mSinCompra > 12) {
        auditBadge = '<span class="badge-chip badge-danger-peligro">🚨 PELIGRO: ' + mSinCompra + ' Meses Sin Compra</span>';
        cardMedalClass += ' is-peligro-card';
    } else if (mSinCompra >= 2 && mSinCompra <= 12) {
        auditBadge = '<span class="badge-chip badge-red-2-12">🔴 ' + mSinCompra + ' Meses Sin Compra</span>';
        cardMedalClass += ' is-red-card';
    } else if (parseNum(c.cu2026) === 0) {
        auditBadge = '<span class="badge-chip" style="background:rgba(239,68,68,0.25); border:1px solid rgba(239,68,68,0.6); color:#fca5a5; font-weight:900;">🚫 CERO COMPRAS 2026</span>';
    } else if (isQuitar) {
        auditBadge = '<span class="badge-chip" style="background:rgba(239,68,68,0.18); border:1px solid rgba(239,68,68,0.5); color:#f87171; font-weight:800;">🚨 Propuesta Quitar</span>';
    } else if (mSinCompra === 1) {
        auditBadge = '<span class="badge-chip" style="background:rgba(245,158,11,0.18); border:1px solid rgba(245,158,11,0.5); color:#fbbf24; font-weight:800;">⏸️ 1 Mes Sin Compra</span>';
    }
    
    return `
    <div class="client-card ${cardMedalClass}" onclick="openClientDetail('${c.id}')">
        <div class="card-top-row">
            <div class="card-name-group">
                <div class="card-avatar">${initials}</div>
                <div class="card-title-box">
                    <div class="card-title">${esc(c.name)}</div>
                    <div class="card-code-sub">
                        <span>#${esc(c.code)}</span>
                        <span>·</span>
                        <span>📍 ${esc(c.city || 'Extremadura')}</span>
                    </div>
                </div>
            </div>
            <div class="badge-cluster">
                ${seqBadge}
                <span class="badge-chip ${health.badgeClass}">${health.badgeText}</span>
                ${isPenaliza ? '<span class="badge-chip" style="background:rgba(239,68,68,0.25); border:1px solid #ef4444; color:#fca5a5; font-weight:900;">⚠️ PENALIZA RUTA (PROPUESTA QUITAR)</span>' : ''}
                ${bloqBadge}
                ${auditBadge}
                ${c.is_nuevo_excel ? `<span class="badge-chip badge-health-nuevo">🆕 NUEVO</span>` : ''}
                ${c.en_rutero ? `<span class="badge-chip badge-rutero">🚚 Rutero</span>` : ''}
                ${c.medal ? `<span class="badge-chip ${medalClass}">${medalIcon} ${esc(c.medal)}</span>` : ''}
                ${bestVolumeBadge ? `<span class="badge-chip badge-cajas-top">${bestVolumeBadge}</span>` : ''}
            </div>
        </div>

        <div class="card-meta-row">
            <div class="meta-item loc">
                <span>📍 ${esc(c.address || c.city || 'Extremadura')}</span>
            </div>
            ${c.ruta_prev ? `<div class="meta-item"><span>🚚 Prev: ${esc(c.ruta_prev)}</span></div>` : ''}
            ${c.dia_visita ? `<div class="meta-item"><span>📅 ${esc(c.dia_visita)}</span></div>` : ''}
        </div>

        <!-- CONSUMO DE CAJAS VISIBLE DIRECTAMENTE -->
        <div class="card-boxes-strip">
            <div class="box-col highlight">
                <span class="box-lbl">2026 (YTD)</span>
                <span class="box-num">${cu26 ? cu26 + ' CJ' : '-'}</span>
            </div>
            <div class="box-col">
                <span class="box-lbl">2025</span>
                <span class="box-num">${cu25 ? cu25 + ' CJ' : '-'}</span>
            </div>
            <div class="box-col">
                <span class="box-lbl">2024</span>
                <span class="box-num">${cu24 ? cu24 + ' CJ' : '-'}</span>
            </div>
            <div class="box-col">
                <span class="box-lbl">2023</span>
                <span class="box-num">${cu23 ? cu23 + ' CJ' : '-'}</span>
            </div>
        </div>

        <div class="card-actions-bar" onclick="event.stopPropagation()">
            ${hasEmail ? `
                <a href="mailto:${esc(c.email)}" class="btn-action-email" title="Enviar correo">
                    ✉️ ${esc(c.email)}
                </a>
                <button onclick="promptQuickEmail('${esc(c.code)}', '${esc(c.name)}', '${esc(c.email)}')" class="mini-btn" title="Modificar correo a mano">✏️</button>
                <button onclick="deleteEmailDirect('${esc(c.code)}')" class="mini-btn del" title="Borrar correo">🗑️</button>
                ${hasPhone ? `
                    <a href="tel:${esc(c.phone)}" class="mini-btn" style="color:#34d399;" title="Llamar: ${esc(c.phone)}">📞</a>
                    <a href="https://wa.me/34${cleanDigits}" target="_blank" class="mini-btn" style="color:#25d366;" title="WhatsApp">💬</a>
                ` : ''}
            ` : `
                <button class="btn-action-addemail" onclick="promptQuickEmail('${esc(c.code)}', '${esc(c.name)}', '')">
                    ✉️ Escribir a mano / Pegar Email
                </button>
            `}
        </div>
    </div>`;
}

// =========================================================================
//  FILTERS & SEARCH
// =========================================================================

function getFilteredList() {
    const q = searchQuery.toLowerCase();
    const tab = currentTab;
    

    let list = clients.filter(c => {
        if (q) {
            const matchSearch =
                (c.name || '').toLowerCase().includes(q) ||
                (c.code || '').toLowerCase().includes(q) ||
                (c.city || '').toLowerCase().includes(q) ||
                (c.address || '').toLowerCase().includes(q) ||
                (c.ruta || '').toLowerCase().includes(q) ||
                (c.ruta_prev || '').toLowerCase().includes(q) ||
                (c.distributor || '').toLowerCase().includes(q) ||
                (c.subcanal || '').toLowerCase().includes(q) ||
                (c.segment || '').toLowerCase().includes(q) ||
                (c.email || '').toLowerCase().includes(q) ||
                (c.phone || '').toLowerCase().includes(q) ||
                (c.cu2026 || '').toLowerCase().includes(q) ||
                (c.cu2025 || '').toLowerCase().includes(q);

            if (!matchSearch) return false;
        }

        // Filter by Exact Date of Visit
        if (currentExactRouteDate !== 'all') {
            if (c.fecha_visita !== currentExactRouteDate) return false;
        }

        const h = getClientHealth(c);

        if (tab === 'all') return true;
        if (tab === 'penalizan_baja') {
            const c26 = parseNum(c.cu2026);
            const b = (c.bloqueo || '').toLowerCase();
            return c26 === 0 && (b.includes('baja') || b.includes('cierre') || b.includes('juridico') || b.includes('jurídico'));
        }
        if (tab === 'baja_cierre') {
            return (c.bloqueo || '').toLowerCase().includes('cierre');
        }
        if (tab === 'baja_temporal') {
            return (c.bloqueo || '').toLowerCase().includes('temporal');
        }
        if (tab === 'sin_compras_dudosos') {
            return parseNum(c.cu2026) === 0 && (c.bloqueo || '').toLowerCase().includes('sin asignar');
        }
        if (tab === 'sin_compra_2_12') {
            const m = getMesesSinCompra(c);
            return m >= 2 && m <= 12;
        }
        if (tab === 'sin_compra_12_plus') {
            const m = getMesesSinCompra(c);
            return m > 12;
        }
        if (tab === 'sin_compra_duda') {
            return parseNum(c.cu2026) === 0;
        }
        if (tab === 'riesgo') return h.status === 'riesgo';
        if (tab === 'creciendo') return h.status === 'creciendo';
        if (tab === 'estables') return h.status === 'estable';
        if (tab === 'nuevos') return Boolean(c.is_nuevo_excel);
        if (tab === 'con_cajas') return Boolean(c.cu2026 && parseFloat(c.cu2026) > 0);
        if (tab === 'top_cajas') {
            const c26 = parseFloat(c.cu2026 || '0');
            const c25 = parseFloat(c.cu2025 || '0');
            return c26 >= 500 || c25 >= 500;
        }
        if (tab === 'rutero') return c.en_rutero === true;
        if (tab === 'con_mail') return Boolean(c.email && c.email.trim());
        if (tab === 'sin_mail') return !c.email || !c.email.trim();
        if (tab === 'oro') return (c.medal || '').toLowerCase().includes('oro');
        if (tab === 'plata') return (c.medal || '').toLowerCase().includes('plata');
        if (tab === 'bronce') return (c.medal || '').toLowerCase().includes('bronce');
        if (tab === 'mantener') return (c.propuesta || '').toLowerCase().includes('mantener');
        if (tab === 'incluir') return (c.propuesta || '').toLowerCase().includes('incluir');
        if (tab === 'quitar') return (c.propuesta || '').toLowerCase().includes('quitar');
        if (tab === 'hosteleria') return c.type === 'hosteleria';
        if (tab === 'restaurante') return c.type === 'restaurante';
        if (tab === 'retail') return c.type === 'retail';

        return true;
    });

    // Sort by sequence when a specific day route is active
    if (currentExactRouteDate !== 'all') {
        list.sort((a, b) => {
            if (a.en_rutero && !b.en_rutero) return -1;
            if (!a.en_rutero && b.en_rutero) return 1;
            const seqA = parseInt(String(a.secuencia || '99999'), 10) || 99999;
            const seqB = parseInt(String(b.secuencia || '99999'), 10) || 99999;
            return seqA - seqB;
        });
    }

    return list;
}

// =========================================================================
//  ROUTE DAY PLANNER ENGINE (RUTA DE HOY & SECUENCIA)
// =========================================================================

let currentExactRouteDate = 'all'; // 'all' or exact string e.g. '05/10/2026'

function selectExactRouteDate(dateStr) {
    currentExactRouteDate = dateStr;

    // Sync select dropdown
    const sel = document.getElementById('routeExactDateSelect');
    if (sel) sel.value = dateStr;

    // Sync quick buttons
    document.querySelectorAll('.date-quick-btn').forEach(b => b.classList.remove('active'));
    if (dateStr === 'all') {
        const btnAll = document.getElementById('qBtn_all');
        if (btnAll) btnAll.classList.add('active');
    } else {
        const key = dateStr.slice(0, 5).replace('/', '_');
        const btn = document.getElementById('qBtn_' + key);
        if (btn) btn.classList.add('active');
    }

    renderStream();
}

function selectFilterTab(tabId) {
    currentTab = tabId;
    document.querySelectorAll('.filter-pill').forEach(b => b.classList.remove('active'));
    const btn = document.getElementById('pill_' + tabId);
    if (btn) btn.classList.add('active');
    renderStream();
}

function handleSearchInput(inp) {
    searchQuery = inp.value.trim();
    const btn = document.getElementById('btnSearchClear');
    if (btn) btn.style.display = searchQuery ? 'flex' : 'none';
    renderStream();
}

function clearSearchInput() {
    const inp = document.getElementById('searchInput');
    if (inp) inp.value = '';
    searchQuery = '';
    const btn = document.getElementById('btnSearchClear');
    if (btn) btn.style.display = 'none';
    renderStream();
}

// =========================================================================
//  DOSSIER & CONTACT HUB
// =========================================================================

function openClientDetail(id) {
    const c = clients.find(x => x.id === id);
    if (!c) return;
    activeDetailId = id;

    const setTxt = (id, val) => {
        const el = document.getElementById(id);
        if (el) el.textContent = val;
    };

    setTxt('dosAvatar', (c.name || '?').slice(0, 2).toUpperCase());
    setTxt('dosName', c.name || '');
    setTxt('dosCity', '📍 ' + (c.city || 'Extremadura') + (c.address ? ' · ' + c.address : ''));

    const medalLower = (c.medal || '').toLowerCase();
    const medalIcon = medalLower.includes('oro') ? '🥇' : medalLower.includes('plata') ? '🥈' : medalLower.includes('bronce') ? '🥉' : '🎖️';
    const propuesta = c.propuesta || '';
    const health = getClientHealth(c);

    let tagsHtml = `
        <span class="badge-chip" style="background:rgba(255,255,255,0.08); color:#cbd5e1; font-family:monospace;">#${esc(c.code)}</span>
        <span class="badge-chip ${health.badgeClass}">${health.badgeText}</span>
        ${c.is_nuevo_excel ? `<span class="badge-chip badge-health-nuevo">🆕 NUEVO (${esc(c.fecha_alta || 'Este Mes')})</span>` : ''}
        ${c.en_rutero ? `<span class="badge-chip badge-rutero">🚚 Rutero BDB</span>` : `<span class="badge-chip" style="background:rgba(255,255,255,0.08); color:#94a3b8;">⚪ POGO</span>`}
        ${c.medal ? `<span class="badge-chip ${medalLower.includes('oro') ? 'badge-oro' : medalLower.includes('plata') ? 'badge-plata' : 'badge-bronce'}">${medalIcon} ${esc(c.medal)}</span>` : ''}
        ${propuesta ? `<span class="badge-chip" style="background:rgba(255,255,255,0.08);">${esc(propuesta)}</span>` : ''}
    `;
    const dosTags = document.getElementById('dosTags');
    if (dosTags) dosTags.innerHTML = tagsHtml;

    // Render Health Banner
    renderHealthBanner(c, health);

    renderDossierContactHub(c);
    setupWebLookupLinks(c);
    renderDossierSections(c);

    const modal = document.getElementById('detailModal');
    if (modal) modal.classList.add('open');
}


// =========================================================================
//  AUDITORÍA COMERCIAL: ¿BAJA DEFINITIVA O PAUSA TEMPORAL?
// =========================================================================

function getMesesSinCompra(c) {
    if (!c || !c.meses_sin_compra) return 0;
    const s = String(c.meses_sin_compra).toUpperCase().replace('M', '').trim();
    const n = parseInt(s, 10);
    return isNaN(n) ? 0 : n;
}

function renderDossierAuditBox(c) {
    const box = document.getElementById('dosAuditVerificationBox');
    if (!box) return;

    const cKey = String(c.code).trim().toUpperCase();
    const currentAudit = userEdits[cKey] ? userEdits[cKey].bajaAudit : null;
    const mSin = getMesesSinCompra(c);
    const p = (c.propuesta || '').toLowerCase();
    const bloq = (c.bloqueo || '').toLowerCase();
    const isQuitar = p.includes('quitar');
    const isZero26 = parseNum(c.cu2026) === 0;

    let diagnosisText = '';
    let boxBorder = 'rgba(255,255,255,0.1)';
    let boxBg = 'rgba(255,255,255,0.02)';

    if (currentAudit === 'activo') {
        diagnosisText = '✅ <strong>Cliente verificado: SIGUE ACTIVO</strong> (Solo fue una pausa temporal de pedidos).';
        boxBorder = 'rgba(16,185,129,0.4)';
        boxBg = 'rgba(16,185,129,0.08)';
    } else if (currentAudit === 'baja') {
        diagnosisText = '❌ <strong>Cliente verificado: CONFIRMADO DE BAJA / CERRADO</strong>.';
        boxBorder = 'rgba(239,68,68,0.4)';
        boxBg = 'rgba(239,68,68,0.1)';
    } else if (bloq.includes('cierre')) {
        diagnosisText = '🏚️ <strong style="color:#ef4444;">ESTADO OFICIAL SAP: BAJA - CIERRE DE NEGOCIO</strong>. La empresa ya tiene registrado que este local cerró. No pierdas tiempo visitándolo salvo que sepas que ha reabierto con nuevo dueño.';
        boxBorder = '#ef4444';
        boxBg = 'linear-gradient(135deg, rgba(127,29,29,0.35), rgba(220,38,38,0.15))';
    } else if (bloq.includes('temporal')) {
        diagnosisText = '⏳ <strong style="color:#fbbf24;">ESTADO OFICIAL SAP: BAJA TEMPORAL</strong>. Local con cierre por temporada, vacaciones o reforma. Preguntar fecha de reapertura.';
        boxBorder = 'rgba(245,158,11,0.5)';
        boxBg = 'rgba(245,158,11,0.1)';
    } else if (isZero26 && bloq.includes('sin asignar')) {
        diagnosisText = '❓ <strong style="color:#38bdf8;">ESTADO: 0 CAJAS SIN MOTIVO DE BAJA ASIGNADO</strong>. Este cliente está a cero compras pero la empresa no lo tiene de baja. <strong>Prioridad de auditoría en tu ruta</strong> para ver si sigue abierto o ha cerrado.';
        boxBorder = '#38bdf8';
        boxBg = 'rgba(2,132,199,0.15)';
    } else if (mSin > 12) {
        diagnosisText = '🚨 <strong style="color:#ef4444;">ALERTA MÁXIMA: ' + mSin + ' MESES SIN COMPRAS (+1 AÑO)</strong>. Muy probable baja definitiva o local cerrado/traspasado.';
        boxBorder = '#ef4444';
        boxBg = 'linear-gradient(135deg, rgba(127,29,29,0.35), rgba(220,38,38,0.15))';
    } else if (mSin >= 2 && mSin <= 12) {
        diagnosisText = '🔴 <strong style="color:#f87171;">ALERTA ROJA: ' + mSin + ' MESES SIN COMPRAS (2 A 12 MESES)</strong>. Cliente en riesgo grave de pérdida. Visita de rescate recomendada.';
        boxBorder = 'rgba(239,68,68,0.5)';
        boxBg = 'rgba(239,68,68,0.1)';
    } else if (isQuitar) {
        diagnosisText = '🚨 <strong>Propuesta "Quitar de ruta" por el sistema</strong>. Verifica en tu próxima visita si el local sigue abierto o si ha cerrado.';
        boxBorder = 'rgba(239,68,68,0.4)';
        boxBg = 'rgba(239,68,68,0.08)';
    } else if (mSin === 1) {
        diagnosisText = '⏸️ <strong>Lleva 1 mes sin registrar compras</strong>. Pausa reciente. ¿Baja real o simplemente no ha necesitado género este mes?';
        boxBorder = 'rgba(245,158,11,0.4)';
        boxBg = 'rgba(245,158,11,0.08)';
    } else {
        diagnosisText = '🟢 Cliente con compras recientes normales. Si detectas que ha cerrado, puedes marcarlo aquí.';
    }

    box.innerHTML = `
        <div style="background:${boxBg}; border:1px solid ${boxBorder}; border-radius:var(--radius-md); padding:12px; transition:all 0.3s;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                <span style="font-size:0.8rem; font-weight:800; color:#ffffff; text-transform:uppercase; letter-spacing:0.5px;">
                    🔍 Auditoría: ¿Baja o Pausa Temporal?
                </span>
                <span style="font-size:0.75rem; color:var(--text-muted);">
                    Meses sin compra: <strong style="color:#fff;">${mSin}</strong>
                </span>
            </div>
            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.4; margin-bottom:10px;">
                ${diagnosisText}
            </div>
            <div style="display:flex; gap:8px; flex-wrap:wrap;">
                <button type="button" onclick="setClientAuditState('${c.code}', 'activo')" style="flex:1; min-width:120px; padding:8px 10px; border-radius:6px; border:1px solid ${currentAudit === 'activo' ? '#10b981' : 'rgba(16,185,129,0.3)'}; background:${currentAudit === 'activo' ? '#10b981' : 'rgba(16,185,129,0.1)'}; color:#fff; font-size:0.78rem; font-weight:800; cursor:pointer;">
                    🟢 Sigue Activo
                </button>
                <button type="button" onclick="setClientAuditState('${c.code}', 'baja')" style="flex:1; min-width:120px; padding:8px 10px; border-radius:6px; border:1px solid ${currentAudit === 'baja' ? '#ef4444' : 'rgba(239,68,68,0.3)'}; background:${currentAudit === 'baja' ? '#ef4444' : 'rgba(239,68,68,0.15)'}; color:#fff; font-size:0.78rem; font-weight:800; cursor:pointer;">
                    🔴 Confirmar Baja
                </button>
                <button type="button" onclick="setClientAuditState('${c.code}', 'duda')" style="flex:1; min-width:120px; padding:8px 10px; border-radius:6px; border:1px solid ${!currentAudit || currentAudit === 'duda' ? '#f59e0b' : 'rgba(245,158,11,0.3)'}; background:${!currentAudit || currentAudit === 'duda' ? 'rgba(245,158,11,0.2)' : 'rgba(255,255,255,0.04)'}; color:#fbbf24; font-size:0.78rem; font-weight:800; cursor:pointer;">
                    🟡 Por Verificar
                </button>
            </div>
        </div>
    `;
}

function setClientAuditState(code, state) {
    const cKey = String(code).trim().toUpperCase();
    if (!userEdits[cKey]) userEdits[cKey] = {};
    userEdits[cKey].bajaAudit = state;
    userEdits[cKey].updatedAt = new Date().toISOString();
    saveUserEditsToStorage();

    const c = clients.find(x => String(x.code).toUpperCase() === cKey);
    if (c) {
        renderDossierAuditBox(c);
        showToast(state === 'activo' ? '✅ Marcado como ACTIVO (Solo pausa)' : state === 'baja' ? '❌ Confirmado como BAJA/CERRADO' : '🟡 Marcado como PENDIENTE de verificar', 'success');
        renderStream();
    }
}

function renderHealthBanner(c, health) {
    const banner = document.getElementById('dosHealthBanner');
    if (!banner) return;

    banner.className = 'dossier-health-banner is-' + health.status;
    banner.innerHTML = `
        <div class="health-banner-top">
            <div style="display:flex; align-items:center; gap:6px;">
                <span style="font-size:1.1rem;">${health.icon}</span>
                <strong style="font-size:0.9rem; color:#fff;">${esc(health.title)}</strong>
            </div>
            <span class="health-status-badge ${health.badgeClass}">${esc(health.badgeText)}</span>
        </div>
        <div class="health-summary-text">${esc(health.summary)}</div>
        <div class="health-action-box" style="border-left-color:${health.color};">
            <div style="font-size:0.68rem; font-weight:800; color:${health.color}; text-transform:uppercase; margin-bottom:2px;">⚡ Acción Comercial Recomendada:</div>
            <div style="color:#f8fafc; font-weight:600;">${esc(health.recommendation)}</div>
        </div>
    `;
}

function renderDossierContactHub(c) {
    const hub = document.getElementById('dosContactHub');
    if (!hub) return;
    const hasEmail = c.email && c.email.trim();
    const hasPhone = c.phone && c.phone.trim();
    const cleanDigits = hasPhone ? c.phone.replace(/\D/g, '') : '';

    let html = `
        <div class="hub-title-row">
            <span class="hub-title">✉️ Correo Electrónico & Contacto</span>
            <span class="hub-badge">💾 Guardado Permanente</span>
        </div>
    `;

    // 1. EMAIL SECTION
    if (hasEmail) {
        html += `
            <div class="contact-active-card">
                <div>
                    <div style="font-size:0.65rem; font-weight:800; color:#38bdf8; margin-bottom:2px;">CORREO GUARDADO:</div>
                    <div class="contact-val-large">✉️ ${esc(c.email)}</div>
                </div>
                <div class="contact-actions-cluster">
                    <a href="mailto:${esc(c.email)}" class="btn-action-email" style="flex:initial; padding:8px 14px;">✉️ Enviar</a>
                    <button onclick="promptEditEmail('${esc(c.code)}', '${esc(c.email)}')" class="mini-btn" title="Modificar a mano">✏️</button>
                    <button onclick="deleteEmailDirect('${esc(c.code)}')" class="mini-btn del" title="Borrar correo">🗑️</button>
                </div>
            </div>
        `;
    } else {
        html += `
            <div class="manual-input-box">
                <span class="manual-input-label">✍️ Escribir correo a mano:</span>
                <div class="manual-input-bar">
                    <input type="email" id="manualEmailInput" placeholder="correo@ejemplo.com" onkeydown="if(event.key==='Enter') saveManualEmailInput('${esc(c.code)}')">
                    <button type="button" onclick="saveManualEmailInput('${esc(c.code)}')">💾 Guardar</button>
                </div>
            </div>
            <button class="btn-clipboard-big" onclick="pasteEmailFromClipboard('${esc(c.code)}')">
                📋 O PEGAR DIRECTO DEL PORTAPAPELES
            </button>
        `;
    }

    // 2. PHONE SECTION
    if (hasPhone) {
        html += `
            <div class="contact-active-card" style="border-color:rgba(16,185,129,0.4); margin-top:2px;">
                <div>
                    <div style="font-size:0.65rem; font-weight:800; color:#34d399; margin-bottom:2px;">TELÉFONO:</div>
                    <div class="contact-val-large" style="color:#34d399; font-size:0.95rem;">📞 ${esc(c.phone)}</div>
                </div>
                <div class="contact-actions-cluster">
                    <a href="tel:${esc(c.phone)}" class="mini-btn" style="color:#34d399;">📞</a>
                    <a href="https://wa.me/34${cleanDigits}" target="_blank" class="mini-btn" style="color:#25d366;">💬</a>
                    <button onclick="promptEditPhone('${esc(c.code)}', '${esc(c.phone)}')" class="mini-btn">✏️</button>
                    <button onclick="deletePhoneDirect('${esc(c.code)}')" class="mini-btn del">🗑️</button>
                </div>
            </div>
        `;
    } else {
        html += `
            <div class="manual-input-bar" style="margin-top:2px;">
                <input type="text" id="manualPhoneInput" placeholder="Teléfono opcional (ej: 600000000)...">
                <button type="button" style="background:#10b981; color:#000;" onclick="saveManualPhoneInput('${esc(c.code)}')">💾 Guardar Teléfono</button>
            </div>
        `;
    }

    hub.innerHTML = html;
}

function setupWebLookupLinks(c) {
    const qEmail = encodeURIComponent(`"${c.name}" ${c.city || ''} email correo`);
    const qGoogle = encodeURIComponent(`"${c.name}" ${c.city || ''} contacto`);
    const qMaps = encodeURIComponent(`${c.name} ${c.address || ''} ${c.city || ''}`);
    const qAmarillas = encodeURIComponent(`${c.name} ${c.city || ''}`);
    const qPhone = encodeURIComponent(`"${c.name}" ${c.city || ''} teléfono`);

    const setLink = (id, href) => {
        const el = document.getElementById(id);
        if (el) el.href = href;
    };

    setLink('btnWebEmail', `https://www.google.com/search?q=${qEmail}`);
    setLink('btnWebGoogle', `https://www.google.com/search?q=${qGoogle}`);
    setLink('btnWebMaps', `https://www.google.com/maps/search/?api=1&query=${qMaps}`);
    setLink('btnWebAmarillas', `https://www.paginasamarillas.es/search/all/all-ma/${qAmarillas}/1/`);
    setLink('btnWebPhone', `https://www.google.com/search?q=${qPhone}`);
}

function renderDossierSections(c) {
    const gridConsumo = document.getElementById('gridConsumo');
    if (gridConsumo) {
        gridConsumo.innerHTML = [
            { label: 'Consumo CU 2026 (YTD)', val: c.cu2026 ? c.cu2026 + ' Cajas' : 'Sin consumo registrado', blue: true },
            { label: 'Consumo CU 2025', val: c.cu2025 ? c.cu2025 + ' Cajas' : '-' },
            { label: 'Consumo CU 2024', val: c.cu2024 ? c.cu2024 + ' Cajas' : '-' },
            { label: 'Consumo CU 2023', val: c.cu2023 ? c.cu2023 + ' Cajas' : '-' }
        ].map(renderCellHTML).join('');
    }

    const gridLogistica = document.getElementById('gridLogistica');
    if (gridLogistica) {
        gridLogistica.innerHTML = [
            { label: 'Ruta DM', val: c.ruta || 'BDB' },
            { label: 'Ruta Preventa', val: c.ruta_prev || '-', blue: true },
            { label: 'Día de Visita', val: c.dia_visita || '-' },
            { label: 'Distribuidor', val: c.distributor || '-', full: true },
            { label: 'Fecha Próx. Visita', val: c.fecha_visita || (c.en_rutero ? 'Según calendario' : 'No en ruta') },
            { label: 'Frecuencia / Secuencia', val: (c.frecuencia ? c.frecuencia + ' días' : '-') + (c.secuencia ? ' · Secuencia #' + c.secuencia : '') },
            { label: 'Estado en Rutero', val: c.en_rutero ? '✅ En Rutero Activo (353)' : '⚪ Prospecto POGO', green: c.en_rutero },
            { label: 'Bloqueo Pedido', val: c.bloqueo && c.bloqueo !== '#' ? c.bloqueo : 'Sin bloqueo', red: (c.bloqueo && c.bloqueo !== '#' && !c.bloqueo.toLowerCase().includes('sin')) }
        ].map(renderCellHTML).join('');
    }

    const gridComercial = document.getElementById('gridComercial');
    if (gridComercial) {
        gridComercial.innerHTML = [
            { label: 'Propuesta POGO', val: c.propuesta || '-', full: true, blue: true },
            { label: 'Puntos POGO', val: c.puntos_pogo || '-' },
            { label: 'Meses sin Compra', val: c.meses_sin_compra ? c.meses_sin_compra + ' meses' : '0' },
            { label: 'Medalla Volumen', val: c.medal || '-', gold: true },
            { label: 'Medalla Potencial', val: c.medal_potencial || '-' },
            { label: 'Visitas Últimos 12M', val: c.visitas_12m || '12' }
        ].map(renderCellHTML).join('');
    }

    const gridLocal = document.getElementById('gridLocal');
    if (gridLocal) {
        gridLocal.innerHTML = [
            { label: 'Dirección Completa', val: c.address || 'Sin dirección', full: true },
            { label: 'Población / Localidad', val: c.city || '-' },
            { label: 'NIF / CIF', val: c.nif || '-' },
            { label: 'Subcanal CCIP', val: c.subcanal || '-' },
            { label: 'Segmento FDE', val: c.segment || '-' },
            { label: 'Grupo de Negocio', val: c.grupo_negocio || '-' },
            { label: 'Cla. Operacional', val: c.cla_operacional || '-' },
            { label: 'Notas Comerciales', val: c.notes || 'Sin notas registradas', full: true }
        ].map(renderCellHTML).join('');
    }
}

function renderCellHTML(it) {
    const colorClass = it.blue ? 'highlight-blue' : it.green ? 'highlight-green' : it.gold ? 'highlight-gold' : it.red ? 'highlight-red' : '';
    return `
    <div class="dossier-cell ${it.full ? 'full' : ''}">
        <span class="cell-label">${it.label}</span>
        <span class="cell-value ${colorClass}">${esc(it.val)}</span>
    </div>`;
}

function closeDetailModal() {
    const modal = document.getElementById('detailModal');
    if (modal) modal.classList.remove('open');
    activeDetailId = null;
}

// =========================================================================
//  SAVE & DELETE ACTIONS
// =========================================================================

function promptQuickEmail(code, name, current) {
    const val = window.prompt(`✉️ Correo de "${name}":\\n\\n(Para borrarlo, déjalo vacío y pulsa Aceptar)`, current || '');
    if (val !== null) {
        commitEmailSave(code, val.trim());
    }
}

async function pasteEmailFromClipboard(code) {
    let text = '';
    try {
        if (navigator.clipboard && navigator.clipboard.readText) {
            text = await navigator.clipboard.readText();
        }
    } catch(e) {}

    if (!text) {
        text = window.prompt('📋 Pega el correo copiado aquí:');
    }

    if (text) {
        const clean = text.trim();
        if (clean.includes('@') && clean.includes('.')) {
            commitEmailSave(code, clean);
        } else {
            showToast('⚠️ No parece un correo válido', 'error');
        }
    }
}

function promptEditEmail(code, current) {
    const val = window.prompt('✏️ Modificar Correo Electrónico:', current || '');
    if (val !== null) {
        commitEmailSave(code, val.trim());
    }
}

function saveManualEmailInput(code) {
    const inp = document.getElementById('manualEmailInput');
    if (!inp) return;
    const val = inp.value.trim();
    if (!val || !val.includes('@')) {
        showToast('⚠️ Introduce un correo válido', 'error');
        return;
    }
    commitEmailSave(code, val);
}

function deleteEmailDirect(code) {
    if (confirm('🗑️ ¿Estás seguro de que quieres eliminar este correo?')) {
        commitEmailSave(code, '');
    }
}

function commitEmailSave(code, emailVal) {
    const cKey = String(code).trim().toUpperCase();
    if (!userEdits[cKey]) userEdits[cKey] = {};
    userEdits[cKey].email = emailVal;
    userEdits[cKey].updatedAt = new Date().toISOString();

    saveUserEditsToStorage();
    rebuildClientList();
    renderStream();

    if (activeDetailId) {
        const c = clients.find(x => x.id === activeDetailId);
        if (c) renderDossierContactHub(c);
    }

    showToast(emailVal ? '✉️ Correo guardado permanentemente' : '🗑️ Correo eliminado', 'success');
}

function promptEditPhone(code, current) {
    const val = window.prompt('✏️ Modificar Teléfono:', current || '');
    if (val !== null) {
        commitPhoneSave(code, val.trim());
    }
}

function saveManualPhoneInput(code) {
    const inp = document.getElementById('manualPhoneInput');
    if (!inp) return;
    commitPhoneSave(code, inp.value.trim());
}

function deletePhoneDirect(code) {
    if (confirm('🗑️ ¿Eliminar este teléfono?')) {
        commitPhoneSave(code, '');
    }
}

function commitPhoneSave(code, phoneVal) {
    const cKey = String(code).trim().toUpperCase();
    if (!userEdits[cKey]) userEdits[cKey] = {};
    userEdits[cKey].phone = phoneVal;
    userEdits[cKey].updatedAt = new Date().toISOString();

    saveUserEditsToStorage();
    rebuildClientList();
    renderStream();

    if (activeDetailId) {
        const c = clients.find(x => x.id === activeDetailId);
        if (c) renderDossierContactHub(c);
    }

    showToast(phoneVal ? '📞 Teléfono guardado' : '🗑️ Teléfono eliminado', 'success');
}

// =========================================================================
//  EDIT / NEW CLIENT MODAL
// =========================================================================

function openNewClientModal() {
    editingClientId = null;
    const setTitle = document.getElementById('editModalTitle');
    if (setTitle) setTitle.textContent = '➕ Nuevo Cliente';
    
    const setVal = (id, val) => {
        const el = document.getElementById(id);
        if (el) el.value = val;
    };

    setVal('inpName', '');
    setVal('inpCode', 'NUEVO_' + Date.now().toString().slice(-6));
    setVal('inpType', 'hosteleria');
    setVal('inpEmail', '');
    setVal('inpPhone', '');
    setVal('inpAddress', '');
    setVal('inpCity', 'Extremadura');
    setVal('inpRutaPrev', 'P01');
    setVal('inpDistributor', 'BDB');
    setVal('inpMedal', 'Bronce');
    setVal('inpNotes', '');
    
    const editModal = document.getElementById('editModal');
    if (editModal) editModal.classList.add('open');
}

function editCurrentClient() {
    if (!activeDetailId) return;
    const c = clients.find(x => x.id === activeDetailId);
    if (!c) return;

    editingClientId = c.id;
    const setTitle = document.getElementById('editModalTitle');
    if (setTitle) setTitle.textContent = '✏️ Editar ' + (c.name || 'Cliente');
    
    const setVal = (id, val) => {
        const el = document.getElementById(id);
        if (el) el.value = val;
    };

    setVal('inpName', c.name || '');
    setVal('inpCode', c.code || '');
    setVal('inpType', c.type || 'hosteleria');
    setVal('inpEmail', c.email || '');
    setVal('inpPhone', c.phone || '');
    setVal('inpAddress', c.address || '');
    setVal('inpCity', c.city || '');
    setVal('inpRutaPrev', c.ruta_prev || '');
    setVal('inpDistributor', c.distributor || '');
    setVal('inpMedal', c.medal || 'Bronce');
    setVal('inpNotes', c.notes || '');

    closeDetailModal();
    const editModal = document.getElementById('editModal');
    if (editModal) editModal.classList.add('open');
}

function closeEditModal() {
    const editModal = document.getElementById('editModal');
    if (editModal) editModal.classList.remove('open');
    editingClientId = null;
}

function submitClientForm() {
    const inpName = document.getElementById('inpName');
    const inpCode = document.getElementById('inpCode');
    const name = inpName ? inpName.value.trim() : '';
    const code = inpCode ? inpCode.value.trim().toUpperCase() : '';
    if (!name || !code) {
        alert('⚠️ Por favor completa el Nombre y Código del cliente.');
        return;
    }

    const cKey = code;
    if (!userEdits[cKey]) userEdits[cKey] = {};

    const getV = (id) => {
        const el = document.getElementById(id);
        return el ? el.value.trim() : '';
    };

    userEdits[cKey] = {
        ...userEdits[cKey],
        name: name,
        code: code,
        type: getV('inpType') || 'hosteleria',
        email: getV('inpEmail'),
        phone: getV('inpPhone'),
        address: getV('inpAddress'),
        city: getV('inpCity') || 'Extremadura',
        ruta_prev: getV('inpRutaPrev'),
        distributor: getV('inpDistributor'),
        medal: getV('inpMedal') || 'Bronce',
        notes: getV('inpNotes'),
        updatedAt: new Date().toISOString(),
        isNew: !clients.some(x => String(x.code).toUpperCase() === cKey)
    };

    if (userEdits[cKey].isNew) {
        userEdits[cKey].id = 'client_' + code.toLowerCase() + '_' + Date.now().toString(36);
        userEdits[cKey].en_rutero = true;
        userEdits[cKey].propuesta = 'Mantener';
        userEdits[cKey].cu2026 = '0';
        userEdits[cKey].cu2025 = '0';
    }

    saveUserEditsToStorage();
    rebuildClientList();
    renderStream();
    closeEditModal();
    showToast('💾 Ficha guardada con éxito', 'success');
}

function deleteCurrentClient() {
    if (!activeDetailId) return;
    const c = clients.find(x => x.id === activeDetailId);
    if (!c) return;

    if (confirm(`🗑️ ¿Seguro que deseas eliminar a "${c.name}"?`)) {
        const cKey = String(c.code).trim().toUpperCase();
        userEdits[cKey] = { status: 'deleted', updatedAt: new Date().toISOString() };
        saveUserEditsToStorage();
        closeDetailModal();
        rebuildClientList();
        renderStream();
        showToast('🗑️ Cliente eliminado', 'success');
    }
}

// =========================================================================
//  SETTINGS MODAL & ZERO-DATA-LOSS IPAD SYNC
// =========================================================================

function openSettingsModal() {
    const modal = document.getElementById('settingsModal');
    if (modal) modal.classList.add('open');
}

function closeSettingsModal() {
    const modal = document.getElementById('settingsModal');
    if (modal) modal.classList.remove('open');
}

function downloadFullSyncPackage() {
    const exportBundle = {
        bliztVersion: '4.0.0-pro',
        exportedAt: new Date().toISOString(),
        deviceOrigin: navigator.userAgent,
        userEdits: userEdits,
        baseUpdates: localStorage.getItem(BASE_UPDATES_KEY) ? JSON.parse(localStorage.getItem(BASE_UPDATES_KEY)) : clients,
        newClientsLog: newClientsLog
    };

    const jsonStr = JSON.stringify(exportBundle, null, 2);
    const blob = new Blob([jsonStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `BLIZT_SINCRONIZACION_IPAD.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);

    showToast('📦 Paquete iPad descargado', 'success');
}

function importSyncPackageFile(file) {
    if (!file) return;
    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const data = JSON.parse(e.target.result);
            if (data && (data.userEdits || data.baseUpdates)) {
                if (data.userEdits) {
                    userEdits = { ...userEdits, ...data.userEdits };
                    saveUserEditsToStorage();
                }
                if (data.baseUpdates && Array.isArray(data.baseUpdates)) {
                    try {
                        localStorage.setItem(BASE_UPDATES_KEY, JSON.stringify(data.baseUpdates));
                    } catch(e) {}
                }
                if (data.newClientsLog) {
                    newClientsLog = { ...newClientsLog, ...data.newClientsLog };
                    try {
                        localStorage.setItem(NEW_CLIENTS_KEY, JSON.stringify(newClientsLog));
                    } catch(e) {}
                }

                rebuildClientList();
                renderStream();
                closeSettingsModal();
                alert('🎉 ¡SINCRONIZACIÓN EN IPAD COMPLETADA!\\n\\nTodos tus datos, clientes actualizados, cajas y correos están listos en tu iPad.');
                showToast('✅ Sincronizado en iPad con éxito', 'success');
            } else {
                throw new Error('Formato inválido');
            }
        } catch(err) {
            console.error(err);
            alert('❌ Error al procesar el archivo de sincronización. Asegúrate de seleccionar el archivo .json descargado del ordenador.');
        }
    };
    reader.readAsText(file);
}

function restoreContactsFromJSON() {
    const box = document.getElementById('jsonRestoreBox');
    if (!box) return;
    const txt = box.value.trim();
    if (!txt) {
        showToast('⚠️ Pega el texto JSON primero', 'error');
        return;
    }
    try {
        const parsed = JSON.parse(txt);
        if (typeof parsed === 'object' && parsed !== null) {
            userEdits = { ...userEdits, ...(parsed.userEdits || parsed) };
            saveUserEditsToStorage();
            rebuildClientList();
            renderStream();
            box.value = '';
            closeSettingsModal();
            showToast('✅ Datos restaurados con éxito', 'success');
        } else {
            throw new Error('Formato inválido');
        }
    } catch(e) {
        alert('❌ Error al procesar el archivo JSON. Verifica que sea un JSON válido.');
    }
}

function exportFullCSV() {
    let csv = 'Codigo,Nombre,Poblacion,Direccion,Email,Telefono,Medalla,Rutero,Propuesta_POGO,Semaforo_Salud,CU_2026,CU_2025,CU_2024,CU_2023,Distribuidor\\n';
    clients.forEach(c => {
        const h = getClientHealth(c);
        const row = [
            `"${c.code || ''}"`,
            `"${(c.name || '').replace(/"/g, '""')}"`,
            `"${(c.city || '').replace(/"/g, '""')}"`,
            `"${(c.address || '').replace(/"/g, '""')}"`,
            `"${c.email || ''}"`,
            `"${c.phone || ''}"`,
            `"${c.medal || ''}"`,
            `"${c.en_rutero ? 'SI' : 'NO'}"`,
            `"${(c.propuesta || '').replace(/"/g, '""')}"`,
            `"${h.status.toUpperCase()}"`,
            `"${c.cu2026 || ''}"`,
            `"${c.cu2025 || ''}"`,
            `"${c.cu2024 || ''}"`,
            `"${c.cu2023 || ''}"`,
            `"${(c.distributor || '').replace(/"/g, '""')}"`
        ];
        csv += row.join(',') + '\\n';
    });

    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `BLIZT_Cartera_Completa_${new Date().toISOString().slice(0,10)}.csv`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    showToast('📤 Excel CSV con Cajas exportado', 'success');
}

// =========================================================================
//  HELPERS & TOAST
// =========================================================================


// =========================================================================
//  EXECUTIVE DASHBOARD & VIEW SWITCHER ENGINE
// =========================================================================

let currentMainView = 'clients';

function switchMainView(viewName) {
    currentMainView = viewName;
    const btnClients = document.getElementById('btnViewClients');
    const btnDash = document.getElementById('btnViewDashboard');
    const secClients = document.getElementById('clientsViewSection');
    const secDash = document.getElementById('dashboardViewSection');
    const fabAdd = document.querySelector('.fab-add');

    if (viewName === 'dashboard') {
        if (btnClients) btnClients.classList.remove('active');
        if (btnDash) btnDash.classList.add('active');
        if (secClients) secClients.style.display = 'none';
        if (secDash) {
            secDash.style.display = 'flex';
            renderDashboard();
        }
        if (fabAdd) fabAdd.style.display = 'none';
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
        if (btnDash) btnDash.classList.remove('active');
        if (btnClients) btnClients.classList.add('active');
        if (secDash) secDash.style.display = 'none';
        if (secClients) secClients.style.display = 'block';
        if (fabAdd) fabAdd.style.display = 'flex';
    }
}

function parseNum(v) {
    if (!v && v !== 0) return 0;
    const n = parseFloat(String(v).replace(',', '.'));
    return isNaN(n) ? 0 : n;
}

function fmtNum(n) {
    return Math.round(n).toLocaleString('es-ES');
}

function renderDashboard() {
    const container = document.getElementById('dashboardViewSection');
    if (!container) return;

    let tot26 = 0, tot25 = 0, tot24 = 0, tot23 = 0;
    let countRisk = 0, countGrowth = 0, countStable = 0, countNew = 0;
    let riskBoxesLost = 0;

    const locMap = {};

    clients.forEach(c => {
        const c26 = parseNum(c.cu2026);
        const c25 = parseNum(c.cu2025);
        const c24 = parseNum(c.cu2024);
        const c23 = parseNum(c.cu2023);

        tot26 += c26;
        tot25 += c25;
        tot24 += c24;
        tot23 += c23;

        const health = getClientHealth(c);
        if (health.status === 'riesgo') {
            countRisk++;
            const maxP = Math.max(c25, c24, c23);
            const drop = maxP - (c26 > 0 ? c26 : c25);
            if (drop > 0) riskBoxesLost += drop;
        } else if (health.status === 'creciendo') {
            countGrowth++;
        } else if (health.status === 'estable') {
            countStable++;
        } else if (health.status === 'nuevo') {
            countNew++;
        }

        const city = (c.city || 'OTRA').trim().toUpperCase();
        if (!locMap[city]) locMap[city] = { count: 0, boxes: 0 };
        locMap[city].count++;
        locMap[city].boxes += (c26 > 0 ? c26 : c25);
    });

    const maxYearVal = Math.max(tot26, tot25, tot24, tot23, 1);
    const pct26 = Math.min(100, Math.round((tot26 / maxYearVal) * 100));
    const pct25 = Math.min(100, Math.round((tot25 / maxYearVal) * 100));
    const pct24 = Math.min(100, Math.round((tot24 / maxYearVal) * 100));
    const pct23 = Math.min(100, Math.round((tot23 / maxYearVal) * 100));

    // TOP 10 VIP (By current or 2025 volume)
    const sortedVIP = [...clients].sort((a, b) => {
        const vA = Math.max(parseNum(a.cu2026), parseNum(a.cu2025));
        const vB = Math.max(parseNum(b.cu2026), parseNum(b.cu2025));
        return vB - vA;
    }).slice(0, 10);

    // TOP 10 A RECUPERAR (Largest absolute box loss)
    const sortedRescue = [...clients].map(c => {
        const c26 = parseNum(c.cu2026);
        const c25 = parseNum(c.cu2025);
        const c24 = parseNum(c.cu2024);
        const c23 = parseNum(c.cu2023);
        const maxPast = Math.max(c25, c24, c23);
        const currentVal = c26 > 0 ? c26 : c25;
        const loss = maxPast - currentVal;
        const pctLoss = maxPast > 0 ? Math.round((loss / maxPast) * 100) : 0;
        return { client: c, loss, pctLoss, maxPast, currentVal };
    }).filter(x => x.loss > 30).sort((a, b) => b.loss - a.loss).slice(0, 10);

    // TOP 5 LOCALIDADES
    const sortedLocs = Object.keys(locMap).map(k => ({ city: k, ...locMap[k] })).sort((a, b) => b.boxes - a.boxes).slice(0, 6);

    const totalClientsCount = clients.length || 1;

    let html = `
        <!-- MULTI-YEAR EVOLUTION -->
        <div class="dash-multi-card">
            <div class="dash-section-title">
                <span>📈 Evolución Histórica de Cajas</span>
                <span class="badge">Multi-Año Consolidado</span>
            </div>
            <div class="year-bars-grid">
                <div class="year-bar-item y2026">
                    <div class="year-bar-label">2026 (YTD Activo)</div>
                    <div class="year-bar-value">${fmtNum(tot26)} CJ</div>
                    <div class="year-progress-track">
                        <div class="year-progress-fill" style="width:${pct26}%; background:#38bdf8;"></div>
                    </div>
                </div>
                <div class="year-bar-item">
                    <div class="year-bar-label">Año 2025</div>
                    <div class="year-bar-value">${fmtNum(tot25)} CJ</div>
                    <div class="year-progress-track">
                        <div class="year-progress-fill" style="width:${pct25}%; background:#10b981;"></div>
                    </div>
                </div>
                <div class="year-bar-item">
                    <div class="year-bar-label">Año 2024</div>
                    <div class="year-bar-value">${fmtNum(tot24)} CJ</div>
                    <div class="year-progress-track">
                        <div class="year-progress-fill" style="width:${pct24}%; background:#94a3b8;"></div>
                    </div>
                </div>
                <div class="year-bar-item">
                    <div class="year-bar-label">Año 2023</div>
                    <div class="year-bar-value">${fmtNum(tot23)} CJ</div>
                    <div class="year-progress-track">
                        <div class="year-progress-fill" style="width:${pct23}%; background:#64748b;"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- HEALTH TRAFFIC LIGHT DISTRIBUTION -->
        <div>
            <div class="dash-section-title">
                <span>🚦 Salud Global de tu Cartera</span>
                <span class="badge">Toca para filtrar clientes</span>
            </div>
            <div class="health-dist-strip">
                <div class="health-dist-card" style="border-color:rgba(239,68,68,0.4);" onclick="switchMainView('clients'); selectFilterTab('riesgo');">
                    <div class="health-dist-title" style="color:#f87171;">🔴 EN RIESGO</div>
                    <div class="health-dist-val" style="color:#ef4444;">${countRisk}</div>
                    <div class="health-dist-pct">${Math.round((countRisk/totalClientsCount)*100)}% de la cartera</div>
                    <div style="font-size:0.7rem; color:#fca5a5; margin-top:4px;">-${fmtNum(riskBoxesLost)} CJ en juego</div>
                </div>
                <div class="health-dist-card" style="border-color:rgba(16,185,129,0.4);" onclick="switchMainView('clients'); selectFilterTab('creciendo');">
                    <div class="health-dist-title" style="color:#34d399;">🟢 CRECIENDO</div>
                    <div class="health-dist-val" style="color:#10b981;">${countGrowth}</div>
                    <div class="health-dist-pct">${Math.round((countGrowth/totalClientsCount)*100)}% en positivo</div>
                </div>
                <div class="health-dist-card" style="border-color:rgba(245,158,11,0.4);" onclick="switchMainView('clients'); selectFilterTab('estables');">
                    <div class="health-dist-title" style="color:#fbbf24;">🟡 ESTABLES</div>
                    <div class="health-dist-val" style="color:#f59e0b;">${countStable}</div>
                    <div class="health-dist-pct">${Math.round((countStable/totalClientsCount)*100)}% consumo regular</div>
                </div>
                <div class="health-dist-card" style="border-color:rgba(244,63,94,0.4);" onclick="switchMainView('clients'); selectFilterTab('all');">
                    <div class="health-dist-title" style="color:#fb7185;">🆕 NUEVOS / ALTA</div>
                    <div class="health-dist-val" style="color:#f43f5e;">${countNew}</div>
                    <div class="health-dist-pct">Sin histórico previo</div>
                </div>
            </div>
        </div>

        <!-- DUAL RANKINGS: TOP 10 VIP vs TOP 10 A RECUPERAR -->
        <div class="rankings-dual-grid">
            
            <!-- TOP 10 VIP -->
            <div class="ranking-card">
                <div class="dash-section-title">
                    <span>🏆 TOP 10 Clientes VIP</span>
                    <span class="badge" style="color:#f59e0b; background:rgba(245,158,11,0.15);">Mayor Volumen</span>
                </div>
                <div class="rank-list">
                    ${sortedVIP.map((c, i) => {
                        const c26 = parseNum(c.cu2026);
                        const c25 = parseNum(c.cu2025);
                        const bestVal = c26 > 0 ? c26 : c25;
                        const badgeCls = i === 0 ? 'gold' : i === 1 ? 'silver' : i === 2 ? 'bronze' : '';
                        return `
                        <div class="rank-item" onclick="openClientDetail('${c.id}')">
                            <div class="rank-num-badge ${badgeCls}">#${i+1}</div>
                            <div class="rank-info">
                                <div class="rank-name">${esc(c.name)}</div>
                                <div class="rank-sub">
                                    <span>${esc(c.city || 'Extremadura')}</span>
                                    ${c.medal ? `<span>• 🏅 ${esc(c.medal)}</span>` : ''}
                                </div>
                            </div>
                            <div class="rank-stat-box">
                                <div class="rank-stat-main" style="color:#38bdf8;">${fmtNum(bestVal)} CJ</div>
                                <div class="rank-stat-sub">${c26 > 0 ? '2026 Activo' : '2025'}</div>
                            </div>
                        </div>`;
                    }).join('')}
                </div>
            </div>

            <!-- TOP 10 A RECUPERAR -->
            <div class="ranking-card" style="border-color:rgba(239,68,68,0.3);">
                <div class="dash-section-title">
                    <span style="color:#f87171;">🚨 TOP 10 a Rescatar</span>
                    <span class="badge" style="color:#f87171; background:rgba(239,68,68,0.15);">Mayor Pérdida de Cajas</span>
                </div>
                <div class="rank-list">
                    ${sortedRescue.map((item, i) => {
                        const c = item.client;
                        return `
                        <div class="rank-item" onclick="openClientDetail('${c.id}')">
                            <div class="rank-num-badge rescue">#${i+1}</div>
                            <div class="rank-info">
                                <div class="rank-name">${esc(c.name)}</div>
                                <div class="rank-sub">
                                    <span>${esc(c.city || 'Extremadura')}</span>
                                    <span>• Hacía ${fmtNum(item.maxPast)} CJ</span>
                                </div>
                            </div>
                            <div class="rank-stat-box">
                                <div class="rank-stat-main" style="color:#ef4444;">-${fmtNum(item.loss)} CJ</div>
                                <div class="rank-stat-sub" style="color:#fca5a5;">-${item.pctLoss}% caída</div>
                            </div>
                        </div>`;
                    }).join('')}
                </div>
            </div>

        </div>

        <!-- TOP LOCALIDADES -->
        <div class="dash-multi-card">
            <div class="dash-section-title">
                <span>📍 Principales Poblaciones por Volumen</span>
                <span class="badge">Concentración de Cartera</span>
            </div>
            <div class="year-bars-grid">
                ${sortedLocs.map(l => `
                <div class="year-bar-item" onclick="switchMainView('clients'); searchQuery='${l.city}'; document.getElementById('searchInput').value='${l.city}'; renderStream();" style="cursor:pointer;">
                    <div class="year-bar-label">${esc(l.city)}</div>
                    <div class="year-bar-value" style="font-size:1.05rem;">${fmtNum(l.boxes)} CJ</div>
                    <div style="font-size:0.72rem; color:var(--text-muted); margin-top:2px;">${l.count} clientes</div>
                </div>`).join('')}
            </div>
        </div>
    `;

    container.innerHTML = html;
}

function esc(str) {
    if (!str && str !== 0) return '';
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

let toastTimer = null;
function showToast(msg, type = 'success') {
    const box = document.getElementById('toastBox');
    if (!box) return;
    box.textContent = msg;
    box.className = 'toast-msg show ' + type;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
        box.classList.remove('show');
    }, 2800);
}
</script>

</body>
</html>"""

html_final = html_template.replace('__JSON_PAYLOAD_PLACEHOLDER__', json_payload)

target_file = r'C:/Users/Adfgd/Desktop/MIPAGINAWEB/blizt.html'
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(html_final)

with open(r'C:/Users/Adfgd/Desktop/MIPAGINAWEB/index.html', 'w', encoding='utf-8') as f:
    f.write(html_final)

print(f"blizt.html & index.html rebuilt successfully with Instant GitHub Sync ({len(html_final)} bytes)")
