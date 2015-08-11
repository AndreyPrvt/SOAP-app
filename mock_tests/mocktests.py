from mock import patch
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer



def test_Dispatcher():
        global dispatcher
        dispatcher = SoapDispatcher(
                    'my_dispatcher',
                    location="http://localhost:8008/",
                    action='http://localhost:8008/', # SOAPAction
                    namespace="http://example.com/sample.wsdl", prefix="ns0",
                    trace=True,
                    ns=True)

@patch("operations.create")
def test_create(mock_create):
    mock_create.return_value = "New user created"
    dispatcher.register_function('Create', mock_create, returns={'Node': str}, args={'name': str, 'surname': str})

@patch("operations.read")
def test_read(mock_read):
    mock_read.return_value = "read by id"
    dispatcher.register_function('Read', mock_read, returns={'Node': str}, args={'st_id': int})

@patch("operations.update")
def test_update(mock_update):
    mock_update.return_value = "New user updated"
    dispatcher.register_function('Update', mock_update, returns={'Node': str}, args={'st_id': int, 'name': str, 'surname': str})

@patch("operations.delete")
def test_delete(mock_delete):
    mock_delete.return_value = "New user deleted"
    dispatcher.register_function('Delete', mock_delete, returns={'Node': str}, args={'st_id': int})

@patch("operations.read_all")
def test_read_all(mock_read_all):
    mock_read_all.return_value = "read all"
    dispatcher.register_function('Read_all', mock_read_all, returns={'Node': str}, args={})


def test_server_run():
    print "Starting server..."
    httpd = HTTPServer(("", 8008), SOAPHandler)
    httpd.dispatcher = dispatcher
    httpd.serve_forever()


test_Dispatcher()
test_create()
test_read()
test_update()
test_delete()
test_read_all()
test_server_run()