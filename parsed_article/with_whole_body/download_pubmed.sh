#!/bin/bash
XML_DIR=xml
# Delete it if it exists
[ -d $XML_DIR ] && rm -r $XML_DIR
mkdir $XML_DIR
cd $XML_DIR


mkdir 2022-09-04
cd 2022-09-04
wget  ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_noncomm/xml/oa_noncomm_xml.incr.2022-09-04.tar.gz 
tar -xf oa_noncomm_xml.incr.2022-09-04.tar.gz 
cd ..


mkdir 2022-09-05
cd 2022-09-05
wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_noncomm/xml/oa_noncomm_xml.incr.2022-09-05.tar.gz 
tar -xf oa_noncomm_xml.incr.2022-09-05.tar.gz 
rm non_comm_use.C-H.xml.tar.gz
cd ..
