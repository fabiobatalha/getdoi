import urllib
import urllib2
import itertools
import mimetools
import mimetypes
from cStringIO import StringIO
from BeautifulSoup import BeautifulSoup
from porteira.porteira import Schema

from settings import *


class MultiPartForm(object):
    """Accumulate the data to be used when posting a form."""

    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = mimetools.choose_boundary()
        return

    def get_content_type(self):
        return 'multipart/form-data; boundary=%s' % self.boundary

    def add_field(self, name, value):
        """Add a simple field to the form data."""
        self.form_fields.append((name, value))
        return

    def add_file(self, fieldname, filename, fileHandle, mimetype=None):
        """Add a file to be uploaded."""
        body = fileHandle.read()
        if mimetype is None:
            mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        self.files.append((fieldname, filename, mimetype, body))
        return

    def __str__(self):
        """Return a string representing the form data, including attached files."""
        # Build a list of lists, each containing "lines" of the
        # request.  Each part is separated by a boundary string.
        # Once the list is built, return a string where each
        # line is separated by '\r\n'.
        parts = []
        part_boundary = '--' + self.boundary

        # Add the form fields
        parts.extend(
            [part_boundary,
              'Content-Disposition: form-data; name="%s"' % name,
              '',
              value,
            ]
            for name, value in self.form_fields
            )

        # Add the files to upload
        parts.extend(
            [part_boundary,
              'Content-Disposition: form-data; name="%s"; filename="%s"' % \
                 (field_name, filename),
              'Content-Type: %s' % content_type,
              '',
              body,
            ]
            for field_name, filename, content_type, body in self.files
            )

        # Flatten the list and add closing boundary marker,
        # then return CR+LF separated data
        flattened = list(itertools.chain(*parts))
        flattened.append('--' + self.boundary + '--')
        flattened.append('')
        return '\r\n'.join(flattened)


class Brocker(object):

    def __init__(self,
                 crossref_api_url=API_URL,
                 query_email=QUERY_EMAIL,
                 user=USER,
                 passwd=PASSWD,
                 xsd='../xsd/crossref_query_input2.0.xsd'):
        """
        Create a Brocker instance.
        xsd default for queries
        """
        xsd = open(xsd).read()
        self.porteira = Schema(xsd)
        self.crossref_api_url = crossref_api_url
        self.user = user
        self.passwd = passwd
        self.query_email = query_email

    def query_doi(self, xml):
        """
        Returns a DOI number according to metadata contained into a given valid XML.
        The XML must be compatible with crossref_query_input2.0.xsd
        This method will return 'False' or a 'DOI number'.
        """

        if self.porteira.validate(xml):
            request_url = "{0}query/?format=xsd_xml&pid={1}&qdata={2}".format(
                                                                        self.crossref_api_url,
                                                                        self.query_email,
                                                                        urllib2.quote(xml))
            query_result = urllib2.urlopen(request_url).read()
            dec = BeautifulSoup(query_result)
            try:
                return dec.query_result.doi.string
            except AttributeError:
                return None
        else:
            return None

    def is_resolved(self, doi):
        """
        Returns True or False for a given DOI number
        """
        request_url = "{0}query/?format=xsd_xml&pid={1}&id={2}".format(
                                                                self.crossref_api_url,
                                                                self.query_email,
                                                                doi)

        query_result = urllib2.urlopen(request_url).read()
        dec = BeautifulSoup(query_result)
        if dec.query_result.query['status'] == 'resolved':
            return True
        else:
            return False

    def request(self, xml):
        """
        Returns True if the request was well done and False if their was an error
        while sending the request to Crossref
        """

        if self.porteira.validate(xml):

            xml_file = StringIO()
            xml_file.write(xml)
            form = MultiPartForm()

            url = "{0}deposit".format(self.crossref_api_url)

            form.add_field('operation', 'doMDUpload')
            form.add_field('login_id', self.user)
            form.add_field('login_passwd', self.passwd)
            form.add_file('fname', 'crossref_query.xml', fileHandle=xml_file)

            body = str(form)

            request = urllib2.Request(url)
            request.add_header('Content-type', form.get_content_type())
            request.add_header('Content-length', len(body))
            request.add_data(body)

            response = urllib2.urlopen(request).read()

            return True

        else:
            return None

