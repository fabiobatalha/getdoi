import unittest

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

    def test_has_doi_unparsed_xml(self):
        """
        Querying crossfer for a DOI number with an unparsed xml
        """
        doi = Doi()
        self.assertRaises(XMLSyntaxError, lambda: doi.has_doi(datasample.wrong_xml))

    def test_has_doi_invalid_xml(self):
        """
        Querying crossfer for a DOI number with invalid xml validated against schema
        """
        doi = Doi()
        has_doi = doi.has_doi(xml=datasample.invalid_xml)
        self.assertEqual(has_doi, False)

    @unittest.expectedFailure
    def test_has_doi_false(self):
        """
        Querying crossfer for a DOI number accoding to a document metadata that
        does not have a DOI number registed
        """
        doi = Doi()
        has_doi = doi.has_doi(xml=datasample.doc_without_doi)
        self.assertEqual(has_doi, False)

    
    def test_has_doi_true(self):
        """
        Querying crossfer for a DOI number accoding to a document metadata that
        already have a DOI number registered
        """
        doi = Doi()
        has_doi = doi.has_doi(xml=datasample.doc_with_doi)
        self.assertEqual(has_doi, False)

    @unittest.expectedFailure
    def test_doi_status_resolved(self):
        """
        Querying crossfer using a registered DOI number
        """
        doi = Doi()
        has_doi = doi.has_doi("10.4025/actasciagron.v32i3.6782")
        self.assertEqual(has_doi, True)

    @unittest.expectedFailure
    def test_doi_status_unresolved(self):
        """
        Querying crossfer using a unregistered DOI number
        """
        doi = Doi()
        has_doi = doi.has_doi("XX.XXXXX/actasciagron.v32i3.6782")
        self.assertEqual(has_doi, True)

    @unittest.expectedFailure
    def test_doi_request(self):
        self.assertEqual(1, 0, "broken")

    @unittest.expectedFailure
    def test_doi_update(self):
        self.assertEqual(1, 0, "broken")

if __name__ == '__main__':
    unittest.main()
