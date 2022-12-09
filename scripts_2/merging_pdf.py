import os


os.chdir('Z:\PgX\PDF_Pages\Individual_Page_generation_folder')
list_Of_pdf_merge = os.listdir()
print(list_Of_pdf_merge)

initial_pgs = ['First_Page.pdf', 'Understanding_your_result.pdf', 'individual_report_summary.pdf','individual_report_summary2.pdf']
report_detail_pg = ['Report_Detail_Title.pdf']
last_pgs = ['Test_Methodology.pdf', 'Reference.pdf', 'Glossary.pdf', 'Disclaimer.pdf', 'Last_Page.pdf']

for x in last_pgs:
        if x in list_Of_pdf_merge:
            print("The files are present")
            continue
        else:
            print("Files are missing")
            break
