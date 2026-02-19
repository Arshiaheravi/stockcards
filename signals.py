<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>StockCards — Your next move.</title>
    <meta name="description" content="Trading signals platform. See what the pros see. No jargon. Just signals.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=IBM+Plex+Mono:wght@400;500;600&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <!-- TICKER TAPE -->
    <div class="ticker-tape">
        <div class="tradingview-widget-container">
            <div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>
            {"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"US 100"},{"proName":"BITSTAMP:BTCUSD","title":"Bitcoin"},{"description":"NVDA","proName":"NASDAQ:NVDA"},{"description":"AAPL","proName":"NASDAQ:AAPL"},{"description":"TSLA","proName":"NASDAQ:TSLA"},{"description":"META","proName":"NASDAQ:META"},{"description":"AMD","proName":"NASDAQ:AMD"}],"showSymbolLogo":false,"isTransparent":true,"displayMode":"adaptive","colorTheme":"dark","locale":"en"}
            </script>
        </div>
    </div>

    <!-- NAV -->
    <nav class="navbar">
        <div class="nav-left">
            <a href="#" class="logo" onclick="navigateTo('dashboard')">
                <span class="logo-text"><span class="brand-top">STOCK</span><span class="brand-bottom">CARDS</span></span>
            </a>
        </div>
        <div class="nav-center">
            <a href="#" class="nav-link active" data-page="dashboard">Dashboard</a>
            <a href="#" class="nav-link" data-page="learn">Learn</a>
            <a href="#" class="nav-link" data-page="news">News</a>
        </div>
        <div class="nav-right">
            <div class="xp-badge"><span class="xp-icon">⚡</span><span class="xp-count" id="xp-display">0 XP</span></div>
        </div>
    </nav>

    <!-- MAIN -->
    <main class="main-content">

        <!-- ── DASHBOARD ── -->
        <section id="page-dashboard" class="page active">
            <div class="hero">
                <div class="hero-content">
                    <h1 class="hero-title"><span class="hero-highlight">Your next move.</span></h1>
                    <p class="hero-subtitle">See what the pros see. No jargon. Just signals.</p>
                    <div class="hero-stats">
                        <div class="stat-card performance"><span class="stat-value">+96.89%</span><span class="stat-label">Verified Performance</span></div>
                    </div>
                </div>
            </div>

            <div class="dashboard-grid">
                <div class="opportunities-section">
                    <div class="section-header">
                        <div style="display:flex;align-items:center;gap:12px">
                            <h2 class="section-title">Opportunities</h2>
                            <span id="signal-count" style="color:var(--text-muted);font-size:0.7rem;font-family:var(--font-mono)"></span>
                        </div>
                        <div class="filter-pills" id="signal-filters">
                            <button class="pill active" data-filter="all">All</button>
                            <button class="pill" data-filter="BREAKOUT">Breakout</button>
                            <button class="pill" data-filter="BUY">Buy</button>
                            <button class="pill" data-filter="READY">Ready</button>
                            <button class="pill" data-filter="WATCH">Watch</button>
                            <button class="pill" data-filter="WAIT">Wait</button>
                            <button class="pill" data-filter="AVOID">Avoid</button>
                        </div>
                    </div>
                    <div class="loading-state" id="loading-signals"><div class="spinner"></div><p>Scanning 100+ stocks across the market...</p></div>
                    <div class="cards-container" id="signals-container"></div>
                </div>

                <aside class="sidebar">
                    <!-- Mood -->
                    <div class="sidebar-card mood-card">
                        <div class="card-header"><h3>Market Mood</h3><span class="mood-source" id="mood-source">Loading...</span></div>
                        <div class="mood-display"><div class="mood-value" id="mood-value">--</div><div class="mood-label" id="mood-label">Loading</div></div>
                        <div class="mood-bar"><div class="mood-fill" id="mood-fill" style="width:50%"></div></div>
                        <div class="mood-scale"><span>Extreme Fear</span><span>Extreme Greed</span></div>
                        <p class="mood-rec" id="mood-rec"></p>
                    </div>
                    <!-- Watchlist -->
                    <div class="sidebar-card">
                        <div class="card-header"><h3>My Watchlist</h3><button class="add-btn" id="add-watchlist">+</button></div>
                        <div class="watchlist-items" id="watchlist-items"></div>
                    </div>
                    <!-- Legend -->
                    <div class="sidebar-card">
                        <div class="card-header"><h3>How to Read Cards</h3></div>
                        <div class="legend-items">
                            <div class="legend-item"><span class="legend-dot gold"></span><div><span class="legend-label">Prime</span><span class="legend-desc">80+ confidence</span></div></div>
                            <div class="legend-item"><span class="legend-dot silver"></span><div><span class="legend-label">Select</span><span class="legend-desc">65-79</span></div></div>
                            <div class="legend-item"><span class="legend-dot bronze"></span><div><span class="legend-label">Standard</span><span class="legend-desc">40-64</span></div></div>
                            <div class="legend-item"><span class="legend-dot red"></span><div><span class="legend-label">Pass</span><span class="legend-desc">Below 40</span></div></div>
                        </div>
                    </div>
                </aside>
            </div>
        </section>

        <!-- ── LEARN ── -->
        <section id="page-learn" class="page">
            <div class="page-header"><h1>Learn to Invest</h1><p>From zero to investor. No fluff.</p></div>
            <div class="levels-grid" id="levels-container"></div>
        </section>

        <!-- ── NEWS ── -->
        <section id="page-news" class="page">
            <div class="page-header"><h1>Market News</h1></div>
            <div class="loading-state" id="loading-news"><div class="spinner"></div><p>Loading news...</p></div>
            <div class="news-grid" id="news-container"></div>
        </section>
    </main>

    <!-- STOCK MODAL -->
    <div class="modal-overlay" id="modal-overlay" onclick="closeModal(event)">
        <div class="modal-card prime" id="modal-card" onclick="event.stopPropagation()">
            <div class="modal-inner">
                <div class="modal-top-bar">
                    <div class="modal-top-left"><span class="tier-badge" id="modal-tier">Prime</span><span class="signal-badge breakout" id="modal-signal"><span class="signal-dot"></span><span id="modal-signal-text">Breakout</span></span></div>
                    <button class="close-btn" onclick="closeModal(event)">&times;</button>
                </div>
                <div class="modal-header"><div class="modal-ticker" id="modal-ticker">NVDA</div><div class="modal-company" id="modal-company">NVIDIA</div></div>
                <div class="modal-blurb"><p id="modal-explanation">Loading...</p></div>
                <div class="info-grid">
                    <div class="info-section">
                        <div class="info-section-title">Technicals</div>
                        <div class="info-row"><span class="info-label">RSI</span><span class="info-value" id="modal-rsi">--</span></div>
                        <div class="info-row"><span class="info-label">Rel. Strength</span><span class="info-value" id="modal-rs">--</span></div>
                        <div class="info-row"><span class="info-label">Uptrend</span><span class="info-value" id="modal-uptrend">--</span></div>
                    </div>
                    <div class="info-section">
                        <div class="info-section-title">Pattern</div>
                        <div class="info-row"><span class="info-label">Flag</span><span class="info-value" id="modal-flag">--</span></div>
                        <div class="info-row"><span class="info-label">Pole Move</span><span class="info-value" id="modal-pole">--</span></div>
                        <div class="info-row"><span class="info-label">Flag Range</span><span class="info-value" id="modal-range">--</span></div>
                    </div>
                </div>
                <div class="modal-chart-wrap"><iframe id="modal-chart" scrolling="no" allowtransparency="true" frameborder="0" src=""></iframe></div>
                <div class="modal-footer">
                    <div class="modal-stats">
                        <div class="modal-stat"><div class="modal-stat-label">ATH</div><div class="modal-stat-value" id="modal-ath">--</div></div>
                        <div class="modal-stat"><div class="modal-stat-label">Stop</div><div class="modal-stat-value" id="modal-stop">--</div></div>
                        <div class="modal-stat"><div class="modal-stat-label">Volume</div><div class="modal-stat-value" id="modal-vol">--</div></div>
                        <div class="modal-stat"><div class="modal-stat-label">Risk</div><div class="modal-stat-value" id="modal-risk">--</div></div>
                    </div>
                    <div class="modal-rating"><div class="modal-rating-bar"><div class="rating-fill" id="modal-rating-bar"></div></div><div class="modal-rating-value" id="modal-rating">--</div></div>
                </div>
            </div>
        </div>
    </div>

    <!-- CHAT -->
    <div class="chat-fab" id="chat-fab" onclick="toggleChat()">💬</div>
    <div class="chat-panel" id="chat-panel">
        <div class="chat-header">
            <div><span class="chat-name">Stock</span><span class="chat-status">Online</span></div>
            <button class="chat-close" onclick="toggleChat()">&times;</button>
        </div>
        <div class="chat-messages" id="chat-messages">
            <div class="chat-msg assistant"><p>Hey! I'm Stock, your investing sidekick. Ask me anything about signals, indicators, or how the market works.</p></div>
        </div>
        <div class="chat-input-wrap">
            <input type="text" id="chat-input" placeholder="Ask Stock anything..." autocomplete="off">
            <button id="chat-send" onclick="sendChat()">→</button>
        </div>
    </div>

    <!-- FOOTER -->
    <footer class="site-footer">
        <p class="disclaimer"><strong>Disclaimer:</strong> StockCards is for educational purposes only. This is not financial advice. Past performance does not guarantee future results. Trading involves risk of loss.</p>
        <span class="copyright">&copy; 2025 StockCards. All rights reserved.</span>
    </footer>

    <script src="app.js"></script>
</body>
</html>
