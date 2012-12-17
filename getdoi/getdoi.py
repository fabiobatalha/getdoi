import urllib2
from BeautifulSoup import BeautifulSoup
from porteira.porteira import Schema

from settings import *


class Doi(object):

    def __init__(self):
        xsd = open('../xsd/crossref_query_input2.0.xsd').read()
        self.porteira = Schema(xsd)

    def query_doi(self, xml):
        """
        Returns a DOI number according to metadata contained into a given valid XML.
        The XML must be compatible with crossref_query_input2.0.xsd
        This method will return 'False' or a 'DOI number'.
        """

        if self.porteira.validate(xml):
            request_url = "{0}?format=xsd_xml&pid={1}&qdata={2}".format(
                                                                        CROSSREF_API_URL,
                                                                        QUERY_EMAIL,
                                                                        urllib2.quote(xml))
            query_result = urllib2.urlopen(request_url).read()
            dec = BeautifulSoup(query_result)
            try:
                return dec.query_result.doi.string
            except AttributeError:
                return False
        else:
            return False

    def is_resolved(self, doi):
        """
        Returns True or False for a given DOI number
        """
        request_url = "{0}?format=xsd_xml&pid={1}&id={2}".format(
                                                                CROSSREF_API_URL,
                                                                QUERY_EMAIL,
                                                                doi)

        query_result = urllib2.urlopen(request_url).read()
        dec = BeautifulSoup(query_result)
        if dec.query_result.query['status'] == 'resolved':
            return True
        else:
            return False

    def doi_request(self, user, passwd, xml):
        pass

    def doi_update(self, user, passwd, xml):
        pass
