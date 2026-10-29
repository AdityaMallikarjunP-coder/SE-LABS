
import pytest
from airline_baggage import baggage_fee, carry_on_ok, check_in_status


# Baggage fee tests

def test_within_allowance():
    assert baggage_fee("economy", 10, "domestic", False) == 0


def test_unknown_cabin():
    with pytest.raises(ValueError, match="unknown cabin"):
        baggage_fee("first", 20, "domestic", False)


def test_negative_weight():
    with pytest.raises(ValueError, match="invalid weight"):
        baggage_fee("economy", -1, "domestic", False)


def test_member_allowance():
    assert baggage_fee("economy", 20, "domestic", True) == 0


def test_business_member():
    assert baggage_fee("business", 45, "domestic", True) == 100


def test_domestic_fee():
    assert baggage_fee("economy", 20, "domestic", False) == 100


def test_international_fee():
    assert baggage_fee("economy", 20, "international", False) == 225


def test_excess_over_20():
    assert baggage_fee("economy", 36, "domestic", False) == 840


def test_international_excess_over_20():
    assert baggage_fee("economy", 36, "international", False) == 2100

def test_premium_allowance():
    assert baggage_fee("premium", 25, "domestic", False) == 0


# Carry-on tests

def test_infant_allowed():
    assert carry_on_ok(10, 2, True) is True


def test_infant_too_many_items():
    assert carry_on_ok(10, 3, True) is False


def test_weight_over_limit():
    assert carry_on_ok(8, 1, False) is False


def test_one_item_allowed():
    assert carry_on_ok(7, 1, False) is True


def test_too_many_items():
    assert carry_on_ok(5, 2, False) is False


# Check-in status tests

def test_checkin_open():
    assert check_in_status(60, True, False) == "open"


def test_checkin_late():
    assert check_in_status(50, True, False) == "late"


def test_checkin_closed():
    assert check_in_status(40, True, False) == "closed"


def test_international_open():
    assert check_in_status(120, False, True) == "open"


def test_international_closed():
    assert check_in_status(80, False, True) == "closed"


def test_no_baggage_open():
    assert check_in_status(45, False, False) == "open"

