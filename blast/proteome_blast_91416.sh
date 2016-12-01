{\rtf1\ansi\ansicpg1252\cocoartf1347\cocoasubrtf570
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\paperw15840\paperh24480\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\fs24 \cf0 #thesis proteome BLAST\
#Sept 14 2016\
\
ssh -i ~/BLAST-Key.pem ubuntu@\
\
aws s3 cp s3://lclark-bio-data/thesis/0316_ProteomeDb.fasta ~/\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural
\cf0 aws s3 cp s3://lclark-bio-data/thesis/transcriptomes_trimmed_db.fasta ~/\
\
makeblastdb -in transcriptomes_trimmed_db.fasta -dbtype prot -out transcriptomes_trimmed_db -title transcriptomes_trimmed_db\
\
blastp -db transcriptomes_trimmed_db -query 0316_ProteomeDb.fasta -evalue 10e-5 -out venom_homologs.csv -outfmt 10 -max_target_seqs 10000000000\
\
mv venom_homologs.csv scripts/python\
mv transcriptomes_trimmed_db scripts/python\
\
python fullPipeline.py transcriptomes_trimmed_db venom_homologs.csv\
\
aws s3 cp venom_homologs.csv s3://lclark-bio-data/thesis/\
aws s3 cp venom_homologs.fasta s3://lclark-bio-data/thesis/}