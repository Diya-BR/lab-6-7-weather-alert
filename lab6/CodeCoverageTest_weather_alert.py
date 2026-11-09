import pytest
from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert


# Wind alert tests
def test_wind_warning():
    assert wind_alert(90) == "warning"


def test_wind_watch():
    assert wind_alert(70) == "watch"


def test_wind_advisory():
    assert wind_alert(40) == "advisory"


def test_wind_none():
    assert wind_alert(10) == "none"


# Rain alert tests
def test_rain_warning():
    assert rain_alert(50, True) == "warning"


def test_rain_watch_high_rain():
    assert rain_alert(50, False) == "watch"


def test_rain_watch_saturated_soil():
    assert rain_alert(10, True) == "watch"


def test_rain_advisory():
    assert rain_alert(10, False) == "advisory"


def test_rain_none():
    assert rain_alert(5, False) == "none"


# Heat alert tests
def test_heat_warning():
    assert heat_alert(45, 40) == "warning"


def test_heat_watch():
    assert heat_alert(40, 50) == "watch"


def test_heat_advisory():
    assert heat_alert(35, 40) == "advisory"


def test_heat_none():
    assert heat_alert(20, 40) == "none"


# Overall alert tests
def test_overall_alert_highest_severity():
    assert overall_alert(["warning", "advisory"]) == "warning"


def test_overall_alert_invalid():
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["invalid"])
