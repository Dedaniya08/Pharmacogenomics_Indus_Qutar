"""functional_interpretation"""
import pandas as pd
import os

def phenotype_deiplotype(deploid_pheno, gne = None):
    """Convert the haplotype to deplotype."""
    if not deploid_pheno:
        diploid_haploid = ' '
        if gne in ['TPMT', 'UGT1A1']: #'SLCO1B1', 'NUDT15', 'CYP2C9', 'CYP2C19']:
            diploid_haploid = "*1/*1"
    else:
        #if len(deploid_pheno) == 1:
            # if gne in ['CYP2C19', 'CYP2C9', 'SLCO1B1', 'NUDT15']:
            #     deploid_pheno += ['*1']
        diploid_haploid = '/'.join(deploid_pheno)
        if gne in ['UGT1A1'] and diploid_haploid in ['*80']:
            diploid_haploid = "*1/*80"
    return diploid_haploid


def function_diplotype_interpretation(diploid_fn, interpretation_fn, deploid_pheno, gne):
    """explanation of the deploid table"""
    final_outcome_fn = []
    gene_to_function = ['CFTR', 'ABCG2',
                        'CYP2B6', 'CYP2C19', 'CYP2C9',
                        'CYP3A5', 'CYP4F2', 'F5', 'IFNL3', 'SLCO1B1',
                        'NUDT15', 'TPMT', 'RYR1', 'VKORC1', 'UGT1A1', 'CYP2D6']

    if gne in gene_to_function:
        deploid_pheno = phenotype_deiplotype(deploid_pheno, gne)
        final_outcome_fn = pd.DataFrame(diploid_fn)
        final_outcome_fn = final_outcome_fn.loc[final_outcome_fn['Diplotype'] == deploid_pheno]
        final_outcome_fn = final_outcome_fn[['Diplotype', 'Coded_Diplotype_Phenotype_Summary',
                                             'Activity_Scores']]
        # print(final_outcome_fn)
        if final_outcome_fn.shape[0]:
            final_outcome_fn = final_outcome_fn.values.tolist()[0]
        else:
            final_outcome_fn = [' ', ' ', ' ']
        # os.system('pause')
    return final_outcome_fn


def function_diplotype_interpretation_specialgene(functional_pheno, diploid_fn, gne, gender, sample_no):
    if gne == 'NAT2':
        function_diploid_pd = pd.read_excel(functional_pheno, sheet_name="Haplotype", index_col=None)
        function_diploid_list = function_diploid_pd.values.tolist()
        function_Haplotype = pd.read_excel(functional_pheno, sheet_name="Combination_Outcome", index_col=None)
        function_combined_outcome_list = function_Haplotype.values.tolist()
        function_interpre_pd = pd.read_excel(functional_pheno, sheet_name="Interpretation", index_col=None)
        function_interpre_list = function_interpre_pd.values.tolist()
        final_outcome_fn = []
        if gne == 'NAT2' and diploid_fn != [] and len(diploid_fn) > 1 and all("Noval" not in s for s in diploid_fn):
            ff = []
            for x in diploid_fn:
                zz = [y[1] for y in function_diploid_list if x == y[0]]
                ff += zz
            kk = [g[2] for g in function_combined_outcome_list if (ff[0] == g[0] and ff[1] == g[1])]
            tt = [rr for rr in function_interpre_list if (kk[0] == rr[0])]
            final_outcome_fn = [phenotype_deiplotype(diploid_fn)]
            final_outcome_fn += [item for sublist in tt for item in sublist]
        elif gne == 'NAT2' and len(diploid_fn) == 1:
            ff = []
            for x in diploid_fn:
                zz = [y[1] for y in function_diploid_list if x == y[0]]
                ff += zz
            try:
                tt = [rr for rr in function_interpre_list if any(ff[0] in s for s in rr)]
                final_outcome_fn = diploid_fn + [item for sublist in tt for item in sublist]
            except:
                final_outcome_fn = [' ', ' ', ' ']

        elif gne == 'NAT2' and '*4' in diploid_fn:
            ff = ['Rapid Acetylator']
            tt = [rr for rr in function_interpre_list if ff[0] == rr[0]]
            final_outcome_fn = diploid_fn + [item for sublist in tt for item in sublist]
        else:
            final_outcome_fn = [' ', ' ', ' ']

        if len(final_outcome_fn) == 1:
            final_outcome_fn += [' ', ' ']

        return final_outcome_fn

    elif gne == 'DPYD':
        function_diploid_pd = pd.read_excel(functional_pheno, sheet_name="Genotype", index_col=None)
        function_diploid_list = function_diploid_pd.values.tolist()
        function_haplotype = pd.read_excel(functional_pheno, sheet_name="Haplotype_functionality", index_col=None)
        function_Haplotype_list = function_haplotype.values.tolist()
        function_interpre_pd = pd.read_excel(functional_pheno, sheet_name="Interpretation", index_col=None)
        function_interpre_list = function_interpre_pd.values.tolist()
        function_noval_pd = pd.read_excel(functional_pheno, sheet_name="Novel", index_col=None)
        function_noval_list = function_noval_pd.values.tolist()
        final_start_allele_DPYD = diploid_fn
        fina_structure = []
        Normal_function_allele = [x[0] for x in function_Haplotype_list if "Normal function" == x[1]]
        # print(diploid_fn)
        if not diploid_fn :
            fina_structure = [' ', ' ', ' ']

        if len(diploid_fn) == 1 and any("Noval" in x for x in diploid_fn):
            # print("1",diploid_fn)
            fina_structure = [' ', ' ', ' ']

        if len(diploid_fn) == 1 and any("Noval" not in x for x in diploid_fn):
            diploid_fn = diploid_fn + [' ']
            # print("2",diploid_fn)

        if len(diploid_fn) == 2:
            # print("3",diploid_fn)
            final_start_allele_DPYD = diploid_fn
            if all([True if x.startswith('Noval') else False for x in diploid_fn]):
                # print("4",diploid_fn)
                diploid_fn = [z[2] if j in z[0] else j for z in function_noval_list for j in diploid_fn]
                # print("4a",diploid_fn)
                diploid_fn = list(diploid_fn)
                # print("4b",diploid_fn)
                diploid_fn = [x for x in diploid_fn if not x.startswith('Noval')]
                # print("4c",diploid_fn)

            elif any(x[4:] != "Noval" for x in diploid_fn) == True:
                # print("5",diploid_fn)
                diploid_fn = [z[2] if j in z[0] else j for z in function_noval_list for j in diploid_fn]
                # print("5a",diploid_fn)
                if diploid_fn.count(diploid_fn[0]) != len(diploid_fn):
                    # print("5b",diploid_fn)
                    diploid_fn = list(set(diploid_fn))
                else:
                    # print("5c",diploid_fn)
                    diploid_fn = diploid_fn[0:2]
                diploid_fn = [x for x in diploid_fn if not x.startswith('Noval')]
                # print("5d",diploid_fn)

            diploid_fn = ["normal" if q in Normal_function_allele else q for q in diploid_fn]
            # print("6a",diploid_fn)
            ty = [s for s in function_diploid_list if (s[0] in diploid_fn[0]) and (s[1] in diploid_fn[1])][0]
            # print("ty",ty)
            yj = [o for o in function_interpre_list if (o[0] == ty[2] and o[1] == ty[3])][0]
            # print("yj",yj)
            yj = [yj[i] for i in [0, 1]]
            # print("yj1",yj)
            final_start_allele_DPYD = [z[1] if j == z[0] else j for
                                       z in function_noval_list for j in final_start_allele_DPYD]
            # print("final_start",final_start_allele_DPYD)
            if diploid_fn.count(diploid_fn[0]) == len(diploid_fn):
                # print("dipliod_fn_count",diploid_fn)
                final_start_allele_DPYD = final_start_allele_DPYD[0:2]
                # print("final_start_allele_dpyd", final_start_allele_DPYD)
            else:
                final_start_allele_DPYD = list(set(final_start_allele_DPYD))
                # print("final_start_allele_dpyd", final_start_allele_DPYD)

            final_start_allele_DPYD = [x for x in final_start_allele_DPYD if not x.startswith('Noval')]
            # print("final_start_allele_DPYD2",final_start_allele_DPYD)
            fina_structure = [final_start_allele_DPYD] + yj
            # print("fina_structure",fina_structure)
        return fina_structure

    elif gne == "G6PD":
        function_haplotype = pd.read_excel(functional_pheno, sheet_name="Diplotype", index_col=None)
        function_Haplotype_list = function_haplotype.values.tolist()
        function_interpre_pd = pd.read_excel(functional_pheno, sheet_name="Group_class", index_col=None)
        function_interpre_list = function_interpre_pd.values.tolist()
        function_noval_pd = pd.read_excel(functional_pheno, sheet_name="Interpretation", index_col=None)
        function_noval_list = function_noval_pd.values.tolist()
        final_outcome_fn = []
        if diploid_fn == []:
            final_outcome_fn = [' ', 'Normal Function', '']
        elif diploid_fn != []:
            if gender == [1]:
                t1 = gender
                t1 += [x[1] for x in function_Haplotype_list if x[0] == diploid_fn[0]]
                t1 += [y[3] for y in function_interpre_list if (y[0] == t1[0] and y[1] == t1[1])]
                final_outcome_fn = [diploid_fn[0]]
                try:
                    final_outcome_fn += [t1[2]]
                except:
                    final_outcome_fn += ['']
                final_outcome_fn += ['']

            if gender == [2]:
                t2 = gender
                t2 += [x[1] for x in function_Haplotype_list if x[0] == diploid_fn[0]]
                if len(diploid_fn) > 1:
                    t2 += [x[1] for x in function_Haplotype_list if x[0] == diploid_fn[1]]
                else:
                    t2 += [' ']
                t2 += [y[3] for y in function_interpre_list if (y[0] == t2[0] and y[1] == t2[1] and y[2] == t2[2])]
                final_outcome_fn = [diploid_fn]
                final_outcome_fn += [t2[2]]
                final_outcome_fn += ['']

        return final_outcome_fn

