#encoding: UTF-8
wrong_request_xml = u'''<?xml version = "1.0" encoding="UTF-8"?>
<query_batch
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
version="2.0"
xmlns="http://www.crossref.org/qschema/2.0"
xsi:schemaLocation="http://www.crossref.org/qschema/2.0 http://www.crossref.org/qschema/crossref_query_input2.0.xsd">
<head>
   <email_address>test@crossref.org</email_address>
   <doi_batch_id>test</doi_batch_id>
</head>
'''.encode('utf-8')

valid_request_xml = u'''
<?xml version="1.0" encoding="UTF-8"?>
<doi_batch version="4.3.0" xmlns="http://www.crossref.org/schema/4.3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.crossref.org/schema/4.3.0 
http://www.crossref.org/schema/deposit/crossref4.3.0.xsd">
  <head>
    <doi_batch_id>123456</doi_batch_id>
    <timestamp>19990628123304</timestamp>
    <depositor>
      <name>xyz</name>
      <email_address>xyz@authorized_depositor.com</email_address>
    </depositor>
    <registrant>AIP</registrant>
  </head>
  <body>
    <journal>
      <journal_metadata language="en">
        <full_title>Applied Physics Letters</full_title>
        <abbrev_title>Appl. Phys. Lett.</abbrev_title>
        <issn media_type="print">0003-6951</issn>
        <coden>applab</coden>
      </journal_metadata>
      <journal_issue>
        <publication_date media_type="print">
          <year>1999</year>
        </publication_date>
        <journal_volume>
          <volume>74</volume>
        </journal_volume>
        <issue>16</issue>
      </journal_issue>
      <journal_article publication_type="full_text">
        <titles>
          <title>Sub-5-fs visible pulse generation by pulse-front-matched noncollinear optical parametric amplification</title>
        </titles>
        <contributors>
          <person_name sequence="first" contributor_role="author">
            <given_name>Ann P.</given_name>
            <surname>Shirakawa</surname>
          </person_name>
          <organization sequence="additional" contributor_role="author">Sample Organization</organization>
        </contributors>
        <publication_date media_type="print">
          <year>1999</year>
        </publication_date>
        <pages>
          <first_page>2268</first_page>
        </pages>
        <publisher_item>
          <identifier id_type="pii">S000369519903216</identifier>
        </publisher_item>
        <doi_data>
          <doi>10.9876/S000369519903216</doi>
          <timestamp>19990628123304</timestamp>
          <resource>http://ojps.aip.org/link/?apl/74/2268/ab</resource>
        </doi_data>
      </journal_article>
    </journal>
  </body>
</doi_batch>
'''.encode('utf-8')

wrong_query_xml = u'''<?xml version = "1.0" encoding="UTF-8"?>
<query_batch
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
version="2.0"
xmlns="http://www.crossref.org/qschema/2.0"
xsi:schemaLocation="http://www.crossref.org/qschema/2.0 http://www.crossref.org/qschema/crossref_query_input2.0.xsd">
<head>
   <email_address>test@crossref.org</email_address>
   <doi_batch_id>test</doi_batch_id>
</head>
'''.encode('utf-8')

invalid_query_xml = u'''<?xml version = "1.0" encoding="UTF-8"?>
<query_batch
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
version="2.0"
xmlns="http://www.crossref.org/qschema/2.0"
xsi:schemaLocation="http://www.crossref.org/qschema/2.0 http://www.crossref.org/qschema/crossref_query_input2.0.xsd">
<head>
   <email_address>test@crossref.org</email_address>
   <doi_batch_id>test</doi_batch_id>
</head>
</query_batch>
'''.encode('utf-8')

doc_without_doi = u'''<?xml version = "1.0" encoding="UTF-8"?>
<query_batch
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
version="2.0"
xmlns="http://www.crossref.org/qschema/2.0"
xsi:schemaLocation="http://www.crossref.org/qschema/2.0 http://www.crossref.org/qschema/crossref_query_input2.0.xsd">
<head>
   <email_address>test@crossref.org</email_address>
   <doi_batch_id>test</doi_batch_id>
</head>
<body>
  <query
    enable-multiple-hits="exact"
    list-components="false"
    expanded-results="false" key="key">
    <article_title match="fuzzy">Time series analysis of water surface temperature and heat flux components in the Itumbiara Reservoir (GO), Brazil</article_title>
    <author search-all-authors="false"></author>
    <issn>2179-975X</issn>
    <volume>23</volume>
    <issue>3</issue>
    <year>2013</year>
    <first_page>245</first_page>
    <journal_title>Acta Limnologica Brasiliensia</journal_title>
  </query>
</body>
</query_batch>'''.encode('utf-8')

doc_with_doi = u'''<?xml version = "1.0" encoding="UTF-8"?>
<query_batch
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
version="2.0"
xmlns="http://www.crossref.org/qschema/2.0"
xsi:schemaLocation="http://www.crossref.org/qschema/2.0 http://www.crossref.org/qschema/crossref_query_input2.0.xsd">
<head>
   <email_address>test@crossref.org</email_address>
   <doi_batch_id>test</doi_batch_id>
</head>
<body>
  <query
    enable-multiple-hits="exact"
    list-components="false"
    expanded-results="false" key="key">
    <article_title match="fuzzy">Time series analysis of water surface temperature and heat flux components in the Itumbiara Reservoir (GO), Brazil</article_title>
    <author search-all-authors="false"></author>
    <issn>2179-975X</issn>
    <volume>23</volume>
    <issue>3</issue>
    <year>2011</year>
    <first_page>245</first_page>
    <journal_title>Acta Limnologica Brasiliensia</journal_title>
  </query>
</body>
</query_batch>'''.encode('utf-8')