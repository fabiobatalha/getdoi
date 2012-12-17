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