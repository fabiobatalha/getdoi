import urllib2
import base64
from lxml.etree import XMLSyntaxError
from porteira.porteira import Schema


class Doi(object):

    def __init__(self):
        xsd = open('../xsd/crossref_query_input2.0.xsd').read()
        self.porteira = Schema(xsd)

    def has_doi(self, xml):
        if self.porteira.validate(xml):
            import pdb; pdb.set_trace()
            request_url = "http://doi.crossref.org/servlet/query?format=xsd_xml&pid=bireme:bireme303&qdata={0}".format(urllib2.quote(xml))
            response = urllib2.urlopen(request_url).read()
        else:
            response = False

        return response

    def doi_status(self):
        pass

    def doi_request(self):
        pass

    def doi_update(self):
        pass