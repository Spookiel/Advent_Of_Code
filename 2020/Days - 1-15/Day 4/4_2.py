
import re
from collections import defaultdict, Counter
from itertools import permutations, combinations,product

adj4 = [[0,1], [1,0], [-1,0], [0,-1]]
adj8 = adj4+[[1,1], [-1,-1], [1,-1], [-1,1]]

def lmii(delim=" "):
    return list(map(int, input().split(delim)))

data = """ecl:grn
cid:315 iyr:2012 hgt:192cm eyr:2023 pid:873355140 byr:1925 hcl:#cb2c03

byr:2027 hcl:ec0cfd ecl:blu cid:120
eyr:1937 pid:106018766 iyr:2010 hgt:154cm

byr:1965 eyr:2028 hgt:157cm
cid:236 iyr:2018 ecl:brn
hcl:#cfa07d pid:584111467

eyr:2029 ecl:hzl
iyr:1972 byr:1966
pid:2898897192
hgt:59cm hcl:z

pid:231652013 hcl:#602927 hgt:166
ecl:grn eyr:2025
byr:2008 iyr:1986

byr:1928 hgt:167cm
hcl:#18171d iyr:2012
ecl:oth pid:237657808 eyr:1944

hgt:73in ecl:grn byr:1931 pid:358388825 iyr:2020
hcl:#602927 eyr:2020

hcl:#efcc98 eyr:2024 ecl:hzl
byr:2030 hgt:192cm
iyr:2013 pid:7479289410

pid:053467220 iyr:2012 hgt:169cm
cid:149 hcl:#866857
eyr:2030
byr:1995 ecl:oth

hgt:162cm hcl:#efcc98 ecl:grn byr:1985 pid:419840766
eyr:2022
iyr:2020

pid:22086957 hcl:c69235 ecl:#c458c5 eyr:1986 byr:2014 hgt:72cm iyr:1934

hcl:#866857
ecl:brn eyr:2024
iyr:2017
pid:505225484 cid:144
byr:1980
hgt:170cm

hcl:#866857 ecl:gry
byr:1972 iyr:2019 eyr:2023
cid:234 pid:721290041 hgt:191cm

pid:346301363
eyr:2020
hcl:#733820 iyr:2019 hgt:177cm
byr:1998

hgt:157cm byr:1963
pid:898055805
hcl:#fffffd ecl:blu iyr:2017 cid:87
eyr:2030

pid:605900764 iyr:2011
hgt:73in ecl:hzl eyr:2024
hcl:#888785
cid:281

iyr:2010 eyr:2026 hcl:#4f7e76 pid:883386029 byr:1946 ecl:brn

hcl:z
iyr:2020 pid:9121928466 byr:2014 ecl:zzz eyr:2025
hgt:172in

hgt:151cm cid:163 pid:670884417 iyr:2012
ecl:oth hcl:#ceb3a1
eyr:2028

hcl:z cid:92 hgt:69cm
byr:2008 pid:492284612
eyr:2020 iyr:2023
ecl:hzl

byr:1933
hcl:#7d3b0c eyr:2020 hgt:170cm
pid:949064511 iyr:2010
ecl:oth

eyr:2025 byr:1989 ecl:oth cid:100 hgt:182cm
pid:629190040 iyr:2017 hcl:#b6652a

ecl:hzl cid:76 hcl:#e71392 eyr:2021 iyr:2013 byr:1995
pid:762177473
hgt:179cm

pid:198500564 eyr:2029 hcl:#733820 cid:51 iyr:2012
hgt:70in byr:1938 ecl:oth

hgt:190cm ecl:brn byr:1952 iyr:2015 hcl:#623a2f
eyr:2023

hgt:169cm hcl:#602927 byr:2001 pid:823979592 iyr:2016 eyr:2029

iyr:2010 ecl:gry
eyr:2022 hgt:156cm byr:1953 pid:434063393
hcl:#733820

pid:091724580 hcl:a7069e eyr:1984 ecl:#95d01e byr:2012 iyr:2005

eyr:2022 byr:1972 hcl:#866857 ecl:hzl pid:227453248
hgt:153cm cid:324 iyr:2018

cid:195 pid:049871343
eyr:2024 hgt:169cm
byr:1952 iyr:2010 ecl:grn

eyr:2035 pid:189cm
hgt:77 iyr:1973 ecl:#dc83d5
hcl:z byr:2004

byr:2027
pid:89338932 hcl:1de39e ecl:grn hgt:159in eyr:2034 iyr:1937

pid:076534920
hgt:152cm
byr:1969
ecl:blu
hcl:#866857 iyr:2011 eyr:2024

iyr:2019 eyr:2028
ecl:blu hgt:169cm
hcl:#888785 pid:332202163 byr:1923

hgt:65in byr:1964 iyr:2019
pid:287612987 ecl:hzl cid:213 eyr:2023 hcl:#ceb3a1

hcl:#623a2f pid:182484027
iyr:2016 ecl:brn byr:1943
hgt:71in eyr:2021 cid:344

hcl:#cdee64 iyr:2011 ecl:brn eyr:2026 hgt:176cm
byr:1985 pid:978641227

eyr:2029 ecl:brn hgt:173cm byr:1920 cid:211
hcl:#866857
iyr:2016 pid:289769625

hcl:#7d3b0c pid:770938833 iyr:2010 byr:1941 ecl:oth eyr:2029 hgt:161cm

hgt:172cm iyr:2015 ecl:gry byr:1948
eyr:2029
pid:466359109 hcl:#341e13

cid:74 pid:405199325 ecl:blu
hcl:#6b5442
eyr:1980 byr:2024 hgt:174cm iyr:2011

hgt:183cm pid:075760048 cid:78 byr:1960 ecl:hzl eyr:2030 hcl:#6b5442 iyr:2014

cid:264 hcl:#7d3b0c
ecl:blu iyr:2011 eyr:2020 hgt:182cm
byr:1929

pid:435338286 byr:1931
hcl:z ecl:amb iyr:2013 hgt:73in
cid:165 eyr:2027

pid:511898552 eyr:2025 hgt:184cm hcl:#602927
iyr:2018 byr:1989 ecl:hzl

iyr:2016
hgt:168in
hcl:#623a2f
eyr:2025 pid:310738569 ecl:#0c3039
byr:2027

pid:158cm byr:1946 ecl:grt
iyr:1920 cid:189
hcl:389bce hgt:165cm

pid:973732906 hcl:#cfa07d iyr:2010 eyr:2020 hgt:180cm
byr:1930
ecl:brn

pid:930994364 byr:1967 hgt:151cm
iyr:2011 eyr:2022

eyr:1968 hgt:75cm cid:241
iyr:2011 pid:5493866745
ecl:grt
byr:1976 hcl:#a97842

eyr:2026 ecl:oth
iyr:2016 hcl:#c0946f
byr:1929
hgt:175cm
pid:9421898537

eyr:2028 iyr:2016 byr:1962
ecl:grn hgt:186cm hcl:#cfa07d pid:432962396

iyr:2010 byr:1934 eyr:2023 hgt:180cm hcl:#cfa07d ecl:gry

cid:168
byr:1978
eyr:2027 hgt:189cm pid:802710287
hcl:#2f980b iyr:2014
ecl:grn

eyr:1970
pid:576329104
ecl:xry iyr:1954 hcl:#341e13 byr:2026
hgt:74in

eyr:2027 hgt:153cm
ecl:oth
hcl:#866857
pid:290407832 byr:1956 iyr:2017

iyr:2011
cid:128
ecl:amb hcl:#7d3b0c hgt:68in pid:743606119 eyr:2020

ecl:oth hcl:#cfa07d
byr:2016 pid:#de98ae iyr:1984 cid:194
hgt:170cm
eyr:2034

pid:526098672 hgt:168cm
hcl:#7d3b0c cid:167 byr:1923 ecl:blu iyr:2016
eyr:2030

pid:495569197 hcl:#866857 hgt:193cm
iyr:2013 eyr:2021 byr:1921 ecl:amb

ecl:amb
hcl:#a97842 pid:862249915 iyr:2012 byr:1964
cid:325
eyr:2021

iyr:1958
byr:2003
hgt:160 hcl:#18171d
ecl:hzl eyr:2020

iyr:2019 byr:1997 ecl:brn
pid:342735713 hcl:#efcc98
hgt:181cm cid:307
eyr:2027

pid:817121616 eyr:2020
iyr:2012
hgt:185cm
hcl:#18171d byr:1969 ecl:hzl

pid:381399203
ecl:oth byr:1930
iyr:2014 hcl:#6b5442 hgt:71in cid:156 eyr:2025

byr:2002 hcl:#18171d iyr:2017
pid:398245854 hgt:64in ecl:gry eyr:2025 cid:127

eyr:2028 hcl:#341e13
ecl:amb iyr:2012
pid:079796480 hgt:69cm
byr:1995

cid:315 iyr:2028
pid:775929239
hgt:162cm ecl:dne byr:1940 eyr:1952 hcl:#c0946f

iyr:2015
hgt:154cm byr:1997
ecl:grn
cid:125 eyr:2024 pid:834780229
hcl:#18171d

ecl:hzl hcl:#a97842 pid:553710574 eyr:2028
hgt:183cm cid:196
iyr:2014

pid:377912488 hgt:159cm ecl:amb eyr:2024 byr:1974
iyr:2014
hcl:#ceb3a1

eyr:2024
byr:1947 hgt:63in ecl:brn
cid:69
pid:185228911 hcl:#b6652a iyr:2016

eyr:2024
hgt:168cm hcl:#602927
iyr:2013
byr:1993
pid:681091728 ecl:gry cid:203

pid:037922164 iyr:2020
byr:1990 hgt:156cm eyr:2023 hcl:#866857
cid:97 ecl:grn

hgt:170cm pid:980455250
iyr:2011 ecl:hzl byr:1957
eyr:2030 hcl:#cfa07d

hgt:158cm
hcl:#602927
byr:2002 ecl:hzl iyr:2013
cid:99
eyr:2020 pid:48646993

byr:1955 pid:814033843 eyr:2030 hcl:#a97842
hgt:191cm iyr:2019

pid:111196491 hgt:191cm iyr:2012 ecl:blu hcl:#a97842
eyr:2026 cid:131 byr:1979

hcl:#fffffd hgt:68in
cid:121 ecl:oth eyr:2024 pid:343836937
byr:1955
iyr:2020

eyr:2025 byr:1954
pid:737517118
cid:343 hcl:#b6652a
iyr:2017 ecl:hzl
hgt:175cm

ecl:brn
iyr:2011 hgt:171cm cid:102 pid:066348279 byr:1981

ecl:oth iyr:2018 byr:1975
eyr:2029
hgt:185cm cid:226
pid:978243407 hcl:#341e13

iyr:2015 pid:918017915 hcl:#3e52b7
byr:1999 ecl:brn cid:314
eyr:2025 hgt:192cm

hcl:#19d1fa byr:1984 ecl:dne hgt:76in
iyr:2015 cid:118 pid:417075672
eyr:2020

iyr:2019
cid:120 hgt:186cm
hcl:#733820 eyr:2024 pid:423238982 ecl:brn byr:1968

hgt:70cm cid:173 pid:767014975
hcl:#866857 eyr:2039 ecl:brn byr:1985

pid:340424924
eyr:2027 hcl:#7d3b0c
hgt:168cm ecl:hzl iyr:2016
byr:1994

ecl:hzl byr:1933 pid:580425691
iyr:2010 hcl:#c0946f eyr:2024
hgt:64in

hcl:#9fe6b0 pid:913184461 ecl:grn eyr:2030
cid:262 iyr:2014

ecl:amb pid:640007768 eyr:2030 byr:2017 iyr:1988 hcl:z

byr:1977 cid:54
eyr:1939 pid:882762394 iyr:2030 hcl:#ceb3a1 ecl:blu

iyr:2011 hcl:#7d3b0c byr:1928
pid:340969354 cid:199 hgt:168cm eyr:2029 ecl:hzl

pid:729464282
iyr:2012 hcl:baae60
eyr:2026 ecl:hzl hgt:166cm byr:2019

pid:930997801 iyr:2019 eyr:2030
hcl:#866857 ecl:oth byr:1960 cid:235 hgt:73in

ecl:brn
byr:1988 hgt:179cm iyr:2017
pid:864768439 cid:305 hcl:#c0946f
eyr:2029

hcl:#7d3b0c ecl:grn
hgt:182cm eyr:2021 pid:719891314
byr:1920 iyr:2017

hgt:62cm
cid:71 ecl:brn hcl:#fffffd iyr:2025 eyr:1997
pid:175cm byr:2022

hcl:#cfa07d cid:239 eyr:2025 ecl:hzl hgt:189in byr:1980 iyr:2020
pid:703047050

byr:1951
eyr:2030
ecl:hzl
pid:130992467 hgt:157cm hcl:#341e13

hgt:175cm
hcl:#623a2f
cid:68 eyr:2025
byr:2001 ecl:oth pid:253618704 iyr:2016

hcl:#fffffd pid:379344553 ecl:grn
eyr:2026
hgt:72in byr:1974 iyr:2013

ecl:#b4e952 byr:1970 hcl:z
eyr:2039 pid:6056894636 iyr:2021 hgt:165cm
cid:328

hcl:#602927 iyr:2014 pid:890429537 byr:1957 hgt:68in eyr:2020 ecl:hzl

cid:265 byr:1961 hcl:#ceb3a1 eyr:2022 iyr:2016 hgt:184cm pid:921615309

byr:1951 eyr:2024
hcl:#341e13
ecl:amb pid:414644982
iyr:2010 hgt:159cm

iyr:2015 cid:319
eyr:2029 ecl:brn pid:380237898
hcl:#efcc98 hgt:157cm byr:1972

pid:237156579 ecl:#312a91
hgt:167cm iyr:2011 hcl:#c0946f eyr:2021 byr:1953

ecl:hzl iyr:2015 pid:10160221 eyr:2025 hgt:175cm hcl:z byr:1939

hgt:59in hcl:#18171d byr:1962 ecl:hzl
iyr:2019 eyr:2025
cid:337 pid:491938615

ecl:utc hgt:82 pid:51674655 byr:2020
eyr:1954 iyr:2029 hcl:z

pid:119530189
cid:103
iyr:2010 byr:1979
hgt:168cm hcl:#a97842 ecl:brn eyr:2029

hgt:177cm ecl:brn
byr:1990
pid:015089628 eyr:2028 hcl:#733820 iyr:2020

ecl:blu iyr:2020 hgt:189cm
hcl:#efcc98 byr:1982 pid:346500376 eyr:2021 cid:160

ecl:brn hgt:173cm iyr:2011 cid:259 hcl:#6b5442 eyr:2026
byr:1995
pid:654875035

ecl:grn eyr:2025 pid:147155222 byr:1942
cid:341 hcl:#602927
hgt:165cm
iyr:2016

pid:543171646
hgt:153cm
iyr:2019 hcl:#fffffd byr:1985 cid:266
eyr:2027
ecl:hzl

ecl:blu
eyr:2022
pid:667939101 byr:1974
cid:259 hcl:#888785

eyr:2030 byr:2016 iyr:2022
pid:86902982
ecl:zzz hgt:72 hcl:ceb867

hcl:#fffffd
ecl:grn pid:046978329
byr:1924
eyr:2025 hgt:158cm iyr:2011

hgt:150cm eyr:2028 byr:1985 ecl:gry hcl:#866857 pid:340615189
iyr:2017
cid:50

cid:171 hcl:#18171d pid:009562218 byr:1981 hgt:175cm eyr:2024 ecl:oth iyr:2017

iyr:2019
eyr:2022
ecl:brn hcl:#cfa07d pid:050270380 cid:159
hgt:151cm
byr:1951

hcl:#7d3b0c hgt:176cm iyr:2015 byr:1923 pid:348188421 ecl:blu eyr:2029

byr:1997 hgt:162cm eyr:2023 pid:445685977
iyr:2012 ecl:amb hcl:#efcc98

iyr:2017 ecl:oth eyr:2028 pid:791977055 hgt:170cm byr:1991
hcl:#623a2f

byr:1998 hcl:#fffffd
eyr:2020
ecl:gry pid:039483695 hgt:163cm iyr:2020
cid:165

ecl:hzl hgt:74in iyr:2016 pid:026214321
cid:152 hcl:#a1f179
eyr:2036 byr:2001

pid:257900949 cid:80 byr:1956 iyr:2012 hgt:165cm eyr:2030

pid:918371363
ecl:xry
iyr:2012
byr:2012 hgt:65cm
eyr:2029

pid:041789006 iyr:2018 byr:1945 eyr:2024 ecl:blu
hcl:#5ab31e hgt:171cm

ecl:gry
byr:1956 cid:318 iyr:2020 hcl:#623a2f
eyr:2030 pid:020576506 hgt:184cm

hgt:173cm iyr:2025
eyr:2023
ecl:amb pid:958983168 hcl:#866857 byr:1935

byr:1974
eyr:2040 pid:57104308 iyr:1980 hcl:z
hgt:192in cid:295 ecl:amb

pid:180cm hcl:1109f7 eyr:2039 byr:2020
ecl:dne hgt:189in iyr:1921

iyr:2013 byr:1961
hcl:#866857
eyr:2025 hgt:158cm ecl:gry

ecl:brn iyr:2013 eyr:2021 pid:978650418 byr:1980
hcl:#ceb3a1 cid:110
hgt:166cm

pid:864880558 ecl:hzl hcl:#c0946f byr:1955 eyr:2027 hgt:169cm iyr:2011

eyr:2023 hgt:191cm hcl:#866857
pid:454509887
ecl:grn byr:1938 iyr:2015

pid:793008846 eyr:2025 ecl:grn hcl:#341e13
hgt:187cm
byr:1973 cid:224
iyr:2013

hcl:#866857 eyr:2022 pid:802335395 hgt:171cm ecl:amb
iyr:2015 byr:1991

hcl:#888785 pid:768625886
hgt:180cm
eyr:2026 ecl:oth cid:178 byr:1958

pid:921387245 cid:82 hgt:190cm hcl:#c0946f ecl:grn
iyr:2015 eyr:2023

pid:0704550258 hcl:1ba8f6 iyr:2010 byr:1978 cid:130
eyr:2030 ecl:dne hgt:66cm

pid:626293279 hcl:#7d3b0c hgt:185cm ecl:oth
eyr:2020 byr:1937 iyr:2012

hgt:175
eyr:1933 ecl:gry
hcl:#7d3b0c byr:2003 pid:#5d8fcc
iyr:2012

eyr:2027
byr:1927 cid:154
ecl:gry pid:683668809 hgt:164cm
hcl:#a97842 iyr:2011

byr:1940 iyr:2014 hgt:172cm eyr:2024 pid:033678324 hcl:#10fded
cid:292 ecl:oth

iyr:1970 ecl:#201515 pid:#4cd485 eyr:2034 hgt:162
byr:2005 cid:67
hcl:#c0946f

cid:306
byr:1948
hcl:#efcc98
eyr:2024 hgt:171cm pid:440657854 iyr:2015 ecl:brn

hgt:172cm ecl:brn byr:1958 pid:054926969 hcl:#4b8065 iyr:2019

pid:45977569 ecl:amb byr:2002 hgt:71cm hcl:z iyr:1983

pid:811407848 hcl:#866857 cid:112 hgt:180cm byr:1986
ecl:brn eyr:2026

ecl:amb
byr:1992
cid:288 pid:417117245 hcl:#623a2f
iyr:2011 hgt:181cm
eyr:2021

byr:1974 hgt:192cm cid:172
eyr:2022
ecl:blu
hcl:#cfa07d iyr:2014

eyr:2024 ecl:gry
pid:874569675 byr:1960 iyr:2017 hgt:186cm
hcl:#6b5442

byr:1988 eyr:2024 iyr:2020 ecl:oth hcl:#866857 pid:227304269 hgt:170cm

ecl:grn iyr:2019 byr:2002 cid:150 hcl:#efcc98
pid:600740993
hgt:167cm eyr:2027

pid:553824537 iyr:2019 ecl:blu eyr:2025 hcl:#e21269 hgt:193cm
byr:1923

byr:2030 iyr:2019 ecl:#cb0911
hcl:#cfa07d hgt:74in eyr:2012
pid:7647207386

cid:289 hgt:128 pid:178cm iyr:2025 ecl:#4ad977 byr:2020 eyr:2036 hcl:#efcc98

cid:119 hgt:150in
hcl:z
iyr:2012
ecl:brn eyr:1975
byr:2007 pid:#0dcd32

hcl:8a1ce7 pid:0434291854
eyr:2034 iyr:2005
hgt:62cm byr:2029 ecl:utc

ecl:gry hcl:#ceb3a1 byr:1976 eyr:2024 iyr:2010 hgt:188cm
pid:636312902

hcl:#888785 byr:2027 hgt:178in iyr:2017 pid:973095872 eyr:1952

hgt:179cm iyr:2015 hcl:#ceb3a1
byr:1944 pid:182079308 cid:317
eyr:2025 ecl:hzl

hcl:#6b5442 ecl:grn eyr:2023 hgt:71in pid:829794667 byr:2000
iyr:2014 cid:192

iyr:2014 pid:096659610 hcl:#c0946f ecl:oth byr:1991 cid:180
hgt:177cm
eyr:2023

byr:2017
eyr:2036 iyr:1933
cid:225 ecl:gmt hgt:179in
hcl:b5c44d pid:99932231

hcl:#18171d
hgt:187cm eyr:2023 byr:1934 cid:286 pid:878541119 iyr:2020 ecl:amb

hgt:185cm
pid:754207134 ecl:oth eyr:2023
hcl:#a97842 cid:313 byr:1966
iyr:2015

hcl:#ceb3a1 byr:1921 eyr:2022 pid:799265846 cid:285
hgt:67in iyr:2015

iyr:2011 byr:1941
hcl:#341e13 cid:65 pid:413556937
hgt:169cm
ecl:amb eyr:2020

iyr:2016
hgt:158cm ecl:grn byr:1931 hcl:#7d3b0c

pid:574299170 iyr:2013 byr:1961 ecl:hzl hcl:#866857 hgt:168cm eyr:2022

eyr:2022 pid:245416405
iyr:2019 hgt:173cm hcl:#c0946f
ecl:brn
byr:1965

byr:1980 hgt:162cm ecl:brn pid:239318191
hcl:#fffffd
cid:58 eyr:2025 iyr:2020

pid:892646915
iyr:2012 hcl:#733820 byr:1991 eyr:2021
hgt:157cm ecl:oth

pid:310597466 eyr:2025
hcl:#cfa07d byr:1944 iyr:2018 ecl:oth
hgt:183cm

iyr:2010 hgt:187cm ecl:oth
pid:975763328
hcl:#866857 eyr:2023 cid:283 byr:1997

iyr:2020 cid:225 hcl:#efcc98 pid:424680047 ecl:blu
hgt:154cm
byr:1968 eyr:2027

ecl:oth eyr:2020 hgt:183cm hcl:#623a2f
pid:771851807
byr:1990
iyr:2017

hcl:#efcc98 ecl:blu byr:1991 hgt:191cm pid:266021118
cid:124
eyr:2025

byr:1993
ecl:hzl eyr:2020
hgt:163cm
iyr:2015 pid:831538073 hcl:#18171d

hgt:74in hcl:#420afb eyr:2028
ecl:grn pid:264469103
byr:1993

eyr:2020
cid:79
byr:1972
pid:084953331 hcl:#a97842 ecl:brn iyr:2010
hgt:170cm

iyr:2014 ecl:gry pid:094812116 eyr:2026 hgt:190cm byr:1965 hcl:#944667

hcl:#fffffd byr:1953 iyr:2014 ecl:hzl hgt:164cm
cid:123 eyr:2023 pid:546394433

iyr:2012 hgt:155cm byr:1998 pid:#2c9be6 eyr:2023 hcl:#ceb3a1 ecl:gry

eyr:2029 ecl:gry pid:752489331 iyr:2015 hgt:167cm hcl:#18171d cid:70 byr:2002

byr:1938
ecl:gry
pid:764937909 iyr:2014
hcl:#7d3b0c
eyr:2022 cid:145 hgt:184cm

cid:340
byr:1924 hgt:169cm eyr:2026
iyr:2013 ecl:amb
pid:499844992 hcl:#18171d

pid:838417672 hgt:175cm
ecl:grt iyr:2017 eyr:2025 hcl:17aa1a

eyr:2020
byr:1925 hcl:#341e13
ecl:brn cid:342 pid:047426814 hgt:156cm iyr:2012

iyr:2011 hcl:#341e13 byr:1959
ecl:amb pid:969679865

byr:1978 cid:320 hgt:180cm hcl:#435ceb pid:363518544 eyr:2023 iyr:2016 ecl:blu

iyr:2010 eyr:2028
pid:183cm byr:1948
ecl:oth cid:133
hcl:#8d3298 hgt:190cm

hcl:#6b5442 byr:1929 iyr:2019 pid:207713865 eyr:2029
hgt:166cm ecl:gry

ecl:blu iyr:2019
byr:1985 eyr:2030 hcl:#866857 hgt:155cm pid:659180287

ecl:hzl
eyr:2020 iyr:2016 pid:440624039
cid:147
hgt:61in byr:1976 hcl:#733820

hcl:#341e13 pid:178082907 eyr:2023
iyr:2015 byr:1956
ecl:amb hgt:163cm

eyr:2023
iyr:2011 hcl:#cfa07d hgt:164cm
pid:291621559 byr:1960 ecl:gry

hcl:#efcc98 byr:1976
iyr:2017 pid:394566091 cid:248
hgt:176cm ecl:hzl eyr:2026

iyr:2013 eyr:2029 hgt:152cm ecl:gry byr:1984 hcl:#623a2f pid:511780941

pid:953716819 iyr:2010 hgt:156cm ecl:amb
byr:1947
hcl:#18171d eyr:2025

eyr:2025 ecl:amb
iyr:2016
hcl:#cfa07d byr:1925 pid:322787273 hgt:168cm

hgt:59in iyr:2012
pid:916978929 byr:1959
hcl:#c0946f eyr:2021
ecl:brn

byr:2018 eyr:1929 hgt:187in
hcl:z
iyr:2003 pid:0377361331 ecl:utc

byr:1949 hcl:#fffffd pid:071791776 eyr:2030 iyr:2015 hgt:71in ecl:hzl

hcl:#341e13
hgt:154cm byr:1927 eyr:2023 ecl:blu iyr:2017
pid:639867283

hcl:z pid:315276249 byr:2026
hgt:151cm
iyr:2028 eyr:2020
ecl:hzl

hcl:#341e13 eyr:2027 byr:1981 cid:342 pid:999898177 hgt:187cm
ecl:blu iyr:2011

byr:2009
hgt:73cm iyr:1921 hcl:z
pid:181cm
ecl:xry

ecl:hzl
byr:1925
pid:034183103 hcl:#341e13 hgt:158cm eyr:2029 iyr:2010

byr:1976
iyr:2011 hgt:177cm pid:833479839 hcl:#dcab9d ecl:blu eyr:2020

cid:230 hcl:#7d3b0c byr:1954
iyr:2014 eyr:2026 pid:122150889
ecl:brn hgt:182cm

hcl:#a97842
ecl:brn hgt:187cm
eyr:2028
pid:427631634 iyr:2002 byr:2004

pid:912516995 ecl:hzl iyr:2017 hcl:#ceb3a1 byr:1929 eyr:2028
hgt:155cm

pid:019809181
cid:128 iyr:2013 hcl:#f5b9f7 byr:1931
hgt:161cm
ecl:amb

hgt:64in byr:1924
iyr:2016 eyr:2029 ecl:hzl pid:474940085 hcl:#c0946f

pid:172419213
ecl:grn
hgt:193cm iyr:2010 byr:1973 hcl:#6b5442
eyr:2027

ecl:#7b5cfd iyr:2019
byr:2016
eyr:2040 hgt:191in
cid:187 hcl:z pid:#c61084

eyr:2032 iyr:2014 pid:430247344 byr:1967
hcl:#ceb3a1
cid:241
ecl:brn hgt:178in

hcl:#623a2f iyr:2017 cid:235
eyr:2020 byr:1978 ecl:blu hgt:175cm

iyr:2013 ecl:amb hgt:174cm hcl:#866857 pid:285533942 byr:1954

hgt:152cm ecl:blu pid:952587262 eyr:2024
iyr:2019 cid:268 hcl:#602927 byr:1947

hgt:176in cid:245 byr:2011 iyr:2018
eyr:1987
hcl:z
pid:346518170
ecl:utc

hgt:180cm
iyr:2015 ecl:brn eyr:2027 pid:807494368 cid:324 byr:1980

byr:1936 hcl:#866857 ecl:blu
eyr:2021 hgt:187cm
iyr:2016 pid:244556968

byr:1950 cid:125
iyr:2020 hgt:168cm hcl:#c0946f eyr:2030 pid:758313758 ecl:blu

eyr:2021
pid:618915663 hcl:#cfa07d iyr:2018 byr:2002
hgt:157cm ecl:blu

byr:1967
ecl:brn hcl:#c0946f pid:200495802 eyr:2021 iyr:2020
cid:335
hgt:181cm

byr:1996
ecl:brn iyr:2015
eyr:2030
hcl:#fffffd cid:207
pid:022460311 hgt:158cm

eyr:2022 hgt:59cm iyr:2023
byr:1974 pid:354098699 hcl:b244f7
ecl:#219505

hcl:#866857 eyr:2025
pid:370874666
byr:1947
cid:162 ecl:oth hgt:186cm iyr:2011

ecl:hzl eyr:2029
byr:1981
iyr:2012 pid:433430792 cid:252
hgt:171cm

pid:512473844 hgt:186cm iyr:2012 eyr:2028 byr:1949 ecl:hzl hcl:#18171d

hgt:60cm iyr:1934
ecl:#4a4017 pid:3067366202 hcl:1161df
eyr:1938 byr:2008

pid:119509757 hcl:#cfa07d eyr:2022 hgt:174cm byr:1983
iyr:2015
ecl:blu

byr:1955 eyr:2023
cid:114
hcl:f1aa8a pid:609049659 ecl:grn hgt:177cm
iyr:2015

eyr:2027 cid:284
pid:654627982 byr:1964 iyr:2018 hgt:168cm
hcl:#fffffd ecl:oth

iyr:1988
hgt:191cm hcl:b87a62 byr:1990 ecl:xry
pid:996624367 eyr:1960

pid:641466821 eyr:2028 hcl:#7d3b0c
iyr:2010 hgt:175cm ecl:gry

hcl:#b6652a
ecl:oth
byr:1926 eyr:2030 iyr:2019 hgt:183cm
pid:057196056

iyr:2017
eyr:2022 pid:936841429
ecl:blu hcl:#6b5442 cid:179 byr:1927 hgt:161cm

eyr:2021
cid:289 hgt:174cm iyr:2013
ecl:grn pid:329574701 byr:1970

eyr:2021 byr:1939 ecl:gry pid:933505139 iyr:2014 hgt:173cm hcl:#7d3b0c

cid:116 hcl:045bff eyr:2030 iyr:1920
ecl:brn
byr:2030
pid:#38f7f3
hgt:155in

eyr:2028
pid:225829241 byr:1928 hcl:#cfa07d iyr:2019
ecl:oth
hgt:166cm

cid:80 byr:1936
iyr:2017
hgt:94 hcl:#2e7503 ecl:oth eyr:2030
pid:597284996

ecl:oth
iyr:2019 hgt:76in
byr:1956 pid:821874039

eyr:2026 hgt:168cm
pid:019015588
iyr:2010
ecl:amb byr:2009 hcl:#623a2f cid:159

iyr:1980 hgt:167in
pid:380644909 eyr:1966 ecl:blu byr:2004 hcl:z

eyr:2020 iyr:2013
hcl:#08ad66 pid:540886868
ecl:oth byr:1980 hgt:158cm

eyr:2026 hgt:186cm byr:1995
cid:275
hcl:z iyr:1958 ecl:blu

eyr:2026 iyr:2012
hgt:61in byr:1936 pid:390833536 cid:298 ecl:grn hcl:#623a2f

pid:393878498 eyr:2023 ecl:gry byr:1943 iyr:2010 hcl:#888785 hgt:158cm

hgt:191cm cid:197 iyr:2014 byr:1945
hcl:#fffffd
eyr:2020
pid:183948344 ecl:amb

ecl:gmt hgt:88
cid:260 iyr:2024 byr:2022 eyr:2031 hcl:z pid:#532c6e

hcl:#a97842
hgt:160cm eyr:2024 ecl:blu iyr:2015 byr:1970

byr:1964 hgt:178cm
eyr:2025
pid:813643223 ecl:brn iyr:2014
hcl:#ceb3a1

byr:1965 eyr:2024 iyr:2018
hgt:165cm hcl:#18171d ecl:grn pid:475669993

hgt:116
iyr:2024 eyr:1974 hcl:504345 byr:2010 cid:206 pid:166cm ecl:zzz

iyr:2014 eyr:2020 pid:096460673 byr:1948
hgt:153cm
ecl:blu hcl:#341e13

hcl:#ceb3a1
iyr:2017 hgt:67cm
pid:178cm byr:2028 ecl:brn
cid:293

hgt:157cm
hcl:#602927 byr:1941
iyr:2012 pid:611003211 eyr:2029

iyr:2019 byr:2000 pid:083917767 eyr:2024 hgt:172cm
cid:248 hcl:#7e4d15

byr:1946
hgt:160cm iyr:2020 hcl:#559278 pid:989139577
ecl:amb eyr:2020

pid:165cm byr:1927 cid:178 hcl:#733820 iyr:2017 hgt:156in
eyr:2029 ecl:brn

hcl:#18171d hgt:163cm eyr:2022 byr:1962 pid:639124940 cid:258 ecl:hzl
iyr:2015

cid:123 pid:4542006033
eyr:1987 byr:2010 iyr:2029 ecl:amb
hgt:191cm hcl:#18171d

hcl:z
byr:1928 iyr:1965
eyr:2022 hgt:75 ecl:oth pid:400765046

hcl:#c0946f hgt:62in
ecl:blu byr:1978 iyr:1923
cid:260 eyr:2021 pid:404628742

pid:#bf1611 ecl:grn
iyr:2018 cid:146 byr:1948
eyr:2025 hcl:#fffffd hgt:87

pid:767547618
iyr:2018 hcl:#b6652a eyr:2029 hgt:165cm ecl:hzl byr:1937

ecl:blu iyr:2019 pid:960083875 eyr:2027 hgt:71in hcl:#c0946f
byr:1921

iyr:2011
pid:9562042482
hcl:z hgt:59cm
eyr:1994 cid:258 ecl:#6c1bcc byr:2025

eyr:2028 pid:494999718 byr:1928 hgt:176cm
iyr:2015 ecl:oth hcl:#733820

cid:78 eyr:2020 hgt:160cm byr:1947 ecl:blu
hcl:#b6652a iyr:2016 pid:069457741

hcl:#6b5442 iyr:2010
byr:1971
eyr:2028 hgt:169cm ecl:brn pid:528961949

eyr:2028
hcl:#7d3b0c
byr:1952
ecl:hzl
cid:317 iyr:2016
pid:832169844

hcl:#c0946f
ecl:brn
iyr:2017 eyr:2028
pid:161390075 byr:1993 cid:50
hgt:171cm

ecl:#ae12d3 hgt:74cm cid:239 hcl:z pid:345439730 iyr:1924 byr:2029 eyr:2031"""


test1 = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
test2 = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""
test3 = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
test4 = """"""



data1 = """byr:1971
ecl:hzl pid:112040163
eyr:2023 iyr:2019
hcl:#b6652a hgt:167cm

pid:108667812 eyr:2023 hcl:#623a2f hgt:171cm iyr:2018 ecl:amb byr:1993

hcl:#cfa07d iyr:2014 ecl:blu eyr:2023 cid:304 hgt:70in byr:1961

byr:1977
hcl:#b6652a
iyr:2017 ecl:oth pid:703877876 hgt:185cm

byr:1972
cid:271
iyr:2016 pid:876104259 hgt:173cm eyr:2028 ecl:brn hcl:#733820

hgt:174cm ecl:gry iyr:2014 eyr:2029 hcl:#c0946f
byr:1967 pid:406306240

hcl:#6b5442
iyr:2011
pid:040592028 eyr:2026
ecl:amb
byr:1923

pid:293598838 byr:1960 cid:87
iyr:2018
ecl:blu eyr:2029
hcl:#7d3b0c
hgt:62in

iyr:2018 cid:137
hcl:1c7db1 ecl:#38812e byr:2006 eyr:2038 pid:1239811353 hgt:84

hcl:#888785 pid:308480529
iyr:2010 byr:1988
eyr:2025 hgt:176cm ecl:amb

cid:79 ecl:lzr
iyr:2013 byr:1991 hcl:2f49ef
hgt:191cm
pid:378428551

iyr:2005
hgt:64in hcl:89c369
ecl:gry byr:1932
eyr:2029 pid:753055776

ecl:amb iyr:2017
byr:1969 hcl:#fffffd
pid:305746470
hgt:173cm

pid:081972188 iyr:2011
hcl:9bb154
eyr:2024 byr:1966 ecl:oth cid:185 hgt:171cm

pid:522553186 hgt:171cm ecl:grn hcl:#7d3b0c
byr:1955
eyr:2025 iyr:1999

iyr:2015
byr:1941 pid:140123640 ecl:amb hgt:153cm hcl:#ceb3a1 eyr:2020

ecl:grn
cid:202 hcl:#602927
eyr:2029
hgt:180cm byr:1974
pid:658341964
iyr:2017

pid:2037156813 eyr:1978 ecl:grn hcl:519b45 iyr:2011 byr:2017

hcl:#fffffd ecl:hzl
pid:658716289 byr:2001 hgt:154cm cid:234 eyr:2031 iyr:2010

byr:2013 pid:#eb519e eyr:2026
hgt:157cm iyr:2030 hcl:7e9d5a ecl:oth

byr:2002
ecl:brn iyr:1998 hgt:60cm
hcl:#7d3b0c pid:#90286d
eyr:1938

byr:1956 hcl:#efcc98
hgt:190cm
iyr:2010 eyr:2023
ecl:amb
cid:342 pid:278521396

hgt:67cm
cid:98 eyr:2036 byr:2028 ecl:grt hcl:08b5ad iyr:2029 pid:187cm

ecl:dne hcl:fca461 hgt:129 iyr:2020 eyr:2027 byr:2022 pid:5014208295

hgt:169cm ecl:gry iyr:2015 eyr:2025 hcl:#733820 pid:240085824 byr:1920

iyr:2020 eyr:2033
pid:#3f8e9d hgt:190in ecl:brn hcl:#efcc98 byr:2004

iyr:2018 hcl:#18171d ecl:brn byr:1933
pid:514517439 hgt:171cm eyr:2028

eyr:2030 pid:053251865
byr:2028 hgt:174cm iyr:2015 hcl:5a0da9 ecl:hzl

hgt:169cm iyr:2014 ecl:oth eyr:2029 pid:348737413 hcl:#b6652a byr:1997

hgt:181cm cid:315
eyr:2021 iyr:2016 byr:1966 ecl:oth pid:779435812 hcl:#733820

pid:5052579 cid:268 hgt:193in
hcl:z
iyr:1942 eyr:1977

eyr:2039 hgt:69cm cid:337
iyr:2023 pid:568948965
byr:2018 hcl:z ecl:amb

byr:2014 eyr:2028
cid:311
pid:158cm ecl:#946399 hgt:99
hcl:z
iyr:1978

pid:474742310 iyr:2015 eyr:2021 hcl:#14f5da
hgt:163cm ecl:oth

hcl:#efcc98
ecl:blu
hgt:178cm pid:815309025 byr:2024
iyr:2008 eyr:1922

byr:1946 eyr:2028 pid:364439229 iyr:2011 hgt:186cm cid:79 ecl:blu

eyr:2028 hgt:157cm
cid:59 iyr:2010 byr:1927
ecl:brn
pid:893074368

hcl:#18171d ecl:#2defe4 hgt:128 byr:1940
pid:181904523 iyr:2022 eyr:1937

eyr:2023 hgt:172cm iyr:2012 hcl:#a97842 ecl:hzl byr:1982 pid:638759541

cid:91 hcl:#623a2f
byr:1996 eyr:2028 pid:181384347 hgt:175cm
iyr:2020

iyr:2017 eyr:2021 ecl:gry
byr:1979 hgt:168cm hcl:#6b5442 pid:950995084

ecl:blu iyr:2012 byr:1972
hcl:#888785 eyr:2022 hgt:179cm pid:293827532

hgt:179cm
ecl:hzl iyr:2011
byr:1982 eyr:2020 hcl:#efcc98 cid:209 pid:626732917

byr:1989
hcl:#6b5442 pid:679850983 iyr:2020
hgt:192cm ecl:blu

pid:333485773 hgt:167in ecl:zzz iyr:1945
eyr:2035 cid:319 hcl:#341e13

hgt:64in
cid:202 eyr:2023 ecl:gry hcl:#c0946f pid:212611149 byr:1928 iyr:2010

hgt:183cm hcl:#e8fa30 ecl:oth eyr:2021
byr:1943 pid:667658434
iyr:2010

cid:117
byr:2022 hcl:z ecl:#c6ae1f iyr:2028
hgt:188cm
pid:0883366415
eyr:2030

hcl:z
pid:99347800 iyr:2030 eyr:2032 ecl:#cd1fd7 hgt:192cm byr:2019

hgt:178cm byr:2013
iyr:2026 hcl:ad3da1
eyr:2020 pid:1626818790

hgt:63cm
iyr:1964
eyr:2032
cid:135 byr:2017 hcl:#a97842 pid:#1b83f5 ecl:gmt

hcl:c352d2 byr:1927 ecl:gmt hgt:187cm
eyr:2031 pid:170cm

byr:2022 eyr:1958 ecl:zzz pid:3692521800 hcl:8b2b50 iyr:1946 hgt:155in

ecl:#43f305 hcl:z byr:2028
pid:63518738 cid:243 eyr:2037
hgt:67cm iyr:1929

ecl:brn hcl:#888785
pid:495215177 byr:1962 eyr:2021
cid:192
hgt:151cm iyr:2012

ecl:#dcca8e cid:64 eyr:2030 pid:380057616
hcl:z iyr:2026 byr:1962

hcl:z
ecl:hzl eyr:2027 byr:2015 pid:302526406 hgt:175cm iyr:2017

byr:1966
cid:133 pid:9953651821 ecl:gry iyr:2020 hgt:152cm
hcl:#fffffd eyr:2026

hgt:191cm byr:1960 pid:752655640 hcl:#888785
cid:249 ecl:blu
iyr:2012 eyr:2028

pid:#c8c988 eyr:2027 hgt:157in hcl:z iyr:2025 byr:2019 ecl:zzz cid:195

hgt:96 pid:95381813 iyr:1950
hcl:#fffffd eyr:2026
byr:2010 cid:318
ecl:#48a819

eyr:2020
ecl:oth byr:1951 pid:080392492
iyr:2015 hcl:#6b5442 hgt:176cm

hgt:162cm pid:897792747 byr:1968
hcl:#ceb3a1 ecl:grn eyr:2026 iyr:2014

eyr:2038 hcl:cc324a byr:1983 ecl:brn
hgt:161 pid:#adf47f cid:208

iyr:2013 ecl:blu hcl:#866857 byr:1981 hgt:157cm eyr:2025 pid:216910202

hgt:152in byr:1990
iyr:2027 hcl:a4a3ae
ecl:#058ae2 eyr:2037 pid:646420120

ecl:oth byr:1982 eyr:2027 hgt:65in iyr:2019
hcl:#efcc98 cid:224
pid:854228141

pid:772612093
iyr:2027
hgt:175in byr:1981 hcl:c0b5a9 ecl:utc

hcl:#888785 iyr:2014 byr:1975
ecl:blu
pid:461319017 cid:229 eyr:2030 hgt:154cm

hgt:179cm eyr:2024
pid:192cm
iyr:2017 ecl:grt byr:1934 hcl:z cid:92

hcl:9c9409 iyr:2020 eyr:2030 hgt:156in
cid:189 pid:732321495
byr:1937 ecl:xry

eyr:2026 pid:092259220 byr:1943
iyr:2010 hgt:153cm hcl:#602927

byr:1925 hgt:180cm hcl:#888785 iyr:2014
pid:402548656 eyr:2023 ecl:hzl
cid:188

eyr:2020 pid:874307939 hcl:#3f85a4
ecl:gry hgt:167cm byr:1959 iyr:2014

eyr:2026 hgt:183cm iyr:2011 byr:1940 ecl:blu pid:810026000
cid:226 hcl:#866857

cid:292 ecl:grt hgt:72cm
byr:2009
iyr:2000 eyr:1946 hcl:7be409 pid:996363336

eyr:2027
iyr:2021
pid:632405666
byr:2027
ecl:#d83a36 hcl:z hgt:190in

cid:80
hgt:173cm
pid:735853952 ecl:gry hcl:#fffffd eyr:2025 iyr:2020 byr:1923

byr:1977
hcl:#733820
iyr:2020 ecl:#698d72 hgt:186cm pid:678869986 cid:67
eyr:2021

hgt:61cm iyr:2022 eyr:1972 hcl:979bcf byr:2023 pid:44037388 ecl:xry

eyr:2032 pid:193cm hcl:z
hgt:68cm byr:2016

byr:2008 cid:239
hcl:ddc745 eyr:2033 ecl:#6858b5 hgt:64cm iyr:2023
pid:89867524

iyr:2016 hgt:74in hcl:#18171d
byr:1959
ecl:blu
pid:848487392
eyr:2027

hgt:165in ecl:grn
byr:1960 eyr:2029
iyr:2017
hcl:#b6652a pid:096349067

eyr:2025 ecl:brn
pid:634481064 iyr:2015
hcl:#7d3b0c
byr:1943

ecl:grn eyr:2021
pid:34753212 cid:51 hgt:184 iyr:1970 byr:2012

eyr:1973 iyr:2014 cid:225
byr:2028 ecl:gmt
hgt:158cm
pid:#74f9b8 hcl:f6932a

hgt:168cm
hcl:#602927
pid:622067991 ecl:amb eyr:2025 iyr:2018

pid:791399958 byr:1956 eyr:2027 hcl:#602927
ecl:brn
iyr:2016 hgt:192cm

hgt:168cm iyr:2015 cid:115 ecl:#3fa48b eyr:2037 hcl:#1bf77b byr:1980 pid:947370470

iyr:2008
byr:2021 ecl:zzz
hcl:z hgt:109 pid:#fc2a91 cid:268 eyr:1957

byr:2018 hcl:fef19c iyr:2014 ecl:blu eyr:2023 cid:259 pid:193cm hgt:156

hcl:#b6652a
iyr:2023 byr:2021 hgt:153cm pid:934391984 eyr:2021 ecl:brn

pid:168cm hcl:b13f1e eyr:2038 iyr:2020 ecl:#7c0a6d hgt:169in

ecl:amb cid:170
pid:300188824 eyr:2024 byr:1954 hcl:#b6652a hgt:166cm
iyr:2013

ecl:brn
eyr:2023
hcl:#b6652a byr:1948 hgt:71in iyr:2015
pid:575973478

eyr:2026 hgt:180cm hcl:#866857 ecl:grn iyr:2013
byr:1997 pid:864648034

ecl:hzl
iyr:2013 eyr:2024 hcl:#02e17f byr:1960
hgt:163cm cid:338 pid:972201795

iyr:1994 eyr:2035 ecl:xry
hcl:z hgt:167in pid:159cm

ecl:hzl
byr:1952
eyr:2024 hgt:191cm pid:229400637 iyr:2011 hcl:#122db6

eyr:2022
pid:467667316 iyr:2019 hcl:#623a2f
hgt:161cm
ecl:oth

ecl:hzl eyr:2030 hcl:#733820 byr:1944
hgt:193cm pid:819137596

cid:321 hgt:184in ecl:hzl iyr:2018 byr:2010 eyr:2020 pid:171cm

ecl:amb eyr:2025 hcl:#c0946f pid:360891963 byr:1925
iyr:2017
hgt:180cm

hcl:#cfa07d byr:1949
eyr:1931 cid:350
ecl:#ff9943
pid:7550350393 hgt:75

eyr:2026 ecl:amb hcl:z pid:746919391 iyr:2014 hgt:179cm byr:1997

pid:157cm iyr:2030
hgt:152cm
hcl:ce8aa7 eyr:1976 ecl:grt cid:160 byr:2011

eyr:2022
hgt:183cm
byr:2000 iyr:2016 hcl:#a97842 ecl:blu pid:500935725

cid:245 eyr:2026 iyr:2015 ecl:gry hcl:#cfa07d
byr:1946

eyr:2022 hgt:168cm
pid:786361311 iyr:2013 hcl:#c0946f byr:1988 cid:244 ecl:hzl

byr:2014 hgt:176in iyr:2021
hcl:z pid:6361650130
eyr:2039 cid:300
ecl:#76310d

ecl:amb hgt:170in byr:2013
iyr:2024 eyr:2033 hcl:#888785

eyr:2025
iyr:1957 cid:182
ecl:blu pid:253552114
hgt:188cm hcl:z

cid:83 ecl:amb
eyr:2022 byr:1947
iyr:2013 hcl:#cfa07d
hgt:188cm pid:447734900

iyr:2013 hcl:#602927 byr:1979 hgt:167cm cid:321 pid:978238277 eyr:2020
ecl:grn

hgt:73cm
cid:199 ecl:amb iyr:2019
hcl:#733820 eyr:2021
byr:1939 pid:364966395

hgt:168in ecl:lzr eyr:2031
pid:#ff10ac byr:2014 iyr:2006

hgt:164cm eyr:1994 iyr:2010
ecl:amb hcl:#7d3b0c cid:240 pid:191cm
byr:2025

ecl:grn
eyr:2029
hcl:#7d3b0c hgt:158cm
byr:1939 iyr:2012 pid:855145518

iyr:2013 hcl:#ceb3a1
hgt:163cm eyr:2023 pid:761215570

hgt:154cm ecl:grn
iyr:2019 byr:1981 eyr:2021 hcl:#602927
cid:80 pid:427938374

eyr:2026 hgt:154cm cid:102 iyr:2012 pid:6632346648 ecl:amb
byr:2010 hcl:z

cid:302 iyr:2014
pid:161cm eyr:2037 byr:2026 ecl:gry hgt:60 hcl:9fb9e0

ecl:brn iyr:2015 pid:041582949 cid:180 byr:1938
hgt:158cm
hcl:#602927 eyr:2026

ecl:xry pid:#546891 hcl:#18171d hgt:71cm byr:1974
iyr:2018 eyr:2026

iyr:2015 eyr:2025 ecl:brn hgt:180cm hcl:#b6652a
byr:1938
pid:752379523

iyr:2020 ecl:grn hgt:179cm byr:1929
cid:103 hcl:#602927
pid:212212232

pid:262917603 ecl:gry iyr:2012 hcl:#fffffd hgt:165cm eyr:2022 byr:1965

byr:1960
eyr:2031 hgt:184in
pid:#ac1606 iyr:2013 hcl:#888785
cid:260 ecl:#7b2c3b

byr:1987
eyr:2025 cid:102
hgt:74in ecl:brn hcl:#4a6c75 pid:20220733 iyr:2028

eyr:2031 pid:823539963
iyr:1957
hgt:159cm byr:1953 ecl:oth cid:186 hcl:26d85f

ecl:gry iyr:2011
hgt:167cm hcl:#fffffd pid:001642707 eyr:2030 byr:1952

iyr:2029 ecl:grt
hcl:z byr:2011 hgt:64cm pid:37027672
eyr:1923

pid:021102096
eyr:2024 hgt:66 hcl:#a97842 byr:1922 ecl:gry iyr:2013

pid:166477382 ecl:oth byr:1982 iyr:2010 eyr:2020
hcl:#866857 hgt:60in

hcl:#7d3b0c
iyr:2018 pid:065652921 byr:1939
ecl:blu
hgt:180cm eyr:2028

ecl:amb iyr:2020 byr:1967 hcl:#fffffd eyr:2028 hgt:157cm

eyr:2029 hgt:185cm cid:85 hcl:z iyr:2014 pid:#1f4787 ecl:grn byr:2010

byr:1987 hcl:d397d9 iyr:2028
hgt:158cm pid:686994921 ecl:hzl

ecl:oth
byr:2008
pid:#db73d9 hgt:174cm hcl:#6b5442 iyr:1955 eyr:2028

eyr:2020 ecl:amb pid:490866828 hcl:#cfa07d cid:113
hgt:165cm

iyr:2011
pid:320518492
eyr:2028 byr:1940 hgt:164cm cid:84
hcl:#341e13 ecl:grn

hgt:142
hcl:z pid:152cm iyr:1953 eyr:2040 ecl:#e44f11 byr:2024

ecl:gmt hcl:be7483 eyr:2027
iyr:2026
pid:396722617 hgt:153cm

ecl:dne byr:2015
pid:330208482
hcl:#7d3b0c iyr:2014 eyr:2022 hgt:95

byr:1925 hcl:#7d3b0c
ecl:gry
eyr:2024
pid:694714722 hgt:158cm iyr:2015 cid:283

eyr:2023
hgt:183cm cid:345
hcl:#6b5442 ecl:hzl iyr:2019 byr:1971 pid:458416257

ecl:#dcae8b
iyr:2027 eyr:1940 byr:2009 hcl:f024de pid:20713584
hgt:169in

hcl:#888785 eyr:2026
byr:1984 iyr:2013 pid:935837461
hgt:193cm
ecl:gry

pid:7343429 byr:2002
hgt:191cm
ecl:lzr iyr:1983
eyr:1966 hcl:#623a2f
cid:302

hcl:#888785 iyr:2014 hgt:173cm
byr:2002 pid:005350165 eyr:2022

byr:2013 iyr:2028
ecl:lzr pid:5426915565 eyr:2018 hcl:z hgt:70cm cid:142

eyr:2021 hgt:157cm ecl:utc iyr:2014
byr:1934 cid:348 hcl:#623a2f pid:607329117

iyr:2015 hgt:167cm ecl:hzl
pid:088516395 hcl:#efcc98 byr:1968 eyr:2029

eyr:2028
iyr:2019
cid:199
ecl:amb
hgt:152cm byr:1928 pid:547112666 hcl:#623a2f

pid:406202463
byr:1950 cid:214
eyr:2021 hcl:#fffffd hgt:177cm
ecl:brn

eyr:2029
cid:210 byr:1982 pid:578085789 ecl:brn
hgt:187cm iyr:2010 hcl:#c0946f

byr:1980 hcl:#c0946f hgt:159cm pid:177650318 eyr:2024 ecl:amb iyr:2019

pid:923359071 byr:1997 ecl:#faa530
eyr:2028 iyr:2013 hcl:e6c902 hgt:177cm

eyr:2040
cid:98 hgt:156in
ecl:oth
iyr:1996 pid:81500971
hcl:#6b5442
byr:2017

byr:2004 iyr:1941
hcl:e1e4bb hgt:67cm pid:1143915351 ecl:#0d3e5d eyr:1972

hgt:184cm hcl:#623a2f
eyr:2028 pid:680951513 ecl:grn iyr:2014 byr:2001

hcl:#866857 hgt:156cm
eyr:2020
ecl:grn iyr:2010 pid:589945116

pid:599795227 iyr:2016 ecl:grn
hcl:#cfa07d hgt:157cm byr:1967 eyr:2029

hcl:#b6652a
byr:1966 iyr:2017 pid:117232314 ecl:oth hgt:186cm eyr:2029

pid:605019880
iyr:2020
hgt:169cm byr:1980 hcl:#623a2f
ecl:hzl eyr:2030

eyr:2019 hcl:#ceb3a1 pid:988269284
iyr:2015 byr:1989 hgt:171cm ecl:oth

cid:311 byr:1998 ecl:hzl
eyr:2027 hgt:152cm pid:734870801 hcl:#7d3b0c
iyr:2013

hcl:#efcc98
hgt:180cm iyr:2020
pid:202682423 byr:2027 ecl:grn eyr:2030

hcl:f0701f pid:161cm cid:291 hgt:160in iyr:2030
ecl:#e12345

cid:248 byr:1943 eyr:2024 hgt:181cm ecl:brn iyr:2010 hcl:#bf813e

byr:2005 hgt:187in eyr:2034 iyr:2025 hcl:z ecl:gmt
pid:78691465

byr:2000
hcl:#574f4e eyr:2024 iyr:2017 pid:#fec795 hgt:185cm ecl:gry

hcl:#a97842 byr:1959
iyr:2019 pid:690444949
hgt:160in eyr:1978

cid:236
iyr:2010 eyr:2025 byr:1976 pid:398376853
hcl:#341e13
hgt:150cm

hgt:182cm iyr:2019 hcl:#866857
ecl:grn
byr:1926 eyr:2029 pid:307880154 cid:94

ecl:blu
hgt:182cm pid:178cm byr:2019 eyr:2025
iyr:2022 hcl:#a2117d

eyr:2020 hcl:#c0946f ecl:amb pid:135511825 byr:1954 hgt:68in iyr:2017

hgt:188cm ecl:amb iyr:2011
pid:949021029 eyr:2028 hcl:#fffffd byr:1986

iyr:1949 pid:#8a8d94 ecl:#922a92 byr:1925 hcl:#63c4a5

hcl:#c0946f
ecl:grn iyr:2013 eyr:2024 pid:420295283 hgt:181cm
byr:1977

byr:1941 pid:299186098 hcl:#f1fa72
iyr:2013 ecl:amb eyr:2022 hgt:152cm
cid:150

ecl:blu eyr:2021 hgt:60in hcl:#623a2f
byr:1930 iyr:2018

eyr:2028 pid:663108638
hgt:75in cid:217
byr:1962 ecl:brn hcl:#733820

hcl:#341e13 hgt:188cm ecl:blu
pid:868930517
eyr:2029
iyr:2010 byr:1938

pid:194376910 byr:1956
hcl:#cd4ab4
eyr:1940 iyr:2012 ecl:#396cc3

pid:#c5da2a hgt:162cm
hcl:#866857
cid:95 ecl:#fa1f85
iyr:1965 byr:1963 eyr:2039

pid:44063430 hcl:289b20
ecl:#77ddd9 eyr:1953
iyr:1924 byr:2026 cid:267 hgt:180in

ecl:brn pid:990171473
eyr:2028 byr:1937
hgt:165cm iyr:2015
hcl:#fffffd cid:68

iyr:1968 ecl:lzr pid:#05a4ab eyr:1944 hcl:z

hgt:185cm hcl:#7d3b0c eyr:2029 ecl:oth
iyr:2016 byr:1997 pid:349316183

hcl:z
ecl:gry
hgt:192in pid:542996841 iyr:2019 cid:144 eyr:2028
byr:2026

eyr:2024
hcl:#18171d
ecl:grn hgt:160cm pid:399767457 byr:1979 iyr:2015

ecl:#924147 pid:665314 cid:216 iyr:2026 hcl:z
byr:2023 hgt:157
eyr:1987

eyr:1989 hcl:4f8779 ecl:#05ff52 iyr:1943 pid:3693010880 hgt:72cm
byr:2009

hcl:#c0946f eyr:2022
iyr:2015 hgt:157cm byr:1928 ecl:grn pid:243566446

eyr:2030
hcl:#733820 byr:1988 iyr:2017 cid:125 hgt:193cm ecl:amb pid:939550667

cid:161 hgt:157in
hcl:#cfa07d eyr:2036 ecl:#4efa35
iyr:2012 pid:3943280550 byr:1979

ecl:lzr hcl:#341e13 hgt:69cm eyr:2026 cid:322 byr:2006 pid:827964469

ecl:amb iyr:2012
eyr:2020 hgt:178cm pid:590705772 cid:218
hcl:#c0946f byr:1922

hcl:632b01 cid:252 byr:1933 ecl:hzl
iyr:2025 eyr:2040 hgt:191cm
pid:406010613

pid:711656819 ecl:blu eyr:2030 hgt:151cm
byr:1999 cid:319
hcl:#efcc98

pid:294223216 iyr:2012
hgt:171cm
eyr:2027
hcl:#ceb3a1 ecl:oth
byr:1952 cid:58

hcl:#888785 pid:457433756 eyr:2022 hgt:186cm
cid:336
byr:1923 iyr:2013 ecl:oth

byr:2014 hcl:6ce7d6 eyr:2030 pid:190cm iyr:2018 hgt:63cm ecl:#5063b9

cid:267 hgt:189cm
eyr:2020 hcl:#ffeffd iyr:2014 byr:1989
ecl:grn
pid:571696542

iyr:1953 hgt:160in
ecl:grt cid:188 eyr:2034
pid:179cm byr:2007
hcl:6895eb

hgt:165cm ecl:oth
iyr:2020
eyr:2028
hcl:#18171d pid:111506895

eyr:1957 cid:133 ecl:hzl pid:#e56ca2 byr:2003 hcl:8a9d65

hcl:6c4ecd byr:1930 hgt:179cm
eyr:2007 iyr:2028 ecl:#3d8705
pid:#dbfeec

eyr:2036
byr:1991 ecl:#2202d0 hcl:#341e13 pid:85636989 hgt:61cm
iyr:1930

byr:1996 iyr:2027 hcl:z
pid:780164868 ecl:zzz eyr:2026 hgt:73cm

byr:1940
iyr:1992 pid:132016954 eyr:2021
cid:147 hcl:#d78bfd ecl:xry

hgt:174cm
byr:1970
eyr:2021 hcl:#341e13 pid:086579106 iyr:2017 ecl:oth

ecl:oth cid:207 byr:1998 pid:479696359
hgt:174cm iyr:2017 eyr:2020 hcl:#6b5442

ecl:hzl iyr:2014
hcl:#cfa07d hgt:163cm eyr:2025
byr:1951 pid:563337128

ecl:gry hgt:172cm iyr:2013 hcl:#efcc98
byr:1970
pid:848996674
eyr:2027

hgt:163cm pid:583600660 iyr:2015 hcl:#18171d byr:1959 ecl:brn

hcl:#efcc98 pid:353178375 cid:145
iyr:2018 byr:1988 ecl:oth eyr:2029

hgt:62in
byr:1921 pid:125944934 hcl:#b6652a
eyr:2025 cid:71 iyr:2018 ecl:blu

iyr:2017 ecl:brn hcl:#602927 hgt:172cm pid:932690969 byr:1957 eyr:2026

hcl:#efcc98 pid:709772213 cid:146 ecl:oth byr:1998 iyr:2010 hgt:74in
eyr:2029

byr:1965
iyr:2011 hcl:#6b5442 cid:325 hgt:68in eyr:2028 pid:813272708 ecl:hzl

pid:57223084 hcl:#602927 ecl:grn
hgt:156cm eyr:1972 iyr:2017

pid:21573000 byr:2030 cid:168
hcl:baee61 eyr:2021 hgt:150cm
iyr:1950 ecl:#acdd7e

ecl:gry hgt:150cm hcl:#6b5442
byr:1927
iyr:2018 pid:161cm eyr:2021

hgt:153cm
iyr:2030 ecl:grn pid:575037626 byr:1921 eyr:2021 hcl:#866857

hgt:175cm iyr:2014
byr:1946 eyr:2025
cid:159 hcl:#18171d
ecl:oth pid:129913905

pid:566885568
hgt:157cm eyr:2021 ecl:gry byr:1933
hcl:#623a2f cid:223

ecl:blu byr:1981 cid:160
iyr:2014
hcl:#a97842 eyr:2021 hgt:172cm pid:714902414

hcl:#b6652a eyr:2021
hgt:168cm byr:1921 iyr:2018 ecl:oth pid:021318713

hgt:168 pid:222439573
cid:209
hcl:z byr:2016 ecl:#26a0fb
eyr:2031

hgt:181cm
byr:1970 eyr:2024
pid:476171876 ecl:hzl
hcl:#efcc98
iyr:2019

hcl:#18171d ecl:oth iyr:2018 byr:1949 hgt:165cm
eyr:2029 pid:078204562

byr:2021 ecl:blu iyr:1963
pid:2911597977 hcl:#ceb3a1 eyr:2020
hgt:154cm

pid:159642237
hcl:#81e94d ecl:gry eyr:2028 byr:1958

hgt:90 hcl:#a97842 pid:#db1158
iyr:1928 ecl:#c82a43 byr:1971 eyr:2036

eyr:2020
hgt:177cm iyr:2013
cid:347 ecl:grn
byr:1998 pid:455369144

byr:1936
pid:444305229 iyr:2013 eyr:2025 hcl:#733820
ecl:gry
hgt:175cm

byr:2027 hcl:z
hgt:61cm ecl:brn pid:836686228 eyr:2023 iyr:2030

byr:1931
ecl:hzl hgt:168cm eyr:2023 pid:956562488 hcl:#fffffd

ecl:#4126e5 pid:182cm iyr:2021
hgt:144 eyr:2039 hcl:z

pid:321400085 hcl:#733820 hgt:189cm
ecl:hzl byr:1923 eyr:2023 iyr:2016

iyr:2011 hgt:192cm hcl:#b6652a byr:1988 pid:998875769
ecl:#e612d9 eyr:2015

eyr:2021 iyr:2011 pid:265966660
byr:1934 hgt:180cm
hcl:#7d3b0c
ecl:gry cid:225

pid:550612542 ecl:oth byr:1931
iyr:2014 cid:99
hcl:#cfa07d hgt:163cm eyr:2026

ecl:gry hgt:156cm iyr:2018 hcl:#5d9d64 pid:295386055 byr:1996
eyr:2025

ecl:gry iyr:2013 pid:855457285 cid:309 eyr:2030
hcl:#733820 byr:1973

eyr:2030 pid:86472746 ecl:blu
hgt:192cm
iyr:2013 byr:1939 hcl:#b6652a

hcl:#888785
byr:1935
iyr:2018
hgt:155cm ecl:grn
pid:612879095 cid:108 eyr:2027

eyr:2016 hcl:z pid:025915371 iyr:2010 hgt:183cm ecl:gry
byr:2010
cid:228

hcl:#38dbf4
byr:1925 ecl:amb eyr:2020 pid:065102805 iyr:2018

cid:244 hgt:171cm
hcl:#cfa07d pid:466737179 eyr:2025
byr:1937 iyr:2020 ecl:oth

ecl:brn byr:1993 hgt:179cm hcl:#341e13 pid:855375268 eyr:2028
iyr:2018

pid:809135189 iyr:2020 hgt:162cm eyr:2027
hcl:#888785 byr:1988 ecl:grn

byr:2003 pid:4446708453
hgt:188cm iyr:2013 hcl:#888785 ecl:blu eyr:2008

hgt:165in ecl:#db642f iyr:2014
eyr:2020
byr:1955 hcl:371f72 pid:756089060

ecl:lzr
hgt:177in eyr:2037 pid:175cm
byr:2023 hcl:03b398 iyr:2026

iyr:2017 ecl:blu byr:1942 hcl:#733820 eyr:2023 hgt:151cm pid:289923625"""

def solve(data):
    lines = [i for i in data.split("\n\n")]

    things = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


    valid = []
    c = 0
    for line in lines:
        flag = True
        #print(line)
        for thing in things:
            if thing not in line:
                flag = False
                break

        c += int(flag)
        if flag:
            valid.append(line.split())
            #print(line.split())
    got = set()
    ans = 0
    for v in valid:
        flag = True
        for field in v:
            #print(field)
            k,val = field.split(":")
            if k=="byr":
                if 1920 <= int(val) <= 2002 and len(val)==4:
                    pass
                else:
                    flag = False

            if k=="iyr":
                if 2010 <= int(val) <= 2020 and len(val)==4:
                    pass
                else:
                    flag = False

            if k=="eyr":
                if 2020 <= int(val) <= 2030 and len(val) == 4:
                    pass
                else:
                    flag = False

            if k=="hgt":
                if val[-2:] == "in":
                    if 59 <= int(val[:-2]) <= 76:
                        pass
                    else:
                        flag = False
                elif val[-2:] == "cm":
                    if 150 <= int(val[:-2]) <= 193:
                        pass
                    else:
                        flag = False
                else:
                    print(v)
                    flag = False


            if k=="hcl":
                if re.fullmatch(r"#([0-9a-f]){6}", val):
                    #print("valid", val)
                    pass
                else:
                    flag = False

            if k=="ecl":
                if val in ["amb","blu", "brn", "gry", "grn", "hzl", "oth"]:
                    #print(val,"valid")
                    pass
                else:
                    flag = False

            if k=="pid":
                if len(val)==9 and re.fullmatch(r"[0-9]{9}", val):
                    pass
                else:
                    flag = False
        ans += int(flag)
        got.add(tuple(v))
    print(ans)
    return got

#solve(test1)
solve(test2)
solve(test3)
#solve(test4)
solve(data)


aidan = solve(data1)

print(aidan)

