import pytest
from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert


# Wind alert: test True and False outcomes of every condition
def test_wind_all_branches():
    assert wind_alert(90) == "warning"
    assert wind_alert(70) == "watch"
    assert wind_alert(40) == "advisory"
    assert wind_alert(10) == "none"


# Rain alert: test rainfall thresholds and both soil conditions
def test_rain_all_branches():
    assert rain_alert(50, True) == "warning"
    assert rain_alert(50, False) == "watch"
    assert rain_alert(10, True) == "watch"
    assert rain_alert(10, False) == "advisory"
    assert rain_alert(5, False) == "none"


# Heat alert: test humidity condition and all index thresholds
def test_heat_all_branches():
    assert heat_alert(45, 40) == "warning"
    assert heat_alert(40, 50) == "watch"
    assert heat_alert(35, 40) == "advisory"
    assert heat_alert(20, 40) == "none"


# Overall alert: test loop, severity comparison and valid alerts
def test_overall_alert_all_branches():
    assert overall_alert([]) == "none"
    assert overall_alert(["advisory", "warning", "none"]) == "warning"


# Test invalid alert branch
def test_overall_alert_invalid_branch():
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["invalid"])
