from pytest_lesson.web_client import SomeResourceClient
import responses
import pytest

@responses.activate
def test_some_web_client():
    valid_answer = {
        'status': 'too-many-requests',
        'result': {
            'message': 'Доступ с вашего IP-адреса временно ограничен',
            'link': 'ru.avito://1/firewall/captcha/show'
        }
    }
    responses.add(method=responses.GET, url="https://www.avito.ru/web/user/get-status/177041581",
                  json=valid_answer, status=200)
    src = SomeResourceClient(url="https://www.avito.ru")
    result = src.get_information("177041581")
    assert result['status'] == 'too-many-requests'
    pass


def test_some_web_client_error():
    valid_answer = {
        "errors": [
            "Not found"
        ]
    }

    responses.add(method=responses.GET, url="https://www.avito.ru/web/user/get-status/177041581--",
                  json=valid_answer, status=404)

    with pytest.raises(KeyError):
        src = SomeResourceClient(url="https://www.avito.ru")
        result = src.get_information("177041581--")