from decimal import Decimal
from src.payments.rounding import quantize_minor_units


def test_usd_two_decimal_rounding() -> None:
    assert quantize_minor_units(Decimal("19.995"), "USD") == Decimal("20.00")


def test_kwd_three_decimal_rounding() -> None:
    assert quantize_minor_units(Decimal("4.1254"), "KWD") == Decimal("4.125")


def test_jpy_zero_decimal_rounding() -> None:
    assert quantize_minor_units(Decimal("1250.6"), "JPY") == Decimal("1251")