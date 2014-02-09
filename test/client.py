import unittest
import os
from cartodb_dashboard import CartoDbDashboard


class CartoDbDashboardTest(object):
    def test_session_headers(self):
        result = self.client.request_session_headers
        self.assertIn('Cookie', result)

    def test_import_shapefile(self):
        result, table = self.client.import_data('test/testdata/localities.zip')
        self.assertTrue(result)

    def test_import_csv(self):
        result, table = self.client.import_data('test/testdata/schools.csv')
        self.assertTrue(result)

    def test_import_csv_update_column(self):
        result, table = self.client.import_data('test/testdata/schools.csv')
        self.assertTrue(result)
        self.assertTrue(self.client.convert_data_type("POINT_PID", "number", table))


class CartoDbDashboardTestClient(CartoDbDashboardTest, unittest.TestCase):
    def setUp(self):
        cartodb_domain = os.environ['CARTDOB_DOMAIN']
        cartodb_host = os.environ['CARTODB_HOST']
        cartodb_protocol = os.environ['CARTODB_PROTOCOL']
        cartodb_version = os.environ['CARTODB_VERSION']
        cartodb_user = os.environ['CARTODB_USER']
        cartodb_password = os.environ['CARTODB_PWD']

        self.client = CartoDbDashboard(cartodb_domain, cartodb_user, cartodb_password, cartodb_host, cartodb_protocol,
                                       cartodb_version)

if __name__ == '__main__':
    unittest.main()
