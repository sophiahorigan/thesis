# -*- coding: utf-8 -*-
"""
Created on Tues May 24 09:24:52 2016

@author: thatbudakguy
"""

# setup test data

#
# findLongestSeq()
#

example_rows = [
['sample1','FJKDHGSKJGHLSKULSDUHRGLSIHUG'],
['sample1','KLSURHGLFIAUHRFLAIWUEHFLAIWUEHFALWEI'],
['sample2','CIVAWUHEFLIAUSBECLIASUEFHLAKEUFHLASIEUFGAKLSEFULAEWK'],
['sample2','CIVAWUHEFLAKLSEFULAEWK'],
['sample3','KSLADJFHALKSUDHFALKSDUHFALKS'],
['sample3','DSLKFAJLSFJ'],
['sample4','SDJKFHALSKDUFHASLKFHASLKJFHASDLKJH'],
['sample5','SKDJFHALKSDJFHFJKGHSLDKFGJHDSKLFJGHSLDKF'],
['sample6','DSSDHJFBAGKJDHFKSDGHK']
]

expected_longest_rows = [
['sample1','KLSURHGLFIAUHRFLAIWUEHFLAIWUEHFALWEI'],
['sample2','CIVAWUHEFLIAUSBECLIASUEFHLAKEUFHLASIEUFGAKLSEFULAEWK'],
['sample3','KSLADJFHALKSUDHFALKSDUHFALKS'],
['sample4','SDJKFHALSKDUFHASLKFHASLKJFHASDLKJH'],
['sample5','SKDJFHALKSDJFHFJKGHSLDKFGJHDSKLFJGHSLDKF'],
['sample6','DSSDHJFBAGKJDHFKSDGHK']
]

#
# splitLinearSeqids()
#

example_linear_seqids = [
'sample1',
'sample2',
'sample3>sample3429',
'sample4>sample3s>__45-dfs_d34|df3',
'sample5>sdf>32off>dfsu0sd$',
'sample6>r32n@'
]

expected_split_linear_seqids = [
'sample1',
'sample2',
'sample3',
'sample3429',
'sample4',
'sample3s',
'__45-dfs_d34|df3',
'sample5',
'sdf',
'32off',
'dfsu0sd$',
'sample6',
'r32n@'
]

#
# reduceNames()
#

example_search_seqids = [
'sample1',
'sample2',
'sample7',
'sample4',
'sample5',
'sample8'
]

example_db_seqids = [
'sample1',
'sample2',
'sample3',
'sample4',
'sample5',
'sample6',
'sample7',
'sample8'
]

example_db_seqs = [
'FJKDHGSKJGHLSKULSDUHRGLSIHUG',
'CIVAWUHEFLIAUSBECLIASUEFHLAKEUFHLASIEUFGAKLSEFULAEWK',
'KSLADJFHALKSUDHFALKSDUHFALKS',
'SDJKFHALSKDUFHASLKFHASLKJFHASDLKJH',
'SKDJFHALKSDJFHFJKGHSLDKFGJHDSKLFJGHSLDKF',
'DSSDHJFBAGKJDHFKSDGHK',
'SDKJFHALKSDFBASLKJFBASLDKDSAKLJDS',
'DFLKJSDFDJKGHSLKDHGSKDJHGKSDJHFGSLKDJHFGG'
]

expected_reduced_data = {
'output_seq_ids':[
'sample1',
'sample2',
'sample4',
'sample5',
'sample7',
'sample8'],
'output_seqs':[
'FJKDHGSKJGHLSKULSDUHRGLSIHUG',
'CIVAWUHEFLIAUSBECLIASUEFHLAKEUFHLASIEUFGAKLSEFULAEWK',
'SDJKFHALSKDUFHASLKFHASLKJFHASDLKJH',
'SKDJFHALKSDJFHFJKGHSLDKFGJHDSKLFJGHSLDKF',
'SDKJFHALKSDFBASLKJFBASLDKDSAKLJDS',
'DFLKJSDFDJKGHSLKDHGSKDJHGKSDJHFGSLKDJHFGG'
]
}

#
# findMissingSeqs()
#

example_names_list = [
'sample1',
'sample2',
'sample3',
'sample3.5',
'sample4',
'sample5',
'sample6',
'sample7',
'sample8',
'sample9'
]

example_data_list = [
'sample1',
'sample2',
'sample3',
'sample4',
'sample5',
'sample6'
]

expected_missing_seqs = [
'sample3.5','sample7','sample8','sample9'
]

#
# readCSV()
#

example_csv_files = [
'sample1.csv',
'sample2.csv'
]

expected_csv_input = {
'sample1': [['Lrf_VG_s019_c73942_g1_i1|m.22795','LFSATIFLVGLAIVLQG--THIFVDARRPFWNIAHMVNAIDQIDPFLNRGANAIEFDIVFNSEGIAQQTHHGVPCDCGRLCNRQEDFVKYLDHIRQVTSPGNKEFREQLILLALDLKLQRISVNQAYAAGGDIANKLIDHYWK-RGNSTARAYILLNIPSIRHFDFINGFKHTIIRREGYEKYNDKYGINFTGNDDLEVTRRMLERMNITSNIWQADGITSCFPRGTRRVKDAIRRRDTEGYKYIYKVYSWTLVTYSAMRRSMRLGVDGIMTNHPERVVYVLGQGYFANRFRMATLEDNPWQKY'],['Phol_VG_s013_c52966_g1_i1|m.7433', 'LFSATIFLVGLAIVLQG--THIFADARRPFWNIAHMVNAIDQIDPFLNRGANAIEFDIVFNSEGIAQQTHHGVPCDCGRLCNRQEDFVKYLDHIRQVTSPGNKEFREQLILLALDLKLQRISVNQAYAAGGDIANKLIDHYWK-RGNSTARAYILLNIPSIRHFDFINGFKHTIIRREGYEEYNDKYGINFTGNDDLEVTRRMLERMNITSNIWQADGITSCFPRGTRRVKDAIRRRDTEGYKYIYKVYSWTLVTYSAMRRSMRLGVDGIMTNHPERV'], ['LAz3_VG_s004_c54163_g1_i1|m.11811', 'KVTTPGTKEFRDQLILLALDLKLQRISVRQAYAAGTDVANKLIDHYWKNKGNSTARAYILLNIPSIRHFDFINGFQHTIVRREGYERYNDKFGINFTGNDDLESTARMLKRMNITSNIWQADGITSCLPRGTRRLRDAIRRRDTPQNKYIYKVYSWTLVTYFAMRRSMRLGVDGIMTNHPERVVNILNERNFANRFRMATIEDNPWEKYRP']],
'sample2': [['Phol_VG_s013_c73238_g1_i3|m.19224','LLYVTLILGCWSALSESAETDVAERANKRPVWIMGHMVNAVAQIDEFVNLGANSIETDVSFDKNANPEYTYHGIPCDCGRTCTKWENFNDFLKGLRKATTPGDSKYHEKLILVVFDLKTGSLYDNQAYDAGTKLAKNLLQHYW-NNGNNGGRAYIVLSIPNLNHYKLIAGFKDTL-KSEGHEDLLEKVGHDFSGNDDIPDVENAYKKAGVTGHVWQSDGITNCLPRTLKRVRLAIANRDSGSG-IINKVYYWTVDKRSTTRDSLDAGVDGIMTNYPDVIADVLSESAYKNKYKIATYEDNPWETFK'],['SPicunLeufu5', 'YVGIGANGLEMDVSFDSNGKAEYTYHGVPCDCFRSCTRSEKFSVYLDYVRQITTPGNPKFRENLIFLIMDLKLNDLEPHALYNAGIDIADQLSKNYWKDDGK--ARAHFLISIPYVSQTAFVDGFRWWF-EKKGLEKYYEKIGWDFSANEDLNSIQATYQKLNITGHTWQSDGITNCLTRGTERLTQAIQKRDTPGNSYLNKVYAWSLDKYGSIKQALDLGVDGVMSNYPQRMVEILSEGTYLERFRLATYEDNPWETFK'], ['LAz3_VG_s004_c27026_g1_i2|m.3016', 'SETFERVDNRRPIWNMGHMVNEIYQIDEFVDLGANSIETDITFDENAVAEYSYHGVPCDCRRWCHKWEYVNDFLNALRRATTPGDSKYRRELVLVVFDLKTGDLSSSTANKGGKLFAQKLLQHYW-NGGNNGGRAYIIISIPDIDHYAFISGFRNAL-KEAGHEELLEKVGYDFSGNDDLNSIRNALHKAGVKDKEHVWQSDGITNCILRGLSRVREAVRNRDS-SNGYINKVYYWTIEKYVSVRDALDAGVDGIMTNEPDVIVNVLNEKAYKQRFRLANYDDNPWETYQ']]
}

#
# readTXT()
#

example_txt_files = [
'sample1.txt',
'sample2.txt'
]

expected_txt_input = {
'sample2':['PerM1_VG_s008_c50163_g1_i1|m.13808-DECOY_SIC','sp|REF_HEVBR|_SCM'],
'sample1':['sp|K2C1_HUMAN|_PHO','sp|REF_HEVBR|_SCO']
}

#
# readFASTA()
#

example_fasta_files = [
'sample1.fasta',
'sample2.fasta'
]

expected_fasta_input = {
'sample1':['Lrf_VG_s019_c73942_g1_i1|m.22795','LFSATIFLVGLAIVLQG--THIFVDARRPFWNIAHMVNAIDQIDPFLNRGANAIEFDIVFNSEGIAQQTHHGVPCDCGRLCNRQEDFVKYLDHIRQVTSPGNKEFREQLILLALDLKLQRISVNQAYAAGGDIANKLIDHYWK-RGNSTARAYILLNIPSIRHFDFINGFKHTIIRREGYEKYNDKYGINFTGNDDLEVTRRMLERMNITSNIWQADGITSCFPRGTRRVKDAIRRRDTEGYKYIYKVYSWTLVTYSAMRRSMRLGVDGIMTNHPERVVYVLGQGYFANRFRMATLEDNPWQKY','Phol_VG_s013_c52966_g1_i1|m.7433','LFSATIFLVGLAIVLQG--THIFADARRPFWNIAHMVNAIDQIDPFLNRGANAIEFDIVFNSEGIAQQTHHGVPCDCGRLCNRQEDFVKYLDHIRQVTSPGNKEFREQLILLALDLKLQRISVNQAYAAGGDIANKLIDHYWK-RGNSTARAYILLNIPSIRHFDFINGFKHTIIRREGYEEYNDKYGINFTGNDDLEVTRRMLERMNITSNIWQADGITSCFPRGTRRVKDAIRRRDTEGYKYIYKVYSWTLVTYSAMRRSMRLGVDGIMTNHPERV','LAz3_VG_s004_c54163_g1_i1|m.11811','KVTTPGTKEFRDQLILLALDLKLQRISVRQAYAAGTDVANKLIDHYWKNKGNSTARAYILLNIPSIRHFDFINGFQHTIVRREGYERYNDKFGINFTGNDDLESTARMLKRMNITSNIWQADGITSCLPRGTRRLRDAIRRRDTPQNKYIYKVYSWTLVTYFAMRRSMRLGVDGIMTNHPERVVNILNERNFANRFRMATIEDNPWEKYRP'],
'sample2':['Phol_VG_s013_c73238_g1_i3|m.19224','LLYVTLILGCWSALSESAETDVAERANKRPVWIMGHMVNAVAQIDEFVNLGANSIETDVSFDKNANPEYTYHGIPCDCGRTCTKWENFNDFLKGLRKATTPGDSKYHEKLILVVFDLKTGSLYDNQAYDAGTKLAKNLLQHYW-NNGNNGGRAYIVLSIPNLNHYKLIAGFKDTL-KSEGHEDLLEKVGHDFSGNDDIPDVENAYKKAGVTGHVWQSDGITNCLPRTLKRVRLAIANRDSGSG-IINKVYYWTVDKRSTTRDSLDAGVDGIMTNYPDVIADVLSESAYKNKYKIATYEDNPWETFK','SPicunLeufu5','YVGIGANGLEMDVSFDSNGKAEYTYHGVPCDCFRSCTRSEKFSVYLDYVRQITTPGNPKFRENLIFLIMDLKLNDLEPHALYNAGIDIADQLSKNYWKDDGK--ARAHFLISIPYVSQTAFVDGFRWWF-EKKGLEKYYEKIGWDFSANEDLNSIQATYQKLNITGHTWQSDGITNCLTRGTERLTQAIQKRDTPGNSYLNKVYAWSLDKYGSIKQALDLGVDGVMSNYPQRMVEILSEGTYLERFRLATYEDNPWETFK','LAz3_VG_s004_c27026_g1_i2|m.3016','SETFERVDNRRPIWNMGHMVNEIYQIDEFVDLGANSIETDITFDENAVAEYSYHGVPCDCRRWCHKWEYVNDFLNALRRATTPGDSKYRRELVLVVFDLKTGDLSSSTANKGGKLFAQKLLQHYW-NGGNNGGRAYIIISIPDIDHYAFISGFRNAL-KEAGHEELLEKVGYDFSGNDDLNSIRNALHKAGVKDKEHVWQSDGITNCILRGLSRVREAVRNRDS-SNGYINKVYYWTIEKYVSVRDALDAGVDGIMTNEPDVIVNVLNEKAYKQRFRLANYDDNPWETYQ']
}

#
# splitCSV() and splitFASTA()
#

expected_split_data = {
'output_seq_ids':
['Lrf_VG_s019_c73942_g1_i1|m.22795',
'Phol_VG_s013_c52966_g1_i1|m.7433',
'LAz3_VG_s004_c54163_g1_i1|m.11811'],
'output_seqs':
['LFSATIFLVGLAIVLQG--THIFVDARRPFWNIAHMVNAIDQIDPFLNRGANAIEFDIVFNSEGIAQQTHHGVPCDCGRLCNRQEDFVKYLDHIRQVTSPGNKEFREQLILLALDLKLQRISVNQAYAAGGDIANKLIDHYWK-RGNSTARAYILLNIPSIRHFDFINGFKHTIIRREGYEKYNDKYGINFTGNDDLEVTRRMLERMNITSNIWQADGITSCFPRGTRRVKDAIRRRDTEGYKYIYKVYSWTLVTYSAMRRSMRLGVDGIMTNHPERVVYVLGQGYFANRFRMATLEDNPWQKY',
'LFSATIFLVGLAIVLQG--THIFADARRPFWNIAHMVNAIDQIDPFLNRGANAIEFDIVFNSEGIAQQTHHGVPCDCGRLCNRQEDFVKYLDHIRQVTSPGNKEFREQLILLALDLKLQRISVNQAYAAGGDIANKLIDHYWK-RGNSTARAYILLNIPSIRHFDFINGFKHTIIRREGYEEYNDKYGINFTGNDDLEVTRRMLERMNITSNIWQADGITSCFPRGTRRVKDAIRRRDTEGYKYIYKVYSWTLVTYSAMRRSMRLGVDGIMTNHPERV',
'KVTTPGTKEFRDQLILLALDLKLQRISVRQAYAAGTDVANKLIDHYWKNKGNSTARAYILLNIPSIRHFDFINGFQHTIVRREGYERYNDKFGINFTGNDDLESTARMLKRMNITSNIWQADGITSCLPRGTRRLRDAIRRRDTPQNKYIYKVYSWTLVTYFAMRRSMRLGVDGIMTNHPERVVNILNERNFANRFRMATIEDNPWEKYRP']
}

#
# GreaterThans()
#
some_greaterthans = [
'>Lrf_VG_s019_c73942_g1_i1|m.22795',
'Phol_VG_s013_c52966_g1_i1|m.7433',
'>LAz3_VG_s004_c54163_g1_i1|m.11811',
'LAz3_VG_s004_c54163_g1_i1|m.11811',
'sp|REF_HEVBR|_SCO'
]

no_greaterthans = [
'Lrf_VG_s019_c73942_g1_i1|m.22795',
'Phol_VG_s013_c52966_g1_i1|m.7433',
'LAz3_VG_s004_c54163_g1_i1|m.11811',
'LAz3_VG_s004_c54163_g1_i1|m.11811',
'sp|REF_HEVBR|_SCO'
]

all_greaterthans = [
'>Lrf_VG_s019_c73942_g1_i1|m.22795',
'>Phol_VG_s013_c52966_g1_i1|m.7433',
'>LAz3_VG_s004_c54163_g1_i1|m.11811',
'>LAz3_VG_s004_c54163_g1_i1|m.11811',
'>sp|REF_HEVBR|_SCO'
]

#
# VenomCodes
#
no_venomcodes = [
'Lrf_VG_s019_c73942_g1_i1|m.22795',
'Phol_VG_s013_c52966_g1_i1|m.7433',
'LAz3_VG_s004_c54163_g1_i1|m.11811',
'LAz3_VG_s004_c54163_g1_i1|m.11811',
'sp|REF_HEVBR|_SCO'
]

has_venomcodes = [
'Lrf_VG_s019_c73942_g1_i1|m.22795_TST',
'Phol_VG_s013_c52966_g1_i1|m.7433_TST',
'LAz3_VG_s004_c54163_g1_i1|m.11811_TST',
'LAz3_VG_s004_c54163_g1_i1|m.11811_TST',
'sp|REF_HEVBR|_SCO_TST'
]

#
# replaceSCodes()
#
no_scodes = [
's019_c73942_g1_i1|m.22795_TST',
'c52966_s013_g1_i1|m.7433_TST',
'c54163_g1_i1|m.11811_TST_s004',
's002_c54163_g1_i1|m.11811_TST',
'sp|REF_HEVBR|_SCO_TST'
]

has_scodes = [
'Lrf_VG_s019_c73942_g1_i1|m.22795_TST',
'c52966_Phol_VG_s013_g1_i1|m.7433_TST',
'c54163_g1_i1|m.11811_TST_LAz3_VG_s004',
'Laz1_VG_s002_c54163_g1_i1|m.11811_TST',
'sp|REF_HEVBR|_SCO_TST'
]