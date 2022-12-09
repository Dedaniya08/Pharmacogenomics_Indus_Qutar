"""main function for clasifing the start allele"""
from supporting_files import removing_cluster


def dict_allele(dict_allele_table, sample_number, dict_chr1, dict_chr2, folder):
    total_list_of_start_allele_checked = []
    dict_allele_table.index.name = None
    key_columns = dict_allele_table.columns.values
    start_allele = dict_allele_table.index.values
    start_allele_chr1_final = []
    start_allele_chr2_final = []

    for i, j in zip(range(len(dict_allele_table)), start_allele):
        row = dict_allele_table.values[i]
        dict_raw = dict(zip(key_columns, row))
        final_dict_2 = {}
        for key, value in dict_raw.items():
            if str(value) != 'nan':
                final_dict_2[key] = [value]
        start_list = [j, final_dict_2]
        # convertering the multiallic info IUPAC nucliotide
        mapper = {'R':'A,G', 'Y':'C,T', 'S':'G,C', 'W':'A,T',
                  'K':'G,T', 'M':'A,C', 'B':'C,G,T', 'H':'A,C,T',
                  'V':'A,C,G', 'N':'A,C,T,G'}
        final_dict = {k: [mapper.get(val, val) for val in v] for k,
                        v in final_dict_2.items()}
        start_list = [j, final_dict]
        for item, value in final_dict.items():
            value = value[0].split(',')
            final_dict[item] = value

        start_confirm = False
        start_confirm2 = False
        start_allele_chr1 = []
        start_allele_chr2 = []

        # f = open(sample_number + ".txt", 'a')
        # sys.stdout = f

        # First chromosome
        def all_keys_available(d1, d2):
            return all(k in d2 for k in d1)

        res = all_keys_available(final_dict, dict_chr1)
        if res is True:
            total_list_of_start_allele_checked.append(j)
            for key in final_dict.keys():
                if key in dict_chr1.keys():
                    nf = [x for x in final_dict[key] if x in dict_chr1[key]]
                    if not nf:
                        start_confirm = False
                        break
                    else:
                        start_confirm = True

            if start_confirm is True:
                start_allele_chr1 = j
        else: start_confirm = False

        #second chromosome

        res2 = all_keys_available(final_dict, dict_chr2)
        if res2 is True:
            # print([(k, final_dict[k]) for k in final_dict], [(k, dict_chr2[k]) for k in final_dict])
            for key in final_dict.keys():
                if key in dict_chr2.keys():
                    if key in dict_chr2.keys():
                        nf2 = [x for x in final_dict[key] if x in dict_chr2[key]]
                        if not nf2:
                            start_confirm2 = False
                            break
                        else:
                            start_confirm2 = True
            # print("******************************************")
            if start_confirm2 is True:
                start_allele_chr2 = j
        else: start_confirm2 = False

        # f.close
        start_allele_chr1_final.append(start_allele_chr1)
        start_allele_chr2_final.append(start_allele_chr2)

    start_allele_chr1_final = [x for x in start_allele_chr1_final if x != []]
    start_allele_chr2_final = [x for x in start_allele_chr2_final if x != []]

    # Removing the cluster SNPs
    start_allele_chr1_final = removing_cluster(start_allele_chr1_final, folder)
    start_allele_chr2_final = removing_cluster(start_allele_chr2_final, folder)

    # Functionality of haploid and diploid
    happ_1 = start_allele_chr1_final[:]
    happ_2 = start_allele_chr2_final[:]

    # Multi list to single list
    deploid_pheno = happ_1 + happ_2


    output_array = [sample_number, folder, start_allele_chr1_final, start_allele_chr2_final]
    return output_array, deploid_pheno, total_list_of_start_allele_checked
