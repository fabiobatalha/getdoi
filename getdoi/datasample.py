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

valid_request_xml = u'''<?xml version="1.0" encoding="UTF-8"?>
<doi_batch xmlns="http://www.crossref.org/schema/4.3.1" version="4.3.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<head>
<doi_batch_id>S2179-975X2011000100010</doi_batch_id>
<timestamp>20111029015048</timestamp>
<depositor>
<name>SciELO</name>
<email_address>bireme.crossref@gmail.com</email_address>
</depositor>
<registrant>10.1590</registrant>
</head>
<body>
<journal>
<journal_metadata language="en">
<full_title>Acta Limnologica Brasiliensia (Online)</full_title>
<abbrev_title>Acta Limnol. Bras. (Online)</abbrev_title>
<issn media_type="electronic">2179-975X</issn>
<coden>ALB</coden>
</journal_metadata>
<journal_issue>
<publication_date media_type="online">
<year>2011</year>
</publication_date>
<journal_volume><volume>23</volume></journal_volume>
<issue>1</issue>
</journal_issue>
<journal_article publication_type="full_text">
<titles>
<title>Effects of nitrate enrichment on leaf litter decomposition</title>
</titles>
<contributors>
<person_name sequence="first" contributor_role="author">
<given_name>Alan Mosele</given_name>
<surname>Tonin</surname>
</person_name>
<person_name sequence="additional" contributor_role="author">
<given_name>Luiz Ubiratan</given_name>
<surname>Hepp</surname>
</person_name>
</contributors>
<publication_date media_type="online">
<month>03</month>
<year>2011</year>
</publication_date>
<pages>
  <first_page>86</first_page>
  <last_page>94</last_page>
</pages>
<publisher_item>
<identifier id_type="pii">S2179-975X2011000100010</identifier></publisher_item>
<doi_data>
<doi>10.1590/S2179-975X2011000100010</doi><timestamp>20111029015048</timestamp>
<resource>http://www.scielo.br/scielo.php?script=sci_arttext&amp;pid=S2179-975X2011000100010&amp;lng=en&amp;nrm=iso&amp;tlng=en</resource>
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