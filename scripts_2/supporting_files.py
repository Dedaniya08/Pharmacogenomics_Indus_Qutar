"""Supporting files"""


def check_for_list_element(test_list):
    for element in test_list:
         if isinstance(element, list) == True:
              return True
    return False


def noval_haplotype(start_allele_cluster, folder):
    """Tag the noval haplotype and replace the start allele"""
    if folder == "CYP2C19":
        new_happ_cluster = ['*2', '*3']
        if start_allele_cluster == new_happ_cluster:
            start_allele_cluster = ['Noval_CYP2C19_Haplotype1']
        new_happ_cluster2 = ['*2', '*17']
        if start_allele_cluster == new_happ_cluster2:
            start_allele_cluster = ['Noval_CYP2C19_Haplotype2']

    if folder == "CYP2B6":
        new_happ_cluster = ['*2', '*9']
        if start_allele_cluster == new_happ_cluster:
            start_allele_cluster = ['Noval_CYP2B6_Haplotype1']
        new_happ_cluster2 = ['*2', '*22']
        if start_allele_cluster == new_happ_cluster2:
            start_allele_cluster = ['Noval_CYP2B6_Haplotype2']
        new_happ_cluster3 = ['*9', '*22']
        if start_allele_cluster == new_happ_cluster3:
            start_allele_cluster = ['Noval_CYP2B6_Haplotype3']
        new_happ_cluster4 = ['*3', '*22']
        if start_allele_cluster == new_happ_cluster4:
            start_allele_cluster = ['Noval_CYP2B6_Haplotype4']


    if folder == "CYP2D6":
        cyp2d6cluster = {
            'Noval_Haplotype_1': ['*10', '*74', '*139'],
            'Noval_Haplotype_2': ['*34', '*119'],
            'Noval_Haplotype_3': ['*65', '*74', '*139'],
            'Noval_Haplotype_4': ['*39', '*139'],
            'Noval_Haplotype_5': ['*39', '*48'],
            'Noval_Haplotype_6': ['*33', '*34'],
            'Noval_haplotype_7': ['*10', '*74'],
            'Noval_Haplotype_8': ['*10', '*119'],
            'Noval_Haplotype_9': ['*10', '*74', '*88', '*139'],
            'Noval_Haplotype_10': ['*10', '*74', '*88'],
            'Noval_Haplotype_11': ['*39', '*119'],
            'Noval_Haplotype_12': ['*10', '*48', '*74'],
            'Noval_Haplotype_13': ['*39', '*48', '*139'],
            'Noval_Haplotype_14': ['*8', '*65'],
            'Noval_Haplotype_15': ['*41', '*74'],
            'Noval_Haplotype_16': ['*10', '*139'],
            'Noval_Haplotype_17': ['*39', '*119'],
            'Noval_Haplotype_18': ['*10', '*48', '*74', '*139'],
            'Noval_Haplotype_19': ['*74', '*139'],
            'Noval_Haplotype_20': ['*18', '*65'],
            'Noval_Haplotype_21':['*3', '*10'],
        }
        for cluster_key, cluster_value in cyp2d6cluster.items():
            if start_allele_cluster == cluster_value:
                start_allele_cluster = [cluster_key]

    if folder == "SLCO1B1":
        new_happ_cluster = ['*20', '*24']
        if start_allele_cluster == new_happ_cluster:
            start_allele_cluster = ['Noval_SLCO1B1_Haplotype1']

    if folder == "UGT1A1":
        new_happ_cluster = ['*6', '*80']
        if start_allele_cluster == new_happ_cluster:
            start_allele_cluster = ['Noval_UGT1A1_Haplotype1']
        new_happ_cluster2 = ['*27', '*80']
        if start_allele_cluster == new_happ_cluster2:
            start_allele_cluster = ['Noval_UGT1A1_Haplotype2']

    if folder == "NAT2":
        new_happ_cluster = ['*5', '*5A', '*5D', '*5k', '*5S', '*5V', '*7',
                            '*7A', '*7B', '*7E', '*11', '*11A', '*13', '*13A']
        new_happ_cluster2 = ['*6', '*6A', '*6B', '*13', '*13A', '*19']
        new_happ_cluster3 = ['*6', '*6A', '*6B', '*6C', '*6F', '*12', '*12A',
                             '*12B', '*13', '*13A', '*19']
        new_happ_cluster4 = ['*5', '*5A', '*5D', '*5K', '*5S', '*5V', '*7',
                             '*7A', '*7B', '*7E', '*11', '*11A', '*13', '*13A'
                             ]
        new_happ_cluster5 = ['*6', '*6A', '*6B', '*6O', '*13', '*13A']
        new_happ_cluster6 = ['*7', '*7A', '*7B', '*7C', '*12', '*12A', '*12B', '*13','*13A']
        new_happ_cluster7 = ['*11','*11A','*12', '*12A', '*12C']
        new_happ_cluster8 = ['*7', '*7A', '*7B', '*7C', '*12','*12A','*12B', '*13', '*13A']
        new_happ_cluster9 = ['*6', '*6B', '*6F', '*12', '*12A']
        new_happ_cluster10 = ['*5', '*5A', '*5D', '*5K', '*5V', '*11', '*11A', '*13', '*13A',
                              '*6', '*6B', '*6F', '*12', '*12A']
        new_happ_cluster11 = ['*5', '*5C', '*5D', '*5E', '*5J', '*5K', '*5Q', '*5R', '*5T', '*6', '*6A',
                              '*6B', '*6C', '*6F', '*12', '*12A', '*12B', '*13', '*13A']
        new_happ_cluster12 = ['*6', '*6A', '*6B', '*6E', '*6N', '*11', '*11A', '*13', '*13A']
        new_happ_cluster13 = ['*5', '*5A', '*5D', '*5E', '*5J', '*5K', '*5V', '*6', '*6A',
                              '*6B','*6E', '*6N', '*11', '*11A', '*13', '*13A']
        new_happ_cluster14 = ['*6', '*6A','*6B', '*6C','*6F', '*6O', '*12', '*12A', '*12B', '*13', '*13A']
        new_happ_cluster15 = ['*5', '*5A', '*5B','*5C', '*5D', '*5G','*5K', '*5T', '*5V', '*11',
                              '*11A', '*12', '*12A', '*12B', '*12C', '*12M', '*13', '*13A', '*19']
        new_happ_cluster16 = ['*6', '*6A', '*6B', '*6E', '*6N', '*11', '*11A', '*13', '*13A','*19']


        if start_allele_cluster == new_happ_cluster:
            start_allele_cluster = ['Noval_NAT2_Haplotype1']
        if start_allele_cluster == new_happ_cluster2:
            start_allele_cluster = ['Noval_NAT2_Haplotype2']
        if start_allele_cluster == new_happ_cluster3:
            start_allele_cluster = ['Noval_NAT2_Haplotype3']
        if start_allele_cluster == new_happ_cluster4:
            start_allele_cluster = ['Noval_NAT2_Haplotype4']
        if start_allele_cluster == new_happ_cluster5:
            start_allele_cluster = ['Noval_NAT2_Haplotype5']
        if start_allele_cluster == new_happ_cluster6:
            start_allele_cluster = ['Noval_NAT2_Haplotype6']
        if start_allele_cluster == new_happ_cluster7:
            start_allele_cluster = ['Noval_NAT2_Haplotype7']
        if start_allele_cluster == new_happ_cluster8:
            start_allele_cluster = ['Noval_NAT2_Haplotype8']
        if start_allele_cluster == new_happ_cluster9:
            start_allele_cluster = ['Noval_NAT2_Haplotype9']
        if start_allele_cluster == new_happ_cluster10:
            start_allele_cluster = ['Noval_NAT2_Haplotype10']
        if start_allele_cluster == new_happ_cluster11:
            start_allele_cluster = ['Noval_NAT2_Haplotype11']
        if start_allele_cluster == new_happ_cluster12:
            start_allele_cluster = ['Noval_NAT2_Haplotype12']
        if start_allele_cluster == new_happ_cluster13:
            start_allele_cluster = ['Noval_NAT2_Haplotype13']
        if start_allele_cluster == new_happ_cluster14:
            start_allele_cluster = ['Noval_NAT2_Haplotype14']
        if start_allele_cluster == new_happ_cluster15:
            start_allele_cluster = ['Noval_NAT2_Haplotype15']
        if start_allele_cluster == new_happ_cluster16:
            start_allele_cluster = ['Noval_NAT2_Haplotype16']

    if folder == "DPYD":
        dpyd_dict = {
            'Noval_Haplotype_1': ['c.1627A>G (*5)', 'c.1775G>A'],
            'Noval_Haplotype_2': ['c.1627A>G (*5)', 'c.2194G>A(*6)'],
            'Noval_Haplotype_3': ['c.496A>G', 'c.2279C>T'],
            'Noval_Haplotype_5':  ['c.85T>C (*9A)', 'c.1627A>G (*5)'],
            'Noval_Haplotype_12': ['c.85T>C (*9A)', 'c.496A>G'],
            'Noval_Haplotype_13': ['c.85T>C (*9A)', 'c.1896T>C'],
            'Noval_Haplotype_14': ['c.85T>C (*9A)', 'c.775A>G'],
            'Noval_Haplotype_15': ['c.85T>C (*9A)', 'c.967G>A'],
            'Noval_Haplotype_16': ['c.85T>C (*9A)', 'c.2194G>A (*6)'],
            'Noval_Haplotype_17': ['c.85T>C (*9A)', 'c.1129-5923C>G, c.1236G>A (HapB3)'],
            'Noval_Haplotype_18': ['c.1627A>G (*5)', 'c.2194G>A (*6)'],
            'Noval_Haplotype_19': ['c.85T>C (*9A)', 'c.775A>G'],
            'Noval_Haplotype_20': ['c.85T>C (*9A)', 'c.2846A>T'],
            'Noval_Hapotype_21': ['c.85T>C (*9A)', 'c.967G>A'],
            'Noval_Haplotype_22': ['c.85T>C (*9A)', 'c.2279C>T'],
            'Noval_Haplotype_23': ['c.1905+1G>A (*2A)', 'c.1627A>G (*5)'],
            'Noval_Haplotype_6': ['c.85T>C (*9A)', 'c.1627A>G (*5)', 'c.2194G>A (*6)'],
            'Noval_Haplotype_7': ['c.85T>C (*9A)', 'c.496A>G', 'c.1627A>G (*5)'],
            'Noval_Haplotype_8': ['c.85T>C (*9A)', 'c.496A>G', 'c.1896T>C', 'c.2194G>A (*6)'],
            'Noval_Haplotype_9': ['c.85T>C (*9A)', 'c.496A>G', 'c.2194G>A (*6)'],
            'Noval_Haplotype_10': ['c.85T>C (*9A)', 'c.496A>G', 'c.2194G>A (*6)', 'c.2639G>T'],
            'Noval_Haplotype_11': ['c.85T>C (*9A)', 'c.703C>T (*8)', 'c.1896T>C'],
            'Noval_Haplotype_24': ['c.496A>G', 'c.1627A>G (*5)'],
            'Noval_Haplotype_25': ['c.1627A>G (*5)', 'c.1896T>C'],
            'Noval_Haplotype_26': ['c.85T>C (*9A)', 'c.496A>G', 'c.1896T>C'],
            'Noval_Haplotype_27': ['c.1260T>A', 'c.1577C>G', 'c.3061G>C']
        }
        for cluster_keys, cluster_value in dpyd_dict.items():
            if start_allele_cluster == dpyd_dict[cluster_keys]:
                start_allele_cluster = [cluster_keys]

        if check_for_list_element(start_allele_cluster) == True:
            start_allele_cluster = start_allele_cluster[0]
            for cluster_keys, cluster_value in dpyd_dict.items():
                if start_allele_cluster == dpyd_dict[cluster_keys]:
                    start_allele_cluster = [cluster_keys]
    return start_allele_cluster


def removing_cluster(start_allele_cluster, folder):
    """removing the sub start allele from the cluster"""
    if folder == "TPMT":
        cluster_1 = ['*3A', '*3B', '*3C']
        if start_allele_cluster == cluster_1:
            start_allele_cluster = ['*3A']

    if folder == "NAT2":
        cluster_1 = ['*5', '*5A', '*5B', '*5C', '*5D', '*5E', '*5G', '*5J', '*5K',
                     '*5Q', '*5R', '*5T', '*5U', '*5V', '*6', '*6A', '*6B', '*6C',
                     '*6E', '*6F', '*6N', '*6R', '*11', '*11A', '*12', '*12A',
                     '*12B', '*12C', '*12M', '*13', '*13A']
        cluster_2 = ['*5', '*5A', '*5B', '*5C', '*5D', '*5E', '*5Q', '*6', '*6B',
                     '*6E', '*6F', '*11', '*11A', '*12', '*12A', '*12C']
        cluster_3 = ['*5', '*5A', '*5B', '*5C', '*5D', '*5G', '*5K', '*5T', '*5V',
                     '*11', '*11A', '*12', '*12A', '*12B', '*12C', '*12M', '*13', '*13A']
        cluster_4 = ['*5', '*5A', '*5B', '*5C', '*5D', '*11', '*11A', '*12', '*12A', '*12C']
        cluster_5 = ['*5', '*5A', '*5D', '*11', '*11A']
        cluster_6 = ['*5', '*5C', '*5D', '*12', '*12A']
        cluster_7 = ['*6', '*6A', '*6B', '*6C', '*6F', '*12', '*12A', '*12B', '*13', '*13A']
        cluster_8 = ['*6', '*6A', '*6B', '*6J', '*6S', '*7', '*7A', '*7B', '*13', '*13A']
        cluster_14 = ['*6', '*6A', '*6B', '*13', '*13A']
        cluster_9 = ['*6', '*6B']
        cluster_10 = ['*12', '*12A', '*12B', '*13', '*13A']
        cluster_15 = ['*12', '*12A']
        cluster_11 = ['*13', '*13A']
        cluster_12 = ['*7', '*7A', '*7B', '*13', '*13A']
        cluster_13 = ['*7', '*7A']

        if start_allele_cluster == cluster_1:
            start_allele_cluster = ['*5R']
        if start_allele_cluster == cluster_2:
            start_allele_cluster = ['*5R']
        if start_allele_cluster == cluster_3:
            start_allele_cluster = ['*5G']
        if start_allele_cluster == cluster_4:
            start_allele_cluster = ['*5B']
        if start_allele_cluster == cluster_5:
            start_allele_cluster = ['*5B']
        if start_allele_cluster == cluster_6:
            start_allele_cluster = ['*5C']
        if start_allele_cluster == cluster_7:
            start_allele_cluster = ['*6C']
        if start_allele_cluster == cluster_8:
            start_allele_cluster = ['*6J']
        if start_allele_cluster == cluster_9:
            start_allele_cluster = ['*6']
        if start_allele_cluster == cluster_14:
            start_allele_cluster = ['*6A']
        if start_allele_cluster == cluster_10:
            start_allele_cluster = ['*12B']
        if start_allele_cluster == cluster_15:
            start_allele_cluster = ['*12']
        if start_allele_cluster == cluster_11:
            start_allele_cluster = ['*13']
        if start_allele_cluster == cluster_12:
            start_allele_cluster = ['*7B']
        if start_allele_cluster == cluster_13:
            start_allele_cluster = ['*7']

    if folder == "SLCO1B1":
        cluster_1 = ['*5', '*15', '*37']
        cluster_2 = ['*4', '*14', '*37']
        cluster_4 = ['*19', '*20', '*37']
        cluster_3 = ['*24', '*37']

        if start_allele_cluster == cluster_1:
            start_allele_cluster = ['*15']
        if start_allele_cluster == cluster_2:
            start_allele_cluster = ['*14']
        if start_allele_cluster == cluster_4:
            start_allele_cluster = ['*20']
        if start_allele_cluster == cluster_3:
            start_allele_cluster = ['*24']

        type_1 = ['*19', '*20', '*37']
        if all(x in start_allele_cluster for x in type_1):
            start_allele_cluster.remove('*19')
            start_allele_cluster.remove('*37')

    if folder == "CYP2C19":
        cluster_1 = ['*2', '*35', '*38']
        cluster_2 = ['*35', '*38']
        cluster_3 = ['*2', '*35']
        cluster_4 = ['*1', '*2']
        cluster_5 = ['*1', '*17']
        cluster_6 = ['*1', '*24']
        cluster_7 = ['*1', '*3']

        if start_allele_cluster == cluster_1:
            start_allele_cluster = ['*2']
        if start_allele_cluster == cluster_2:
            start_allele_cluster = ['*35']
        if start_allele_cluster == cluster_3:
            start_allele_cluster = ['*2']
        if start_allele_cluster == cluster_4:
            start_allele_cluster = ['*2']
        if start_allele_cluster == cluster_5:
            start_allele_cluster = ['*17']
        if start_allele_cluster == cluster_6:
            start_allele_cluster = ['*24']
        if start_allele_cluster == cluster_7:
            start_allele_cluster = ['*3']

        type_1 = ['*1', '*2']
        if all(x in start_allele_cluster for x in type_1):
            start_allele_cluster.remove('*1')

    if folder == "CYB2B6":
        cluster_1 = ['*8', '*9']
        if start_allele_cluster == cluster_1:
            start_allele_cluster = ['*13']
        cluster_2 = ['*4','*6','*9']
        if start_allele_cluster == cluster_2:
            start_allele_cluster = ['*6']

    if folder == "CYP4F2":
        cluster_1 = ['*2', '*3']
        if start_allele_cluster == cluster_1:
            start_allele_cluster = ['*3']

    if folder == "CYP2D6":
        cluster_1 = ['*2', '*10', '*34', '*39', '*41', '*65', '*69', '*119']
        cluster_2 = ['*2', '*10', '*34', '*39', '*65']
        cluster_3 = ['*2', '*34', '*39', '*48', '*102']
        cluster_4 = ['*2', '*34', '*39', '*41', '*119']
        cluster_5 = ['*2', '*34', '*39']

        if start_allele_cluster == cluster_1:
            start_allele_cluster = ['*69']
        if start_allele_cluster == cluster_2:
            start_allele_cluster = ['*65']
        if start_allele_cluster == cluster_3:
            start_allele_cluster = ['*102']
        if start_allele_cluster == cluster_4:
            start_allele_cluster = ['*41']
        if start_allele_cluster == cluster_5:
            start_allele_cluster = ['*2']


        if all(x in start_allele_cluster for x in cluster_2):
            start_allele_cluster = [e for e in start_allele_cluster
                                    if e not in ('*2', '*10', '*34', '*39')]

        if all(x in start_allele_cluster for x in cluster_4):
            start_allele_cluster = [e for e in start_allele_cluster
                                    if e not in ('*2', '*34', '*39', '*119')]

        if all(x in start_allele_cluster for x in cluster_5):
            start_allele_cluster = [e for e in start_allele_cluster if e not in ('*34', '*39')]

        type_1 = ['*10', '*39']
        if all(x in start_allele_cluster for x in type_1):
            start_allele_cluster.remove('*39')

    start_allele_cluster = noval_haplotype(start_allele_cluster, folder)

    return start_allele_cluster
