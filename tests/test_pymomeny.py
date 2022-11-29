from src.DH_PyMoment import *
from src.DH_PyLogger import Log

# 현재 datetime 가져오는 기능 테스트
def test_get_now():
    Log.d(D.get_now(), D.get_now(format="%Y-%m-%d %H:%M"), D.get_now(format="%Y-%m-%d"))

# 연도 계산해서 가져오는 기능 테스트
def test_get_year():
    assert type(D.get_year()) == int
    assert D.get_year() in [x for x in range(1990, 2200)]

# 월 계산해서 가져오는 기능 테스트
def test_get_month():
    assert type(D.get_month()) == int
    assert D.get_month() in [x for x in range(1, 13)]

# 일 계산해서 가져오는 기능 테스트
def test_get_day():
    assert type(D.get_day()) == int
    assert D.get_day() in [x for x in range(1, 32)]

# 초 -> 시간 환산기능 테스트
def test_convert_sec_to_datetime():
    assert D.conv_sec_to_datetime(sec=60) == "1분"