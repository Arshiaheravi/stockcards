"""
Signal generation and scoring engine.

This is the brain of StockCards. It takes raw technical data and
produces a trading signal with a confidence score.

DESIGN: Score-based, not gate-based.
    Every criterion adds points. The total score determines the signal.
    No single missing criterion kills a good setup.

SIGNAL HIERARCHY (by score):
    BREAKOUT  85+   All stars aligned + volume confirmation
    BUY/READY 65-84 Strong setup, waiting for breakout trigger
    WATCH     45-64 Interesting — some criteria met, keep monitoring
    WAIT      25-44 Not ready, needs more development
    AVOID     <25   Actively bad — downtrend, overextended, lagging
"""

from dataclasses import dataclass


@dataclass
class SignalResult:
    """Output of the signal engine."""

    signal: str
    confidence: int
    summary: str
    explanation: str
    risk: str
    potential: str
    timeframe: str


def generate_signal(
    rsi: float,
    has_flag: bool,
    uptrend: bool,
    near_ath: bool,
    pole_move: float,
    flag_range: float,
    relative_strength: float = 1.0,
    volume_surge: bool = False,
) -> tuple[str, int]:
    """Score technical criteria and produce a signal.

    Additive scoring — every positive adds, every negative subtracts.
    Total determines signal. No single gate kills a setup.
    """
    score = 0

    # --- Trend (most important) ---
    if uptrend:
        score += 20
    else:
        score -= 5  # Small penalty, not death

    # --- Proximity to ATH ---
    if near_ath:
        score += 15

    # --- Pattern ---
    if has_flag:
        score += 20
        if flag_range < 10:
            score += 5  # Tight flag bonus

    # --- RSI zones ---
    if 45 <= rsi <= 55:
        score += 15  # Sweet spot
    elif 55 < rsi <= 60:
        score += 10
    elif 60 < rsi <= 65:
        score += 5
    elif rsi > 70:
        score -= 15  # Overbought

    # --- Pole strength ---
    if pole_move >= 20:
        score += 5

    # --- Relative Strength ---
    if relative_strength >= 1.3:
        score += 15  # Strong leader
    elif relative_strength >= 1.1:
        score += 10
    elif relative_strength >= 1.0:
        score += 5
    elif relative_strength < 0.8:
        score -= 10  # Weak laggard

    # --- Volume ---
    if volume_surge:
        score += 10

    # --- Map score to signal ---
    if score >= 85 and has_flag and volume_surge and uptrend:
        signal = "BREAKOUT"
    elif score >= 65:
        signal = "READY"
    elif score >= 45:
        signal = "WATCH"
    elif score >= 25:
        signal = "WAIT"
    else:
        signal = "AVOID"

    # BUY = READY + flag + uptrend (a more specific call)
    if signal == "READY" and has_flag and uptrend:
        signal = "BUY"

    confidence = max(15, min(95, score))
    return signal, confidence


def get_signal_details(
    signal: str,
    rsi: float,
    flag_range: float,
    pole_move: float,
    relative_strength: float = 1.0,
    volume_surge: bool = False,
) -> SignalResult:
    """Generate human-readable explanation for a signal."""
    strengths = []
    weaknesses = []

    if relative_strength >= 1.1:
        strengths.append(f"Outperforming S&P500 by {int((relative_strength - 1) * 100)}%")
    elif relative_strength < 0.9:
        weaknesses.append("Underperforming the market")

    if volume_surge:
        strengths.append("High volume — institutions buying")
    if rsi > 70:
        weaknesses.append("Overbought (RSI > 70)")
    elif rsi > 65:
        weaknesses.append("RSI getting elevated")
    if flag_range > 20:
        weaknesses.append("Consolidation too wide")

    strength_text = ". ".join(strengths) + ". " if strengths else ""
    weakness_text = ". ".join(weaknesses) + ". " if weaknesses else ""

    templates = {
        "BREAKOUT": SignalResult(
            signal="BREAKOUT", confidence=0,
            summary="Flag breaking out with volume!",
            explanation=f"{strength_text}This is the moment we wait for! The stock consolidated nicely and is now pushing higher with conviction.",
            risk="Low", potential="18-25%", timeframe="2-3 weeks",
        ),
        "BUY": SignalResult(
            signal="BUY", confidence=0,
            summary="Strong setup with flag pattern forming",
            explanation=f"{strength_text}The stock is in a healthy uptrend and building a nice base. Good risk/reward entry.",
            risk="Medium-Low", potential="12-18%", timeframe="2-4 weeks",
        ),
        "READY": SignalResult(
            signal="READY", confidence=0,
            summary="Strong setup — approaching buy zone",
            explanation=f"{strength_text}Multiple criteria are lining up. Watch for a flag pattern or volume confirmation to trigger entry.",
            risk="Medium", potential="12-18%", timeframe="2-4 weeks",
        ),
        "WATCH": SignalResult(
            signal="WATCH", confidence=0,
            summary="On the radar — developing setup",
            explanation=f"{strength_text}{weakness_text}Some pieces are in place but needs more confirmation. Keep it on your watchlist.",
            risk="Medium-High", potential="10-15%", timeframe="4-6 weeks",
        ),
        "WAIT": SignalResult(
            signal="WAIT", confidence=0,
            summary="Not ready yet — patience pays",
            explanation=f"{weakness_text}Most criteria aren't met. Better opportunities elsewhere right now.",
            risk="High", potential="5-10%", timeframe="Uncertain",
        ),
        "AVOID": SignalResult(
            signal="AVOID", confidence=0,
            summary="Risk too high — skip this one",
            explanation=f"{weakness_text}{'Moved too far too fast. ' if pole_move > 40 else ''}High pullback risk. Wait for a better setup.",
            risk="Very High", potential="Uncertain", timeframe="Uncertain",
        ),
    }

    return templates.get(signal, SignalResult(
        signal=signal, confidence=0, summary="Analyzing...",
        explanation="Analysis in progress", risk="Medium",
        potential="10-15%", timeframe="2-4 weeks",
    ))
