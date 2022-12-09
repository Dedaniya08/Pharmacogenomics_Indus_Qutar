"""Class for PDF generation"""
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
import os
import pandas as pd
import pdfkit
from collections import OrderedDict
import shutil
import multiprocessing
pd.options.mode.chained_assignment = None
pd.options.display.max_colwidth = 10000

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
color_code = pd.read_excel("./Supporting_files/color_code.xlsx")
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
color_code = color_code.values.tolist()
orientation = [x[0] for x in color_code]
color_code2 = pd.read_excel("./Supporting_files/color_code2.xlsx")
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
color_code2 = color_code2.values.tolist()

def report_summary_page(Individual_report_summary):
    """Report Summary page 1"""
    class_catogery = set(Individual_report_summary['Catogery'].values.tolist())
    final_classlist = OrderedDict()

    for x in class_catogery:
        e = [e[1] for e in color_code if x in e[0]]
        y = Individual_report_summary[Individual_report_summary['Catogery'] == x]
        drug_catoegry = set(y['Drug_Name'].values.tolist())
        drug_catlogy = {}
        for z in drug_catoegry:
            w = Individual_report_summary[Individual_report_summary['Drug_Name'] == z]
            h = w[['Gene', 'Phenotype', 'Drug_Response', 'Recomendation', 'Symbol']]
            header = ['Gene', 'Phenotype', 'Drug_Response', 'Recomendation', 'Symbol', 'Drug']
            k = h.values.tolist()
            i = {}
            for j in k:
                gene_header = j[0]
                j += [z]
                i[gene_header] = dict(zip(header, j))
            i = {key: value for key, value in sorted(i.items())}
            drug_catlogy[z] = i
        drug_catlogy = {key: value for key, value in sorted(drug_catlogy.items())}
        final_classlist[x] = e + [drug_catlogy]
    ###  ordered the dict  ####
    final_classlist = {key: value for key, value in sorted(final_classlist.items())}
    additionaldict = {}
    additionaldict['ANESTHESIOLOGY'] = final_classlist['ANESTHESIOLOGY']
    final_classlist.pop('ANESTHESIOLOGY', None)
    final_classlist.update(additionaldict)
    # final_classlist = OrderedDict([(el, final_classlist[el]) for el in orientation])
    os.chdir(r'Z:\PgX\Software')
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("templates/report_summary.html")
    os.chdir(r'Z:\PgX\PDF_Pages\Individual_Page_generation_folder')
    base_url = os.path.dirname(os.path.relpath(__file__))
    output = template.render(dict=final_classlist, list=color_code)
    HTML(string=output, base_url= base_url).write_pdf("individual_report_summary.pdf")
    return final_classlist

def drug_introduction(individual_drug_list):
    """drug intro based on the required pages"""
    os.chdir(r'Z:\PgX\Software')
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("templates/drug-index.html")
    drug_intro_doc = pd.read_excel(r'Z:\PgX\Supporting_file\Drug_Content\DRUG_INTRODUCTION_CONTENT_PGX_REPORT.xlsx')
    Personalize_drug_intro_pages = drug_intro_doc[drug_intro_doc['Drug'].isin(individual_drug_list)]
    Personalize_drug_intro_pages_list = Personalize_drug_intro_pages.values.tolist()
    drug_header = ['Catogery',	'Drug',	'what_is_it', 'where_is_it_used', 'how_does_it_works', 'images']
    for x in Personalize_drug_intro_pages_list:
        file_name = x[1]
        dict_to_print = dict(zip(drug_header, x))
        os.chdir(r'Z:\PgX\PDF_Pages\Individual_Page_generation_folder')
        base_url = os.path.dirname(os.path.relpath(__file__))
        output = template.render(dict_to_print)
        HTML(string=output, base_url=base_url).write_pdf(file_name+".pdf")


def allele_def_table(allele_table_dict):
    # Drug start allele Detecting Template.
    os.chdir(r'Z:\PgX\Software')
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("templates/start_allele_table.html")
    os.chdir(r'Z:\PgX\PDF_Pages\Individual_Page_generation_folder')
    base_url = os.path.dirname(os.path.relpath(__file__))
    output2 = template.render(dict=allele_table_dict)
    HTML(string=output2, base_url=base_url).write_pdf("Allele_Table.pdf")


def pdf_first_page(individual_name):
    """Individual first page with name and detials."""
    os.chdir(r'Z:\PgX\Software')
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("templates/first_page.html")
    os.chdir(r'Z:\PgX\PDF_Pages\Individual_Page_generation_folder')
    base_url = os.path.dirname(os.path.relpath(__file__))
    # print(type(individual_name), individual_name)
    output2 = template.render(individual_name)
    HTML(string=output2, base_url=base_url).write_pdf("First_Page.pdf")

def details_pages_for_report_summary(drug_detial_pages):
    """detials page explanation of all the drug labeled in report summary"""
    os.chdir(r'Z:\PgX\Software')
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("templates/report-details.html")
    os.chdir(r'Z:\PgX\PDF_Pages\Individual_Page_generation_folder')
    base_url = os.path.dirname(os.path.relpath(__file__))
    Complete_text = drug_detial_pages.values.tolist()
    title_page = ['Catogery', 'Drug_Name', 'Gene', 'Gene_Content',
                      'Diploid', 'Images', 'Clinical_Effect', 'What_does_your_result_mean',
                      'Recommendations', 'Further_Interacting_Factors', 'FileName']
    for lin in Complete_text:
        page_dict = {}
        page_dict = dict(zip(title_page, lin))
        ttt = page_dict['FileName']
        output = template.render(page_dict)
        HTML(string=output, base_url=base_url).write_pdf(ttt)


    # def multi_page(lin):
    #     title_page = ['Catogery', 'Drug_Name', 'Gene', 'Gene_Content',
    #                   'Diploid', 'Images', 'Clinical_Effect', 'What_does_your_result_mean',
    #                   'Recommendations', 'Further_Interacting_Factors', 'FileName']
    #     page_dict = dict(zip(title_page, lin))
    #     ttt = page_dict['FileName']
    #     output = template.render(page_dict)
    #     HTML(string=output, base_url=base_url).write_pdf(ttt)
    #
    # if __name__ == '__main__':
    #     # use one less process to be a little more stable
    #     p = multiprocessing.Pool(processes=multiprocessing.cpu_count() - 2)
    #     p.map(multi_page, Complete_text)



def report_summarty_page_2(Individual_report_summary2):
    """Report Summary page 2"""
    class_catogery = set(Individual_report_summary2['Catogery'].values.tolist())
    final_classlist = OrderedDict()
    for x in class_catogery:
        e = [e[1] for e in color_code2 if x in e[0]]
        # e = '#96989A'
        y = Individual_report_summary2[Individual_report_summary2['Catogery'] == x]
        drug_catoegry = set(y['Drug_Name'].values.tolist())
        drug_catlogy = {}
        for z in drug_catoegry:
            #'Catogery', 'Drug_Name', 'Gene', 'Phenotype', 'Diploid','Effect', 'Drug_Response', 'Recomendation', 'Symbol'
            w = Individual_report_summary2[Individual_report_summary2['Drug_Name'] == z]
            h = w[['Gene', 'Phenotype', 'Diploid', 'Recomendation']]
            header = ['Gene', 'Phenotype', 'Diploid', 'Recomendation', 'Drug']
            k = h.values.tolist()
            i = {}
            for j in k:
                gene_header = j[0]
                j += [z]
                i[gene_header] = dict(zip(header, j))
            i = {key: value for key, value in sorted(i.items())}
            drug_catlogy[z] = i
        drug_catlogy = {key: value for key, value in sorted(drug_catlogy.items())}
        final_classlist[x] = e + [drug_catlogy]
    ###  ordered the dict  ####
    # final_classlist = OrderedDict([(el, final_classlist[el]) for el in orientation])
    final_classlist = {key: value for key, value in sorted(final_classlist.items())}
    os.chdir(r'Z:\PgX\Software')
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("templates/report_summary2.html")
    os.chdir(r'Z:\PgX\PDF_Pages\Individual_Page_generation_folder')
    base_url = os.path.dirname(os.path.relpath(__file__))
    output = template.render(dict=final_classlist, list=color_code2)
    HTML(string=output, base_url=base_url).write_pdf("individual_report_summary2.pdf")


def drug_introduction():
    """drug intro based on the required pages"""
    os.chdir(r'Z:\PgX\Software')
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("templates/drug-index.html")
    drug_intro_doc = pd.read_excel(r'Z:\PgX\Supporting_file\Drug_Content\DRUG_INTRODUCTION_CONTENT_PGX_REPORT.xlsx')
    # Personalize_drug_intro_pages = drug_intro_doc[drug_intro_doc['Drug'].isin(individual_drug_list)]
    Personalize_drug_intro_pages_list = drug_intro_doc.values.tolist()
    drug_header = ['Catogery',	'Drug',	'what_is_it', 'where_is_it_used', 'how_does_it_works', 'images']
    for x in Personalize_drug_intro_pages_list:
        file_name = x[1]
        dict_to_print = dict(zip(drug_header, x))
        os.chdir(r'Z:\PgX\PDF_Pages\Individual_Page_generation_folder')
        base_url = os.path.dirname(os.path.relpath(__file__))
        output = template.render(dict_to_print)
        HTML(string=output, base_url=base_url).write_pdf(file_name+".pdf")

def copy_drug_intro(drug_name):
    """Move the Drug intro."""
    source_dir = 'Z:/PgX/PDF_Pages/Drug_intro_Pages'
    target_dir = 'Z:/PgX/PDF_Pages/Individual_Page_generation_folder'
    os.chdir('Z:/PgX/PDF_Pages/Drug_intro_Pages')
    file_names = os.listdir(source_dir)
    page_in_order=[]
    for x4 in drug_name:
        page_in_order += [i for i in file_names if i.startswith(x4)]

    for file_name in page_in_order:
        shutil.copy2(os.path.join(source_dir, file_name), target_dir)


#
# def details_pages_for_report_summary_all():
#     """detials page explanation of all the drug labeled in report summary"""
#     druglist_pd = pd.read_excel('Z:\PgX\Supporting_file\Drug_Content\MEDNAwise_DETAILED_REPORT_CONTENT_13042022.xlsx')
#     drug_detial_pages = druglist_pd[['Catogery', 'Drug_Name', 'Gene', 'Gene_Content',
#                     'Images', 'Clinical_Effect', 'What_does_your_result_mean',
#                   'Recommendations', 'Further_Interacting_Factors','Phenotype']]
#     drug_detial_pages['Diploid'] = '*3/*3'
#     drug_detial_pages['Further_Interacting_Factors'].fillna(" ", inplace=True)
#     drug_detial_pages['FileName'] = drug_detial_pages['Drug_Name'] + '_' + drug_detial_pages['Gene']+\
#                                     '_' + drug_detial_pages['Phenotype'].str.replace(" ",'') +".pdf"
#     drug_detial_pages = drug_detial_pages[['Catogery',	'Drug_Name',	'Gene',	'Gene_Content',
#                   'Diploid', 'Images', 'Clinical_Effect', 'What_does_your_result_mean',
#                   'Recommendations', 'Further_Interacting_Factors', 'FileName']]
#     print(drug_detial_pages)
#     os.chdir(r'Z:\PgX\Software')
#     env = Environment(loader=FileSystemLoader('.'))
#     template = env.get_template("templates/report-details.html")
#     os.chdir(r'Z:\PgX\PDF_Pages\Individual_Page_generation_folder')
#     base_url = os.path.dirname(os.path.relpath(__file__))
#     Complete_text = drug_detial_pages.values.tolist()
#     title_page = ['Catogery',	'Drug_Name',	'Gene',	'Gene_Content',
#                   'Diploid', 'Images', 'Clinical_Effect', 'What_does_your_result_mean',
#                   'Recommendations', 'Further_Interacting_Factors', 'FileName']
#     for lin in Complete_text:
#         page_dict = {}
#         page_dict = dict(zip(title_page, lin))
#         ttt = page_dict['FileName']
#         output = template.render(page_dict)
#         HTML(string=output, base_url=base_url).write_pdf(ttt)


# drug_introduction()
# details_pages_for_report_summary_all()