
import pytest
from photo_print_order import (
    extra_print_charge,
    order_valid,
    dispatch_status
)


# EXTRA PRINT CHARGE

def test_invalid_size():
    with pytest.raises(ValueError):
        extra_print_charge("10x12", 10, "matte", False)


def test_negative_copies():
    with pytest.raises(ValueError):
        extra_print_charge("4x6", -1, "matte", False)


def test_member_discount():
    assert extra_print_charge("4x6", 30, "matte", True) == 20


def test_non_member_no_discount():
    assert extra_print_charge("4x6", 30, "matte", False) == 40


def test_eight_by_ten_member():
    assert extra_print_charge("8x10", 20, "matte", True) == 40


def test_no_extra_charge():
    assert extra_print_charge("4x6", 20, "matte", False) == 0


def test_matte_finish():
    assert extra_print_charge("4x6", 21, "matte", False) == 4


def test_glossy_finish():
    assert extra_print_charge("4x6", 21, "glossy", False) == 7


def test_large_glossy_order():
    assert extra_print_charge("4x6", 80, "glossy", False) == 540


def test_large_canvas_order():
    assert extra_print_charge("4x6", 80, "canvas", False) == 840


# ORDER VALIDATION

def test_rush_valid():
    assert order_valid(10, 50, True) is True


def test_rush_invalid():
    assert order_valid(10, 51, True) is False


def test_file_size_exceeded():
    assert order_valid(26, 100, False) is False


def test_file_size_allowed():
    assert order_valid(25, 100, False) is True


def test_normal_order_valid():
    assert order_valid(10, 500, False) is True


def test_normal_order_invalid():
    assert order_valid(10, 501, False) is False


# DISPATCH STATUS

def test_framed_domestic_on_time():
    assert dispatch_status(24, True, False) == "on_time"


def test_unframed_international_tight():
    assert dispatch_status(30, False, True) == "tight"


def test_framed_international_missed():
    assert dispatch_status(30, True, True) == "missed"


def test_unframed_domestic_on_time():
    assert dispatch_status(12, False, False) == "on_time"
