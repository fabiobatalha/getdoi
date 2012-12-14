#encoding: UTF-8

wrong_xml = u'''<?xml version = "1.0" encoding="UTF-8"?>
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

invalid_xml = u'''<?xml version = "1.0" encoding="UTF-8"?>
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

unresolved_response = u'''<?xml version="1.0" encoding="UTF-8"?>
<crossref_result xmlns="http://www.crossref.org/qrschema/2.0" version="2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.crossref.org/qrschema/2.0 http://www.crossref.org/schema/queryResultSchema/crossref_query_output2.0.xsd">
  <query_result>
    <head>
      <email_address>test@crossref.org</email_address>
      <doi_batch_id>test</doi_batch_id>
    </head>
    <body>
      <query key="key" status="unresolved" fl_count="0">
        <article_title>Time series analysis of water surface temperature and heat flux components in the Itumbiara Reservoir (GO), Brazil</article_title>
        <first_page>245</first_page>
        <issn>2179975X</issn>
        <issue>3</issue>
        <journal_title>Acta Limnologica Brasiliensia</journal_title>
        <volume>23</volume>
        <year>2013</year>
      </query>
    </body>
  </query_result>
</crossref_result>
'''

resolved_response = u'''<?xml version="1.0" encoding="UTF-8"?>
<crossref_result xmlns="http://www.crossref.org/qrschema/2.0" version="2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.crossref.org/qrschema/2.0 http://www.crossref.org/schema/queryResultSchema/crossref_query_output2.0.xsd">
  <query_result>
    <head>
      <email_address>test@crossref.org</email_address>
      <doi_batch_id>test</doi_batch_id>
    </head>
    <body>
      <query key="key" status="resolved" fl_count="0">
        <doi type="journal_article">10.1590/S2179-975X2012005000002</doi>
        <issn match="exact" type="electronic">2179-975X</issn>
        <journal_title match="exact">Acta Limnologica Brasiliensia</journal_title>
        <author>Alcântara</author>
        <volume match="optional">23</volume>
        <issue match="optional">3</issue>
        <first_page match="optional">245</first_page>
        <year match="optional" media_type="online">2011</year>
        <publication_type>full_text</publication_type>
      </query>
    </body>
  </query_result>
</crossref_result>
'''