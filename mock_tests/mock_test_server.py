from pysimplesoap.client import SoapClient
import unittest


class TestLab3(unittest.TestCase):
    def test_client(self):
        global client
        client = SoapClient(
            location="http://localhost:8008/",
            action='http://localhost:8008/', # SOAPAction
            namespace="http://example.com/sample.wsdl",
            soap_ns='soap',
            trace=True,
            ns=False)

    def test_client_create(self):
        response = client.Create(name='name', surname='surname')
        print response.Node
        self.assertEqual("New user created", str(response.Node))

    def test_client_update(self):
        response = client.Update(st_id=1, name='name', surname='surname')
        print response.Node
        self.assertEqual("New user updated", str(response.Node))

    def test_client_deleted(self):
        response = client.Delete(st_id=1)
        print response.Node
        self.assertEqual("New user deleted", str(response.Node))

    def test_client_read_all(self):
        response = client.Read_all()
        print response.Node
        self.assertEqual(str(response.Node), "read all")

    def test_client_read(self):
        response = client.Read(st_id=1)
        print response.Node
        self.assertEqual(str(response.Node), "read by id")