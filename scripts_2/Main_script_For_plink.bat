



Z:/PgX/Scripts/plink/plink.exe --file Z:/PgX/Genotype_raw/Run --extract Z:/PgX/Supporting_file/SNPs_plink/final_list_V3_04102021.txt --make-bed --out Z:/PgX/temp_files/Run_matrix_extract

PAUSE

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract --update-map Z:/PgX/Supporting_file/SNPs_plink/SNP_NAME_UPDATE.txt --update-name --make-bed --out Z:/PgX/temp_files/Run_matrix_extract_SNP_UPDATE

PAUSE

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_SNP_UPDATE --flip Z:/PgX/Supporting_file/flipstrand/SNP_TO_FLIP_2.txt  --make-bed --out Z:/PgX/temp_files/Run_matrix_extract_flip

PAUSE

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_flip --chr 1 --make-bed --out Z:/PgX/linux_shapeit/plink_shapeit_raw/Run_matrix_extract_1

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_flip --chr 2 --make-bed --out Z:/PgX/linux_shapeit/plink_shapeit_raw/Run_matrix_extract_2

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_flip --chr 4 --make-bed --out Z:/PgX/linux_shapeit/plink_shapeit_raw/Run_matrix_extract_4

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_flip --chr 6 --make-bed --out Z:/PgX/linux_shapeit/plink_shapeit_raw/Run_matrix_extract_6

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_flip --chr 7 --make-bed --out Z:/PgX/linux_shapeit/plink_shapeit_raw/Run_matrix_extract_7

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_flip --chr 8 --make-bed --out Z:/PgX/linux_shapeit/plink_shapeit_raw/Run_matrix_extract_8

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_flip --chr 10 --make-bed --out Z:/PgX/linux_shapeit/plink_shapeit_raw/Run_matrix_extract_10

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_flip --chr 12 --make-bed --out Z:/PgX/linux_shapeit/plink_shapeit_raw/Run_matrix_extract_12

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_flip --chr 13 --make-bed --out Z:/PgX/linux_shapeit/plink_shapeit_raw/Run_matrix_extract_13

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_flip --chr 16 --make-bed --out Z:/PgX/linux_shapeit/plink_shapeit_raw/Run_matrix_extract_16

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_flip --chr 18 --make-bed --out Z:/PgX/linux_shapeit/plink_shapeit_raw/Run_matrix_extract_18

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_flip --chr 19 --make-bed --out Z:/PgX/linux_shapeit/plink_shapeit_raw/Run_matrix_extract_19

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_flip --chr 22 --make-bed --out Z:/PgX/linux_shapeit/plink_shapeit_raw/Run_matrix_extract_22

Z:/PgX/Scripts/plink/plink.exe --bfile Z:/PgX/temp_files/Run_matrix_extract_flip --chr 23 --make-bed --out Z:/PgX/linux_shapeit/plink_shapeit_raw/Run_matrix_extract_23


PAUSE

