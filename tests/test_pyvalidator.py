from src.DH_PyValidator import Validator


# 비빌번호 검증기능 테스트
def test_validate_password():
    assert Validator.validate_password("123123") == False
    assert Validator.validate_password("ASDASDASD") == False
    assert Validator.validate_password("Aa123ddf!!") == True