### Bitácora gut_microbiomeL4-7



27012021

```shell
#Espacio de trabajo para gutL4-7
/space31/PEG/hoaxaca/gutL4_7
Los datos: /space31/PEG/hoaxaca/gutL4_7/data2/
#Verificar la integridad de mis datos
md5sum *.gz

38e9408c571e5c0969946adc6628f87b  ITA_1.fastq.gz
b4830b0c240d07111538d25b2a521510  ITA_2.fastq.gz
e284537ee3b42fa8e0cd2ee904bb5c96  ITB_1.fastq.gz
8ded2bb9e11f54bd405316e34e76f2b9  ITB_2.fastq.gz
526ec3a289caed26bb8246148f5c1b43  ITC_1.fastq.gz
2bbc0c07a2385e176557cc57fc59116a  ITC_2.fastq.gz
693d83b58bf62016a91756957f3c008f  UIA_1.fastq.gz
2fcd41ab778128ffe493f808285071d6  UIA_2.fastq.gz
da834cd5eb060d48b301d24054ba1cad  UIB_1.fastq.gz
a0868ba433bc90a4eca02d4e4d813219  UIB_2.fastq.gz
218bd45c88ca2d2456d7fd58c15cb811  UIC_1.fastq.gz
081bae41914e47dddd4100c7b118fd29  UIC_2.fastq.gz

#Descomprimir los fastq para limpiar
gunzip *.gz &

##Para OVAI
/space31/PEG/hoaxaca/OVAI/data
#Verificar la integridad de mis datos
md5sum *.gz >> md5sum.txt
#Descomprimir los fastq para limpiar
gunzip *.gz &
```

#### Stats Macrogen

| Sample ID | Total read bases (bp) | Total reads | GC(%) | AT(%) | Q20(%) | Q30(%) |
| --------- | --------------------- | ----------- | ----- | ----- | ------ | ------ |
| ITA       | 13,287,859,268        | 87,999,068  | 35.57 | 64.43 | 97.0   | 92.03  |
| ITB       | 14,275,957,666        | 94,542,766  | 35.63 | 64.37 | 96.89  | 91.78  |
| ITC       | 15,429,987,246        | 102,185,346 | 35.54 | 64.46 | 97.02  | 92.08  |
| UIA       | 14,387,769,844        | 95,283,244  | 36.66 | 63.34 | 96.85  | 91.86  |
| UIB       | 14,320,469,144        | 94,837,544  | 36.2  | 63.8  | 96.93  | 91.89  |
| UIC       | 15,345,650,424        | 101,626,824 | 36.02 | 63.98 | 96.88  | 91.93  |



#### TrimGalore

27012021

```shell
#Limpiar las lecturas para remover adaptadores
  #Para las de instar temprano
#!/bin/bash
nohup trim_galore --fastqc  --retain_unpaired --illumina --paired ../raw_data/ITA_1.fastq ../raw_data/ITA_2.fastq &
nohup trim_galore --fastqc  --retain_unpaired --illumina --paired ../raw_data/ITB_1.fastq ../raw_data/ITB_2.fastq &
nohup trim_galore --fastqc  --retain_unpaired --illumina --paired ../raw_data/ITC_1.fastq ../raw_data/ITC_2.fastq &
  #Para las de instar tardío
nohup trim_galore --fastqc  --retain_unpaired --illumina --paired ../raw_data/UIA_1.fastq ../raw_data/UIA_2.fastq &
nohup trim_galore --fastqc  --retain_unpaired --illumina --paired ../raw_data/UIB_1.fastq ../raw_data/UIB_2.fastq &
nohup trim_galore --fastqc  --retain_unpaired --illumina --paired ../raw_data/UIC_1.fastq ../raw_data/UIC_2.fastq &

chmod u+x trim_galore.sh
nohup ./trim_galore.sh &

#Lo mismo para OVAI
mkdir TrimGalore && cd TrimGalore
trim_galore --fastqc  --retain_unpaired --illumina --paired ../data/OVAI_1.fastq ../data/OVAI_2.fastq

#Pasar los reads limpios al directorio data deacuerdo a las muestras gutL4-7 y OVAI
mv TrimGalore/*_val_?.fq .

#Comprimir los raw data para limpiar espacio del servidor

```

|       | raw reads  | Reads with adapters(%) | Total processed (pb) | Quality-trimmed (bp) | Total filtered (bp)  |
| ----- | ---------- | ---------------------- | -------------------- | -------------------- | -------------------- |
| ITA_1 | 43,999,534 | 16,581,767 (37.7%)     | 6,643,929,634        | 8,249,172 (0.1%)     | 6,611,798,423(99.5%) |
|       |            |                        |                      |                      |                      |
|       |            |                        |                      |                      |                      |
|       |            |                        |                      |                      |                      |
|       |            |                        |                      |                      |                      |
|       |            |                        |                      |                      |                      |
|       |            |                        |                      |                      |                      |
|       |            |                        |                      |                      |                      |
|       |            |                        |                      |                      |                      |





```
gzip UIA_1.fastq.gz &
gzip UIA_2.fastq.gz &
gzip UIC_1.fastq.gz &
gzip UIB_1.fastq.gz &
gzip ITB_1.fastq.gz &
gzip ITB_2.fastq.gz &
gzip ITA_2.fastq.gz &
gzip ITA_1.fastq.gz &
gzip ITC_1.fastq.gz &
gzip UIB_2.fastq.gz &
gzip UIC_2.fastq.gz &
gzip ITC_2.fastq.gz &
```

#### Kraken

280121

```shell
#1.Clasificar las lecturas de OVAI para ver cuantos taxa microbianos hay en ovarios

conda activate kraken2
nohup kraken2 --db /space29/data/kraken/minikraken2_v1_8GB --threads 14 --paired ../data/OVAI_1_val_1.fq ../data/OVAI_2_val_2.fq  --classified-out classreads#.fq --report krakenReads.report --use-mpa-style --output krakenReadsOVAI.out &
 #RESULTS
 90920072 sequences (27291.57 Mbp) processed in 398.809s (13678.7 Kseq/m, 4105.96 Mbp/m).
  2064517 sequences classified (2.27%)
  88855555 sequences unclassified (97.73%)
```

```
nohup kraken2 --db /space29/data/kraken/minikraken2_v1_8GB --threads 14 --paired ../data/OVAI_1_val_1.fq ../data/OVAI_2_val_2.fq  --classified-out classreads#.fq --report
```

#### Metaxa

```
metaxa2 -- Improved Identification and Classification of barcoding genes in environmental datasets
by Johan Bengtsson-Palme, University of Gothenburg
Version: 2.2
```

```shell
nohup metaxa2 -1 rdc_1.fastq -2 rdc_2.fastq --distance 350 --cpu 14 --plus T -o metaxa_rdc.out &
nohup metaxa2 -1 data/OVAI_1_val_1.fq -2 data/OVAI_2_val_2.fq --distance 350 --cpu 14 --plus T -o metaxaOVAI &

#results
#OVAI
Processed 90920072 sequence pairs and discarded 0 pairs of reads.
Low quality first reads:               0
Low quality second reads:              0
Pairs with both reads of low quality:  0
Pairs with both reads of good quality: 90920072
Discarded read pairs:                  0
Kept read pairs (high quality):        90920072
umber of sequences in input file:              90920072
Sequences detected as SSU rRNA by Metaxa:       25186
  On main strand:               12255
  On complementary strand:      12931
Number of SSU rRNA sequences to be classified by Metaxa:        25187
Number of SSU rRNA having at least one database match:          25184
Number of SSU rRNA successfully classified by Metaxa:           25186
Number of uncertain classifications of SSU rRNA sequences:      0
Total number of classifications made by Metaxa:                 25186
Number of SSU rRNA sequences assigned to each origin:
  Archaea:      0
  Bacteria:     32
  Eukaryota:    21469
  Chloroplast:  0
  Mitochondria: 3685
  Uncertain:    0
  
##RDC
Number of sequences in input file:              91554326
Sequences detected as SSU rRNA by Metaxa:       59192
  On main strand:               29728
  On complementary strand:      29464
  Number of SSU rRNA sequences to be classified by Metaxa:        59193
Number of SSU rRNA having at least one database match:          59192
Number of SSU rRNA successfully classified by Metaxa:           59192
Number of uncertain classifications of SSU rRNA sequences:      0
Total number of classifications made by Metaxa:                 59192
Number of SSU rRNA sequences assigned to each origin:
  Archaea:      0
  Bacteria:     201
  Eukaryota:    58986
  Chloroplast:  0
  Mitochondria: 5
  Uncertain:    0
```



SQM 300121

```
nohupSqueezeMeta.pl -m coassembly -p GutL4_7 -s samples.file -f data/ -c 1000 --Euk --D &
```

Kaiju 310121

```shell
#ITA
nohup kaiju -m 13 -z 14 -t /space29/data/kaiju/nr_euk/nodes.dmp -f /space29/data/kaiju/nr_euk/kaiju_db_nr_euk.fmi -i ../data/ITA_1_val_1.fq -j ../data/ITA_2_val_2.fq -o ITA_nrEuk_greedy.out 

kaijuReport -t /space29/data/kaiju/nr_euk/nodes.dmp -n /space29/data/kaiju/nr_euk/names.dmp -i ITA_nrEuk_greedy.out -p -u -r genus -o ITA.report
##ITA RESULTS
43 999 534 total
39 956 868 U
 4 008 540 C

nohup kaiju -m 13 -z 14 -t /space29/data/kaiju/refseq/nodes.dmp -f /space29/data/kaiju/refseq/kaiju_db.fmi -i ../data/ITA_1_val_1.fq -j ../data/ITA_2_val_2.fq -o ITA_Refseq_greedy.out &

kaijuReport -t /space29/data/kaiju/refseq/nodes.dmp -n /space29/data/kaiju/refseq/names.dmp -i ITA_Refseq_greedy.out -p -u -r genus -o ITA_refseq.report
##RESULTS
41 461 662 U
 2 503 746 Cexit

#UIA
nohup kaiju -m 13 -z 14 -t /space29/data/kaiju/refseq/nodes.dmp -f /space29/data/kaiju/refseq/kaiju_db.fmi -i ../data/UIA_1_val_1.fq -j ../data/UIA_2_val_2.fq -o UIA_Refseq_greedy.out &

kaijuReport -t /space29/data/kaiju/refseq/nodes.dmp -n /space29/data/kaiju/refseq/names.dmp -i UIA_Refseq_greedy.out -p -u -r genus -o UIA.report

#UIA RESULTS
47 641 622 Total
43 373 215 U
 4 208 265 C

```



##### NOTAS

* Para quitar el base de conda

  ```python
  #verificar si está activado el base
  conda config --show | grep auto_activate_base
  auto_activate_base: True
  #Cambiar a False el base 
  conda config --set auto_activate_base False
  #Activar el promp de env al activar conda env
  conda config --set changeps1 True
  #salir
  exit
  #y volver a entrar
  ##Cada vez que se quiera activar un ambiente activar conda antes
  ```

* Para colores https://perez987.es/colorear-terminal/

  ```
  export TERM=xterm-color
  export CLICOLOR=1
  export LSCOLORS=exfxcxdxbxegedabagacad
  ```

* Listar el contenido de un archivo tar.gz

  ```
  tar -tzf Bonampak.tar.gz
  ```

* Para transferir archivos, además de scp, también se puede usar rsync

  ```
  rsync -avP Bonampak.tar.gz hoaxaca@132.248.220.19:/space21/PGC/hoaxaca/Doctorado/Mis_datos
  ```

* Transferir archivos en nohup 

  ```
  nohup  scp hoaxaca@132.248.220.35:/space31/PEG/hoaxaca/Bonampak.tar.gz .
  ctrl + D ==> Para salir
  
  ```

* IQtree

  ```
  iqtree -s alineamiento.mafft.fa -m GTR+F+R5 -bb 10000 -alrt 10000 -bnni -nt 15 -ntmax 15 redoullq
  ```

  