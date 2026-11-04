from decimal import Decimal, ROUND_HALF_UP

ZERO_DECIMAL_CURRENCIES = frozenset({"JPY", "KRW", "VND"})
THREE_DECIMAL_CURRENCIES = frozenset({"KWD", "BHD", "OMR"})


def quantize_minor_units(amount: Decimal, currency: str) -> Decimal:
    code = currency.upper().strip()
    if code in THREE_DECIMAL_CURRENCIES:
        exponent = Decimal("0.001")
    else:
        # Bug: hardcoded 2-decimal exponent breaks zero-decimal currencies like JPY
        exponent = Decimal("0.01")
    return amount.quantize(exponent, rounding=ROUND_HALF_UP)