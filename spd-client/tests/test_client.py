from pathlib import Path
import pytest
import httpx
from client import SPDClient


HOST='localhost'
PORT=6800
USERNAME='admin'
PASSWORD='admin'
TEST_PROJECT='newsfeed'
TEST_VERSION='1662058573'
TEST_SPIDER='defensefeed'

CREATE_PROJECT='test'
CREATE_VERSION='0.0.1'
TEST_EGG_PATH=Path(__file__).parent.joinpath('eggs','newsfeed.egg').resolve()
CREATE_JOB_ID='test_job'
SPIDER_ARGS={
    'feedurls':'https://bulgarianmilitary.com/category/military-conflicts/feed|https://bulgarianmilitary.com/category/military-and-defence-systems/global-air-systems/feed'
}
SPIDER_SETTINGS={
    'DOWNLOAD_DELAY': 5,
}


@pytest.fixture
def create_client():
    client = SPDClient(HOST,PORT,USERNAME,PASSWORD)
    if client.daemon_status()['status'] == 'ok':
        return client
    else:
        raise Exception('Scrapyd Server is not running')


def test_add_version_no_version(create_client):
    response = create_client.add_version(project=CREATE_PROJECT,egg=TEST_EGG_PATH)
    assert response['status'] == 'ok'

def test_add_version_with_version(create_client):
    response = create_client.add_version(project=CREATE_PROJECT,version=CREATE_VERSION,egg=TEST_EGG_PATH)
    assert response['status'] == 'ok'

def test_daemon_status(create_client):
    response=create_client.daemon_status()
    assert response['status'] == 'ok'

def test_list_projects(create_client):
    response = create_client.list_projects()
    assert response['status'] == 'ok'

def test_list_spiders(create_client):
    response = create_client.list_spiders(project=TEST_PROJECT)
    assert response['status'] == 'ok'

def test_list_spiders_version(create_client):
    response = create_client.list_spiders(project=TEST_PROJECT,version=TEST_VERSION)
    assert response['status'] == 'ok'

def test_list_versions(create_client):
    response = create_client.list_versions(project=TEST_PROJECT)
    assert response['status'] == 'ok'

def test_schedule(create_client):
    response = create_client.schedule(project=TEST_PROJECT,spider=TEST_SPIDER)
    assert response['status'] == 'ok'

def test_schedule_args(create_client):
    response = create_client.schedule(project=TEST_PROJECT,spider=TEST_SPIDER,spider_args=SPIDER_ARGS)
    assert response['status'] == 'ok'

def test_schedule_settings(create_client):
    response = create_client.schedule(project=TEST_PROJECT,spider=TEST_SPIDER,setting=SPIDER_SETTINGS)
    assert response['status'] == 'ok'

def test_schedule_all(create_client):
    response = create_client.schedule(project=TEST_PROJECT,jobid=CREATE_JOB_ID,priority=10,version=CREATE_VERSION,spider=TEST_SPIDER,spider_args=SPIDER_ARGS,setting=SPIDER_SETTINGS)
    assert response['status'] == 'ok'

def test_cancel(create_client):
    response = create_client.cancel(project=TEST_PROJECT,job='test_job')
    assert response['status'] == 'ok'

def test_delversion(create_client):
    response = create_client.delversion(project=CREATE_PROJECT,version=CREATE_VERSION)
    assert response['status'] == 'ok'

def test_delproject(create_client):
    response = create_client.delproject(project=CREATE_PROJECT)
    assert response['status'] == 'ok'






    