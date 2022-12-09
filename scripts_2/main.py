"""The complete script of PGX it is complex, caution handle with care"""
import os
import pandas as pd
import numpy as np
from main_start_allele import dict_allele
from functional import function_diplotype_interpretation
from functional import function_diplotype_interpretation_specialgene
from drug_integration import drug_integration_to_pdf
from oracle_database_integration import orcle_create_table


def sample_mapping_with_reference(dict_chr1, dict_chr2, sample_number, Gender):
    sample_id = sample_number[1]
    os.chdir(r'Z:/PgX/Supporting_file/Gene')
    path_1 = "Z:/PgX/Supporting_file/Gene"
    gene_folder = os.listdir()
    final_table_per_sample_per_individual = []
    Gender_sample = [int(x[1]) for x in Gender if x[0] == sample_id]
    for folder in gene_folder:
        os.chdir(os.path.join(path_1 + "/" + folder))
        allele_definition_table = [filename for filename in os.listdir('.')
                                   if filename.startswith("Allele")][0]
        allele_definition_table_pd = pd.read_excel(allele_definition_table,
                                                   skiprows=[0, 1, 2, 3, 4, 5, 7, 8],
                                                   sheet_name="Alleles", index_col=0)
        output_array, deploid_pheno, start_alllele_checked = dict_allele(allele_definition_table_pd,
                                                                         sample_id, dict_chr1, dict_chr2, folder)

        gene_to_function = ['CFTR', 'ABCG2', 'CYP2B6', 'CYP2C19', 'CYP2C9',
                            'CYP3A5', 'CYP4F2', 'F5', 'IFNL3', 'SLCO1B1',
                            'NUDT15', 'RYR1', 'TPMT', 'VKORC1', 'UGT1A1', 'CYP2D6']
        gene_to_function_2 = ['NAT2', 'DPYD', 'G6PD']

        output_function_dis = [' ', ' ', ' ']
        if folder in gene_to_function:
            function_table = [filename for filename in os.listdir('.') if filename.startswith("Diplotype")][0]
            function_diploid_pd = pd.read_excel(function_table, sheet_name="Diplotypes", index_col=None)
            function_interpretation_pd = pd.read_excel(function_table, sheet_name="Interpretation", index_col=None)

            # to extract the information of function_table from diploid
            output_function_dis = function_diplotype_interpretation(function_diploid_pd,
                                                                    function_interpretation_pd,
                                                                    deploid_pheno,
                                                                    folder)
        if folder in gene_to_function_2:
            function_table = [filename for filename in os.listdir('.') if filename.startswith("Diplotype")][0]
            output_function_dis = function_diplotype_interpretation_specialgene(function_table,
                                                                                deploid_pheno, folder,
                                                                                Gender_sample, sample_number)

        final_output_array = output_array[:] + output_function_dis[:] + [start_alllele_checked[:]]
        # print("the gene is :", final_output_array[1])
        print(final_output_array)
        if final_output_array[1] in ['CFTR', 'RYR1'] and final_output_array[4] == ' ':
            final_output_array[4] = 'Reference'
        if final_output_array[5] == ' ':
            final_output_array[5] = 'Phenotype could not be inferred'
            x_2 = final_output_array[2]
            x_3 = final_output_array[3]
            if x_2 != [] and all([True if x.startswith('Noval') else False for x in x_2]):
                final_output_array[2] = 'Unreported Genotype'
            if x_3 != [] and all([True if x.startswith('Noval') else False for x in x_3]):
                final_output_array[3] = 'Unreported Genotype'
            final_output_array[4] = ''.join(final_output_array[2]) + "/" + ''.join(final_output_array[3])
        # if final_output_array[1] in ['G6PD']:
        #     final_output_array[5] = 'Phenotype could not be inferred'
        else:
            pass
        final_table_per_sample_per_individual.append(final_output_array)
    final_table_per_sample_per_individual = pd.DataFrame(final_table_per_sample_per_individual)
    # os.chdir(r'Z:/PgX/Report_csv')
    # final_table_per_sample_per_individual.to_csv((sample_id + ".csv"), index=False, header=False)
    drug_integration_to_pdf(final_table_per_sample_per_individual, sample_id)


def find_to_start_allele_in_customer():
    """Indentifying the start allele in the customer"""
    os.chdir(r'Z:\PgX\linux_shapeit\result_shapeit')
    table_list = []
    table_np = []
    np_rs = []
    np_genotype = []
    table_list_sample = []
    # pd_rs = pd.DataFrame([])

    with open("final_hap.phased.sample") as file:
        while line := file.readline().rstrip():
            table_list_sample = table_list_sample + [line]
    table_list_sample = [x.split(' ') for x in table_list_sample]
    table_list_sample = table_list_sample[2:]
    sample_file = [x[0:2] for x in table_list_sample]
    Gender = [[y for (i, y) in enumerate(h) if i in [1, 5]] for h in table_list_sample]
    with open("final_hap.phased.haps") as file:
        while line := file.readline().rstrip():
            table_list = table_list + [line]

    np_lines = np.array(table_list)
    for i in range(0, len(np_lines)):
        a = np_lines[i].split(" ")
        header = a[:3]
        allele = a[3:5]
        allele_code = ['0', '1']
        dict_allele_new = dict(zip(allele_code, allele))
        genotype = a[5:]
        replaced_genotype = [x if x not in dict_allele_new else dict_allele_new[x] for x in genotype]
        np_rs_1 = np.array(header[1])
        table_np.append(replaced_genotype)
        np_genotype = np.array(table_np)
        np_rs = np.append(np_rs, np_rs_1)

    pd_genotype = pd.DataFrame(np_genotype)
    # dict_sample_chr1 = {}
    # dict_sample_chr2 = {}
    for i, j in zip(range(0, len(sample_file)), range(0, pd_genotype.shape[1], 2)):
        sample_chr1 = pd_genotype[j].tolist()
        sample_chr2 = pd_genotype[j+1].tolist()
        dict_sample_chr1 = dict(zip(np_rs, sample_chr1))
        for keys, values in dict_sample_chr1.items():
            dict_sample_chr1[keys] = [values]

        dict_sample_chr2 = dict(zip(np_rs, sample_chr2))
        for keys, values in dict_sample_chr2.items():
            dict_sample_chr2[keys] = [values]
        sample_number = sample_file[i]
        if sample_number[1] in ["IHP210051677",
                                "IHP210051719","IHP210052268","IHP210052271",
                                "IHP210051808",
                                "IHP210052239",
                                "IHP210052402",
                                "IHP210052241",
                                "IHP210052336",
                                "IHP210052338"]:
            try:
                sample_mapping_with_reference(dict_sample_chr1, dict_sample_chr2, sample_number, Gender)
            except Exception as er:
                print("The issue with sample is, ", er)
        else: pass

if __name__ == '__main__':
    find_to_start_allele_in_customer()
    orcle_create_table()