"""Trying to integrated the Drug information based on the phenotype and star allele"""
import pandas as pd
import os
import pdf_pages
from datetime import date
today = date.today()
import shutil
from PyPDF2 import PdfFileMerger
from compress import compress_file


def condition_startallele_activity_score(out1):
    out2 = out1.loc[out1['Gene'].isin(['CYP2D6', 'UGT1A1', 'CYP2C9'])]
    # print("out2", out2.shape[0])
    out3 = out1.loc[~out1['Gene'].isin(['CYP2D6', 'UGT1A1', 'CYP2C9'])]
    # print("out3", out3.shape[0])
    out_2_specific_drug = out2[out2['Activity_score'].notnull()]
    y = []
    out2_filter = pd.DataFrame()
    if not out_2_specific_drug.empty:
        out_2specificdruglist = out_2_specific_drug.values.tolist()
        for x in out_2specificdruglist:
            if float(x[12]) == float(x[26]):
                y += [x]
        out2_filter = pd.DataFrame(y, columns=out_2_specific_drug.columns)
    out_2_add = out2[out2['Activity_score'].isnull()]
    # print("out_2_add", out_2_add.shape[0])
    # print("out2_filter", out2_filter.shape[0])
    out_2_add = out_2_add.append(out2_filter)
    out_2_add = out_2_add.append(out3)
    #
    # out_2_startallele = out_2_add[out_2_add['Start_allele_Conditions'].notnull()]
    # if not out_2_startallele.empty:
    #     out_2startallelelist = out_2_startallele.values.tolist()
    #     for x in out_2startallelelist:
    #         print(x[11])
    return out_2_add

def drug_integration_to_pdf(individual_report_startallele, sample_id):
    """Report generation and Drug_content_fetching"""
    # print("sample id", sample_id)

    os.chdir(r'Z:/PgX/Report_csv')
    individual_report_startallele.to_csv((sample_id + ".csv"), index=False, header=False)
    os.chdir(r'Z:/PgX/Individual_raw')
    files_in_folder = os.listdir()
    files_in_folder = files_in_folder[0]
    individual_pheno = pd.read_excel(files_in_folder)
    # orcle_create_table(individual_pheno)
    individual_report_startallele.columns = ['Barcode Id', 'Gene', 'Happ_1', 'Happ_2', 'Diploid',
                                             'Phenotype', 'Activity_scores', 'Start_alleles']
    individual_report_startallele['Barcode Id'] = individual_report_startallele['Barcode Id'].astype('str')
    print("The total individual in the file is :", individual_pheno.shape[0])
    individual_pheno['Barcode Id'] = individual_pheno['Barcode Id'].astype('str')
    individual_report_startallele = individual_report_startallele.merge(
        individual_pheno, how='inner', on=['Barcode Id'])
    individual_report_startallele['DATE'] = today.strftime("%b-%d-%Y")

    os.chdir(r'Z:/PgX/Report_csv')
    individual_report_startallele.to_csv((sample_id + ".csv"), index=False, header=False)
    drug_pd = pd.read_excel(r'Z:\PgX\Supporting_file\Drug_Content\MEDNAwise_DETAILED_REPORT_CONTENT_16052022.xlsx')
    out1 = drug_pd.merge(individual_report_startallele, how='inner', on=['Gene', 'Phenotype'])
    final_individual_drug_info = condition_startallele_activity_score(out1)
    final_individual_drug_info_2 = drug_drug_interaction(final_individual_drug_info)
    # print(final_individual_drug_info_2)
    # print(final_individual_drug_info_2.at[10,'SEX'])
    final_individual_drug_info_2.reset_index(inplace=True)
    ## Removing Gynecology or male
    if final_individual_drug_info_2.at[10, 'SEX'] == 'Male':
        print(final_individual_drug_info_2.at[10, 'SEX'])
        final_individual_drug_info_2 = final_individual_drug_info_2[
            final_individual_drug_info_2.Catogery != "GYNECOLOGY"]

    # ## Activity_score Activity_scores
    os.chdir(r'Z:/PgX/Drug_content_csv')
    path2 = "Drug_" + sample_id + ".csv"
    final_individual_drug_info_2.drop('index', axis=1, inplace=True)
    final_individual_drug_info_2.rename(columns={'DNA Product': "Product_Details"}, inplace=True)
    list_of_header_to_change = ["Catogery","Drug_Name",
                      "what_is_it","where_is_it_used",
                      "how_does_it_works","Gene","Gene_Content",
                      "Phenotype","Clinical_Effect","What_does_your_result_mean",
                      "Recommendations","Start_allele_Conditions",
                      "Activity_score","Images",
                      "Further_Interacting_Factors",
                      "Reference","donotduisturb",
                      "Effect","Drug_Response",
                      "Recomendation",
                      "Symbol",
                      "detailed_report_images",
                      "Barcode Id",
                      "Happ_1",
                      "Happ_2",
                      "Diploid",
                      "Activity_scores",
                      "Start_alleles",
                      "Member id",
                      "Beneficiary Name",
                      "AGE",
                      "SEX",
                      "Beneficiary ID",
                      "QC Status",
                      "Batch no",
                      "Recipts",
                      "Recipts status",
                      "HRA Status",
                      "EHR ID",
                      "VISIT ID",
                      "GSA Status GSA (Pass=>97%/Fail=<97%)",
                      "ContactNo",
                      "Email ID",
                      "Language",
                      "Product_Details",
                      "DATE"]
    final_individual_drug_info_2 = final_individual_drug_info_2[list_of_header_to_change]
    final_individual_drug_info_2.to_csv(path2, index=False)
    # Oracle_pdf(final_individual_drug_info_2)
    drug_pheno_to_summary_report(final_individual_drug_info_2, sample_id)



def drug_drug_interaction(drug_info):
    """Adding info of drug drug interaction"""
    os.chdir("Z:\PgX\Supporting_file\Drug_Content")
    extra_drug_content = pd.read_excel("COMPLEX_DRUG_CONTENT.xlsx")
    extra_drug_contentlist = extra_drug_content.values.tolist()
    yy = []
    for xx in extra_drug_contentlist:
        yy += [[xx[:3]] + [xx[3:6]] + [xx[6]]]
    k = pd.DataFrame()
    drug_to_add_content = set(extra_drug_content['Drug1'].values.tolist())
    k = drug_info.loc[~drug_info['Drug_Name'].isin(drug_to_add_content)]
    w = drug_info.loc[drug_info['Drug_Name'].isin(drug_to_add_content)]
    for xt in drug_to_add_content:
        gg = w[w['Drug_Name'] == xt]
        check_1 = gg[['Drug_Name', 'Gene', 'Phenotype']]
        check_1_list = check_1.values.tolist()
        check_1_list = [list(t) for t in set(tuple(element) for element in check_1_list)]
        for xa in yy:
            try:
                if check_1_list[0] in xa and check_1_list[1] in xa:
                    gg['Recommendations'] = gg['Recommendations'].map(lambda x: str(x)[:-5])
                    gg['Recommendations'] = gg['Recommendations'].astype(str) + xa[2]
            except:
                pass
        k = k.append(gg)
    return k


def drug_pheno_to_summary_report(out1, sample_id):
    """Final drug list into 2 report summary """
    first_page_info = {}
    print("Sample ID is :", sample_id)
    # druglist_pd = pd.read_csv(r'Z:\PgX\Drug_content_csv\Drug_15001902090926.csv', encoding='unicode_escape')
    druglist_pd = out1

    first_page_info = druglist_pd[['Beneficiary Name',	'AGE',	'SEX',	'Beneficiary ID', 'EHR ID', 'DATE']]
    first_page_info = first_page_info.rename(
        columns={'Beneficiary Name': 'Name', 'Beneficiary ID': 'Beneficiary_ID', 'EHR ID': 'EHR_ID'})
    try:
        first_page_info = first_page_info.head(1).to_dict(orient='records')[0]
    except:
        print(" Sample is missing :", str(sample_id))
    allele_table = druglist_pd[['Gene', 'Start_alleles']]
    # allele_table['Start_alleles'] = str(allele_table['start_alleles']).split('[]')
    # allele_table['Start_alleles'] = [','.join(map(str, l)) for l in allele_table['Start_alleles']]
    allele_table = allele_table.drop_duplicates(subset=['Gene'], keep='first')
    allele_table_dict = dict(zip(allele_table.Gene, allele_table.Start_alleles))
    summary_report_2 = druglist_pd[
        druglist_pd['Phenotype'].str.contains('Indeterminate|Phenotype could not be inferred')]
    summary_report_2_to_pdf = summary_report_2[['Catogery', 'Drug_Name', 'Gene', 'Phenotype', 'Diploid',
                                                'Effect', 'Drug_Response', 'Recomendation', 'Symbol']]
    summary_report_1 = druglist_pd[
        ~druglist_pd['Phenotype'].str.contains('Indeterminate|Phenotype could not be inferred')]
    summary_report_3_to_pdf = druglist_pd[['Catogery', 'Drug_Name', 'Gene', 'Phenotype',
                                                'Effect', 'Drug_Response', 'Recomendation', 'Symbol']]
    # ******* Getting The Pandas data structure to the pdf format  ************ #
    summary_report_1_to_pdf = summary_report_1[['Catogery', 'Drug_Name', 'Gene', 'Phenotype',
                                                'Effect', 'Drug_Response', 'Recomendation', 'Symbol']]
    drug_detial_page_from_summary_page_1 = summary_report_1[
        ~summary_report_1['Clinical_Effect'].isna()]
    drug_detial_pages = drug_detial_page_from_summary_page_1[['Catogery', 'Drug_Name', 'Gene', 'Gene_Content',
                  'Diploid', 'Images', 'Clinical_Effect', 'What_does_your_result_mean',
                  'Recommendations', 'Further_Interacting_Factors']]
    drug_detial_pages['Further_Interacting_Factors'].fillna(" ", inplace=True)
    drug_detial_pages['FileName'] = drug_detial_pages['Drug_Name'] + '_' + drug_detial_pages['Gene'] + ".pdf"
    # print(drug_detial_page_from_summary_page_1)
    individual_drug_list_for_intropage = list(set(drug_detial_page_from_summary_page_1['Drug_Name'].values.tolist()))

    """ Generating Pdf from info """
    print("page generation")
    pdf_pages.pdf_first_page(first_page_info)
    pdf_pages.allele_def_table(allele_table_dict)
    report_summary_drug_list = pdf_pages.report_summary_page(summary_report_3_to_pdf)
    # pdf_pages.report_summarty_page_2(summary_report_2_to_pdf)
    pdf_pages.copy_drug_intro(individual_drug_list_for_intropage)
    # pdf_pages.drug_introduction(individual_drug_list_for_intropage)
    pdf_pages.details_pages_for_report_summary(drug_detial_pages)

    source_dir = 'Z:/PgX/PDF_Pages/Additional_pages'
    target_dir = 'Z:/PgX/PDF_Pages/Individual_Page_generation_folder'
    file_names = os.listdir(source_dir)
    for file_name in file_names:
        shutil.copy2(os.path.join(source_dir, file_name), target_dir)

    list_in_oder_for_Pages = []
    for k, v in report_summary_drug_list.items():
        l1 = []
        for k1,v1 in v[1].items():
            l1.append(k1)
        l1 = sorted(l1, key=str.lower)
        list_in_oder_for_Pages += l1

    page_in_order = []
    os.chdir('Z:\PgX\PDF_Pages\Individual_Page_generation_folder')
    list_Of_pdf_merge = os.listdir()
    for x4 in list_in_oder_for_Pages:
        page_in_order += [i for i in list_Of_pdf_merge if i.startswith(x4)]

    initial_pgs = ['First_Page.pdf','Table_of_content.pdf', 'understanding_report.pdf','Summary_Cover.pdf', 'individual_report_summary.pdf',
                    'Report_Detail_Title.pdf']
    last_pgs = ['Allele_Table.pdf', 'appendix.pdf','appendix_II.pdf', 'Test_Methology_and_limitaton.pdf', 'references.pdf', 'glossary.pdf',
                'disclaimer.pdf', 'Last_Page.pdf']

    os.chdir('Z:\PgX\PDF_Pages\Individual_Page_generation_folder')
    pdfs_all = initial_pgs + page_in_order + last_pgs
    merger = PdfFileMerger()
    for pdf in pdfs_all:
        merger.append(pdf)

    # merger.encrypt("test")
    merger.write("Z:/PgX/PDF/uncompressed/" + sample_id + ".pdf")
    merger.close()

    os.chdir('Z:\PgX\PDF_Pages\Individual_Page_generation_folder')
    mydir = 'Z:\PgX\PDF_Pages\Individual_Page_generation_folder'
    filelist = [f for f in os.listdir(mydir)]
    for f in filelist:
        os.remove(os.path.join(mydir, f))

    compress_file(sample_id)