import random

async def get_io_report():
    return (
        "📊 IO Raporu\n"
        f"Market Hacmi: {round(random.uniform(100,300),2)}B$\n"
        f"Kısa Vadeli Alım Gücü: {round(random.uniform(0.3,0.8),2)}X"
    )

async def get_nls_signal(pattern: str):
    return f"🔔 NLS Sinyali | Pattern: {pattern or 'GENEL'} | RSI:{round(random.uniform(20,70),2)}"

async def get_npr_signal(coin: str):
    return (
        f"📈 NPR {coin}\n"
        f"15m:{round(random.uniform(40,60),2)}% | 1h:{round(random.uniform(45,65),2)}%"
    )
