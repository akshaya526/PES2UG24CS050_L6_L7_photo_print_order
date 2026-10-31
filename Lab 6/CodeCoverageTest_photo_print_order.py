
import pytest
from photo_print_order import (
    extra_print_charge,
    order_valid,
    dispatch_status
)


# EXTRA PRINT CHARGE TESTS

def test_within_included_prints():
    assert extra_print_charge("4x6", 15, "matte", False) == 0


def test_member_extra_prints():
    assert extra_print_charge("4x6", 30, "matte", True) == 20


def test_non_member_extra_prints():
    assert extra_print_charge("5x7", 20, "glossy", False) == 35


def test_eight_by_ten_prints():
    assert extra_print_charge("8x10", 15, "matte", True) == 20


def test_large_canvas_order():
    assert extra_print_charge("4x6", 80, "canvas", False) == 840


def test_large_glossy_order():
    assert extra_print_charge("4x6", 80, "glossy", False) == 540


def test_unknown_print_size():
    with pytest.raises(ValueError):
        extra_print_charge("10x12", 10, "matte", False)


def test_negative_copies():
    with pytest.raises(ValueError):
        extra_print_charge("4x6", -1, "matte", False)


# ORDER VALIDATION TESTS

def test_rush_order_valid():
    assert order_valid(30, 50, True) is True


def test_rush_order_invalid():
    assert order_valid(10, 51, True) is False


def test_large_file_invalid():
    assert order_valid(30, 100, False) is False


def test_normal_order_valid():
    assert order_valid(10, 500, False) is True


def test_normal_order_too_many_copies():
    assert order_valid(10, 501, False) is False


# DISPATCH STATUS TESTS

def test_framed_domestic_on_time():
    assert dispatch_status(24, True, False) == "on_time"


def test_unframed_international_tight():
    assert dispatch_status(30, False, True) == "tight"


def test_framed_international_missed():
    assert dispatch_status(30, True, True) == "missed"
