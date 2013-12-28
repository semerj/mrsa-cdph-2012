mrsa-cdph-2012
==============

Converting publically reported CA 2012 MRSA data from PDFs into spreadsheets

> This report by the California Department of Public Health (CDPH) on methicillin-resistant Staphylococcus aureus (MRSA) and vancomycin-resistant Enterococci (VRE) Bloodstream Infections (BSIs) is the fourth by the California Department of Public Health (CDPH) and the third using information submitted by California hospitals to the Centers for Disease Control and Prevention (CDC) National Healthcare Safety Network (NHSN). The data were reported from January 1, 2012 through December 31, 2012, through NHSN laboratory-based identification of cases.

> New in this report, we present hospital-specific MRSA BSI standardized infection ratios (SIRs) for general acute care hospitals, other than long-term and rehabilitation acute care hospitals. The MRSA BSI SIR adjusts for significant risk factors, including hospital bed size, affiliation with a medical school, and the community burden of MRSA BSI as observed in patients admitted to the hospital. Adjusting for these factors provides for a more accurate comparison of hospitals’ infections. We labeled each SIR as indicating either: N (no difference in number of observed and predicted infections), high (H, more infections than predicted), or low (L, fewer infections than predicted). As in prior reports, for long term acute care (LTAC) and rehabilitation acute care hospitals, we present MRSA BSI rates, because LTAC and rehabilitation hospitals are currently excluded from NHSN SIR analyses.

More information [here](http://www.cdph.ca.gov/programs/hai/Pages/MRSAandVRE-Report.aspx).

You'll need:
* [qpdf](http://qpdf.sourceforge.net/) for decryption
* [pdftotext](http://www.bluem.net/en/mac/packages/) for text conversion and document layout preservation
* [Pandas](http://pandas.pydata.org/) for data munging

Make sure both `dostuff.sh` and `mrsa2012.py` are the ONLY documents in the same directory. Then run `dostuff.sh`. Boom.
