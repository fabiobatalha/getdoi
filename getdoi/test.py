import unittest
from urllib2 import HTTPError, URLError
from lxml.etree import XMLSyntaxError
from getdoi import Doi
import datasample


class MainTests(unittest.TestCase):
    """
        Testing all doi tasks
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_query_doi_invalid_wrong_api_url(self):
        """
        Testing the query_doi method using an invalid URL
        """
        doi = Doi(query_email='http://wrongurl.crossref.org/servlet/query')
        self.assertRaises(URLError,
                          lambda: doi.query_doi(xml=datasample.doc_without_doi))

    def test_query_doi_invalid_query_email(self):
        """
        Testing the query_doi method using an invalid query e-mail
        """
        doi = Doi(query_email='invalid@email.com')
        self.assertRaises(HTTPError,
                          lambda: doi.query_doi(xml=datasample.doc_without_doi))

    def test_query_doi_unparsed_xml(self):
        """
        Querying crossfer for a DOI number with an unparsed xml
        """
        doi = Doi()
        self.assertRaises(XMLSyntaxError,
                          lambda: doi.query_doi(xml=datasample.wrong_query_xml))

    def test_query_doi_invalid_xml(self):
        """
        Querying crossfer for a DOI number with invalid xml validated against schema
        """
        doi = Doi()
        query_doi = doi.query_doi(xml=datasample.invalid_query_xml)
        self.assertEqual(query_doi, False)

    def test_query_doi_false(self):
        """
        Querying crossfer for a DOI number accoding to a document metadata that
        does not have a DOI number registed
        """
        doi = Doi()
        query_doi = doi.query_doi(xml=datasample.doc_without_doi)
        self.assertEqual(query_doi, False)

    def test_query_doi_true(self):
        """
        Querying crossfer for a DOI number accoding to a document metadata that
        already have a DOI number registered
        """
        doi = Doi()
        query_doi = doi.query_doi(xml=datasample.doc_with_doi)
        self.assertEqual(query_doi, "10.1590/S2179-975X2012005000002")

    def test_query_doi_is_resolved_wrong_api_url(self):
        """
        Testing the is_resolved method using an invalid url
        """
        doi = Doi(crossref_api_url='http://wrongurl.crossref.org/servlet/query')
        self.assertRaises(URLError,
                          lambda: doi.is_resolved("10.1590/S2179-975X2012005000002"))

    def test_query_doi_is_resolved_query_email(self):
        """
        Testing the is_resolved method using an invalid email
        """
        doi = Doi(query_email='invalid@email.com')
        self.assertRaises(HTTPError,
                          lambda: doi.is_resolved("10.1590/S2179-975X2012005000002"))

    def test_doi_is_resolved_resolved(self):
        """
        Querying crossfer using a registered DOI number
        """
        doi = Doi()
        is_resolved = doi.is_resolved("10.1590/S2179-975X2012005000002")
        self.assertEqual(is_resolved, True)

    def test_doi_is_resolved_unresolved(self):
        """
        Querying crossfer using a unregistered DOI number
        """
        doi = Doi()
        is_resolved = doi.is_resolved("10.1590/S2179-975X20120050XXXXX")
        self.assertEqual(is_resolved, False)

    @unittest.expectedFailure
    def test_doi_request_unparsed_xml(self):
        self.assertEqual(1, 0, "broken")

    @unittest.expectedFailure
    def test_doi_request_invalid_xml(self):
        self.assertEqual(1, 0, "broken")

    @unittest.expectedFailure
    def test_doi_request_valid_xml(self):
        self.assertEqual(1, 0, "broken")

    @unittest.expectedFailure
    def test_doi_update(self):
        self.assertEqual(1, 0, "broken")

if __name__ == '__main__':
    unittest.main()
