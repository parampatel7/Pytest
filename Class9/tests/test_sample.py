

from unittest import mock

import pytest

from samplecode.sample import get_ip, guess_number

@pytest.mark.parametrize("_input, expected", [(3, "You WON!"), (4, "You LOST!")])
@mock.patch("samplecode.sample.roll_dice")
def test_guess_number(mock_roll_dice, _input, expected ):
    mock_roll_dice.return_value =3
    assert guess_number(3) == "You WON!"
    mock_roll_dice.assert_called_once()

@mock.patch("samplecode.sample.requests.get")
def test_get_ip(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(name="mock response",
                                               **{"status_code": 200, "json.return_value": {"origin": "0.0.0.0"}})

    assert get_ip() == "0.0.0.0"
    mock_requests_get.assert_called_once_with("https://httpbin.org/ip")