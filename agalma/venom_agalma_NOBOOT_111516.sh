#AMI: agalma_AllData_uploaded
#N. Virginia
ssh -i ~/agalma_key.pem ubuntu@ec2-54-173-103-151.compute-1.amazonaws.com

rm *.fasta

#remove previous diagnostics
agalma diagnostics delete 1
agalma diagnostics delete 2
agalma diagnostics delete 3

#upload data
aws s3 cp s3://lclark-bio-data/thesis/venom_untranslated/ARC_v.fasta ~/agalma/data
aws s3 cp s3://lclark-bio-data/thesis/venom_untranslated/DRY_v.fasta ~/agalma/data
aws s3 cp s3://lclark-bio-data/thesis/venom_untranslated/LAZ_v.fasta ~/agalma/data
aws s3 cp s3://lclark-bio-data/thesis/venom_untranslated/LRE_v.fasta ~/agalma/data
aws s3 cp s3://lclark-bio-data/thesis/venom_untranslated/LRU_v.fasta ~/agalma/data
aws s3 cp s3://lclark-bio-data/thesis/venom_untranslated/LSP_v.fasta ~/agalma/data
aws s3 cp s3://lclark-bio-data/thesis/venom_untranslated/PER_v.fasta ~/agalma/data
aws s3 cp s3://lclark-bio-data/thesis/venom_untranslated/PHO_v.fasta ~/agalma/data
aws s3 cp s3://lclark-bio-data/thesis/venom_untranslated/PLE_v.fasta ~/agalma/data
aws s3 cp s3://lclark-bio-data/thesis/venom_untranslated/SCY_v.fasta ~/agalma/data
aws s3 cp s3://lclark-bio-data/thesis/venom_untranslated/SIC_v.fasta ~/agalma/data

cd data
agalma catalog insert --id ARC_v --paths ARC_v.fasta --species "Austrarchaea mainae" --ncbi_id 1028200 --itis_id 852634
agalma catalog insert --id DRY_v --paths DRY_v.fasta --species "Drymusa serrana" --ncbi_id 571550
agalma catalog insert --id LAZ_v --paths LAZ_v.fasta --species "Loxosceles arizonica" --ncbi_id 196454 --itis_id 859845
agalma catalog insert --id SIC_v --paths SIC_v.fasta --species "Sicarius dolichocephalus" --ncbi_id 571538 --itis_id 866935
agalma catalog insert --id PER_v --paths PER_v.fasta --species "Periegops suterii" --ncbi_id 440353 --itis_id 864886
agalma catalog insert --id PHO_v --paths PHO_v.fasta --species "Physocyclus mexicanus" --itis_id 865305
agalma catalog insert --id PLE_v --paths PLE_v.fasta --species "Plectreurys tristis" --ncbi_id 33319 --itis_id 865542
agalma catalog insert --id LRE_v --paths LRE_v.fasta --species "Loxosceles reclusa" --ncbi_id 6921 --itis_id 859907
agalma catalog insert --id SCY_v --paths SCY_v.fasta --species "Scytodes thoracica" --ncbi_id 1112478 --itis_id 866750
agalma catalog insert --id LRU_v --paths LRU_v.fasta --species "Loxosceles rufescens" --ncbi_id 571528 --itis_id 859921
agalma catalog insert --id LSP_v --paths LSP_v.fasta --species "Loxosceles spinulosa" --ncbi_id 571532 --itis_id 865542

cd ../scratch
agalma postassemble --id ARC_v --external
agalma postassemble --id DRY_v --external
agalma postassemble --id LAZ_v --external
agalma postassemble --id LRE_v --external
agalma postassemble --id LRU_v --external
agalma postassemble --id LSP_v --external
agalma postassemble --id PER_v --external
agalma postassemble --id PHO_v --external
agalma postassemble --id PLE_v --external
agalma postassemble --id SCY_v --external
agalma postassemble --id SIC_v --external

agalma load --id ARC_v
agalma load --id DRY_v
agalma load --id LAZ_v
agalma load --id LRE_v
agalma load --id LRU_v
agalma load --id LSP_v
agalma load --id PER_v
agalma load --id PHO_v
agalma load --id PLE_v
agalma load --id SCY_v
agalma load --id SIC_v

export LOAD_IDS="15 16 17 18 19 20 21 22 23 24 25"

agalma homologize --id VenomNB 15 16 17 18 19 20 21 22 23 24 25

agalma multalign --id VenomNB
agalma genetree --id VenomNB
agalma treeprune --id VenomNB 
agalma multalign --id VenomNB 
agalma supermatrix --id VenomNB --proportion 0.6 
agalma speciestree --id VenomNB --raxml_flags="-o Austrarchaea_mainae" 

cd ../
agalma report --id VenomNB --outdir reports/VenomNB
agalma resources --id VenomNB --outdir reports/VenomNB
agalma phylogeny_report --id Venom --outdir reports/Venom

#download files to desktop
scp -rp -i agalma_key.pem ubuntu@ec2-54-173-103-151.compute-1.amazonaws.com:~/agalma/reports/VenomNB ~/Desktop/