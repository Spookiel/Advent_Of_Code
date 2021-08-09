import re
data =  """departure location: 44-709 or 728-964
departure station: 42-259 or 269-974
departure platform: 39-690 or 701-954
departure track: 49-909 or 924-965
departure date: 48-759 or 779-957
departure time: 38-115 or 121-965
arrival location: 32-808 or 818-949
arrival station: 45-418 or 439-949
arrival platform: 35-877 or 894-962
arrival track: 26-866 or 872-958
class: 32-727 or 736-969
duration: 35-446 or 460-968
price: 26-545 or 571-961
route: 35-207 or 223-960
row: 43-156 or 165-955
seat: 26-172 or 181-966
train: 49-582 or 606-952
type: 36-279 or 303-968
wagon: 26-657 or 672-959
zone: 36-621 or 637-963

your ticket:
83,127,131,137,113,73,139,101,67,53,107,103,59,149,109,61,79,71,97,89

nearby tickets:
539,619,928,309,835,99,521,478,54,340,849,859,376,357,524,841,221,935,806,147
231,827,907,526,238,542,181,853,303,143,116,701,206,140,927,203,443,753,151,258
445,679,816,617,82,102,197,100,239,490,488,78,707,349,689,335,847,183,144,314
476,833,232,489,937,256,87,409,223,364,978,939,398,331,153,945,513,237,934,272
492,927,578,788,808,529,739,20,201,688,405,877,228,168,361,521,400,398,618,520
332,694,481,571,523,516,395,122,844,358,232,132,315,486,899,154,269,201,831,50
907,706,927,126,133,97,217,334,745,751,580,862,526,845,680,125,96,445,863,322
498,753,844,670,150,657,853,150,377,487,152,369,500,241,360,204,142,236,948,91
578,675,491,230,332,464,258,858,508,330,492,780,494,234,839,645,160,795,896,687
814,875,617,185,490,490,501,940,224,751,609,844,442,525,640,609,336,251,532,685
684,196,757,841,580,576,18,319,150,249,676,337,155,115,652,638,475,398,789,379
445,490,199,140,88,694,184,247,307,386,198,85,905,860,484,244,532,224,681,251
172,936,701,440,779,941,639,351,238,70,787,91,259,340,58,541,815,399,238,202
715,369,504,226,138,866,783,231,580,147,82,335,533,144,530,462,836,751,473,801
932,459,242,947,653,150,618,683,198,608,88,342,948,497,675,53,681,544,315,615
422,244,791,929,799,128,374,473,148,931,381,822,318,853,147,367,531,412,242,470
464,899,490,846,381,326,271,948,396,318,653,981,310,822,502,895,78,935,78,461
231,339,79,530,680,461,863,521,839,517,379,108,395,613,644,751,823,212,206,151
526,507,403,354,931,859,787,728,247,781,643,203,847,326,506,79,65,332,91,783
571,182,753,841,338,746,254,307,896,648,726,89,314,706,943,464,444,481,465,928
184,513,335,941,303,198,537,571,409,337,497,621,350,617,98,897,850,679,794,260
235,255,393,310,188,65,943,543,94,374,500,482,122,992,656,523,704,742,331,792
315,152,320,983,493,166,754,376,619,480,149,929,330,80,529,131,150,57,251,842
54,77,540,141,61,205,273,214,745,145,166,131,93,525,500,521,223,52,237,404
300,616,784,250,852,354,327,944,675,859,673,941,789,829,234,104,842,85,742,98
110,244,95,93,529,162,82,309,142,680,65,410,531,758,511,790,333,352,926,397
496,518,828,896,52,828,805,62,470,121,853,831,346,654,684,196,535,15,251,381
231,444,530,616,795,620,78,460,947,748,757,78,706,336,82,317,186,256,216,196
520,838,365,445,928,855,418,943,195,689,176,638,151,59,82,495,58,681,737,545
172,755,782,71,514,336,383,470,168,70,168,199,307,102,793,250,739,174,368,279
897,734,446,184,254,785,499,949,903,405,401,679,356,753,354,351,842,443,207,203
60,577,746,229,105,475,640,877,848,477,545,525,793,752,313,315,318,983,537,249
474,833,611,169,61,800,759,228,321,833,303,673,513,862,76,122,803,520,67,667
504,919,413,521,514,251,785,170,656,759,510,537,579,462,794,756,687,479,864,507
949,774,866,805,357,442,183,874,934,195,511,742,756,683,396,407,637,348,866,344
687,305,781,780,821,586,945,94,87,230,353,376,849,379,510,368,709,489,113,191
275,356,277,655,529,493,541,141,132,804,620,171,382,443,483,978,737,536,532,904
357,369,142,383,802,782,722,391,905,684,226,413,379,74,792,618,351,939,580,578
368,394,514,461,445,933,677,324,318,250,863,266,855,703,781,142,460,74,753,947
935,852,127,241,309,825,481,206,642,81,375,862,330,21,496,60,677,238,532,138
258,680,336,136,640,193,372,100,227,856,495,103,92,341,356,703,568,147,311,514
412,673,398,244,397,313,378,780,107,905,318,208,172,374,464,690,379,686,538,638
660,321,894,681,515,539,486,403,469,91,675,186,386,839,197,639,411,873,69,837
845,413,996,87,314,674,362,258,783,412,341,529,519,654,526,757,899,617,909,492
127,749,682,785,735,418,112,834,934,381,613,107,748,474,84,72,514,355,942,701
541,100,75,155,645,410,612,519,976,656,854,140,61,140,401,827,466,798,385,192
332,126,836,373,545,313,379,69,345,751,348,750,746,643,763,519,943,508,679,274
642,521,55,479,54,615,323,247,736,80,979,489,97,238,759,579,363,826,91,929
227,497,467,249,808,441,906,361,815,523,206,352,383,521,798,84,360,74,680,100
96,486,465,382,796,198,500,717,462,617,245,247,649,941,946,750,408,845,637,311
379,168,181,100,507,798,928,784,174,128,830,480,113,311,379,474,361,613,909,325
130,144,649,305,273,637,112,353,528,786,944,866,931,269,381,271,153,902,552,129
520,908,58,249,842,831,756,253,21,238,645,607,902,200,439,100,112,324,374,672
614,173,149,316,132,309,484,270,249,104,542,524,350,357,244,331,507,405,793,345
943,140,784,620,818,558,780,53,894,673,500,370,109,539,372,376,505,785,909,782
900,187,113,464,991,534,368,181,463,841,747,362,945,640,153,227,241,944,833,743
863,838,340,366,230,500,643,103,772,127,88,754,611,496,791,444,440,903,75,467
649,828,617,466,188,502,315,352,866,758,919,247,835,574,750,409,468,247,359,202
371,846,121,755,474,472,176,325,153,97,949,201,65,171,908,500,277,937,90,388
929,392,539,469,843,440,947,893,347,312,128,63,754,685,947,227,679,470,945,303
731,77,872,620,88,616,104,681,204,312,115,688,386,195,676,506,87,707,519,149
278,365,780,785,874,251,114,321,499,898,729,101,637,684,167,797,826,930,615,51
319,924,819,856,202,71,102,55,838,81,231,150,656,840,354,679,744,475,344,814
926,657,378,507,927,389,680,238,185,319,475,897,132,936,685,540,16,331,508,613
681,897,228,303,835,356,523,403,314,709,382,272,370,109,470,479,923,443,896,782
677,239,501,233,180,928,351,101,373,151,321,347,445,198,112,679,828,751,680,96
840,497,237,318,490,848,248,351,413,850,945,662,460,945,439,929,126,199,330,320
647,489,508,105,648,253,270,807,201,110,537,12,336,369,581,609,190,535,676,489
534,668,686,442,938,394,798,755,190,412,505,375,101,752,490,405,875,573,417,677
231,461,260,138,611,824,333,331,406,351,229,97,756,926,678,849,488,758,230,121
82,347,442,172,652,898,687,491,392,539,538,389,257,505,334,325,840,89,918,138
517,352,192,701,848,617,804,704,344,785,58,839,351,140,394,242,144,342,179,142
166,140,226,442,183,499,166,272,839,795,908,165,901,703,262,91,358,127,872,834
788,157,156,675,876,376,473,404,709,752,373,780,324,146,169,819,807,337,514,204
190,511,822,204,495,948,123,117,932,509,148,706,66,110,861,674,637,545,486,855
119,227,439,442,808,378,929,949,313,142,359,789,503,442,908,310,315,474,395,935
367,210,531,480,142,245,833,172,320,137,468,800,827,930,199,318,904,642,516,865
538,198,113,62,362,528,787,668,936,657,184,345,895,236,385,829,522,253,758,352
315,708,796,639,162,690,688,750,366,171,509,476,708,782,637,368,934,125,73,248
617,156,576,737,521,755,932,266,939,203,690,578,853,98,414,50,759,440,819,331
593,232,442,468,578,949,383,129,800,152,77,386,935,819,925,470,305,396,308,874
102,361,319,187,226,942,493,272,247,68,475,364,398,141,821,900,56,480,814,307
650,796,98,92,687,646,128,140,168,813,203,825,851,80,136,473,581,150,865,806
263,520,275,378,406,113,59,194,759,128,522,183,498,167,185,702,652,606,133,578
707,331,737,748,820,759,257,742,856,500,318,814,507,898,244,153,470,319,532,110
488,382,380,145,126,807,359,343,606,82,750,194,607,981,409,151,860,862,339,900
873,620,230,924,345,750,62,387,802,113,97,930,63,416,750,76,657,507,260,325
111,749,114,785,477,572,248,687,500,64,925,931,132,783,795,491,998,248,754,56
115,83,245,512,638,327,108,451,826,757,675,521,342,350,102,462,348,841,874,798
941,822,582,948,500,645,393,757,214,362,103,132,181,515,227,828,827,406,375,232
647,362,660,738,497,366,803,505,335,105,75,153,313,759,501,241,62,149,748,926
123,146,613,390,742,638,907,515,334,686,411,854,933,469,174,126,169,395,842,351
830,315,59,573,843,656,523,533,528,403,259,141,523,333,876,355,880,680,134,942
234,22,808,145,529,374,142,572,344,409,607,930,858,825,804,223,534,505,466,539
684,688,940,524,357,684,844,673,381,794,895,516,308,582,380,487,731,241,797,685
196,112,331,528,533,396,489,579,266,496,77,440,650,165,399,469,475,507,364,56
354,139,945,330,742,894,782,989,87,231,54,358,51,681,350,652,936,745,134,936
804,439,935,234,944,849,186,173,254,690,326,102,149,926,115,792,829,167,508,746
388,684,243,814,80,350,637,335,442,146,474,825,477,686,578,331,269,378,472,828
826,863,520,70,279,522,801,579,500,237,696,534,242,259,932,540,182,544,72,701
886,227,369,89,612,147,488,152,511,646,104,853,352,94,741,223,858,150,383,680
792,51,440,64,838,116,195,674,70,902,829,779,682,404,808,860,619,466,807,836
652,499,177,830,104,674,377,128,787,123,153,782,230,237,526,478,273,523,92,85
418,364,405,327,502,538,539,278,372,508,245,306,325,488,548,674,97,135,944,906
409,996,83,929,461,485,829,384,171,844,933,755,780,860,491,331,473,541,874,142
390,92,141,310,747,142,653,498,203,829,946,393,142,251,360,22,804,385,240,167
874,255,324,340,562,529,366,190,100,480,109,171,947,491,188,154,680,404,275,486
945,947,61,110,500,920,875,248,352,56,475,949,876,686,745,443,171,821,348,645
705,498,139,798,369,418,666,124,227,578,530,376,607,122,613,87,101,50,930,129
475,235,549,581,610,820,206,96,901,802,128,818,413,542,151,362,401,474,76,331
506,608,462,708,980,838,582,803,56,503,83,258,384,925,171,874,152,823,170,89
517,606,475,644,105,195,846,445,323,619,498,183,310,79,493,155,90,533,259,218
63,619,373,850,902,90,153,542,269,330,94,357,797,203,909,201,776,615,606,340
501,342,74,394,94,212,401,475,877,72,519,128,148,640,859,68,525,54,358,904
875,821,377,781,823,781,398,619,945,130,930,750,802,752,704,439,1,645,337,309
533,830,474,829,98,613,896,744,512,126,248,511,113,250,66,515,585,128,877,259
201,858,793,791,828,471,859,581,899,76,836,738,259,155,816,360,474,414,277,835
5,324,784,71,677,617,745,808,184,56,478,682,578,310,390,330,656,872,305,684
508,686,519,385,245,759,766,136,898,128,332,205,276,58,60,252,906,167,737,169
799,650,674,67,181,243,155,254,785,208,934,197,835,350,76,865,516,248,837,503
361,90,874,251,310,733,155,60,69,276,325,370,330,149,62,397,519,704,823,345
186,256,497,252,75,880,516,278,172,381,61,357,358,115,858,202,512,375,836,247
465,324,828,443,518,708,781,895,122,334,161,759,517,356,616,399,65,796,127,236
792,170,109,461,141,928,758,201,101,114,739,153,108,675,938,512,177,330,580,943
92,407,385,278,92,723,333,757,936,373,90,788,388,505,738,609,826,321,153,858
350,780,492,311,414,306,702,252,257,782,837,823,137,166,988,648,186,781,613,789
83,341,408,537,607,483,948,122,349,757,144,81,945,757,758,474,370,651,947,567
110,689,77,706,383,353,395,187,399,402,186,223,816,373,112,530,908,327,531,851
492,137,785,209,610,392,791,411,523,198,377,386,225,236,344,837,491,781,393,579
233,172,271,138,875,789,512,81,63,406,479,232,122,704,895,946,448,136,684,949
351,238,909,505,96,523,192,444,491,259,313,345,100,530,116,257,532,646,103,675
642,149,898,346,487,470,896,358,493,674,275,461,503,572,443,787,839,905,499,117
306,947,308,523,334,467,127,782,389,835,448,862,895,482,614,278,252,402,641,336
232,368,805,944,138,86,143,499,644,60,320,942,89,533,489,71,782,927,327,17
141,672,108,175,844,378,843,647,223,372,140,109,705,785,407,843,795,400,182,310
253,684,377,93,409,606,688,23,476,51,709,828,860,736,156,75,483,169,441,92
519,312,95,899,115,949,818,308,119,611,206,372,643,524,63,757,89,538,783,801
577,872,902,510,51,239,278,541,576,235,780,475,758,321,350,575,117,324,83,410
932,796,508,832,894,392,314,90,58,13,478,440,942,818,145,271,736,475,181,937
113,737,758,182,145,454,332,66,52,488,545,129,500,126,509,703,306,137,534,618
928,900,799,575,417,254,903,373,803,803,263,313,365,100,894,250,842,799,929,128
69,705,638,72,321,814,610,397,926,902,67,499,122,508,74,744,825,746,183,410
926,316,324,483,348,356,544,945,865,538,380,508,76,758,506,380,326,640,118,824
832,340,786,225,704,206,508,535,843,347,326,120,620,473,650,247,100,238,309,337
677,581,526,334,677,705,266,60,367,485,646,88,252,104,752,509,908,486,684,377
55,861,490,521,265,182,339,876,575,242,782,153,673,495,256,534,360,346,233,361
446,126,228,876,991,351,271,499,239,831,618,708,935,256,704,904,129,131,227,850
219,642,394,413,129,276,843,701,619,349,242,247,608,320,824,864,894,536,701,255
544,642,256,128,379,279,307,523,256,75,410,536,357,785,806,790,663,826,642,392
311,337,896,352,315,538,786,271,370,54,129,89,946,837,71,519,715,818,76,270
871,638,385,795,238,63,645,226,388,337,128,270,679,839,846,516,314,607,616,475
94,794,188,392,490,73,144,908,504,139,182,573,844,391,947,333,528,549,782,384
758,517,808,637,347,836,105,610,643,852,55,719,581,646,74,362,396,410,141,337
949,749,745,848,187,51,350,497,165,543,929,321,245,945,272,121,396,810,198,108
407,54,341,519,926,801,73,397,606,524,385,470,413,346,670,80,279,360,901,392
794,139,837,745,834,380,701,312,463,705,151,313,682,168,866,1,703,500,476,202
544,892,621,354,924,134,736,793,338,872,346,80,823,675,121,97,801,464,508,58
370,538,474,641,171,189,342,381,94,145,999,384,383,400,645,866,513,140,618,97
230,621,616,240,675,414,933,22,362,828,618,926,486,393,895,88,110,230,528,940
483,852,446,339,512,684,582,200,896,862,979,353,319,610,145,374,581,446,750,252
157,648,683,439,460,224,357,135,279,69,899,154,75,515,321,349,115,657,156,189
414,794,652,930,397,440,655,306,484,512,342,861,344,902,100,860,513,976,66,388
405,932,488,444,745,870,528,446,657,188,863,689,475,56,708,476,325,757,336,638
456,783,396,84,237,107,443,645,106,652,304,337,110,477,134,899,145,410,709,544
334,865,677,708,642,660,343,83,945,855,899,529,704,877,675,199,639,342,337,848
490,855,851,784,119,652,489,416,349,538,705,439,736,537,751,312,152,273,307,95
696,125,500,754,90,516,681,533,902,226,97,377,57,322,312,191,384,794,109,196
195,50,197,253,339,992,502,168,402,107,757,137,247,62,275,855,245,231,645,86
638,316,191,524,699,821,898,205,102,98,375,279,376,97,82,582,233,386,347,242
177,369,248,754,803,270,927,382,305,532,854,854,614,355,746,356,484,253,388,406
844,896,376,832,385,757,755,930,376,509,353,569,255,442,166,312,498,894,394,738
362,591,803,532,678,527,517,852,345,440,832,948,403,673,96,228,861,909,840,412
484,817,196,102,476,352,232,742,359,367,609,82,207,201,520,521,233,940,384,480
906,329,207,67,510,71,98,920,857,384,77,247,571,388,121,387,147,241,894,478
390,530,97,924,187,681,120,69,151,226,239,750,945,399,389,613,334,897,463,223
345,276,484,617,229,102,580,989,155,683,639,485,545,89,348,800,940,257,137,98
68,711,59,69,646,496,410,352,94,519,947,896,465,67,76,830,481,411,95,255
704,535,780,309,314,64,63,904,509,93,408,225,189,372,503,139,146,512,4,621
277,406,273,709,461,324,923,377,645,747,56,327,820,576,60,502,487,191,754,876
364,325,755,509,677,385,235,349,945,480,641,858,142,905,933,214,306,806,97,827
4,187,466,402,929,944,125,256,705,199,130,849,741,136,234,944,650,274,682,781
318,340,499,237,348,396,682,62,131,574,708,380,278,866,927,85,267,877,830,371
776,196,576,749,353,362,934,315,476,538,272,510,396,575,93,574,498,185,741,256
50,909,410,647,920,305,655,184,233,361,391,908,258,779,530,708,655,793,92,651
677,226,140,709,312,201,443,91,657,899,111,502,464,62,365,374,195,330,670,833
555,346,608,401,256,128,318,418,353,56,187,743,231,87,133,909,113,363,319,939
204,313,485,190,620,390,820,369,737,323,197,121,488,460,655,812,529,617,185,902
749,678,375,242,514,752,325,709,736,532,143,776,269,656,510,486,865,484,305,905
942,247,779,305,361,707,817,270,323,833,440,105,242,687,201,875,334,411,132,863
484,653,224,511,322,387,229,309,470,64,186,362,202,482,277,660,645,342,320,501
608,465,234,143,369,740,363,164,928,805,189,315,154,828,147,346,690,846,621,524
825,78,355,520,840,768,58,410,304,581,464,279,572,145,521,534,908,872,755,148
71,901,640,395,718,200,860,854,834,908,371,832,277,904,441,378,780,756,927,130
489,79,794,258,54,790,792,82,246,80,513,821,97,350,846,144,572,277,695,190
139,571,742,381,506,515,679,649,822,853,532,908,23,516,132,474,132,73,857,251
61,805,355,524,851,894,691,81,905,924,898,473,652,749,460,948,512,185,414,519
505,752,239,508,817,188,345,906,198,525,340,355,688,516,247,517,476,847,542,169
649,646,898,462,539,472,396,310,148,832,303,187,362,848,402,646,853,661,477,91
612,383,369,231,229,939,351,106,820,313,401,175,654,644,342,334,235,367,675,853
794,120,754,469,399,383,613,579,360,87,418,414,390,828,864,606,345,860,309,200
746,539,316,14,800,274,641,507,335,410,745,872,947,131,227,656,900,535,802,460
945,836,325,610,376,939,616,235,311,408,322,102,743,442,697,141,825,321,534,861
252,203,78,611,824,653,348,700,946,508,864,338,98,78,611,319,439,344,791,232
508,943,13,933,83,193,149,647,786,385,739,477,707,199,486,746,169,155,466,315
472,782,945,275,53,618,340,377,390,545,849,753,375,355,468,704,856,480,157,305
338,507,476,303,271,541,135,528,790,53,565,505,249,387,678,747,860,509,466,844
140,246,64,309,196,94,834,193,136,97,471,827,251,170,713,757,738,344,460,388
847,290,440,313,534,754,481,822,754,740,316,469,538,790,793,864,325,196,575,796
645,672,342,193,646,305,781,189,139,979,316,900,749,324,478,525,753,934,256,73
613,324,781,581,56,335,524,812,74,142,229,748,873,378,895,529,316,755,147,342
95,106,310,303,345,490,736,145,544,614,127,193,93,333,15,56,463,532,861,947
366,460,388,806,540,444,96,58,442,577,620,741,685,836,209,785,53,933,787,576
522,322,739,572,618,938,686,444,756,254,482,196,333,360,799,101,639,572,768,356
127,856,860,943,658,87,115,108,862,619,675,384,581,70,526,789,403,369,938,139
475,256,471,91,840,71,183,938,316,255,582,522,840,501,145,677,700,839,866,655
744,262,389,538,839,844,194,907,228,181,478,941,418,948,329,418,329,379,643,127
237,85,72,150,574,619,678,82,658,71,411,674,273,527,856,791,834,327,87,756
390,500,270,354,74,701,567,497,611,779,146,741,328,383,877,309,90,749,279,237
379,155,70,508,530,171,906,257,376,535,778,152,439,129,235,80,803,859,743,522
527,690,385,491,249,780,618,57,798,365,409,223,924,537,903,498,874,137,720,580
536,875,477,246,114,167,55,803,609,525,670,834,244,67,54,704,753,757,127,829
653,942,643,938,214,751,80,749,749,513,645,838,866,538,145,60,275,674,673,346
914,113,304,639,310,783,851,825,685,309,69,351,875,155,152,238,353,575,78,638
822,334,935,793,146,492,861,767,529,753,277,758,843,321,468,491,340,679,83,226
444,870,341,653,852,89,651,941,309,258,645,841,606,364,649,873,138,529,259,800
898,683,464,783,897,607,99,183,483,395,219,932,706,847,737,128,754,409,259,409
608,564,144,86,523,941,226,519,97,925,333,67,383,501,226,581,106,805,481,614
171,55,392,79,501,925,189,196,366,269,996,833,531,371,110,785,354,201,759,352
374,60,400,272,54,74,353,522,494,785,811,277,69,201,744,399,341,929,940,66
190,805,131,494,806,260,753,576,131,531,896,384,607,354,791,194,149,644,904,500
68,498,742,747,57,792,9,256,508,942,354,614,110,339,325,851,826,64,64,143
443,92,847,250,516,827,247,562,71,794,224,751,498,484,279,202,513,244,641,542
379,487,709,324,906,204,613,207,553,904,319,792,805,368,168,617,840,442,488,205
249,876,640,471,542,801,744,245,127,206,808,978,823,925,513,873,347,69,931,442
818,353,391,512,102,175,402,362,94,247,682,257,493,441,73,397,123,839,575,738
135,59,606,183,743,255,528,171,387,513,473,577,66,899,139,65,410,757,371,178
100,315,606,894,345,131,199,472,123,931,646,993,493,615,611,154,182,418,106,835
227,580,210,650,201,225,374,675,362,366,269,402,127,399,808,409,504,688,205,506
83,862,749,940,760,446,483,468,223,103,378,740,379,132,753,131,329,169,197,136"""
L = list(l.strip() for l in data.splitlines())
limits = []
mine = None
other = []
for l in L:
    ints = [int(x) for x in re.findall('\d+', l)]
    if len(ints) == 4:
        limits.append(ints)
    elif len(ints) > 4:
        if mine is None:
            mine = ints
        else:
            other.append(ints)

n = len(limits)
assert n == 20

p1 = 0
OK = [[True for _ in range(n)] for _ in range(n)]

for vs in other:
    assert len(vs) == len(limits)
    ticket_valid = True
    for v in vs:
        valid = False
        for a,b,c,d in limits:
            if a<=v<=b or c<=v<=d:
                valid = True
        if not valid:
            p1 += v
            ticket_valid = False

    if ticket_valid:
        for i,v in enumerate(vs):
            for j,(a,b,c,d) in enumerate(limits):
                #print(f" FOR TICKET {i} AT RULE {j} WITH VAL {v} AND LIMS {(a,b,c,d)}")
                if not (a<=v<=b or c<=v<=d):
                    print(f" FOR TICKET {i} AT RULE {j} WITH VAL {v} AND LIMS {(a,b,c,d)}")
                    OK[i][j] = False
        #input()
print(p1)

MAP = [None for _ in range(20)]
USED = [False for _ in range(20)]
found = 0
while True:
    for i in range(20):
        valid_j = [j for j in range(20) if OK[i][j] and not USED[j]]
        if len(valid_j) == 1:
            MAP[i] = valid_j[0]
            USED[valid_j[0]] = True
            found += 1
    if found == 20:
        break

print(MAP)
p2 = 1
for i,j in enumerate(MAP):
    if j<6:
        p2 *= mine[i]
print(p2)