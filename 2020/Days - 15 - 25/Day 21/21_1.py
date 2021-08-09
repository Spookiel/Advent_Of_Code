
import re
from collections import defaultdict, Counter
from itertools import permutations, combinations,product
from functools import lru_cache
adj4 = [[0,1], [1,0], [-1,0], [0,-1]]
adj8 = adj4+[[1,1], [-1,-1], [1,-1], [-1,1]]

def lmii(delim=" "):
    return list(map(int, input().split(delim)))

data = """bffxt gbsr qsfjh gvcrp bdmmnn fghcjm svxjl bbsjt vjgvx lvtglg mgbcxxg pqkzl zqrgzc gxg sgtkj rcsrk ltzdz pzsx zhpn tznx mgvm slhrk fzbn tttc mjmfk nlph mnbbg fgmjgxx lftp vxsjdfl xldmrv grspss nphhnzj kdct qlpsq jcvrbsv rbxb jbbsjh pmrf tvxrpmq tdmqcl cmqj bfhkjm pncz qtrk gjpgp xmd gnfl xktgd qsr bdlcbg cpttmnv skzkfc svgrpz mvtjf vnjxjg qrhrmj xdpjls dcdjzd grn blltznj rsjt rnjktbf ccrbr hqgc cmdfcb qfdh kkhr tlbk vfrhm mzqjxq bnjfqpv (contains sesame)
qrfpq rnjktbf tsgb cpk ppqsg zbxfm qbxmst jqkc nlph tcc qjvgh lftp fbtqkzc tvxrpmq mzqjxq ltzdz gvcrp hdzxfn zrcqxd vzf nphhnzj mjmfk qrhrmj hbrk zfj rmmzt bcc tttc vjgvx svgrpz hdxpf bdlcbg crbl ddpg kvvzs gbsr bbsjt pgdc frcxz pqqsx srffnhh zqrgzc bvmld dhhsr ghfd rqqxrb tdmqcl cpttmnv jbbsjh jcvrbsv snksnr cjhgj vbx ccrbr gxh fgdts bshd gmspg xhksx vzjk mgvm kg fsfxl blltznj jxdk cxxdh gcspgn xldmrv (contains nuts, dairy, eggs)
zqbhtj svgrpz fgdts dblp tttc zrcqxd gmspg sgtkj bsdtlx bffxt gvkcgbb cxxdh tsc bdlcbg kpvxqt lvtglg fbtqkzc vnjxjg fsfxl vhb rlxvs tdpgb mzqjxq mvskm gjpgp dgnbsz grn zbxfm rxdbdq qrdqpnd rqqxrb gfcpds qbxmst ccrbr nlph jcvrbsv kdct cbhfjjq dhhsr hdzxfn kvhhnx svxjl kg hqgc qxksrfh lftp gprsvmt hlxr tlbk jbbsjh rmmzt bv xldmrv fmxltts mgbcxxg tcpjd jdpl gtpzt cmqj pzsx rzbjx fghcjm gvpq gfjgh nzzxdj frcxz bdmmnn cjhgj qjvgh bvmld mjmfk jxdk pqkzl cpttmnv bvvrkn zhpn (contains wheat)
mvskm vfrhm zqrgzc cxxdh lftp zqbhtj grspss mjmfk zfj mgbcxxg kbml cvhn bsdtlx tdmqcl fzbn rnjktbf xmd cpttmnv kg svxjl gprsvmt qrdqpnd pchkj bnjfqpv scqvnn snksnr vzjk jqkc zcvzt cbhfjjq mfdtjx pncz grpdz bshd ccrbr nphhnzj plqgqvk ghfd qlpsq dhhsr xktgd fgdts hsgzgb cjhgj lllm gcspgn zrcqxd hdv ndjs tznx mzqjxq fsfxl pgdc nlph gtpzt crznk mnbbg gvpq kvhhnx gxg dgnbsz hlxr cpk tbbf skzkfc vnjxjg tcpjd qjvgh srffnhh jbbsjh jdpl qtrk dtkdz xdpjls bvvrkn (contains nuts, eggs, soy)
stq vgzx ccrbr hbrk kfqnkld gvkcgbb bvvrkn cnfzz tvxrpmq mvtjf plqgqvk bshd vhb tznx bbsjt grpdz qhlntcc mjmfk gjgqxt qtrk svgrpz bv tdmqcl srffnhh qrhrmj kg svxjl pqqsx mzqjxq crbl lrrkhsq qjvgh rmmzt rcsrk lllm zqrgzc rsjt jcvrbsv tgqjnp gfcpds mnbbg nlph kkhr fgdts fmxltts fgmjgxx nphhnzj vnjxjg cmdfcb gcspgn bsdtlx sngvn fbtqkzc hxpc qstnz tlbk bnjfqpv jbbsjh tbjnhb hsgzgb zrcqxd rlxvs mgvm ltzdz vzjk zhpn pncz grn lzqfh (contains sesame, peanuts, eggs)
slhrk kvvzs vnjxjg gmspg gfcpds gkntmb cvhn tsgb dgnbsz gvcrp vzf bv cpttmnv tnhcqg dcdjzd vfjp lvtglg hpkznb vbx mvskm vjgvx hsgzgb khtfps gxh crznk vhb qbpts bdmmnn qtrk kdct sgtkj gtpzt shb ccrbr stq pzln tsc scqvnn tznx nlph xmd gjgqxt tlbk qlqqf hkbzj zrcqxd dtkdz dhpqh fbtqkzc cbhfjjq grpdz qlpsq ghfd qsfjh bshd cjhgj qsr kkhr vzjk qjvgh skzkfc tdmqcl ltzdz xktgd frcxz jbbsjh rnjktbf vfrhm (contains nuts)
nlph kkhr dcdjzd fgdts bdlcbg scqvnn cvhn qrhrmj rnjktbf gfcpds qhlntcc cpk qbxmst vzf gcspgn rmmzt lzqfh fzbn zcvzt grn hkbzj rsjt frcxz xhlgnz bnjfqpv tp tgqjnp dhpqh kpvxqt fgmjgxx sngvn qxksrfh slhrk gvkcgbb fbtqkzc jbbsjh qsfjh qsr svgrpz cpttmnv gmspg ddpg nphhnzj tdmqcl dbpr xktgd vzjk pzln gprsvmt grspss ccrbr vfrhm tvxrpmq fsfxl bbsjt mzqjxq pmrf hpkznb crznk bdmmnn dblp zbxfm svxjl mjmfk lftp zhpn tbbf bcc pqqsx qrdqpnd mgvm (contains nuts)
tcc bdlcbg tznx kkhr rlxvs fgdts xhlgnz cpttmnv sgtkj svxjl vfrhm cxxdh zhpn zqrgzc crznk nzzxdj czfhm tbjnhb xlgjn bsdtlx grn gvcrp zrcqxd nphhnzj bvmld hxpc grspss tmbtvld cbhfjjq hdv vnjxjg ccrbr tgqjnp qfdh mgvm tsgb vgzx jbbsjh rnjktbf ghfd cpk gvpq mnbbg fzbn fbtqkzc pchkj vzjk qsfjh pncz hdxpf mcc fmxltts mzqjxq pzsx hpkznb bvvrkn rmmzt xhksx gjpgp rbxb grpdz qjvgh gkntmb zjpc gfjgh tlbk gtpzt mjmfk ltzdz vzf scxkgk nlph bv fhbbjj cjhgj xdpjls zpfs fsfxl rzbjx shb bshd pzln (contains shellfish, eggs, wheat)
crbl tnhcqg fsfxl jvjdqd crznk zbxfm gjgqxt dcdjzd pmrf gxg zjpc zrjh nzzxdj kkhr tdmqcl hdzxfn scxkgk cvhn mcc fbtqkzc lftp kpvxqt fhbbjj ccrbr kvhhnx tgqjnp fgdts bbsjt gvcrp qxksrfh xktgd lllm lvtglg shb dhpqh svgrpz dhhsr tcpjd mgbcxxg plqgqvk gnfl vhb qlpsq bvvrkn gxh cpk zcvzt bsdtlx rnjktbf fghcjm pchkj vzjk zhpn vfrhm qsfjh blltznj nlph bnjfqpv grn pzsx dbpr tcc cpttmnv jbbsjh vnjxjg jtlpb qstnz cmqj khtfps ncnzr vgzx mnbbg qlqqf qrdqpnd (contains nuts, eggs, peanuts)
gjpgp grpdz xlgjn hlxr krv svxjl pzln nlph hdxpf cmqj rnjktbf dcdjzd lllm ppqsg fbtqkzc nphhnzj qstnz xhlgnz vfjp zqrgzc jdpl bdmmnn kvhhnx gxg jxdk hdzxfn gkntmb xdpjls tbbf jbbsjh zfj lzqfh tmbtvld tttc zrcqxd vzjk ccrbr cpttmnv cpk pqqsx gmspg plqgqvk pchkj mgvm mzqjxq ltzdz rbxb skzkfc tsc zpfs rsjt bvmld bshd jvjdqd hqgc grn lrrkhsq zjpc dbpr gvcrp xldmrv tcc mvtjf zhpn scxkgk sngvn rcsrk rzbjx qrfpq tdmqcl rqqxrb fhbbjj pzsx rmmzt (contains dairy)
tmbtvld kvhhnx stq jvjdqd zqrgzc vnjxjg ccrbr sngvn lrrkhsq lftp slhrk lvtglg hdzxfn frcxz cvhn tdpgb fghcjm cmdfcb rbxb cpk ddpg hbrk pgdc fbtqkzc qstnz qjvgh tdmqcl vzjk jbbsjh qbpts hqgc qrhrmj bvvrkn ltzdz jdpl mzqjxq bbsjt qsfjh nphhnzj qrfpq zfj vxsjdfl zpfs qsr cmqj gcspgn bdlcbg gnfl crznk zcvzt pqkzl nlph tvxrpmq svgrpz jqkc (contains sesame, soy, wheat)
blltznj mzqjxq vfrhm xhksx shb cpttmnv mvtjf vzf xktgd svxjl hbrk fsfxl gvcrp hdxpf cmqj zbxfm glpm gkntmb hdzxfn bvvrkn gxh mgbcxxg fgdts hkbzj czfhm gxg rxdbdq bnjfqpv tvxrpmq bbsjt bvmld pchkj rmmzt xldmrv tdmqcl pgdc gjgqxt tbbf qbpts tcc fhbbjj sgtkj qrhrmj xhlgnz kpvxqt ppqsg grn grpdz xlgjn vhb gnfl tmbtvld cvhn snksnr cbhfjjq fbtqkzc gprsvmt jbbsjh vnjxjg qfdh dbpr nlph (contains sesame, soy, dairy)
tlbk qrhrmj bvmld qbpts mcc fgmjgxx fghcjm gfcpds vnjxjg snksnr gjgqxt ncnzr xdpjls vjgvx vbx grpdz bffxt stq jtlpb bnjfqpv gxg pchkj bshd jbbsjh fmxltts blltznj xlgjn crznk zbxfm zrcqxd czfhm qstnz mvtjf bvvrkn mgvm qlqqf pncz tdpgb mfdtjx tdmqcl cpttmnv tgqjnp fbtqkzc ccrbr gprsvmt xmd mzqjxq ltzdz gvpq ndjs jqkc kbml grn hqgc xktgd cxxdh shb hdzxfn (contains eggs, sesame)
hkbzj gfjgh crbl hdv jbbsjh gxg gvkcgbb vjgvx vzjk pzln cjhgj fsfxl lllm bdmmnn kg dhhsr qrdqpnd shb jvjdqd rnjktbf ltzdz grspss svxjl kbml bvvrkn fgdts qstnz tsgb zpfs czfhm dhpqh dbpr tbbf lrrkhsq mzqjxq cpttmnv lvtglg xhlgnz mjmfk krv zhpn kpvxqt fhbbjj pzsx qsfjh hdxpf ddpg ncnzr fmxltts skzkfc xldmrv ndjs vgzx nzzxdj grn hlxr khtfps crznk bffxt vfjp zbxfm dtkdz tbjnhb qxksrfh mnbbg xhksx qrhrmj gprsvmt tvxrpmq ccrbr gmspg svgrpz blltznj dblp hpkznb nlph hdzxfn jqkc fbtqkzc mcc tp frcxz vnjxjg gjgqxt vfrhm (contains dairy)
gvkcgbb hbrk pmrf mzqjxq hdzxfn gfjgh vgzx qrhrmj hqgc qlqqf kdct tvxrpmq cnfzz fzbn bbsjt tgqjnp bvmld kpvxqt qhlntcc nlph tbjnhb rmmzt mvskm xktgd kg pqqsx xlgjn ccrbr gcspgn crbl vfrhm rqqxrb qbpts cmdfcb gxh qsfjh pzsx khtfps ddpg bfhkjm hkbzj skzkfc pncz dgnbsz grpdz bffxt tdmqcl fbtqkzc svgrpz tcc zrjh tcpjd gbsr bvvrkn ncnzr svxjl zcvzt scxkgk rnjktbf gfcpds gjgqxt kbml ndjs jbbsjh shb nphhnzj vnjxjg jvjdqd zqbhtj (contains eggs)
blltznj lrrkhsq gvpq tcpjd vgzx vfjp rxdbdq zrcqxd kkhr gnfl gbsr rcsrk hxpc tznx zpfs svgrpz bffxt tdmqcl zhpn gjpgp lvtglg bshd fsfxl rsjt cmqj kvhhnx jbbsjh bsdtlx ghfd pzln pchkj frcxz jcvrbsv snksnr xmd zcvzt pzsx vzjk slhrk gprsvmt fhbbjj hdv bnjfqpv hsgzgb xhksx dbpr dcdjzd vbx cpttmnv scxkgk gjgqxt fghcjm fgdts mzqjxq xlgjn qrdqpnd fzbn jxdk hdzxfn bdmmnn fbtqkzc gmspg pqqsx vnjxjg ccrbr tttc vxsjdfl tnhcqg nzzxdj mvtjf mfdtjx (contains peanuts, nuts, dairy)
qfdh mzqjxq tbbf gfjgh ccrbr gvpq svgrpz tcc fbtqkzc gfcpds mvskm rlxvs pzln bsdtlx jxdk gbsr vgzx xktgd pncz cpttmnv qbpts rqqxrb tttc sngvn rsjt lllm qrdqpnd jtlpb vzf dgnbsz zfj gjpgp qrhrmj khtfps crznk jdpl cvhn xldmrv gjgqxt zjpc vnjxjg vxsjdfl frcxz tdmqcl tnhcqg xdpjls tvxrpmq mgvm vbx grpdz kkhr dhhsr jbbsjh (contains eggs, sesame)
vfjp pncz jvjdqd xmd tsgb gvkcgbb rlxvs pqkzl bsdtlx mcc nzzxdj qrdqpnd cjhgj tnhcqg zbxfm krv tlbk tmbtvld grn kvhhnx mzqjxq mnbbg hxpc pqqsx bvvrkn stq vnjxjg cbhfjjq shb gfjgh gjpgp hdxpf tcc jbbsjh qrfpq cpttmnv mgbcxxg ddpg qlqqf pchkj svxjl tp fgdts qstnz jcvrbsv bcc bdlcbg dtkdz scqvnn fsfxl nlph qbxmst tdpgb tsc gvpq tbbf cvhn tbjnhb pmrf fhbbjj tdmqcl mfdtjx cpk lvtglg gjgqxt tcpjd fmxltts hbrk fbtqkzc jtlpb ppqsg qjvgh (contains eggs, nuts, wheat)
fgmjgxx zqrgzc ghfd dgnbsz vnjxjg crbl kdct gtpzt vxsjdfl grn rcsrk mfdtjx zqbhtj hdv ltzdz mzqjxq rlxvs gvpq vgzx qsr tsc pqqsx tcc xktgd cmdfcb dbpr zfj lllm gjgqxt qbxmst gjpgp jbbsjh gbsr mnbbg pncz bsdtlx kpvxqt tdmqcl xldmrv cpttmnv hbrk qsfjh kkhr nphhnzj hdzxfn lftp gprsvmt kg rzbjx pchkj nlph kvhhnx hsgzgb tttc bvvrkn jvjdqd bfhkjm bdmmnn gvkcgbb plqgqvk zrcqxd qfdh sngvn cvhn tdpgb vfjp qrfpq vhb tp mvskm lrrkhsq xhlgnz bvmld ccrbr jdpl kbml pzsx pgdc zpfs svgrpz zcvzt (contains shellfish)
mcc qrfpq qrdqpnd tdmqcl ncnzr rlxvs ccrbr tttc vnjxjg dhpqh gprsvmt hdxpf nlph cxxdh vbx tsc crbl jdpl skzkfc hkbzj tbjnhb kpvxqt cnfzz kvhhnx qbpts pzsx gkntmb tnhcqg qlqqf vjgvx bcc czfhm bffxt ltzdz cpttmnv mjmfk zcvzt xlgjn vgzx lvtglg dbpr rmmzt gxh plqgqvk pgdc shb cbhfjjq fbtqkzc stq gjgqxt gfcpds mzqjxq (contains shellfish)
krv qlqqf ndjs rnjktbf tcpjd zjpc mzqjxq vbx kbml svxjl bfhkjm vfjp jbbsjh qsfjh zrcqxd zbxfm cvhn frcxz qhlntcc qbxmst tmbtvld dtkdz sngvn vgzx bdlcbg mjmfk fbtqkzc crbl ltzdz fmxltts nlph zqbhtj rqqxrb ccrbr vzjk ncnzr pmrf lvtglg glpm dhhsr tdmqcl qrdqpnd qstnz vnjxjg gxg bshd snksnr ghfd hqgc xldmrv pqqsx xhksx jqkc fgmjgxx jdpl fhbbjj mgvm qrfpq kdct kpvxqt pncz qrhrmj bvmld ddpg qlpsq rxdbdq vjgvx xdpjls ppqsg vzf hdzxfn xlgjn svgrpz lrrkhsq (contains dairy, wheat)
svxjl tdmqcl mgbcxxg cmqj pchkj gprsvmt gbsr zjpc vfjp grn gjgqxt hdzxfn rqqxrb mnbbg tttc lftp lllm vjgvx dbpr xhksx lzqfh tznx fsfxl ccrbr nlph ghfd rbxb srffnhh skzkfc jbbsjh ndjs tdpgb fgmjgxx zrcqxd sgtkj pqkzl vhb gnfl mcc zqrgzc jvjdqd jqkc rsjt bv cbhfjjq jtlpb gvpq gfcpds tp zhpn rnjktbf qlqqf bfhkjm fzbn grpdz mgvm vnjxjg bbsjt fbtqkzc blltznj ppqsg qfdh qlpsq rlxvs ncnzr cpttmnv rxdbdq xdpjls gvkcgbb (contains eggs, dairy, sesame)
kbml qfdh fbtqkzc ccrbr jvjdqd xlgjn ddpg fhbbjj vgzx snksnr skzkfc hsgzgb xmd mgbcxxg grspss zhpn dtkdz fghcjm mcc nzzxdj tlbk czfhm rbxb tbbf tmbtvld gxh jbbsjh xhksx pncz hqgc ncnzr gjpgp rqqxrb pzln jqkc tsc fgdts zjpc dblp nlph jxdk cpk qxksrfh xhlgnz jtlpb tcpjd gcspgn qlpsq qtrk vnjxjg qsfjh gtpzt dhhsr hkbzj dbpr tdmqcl lrrkhsq hbrk hlxr lllm qrhrmj jcvrbsv rcsrk kdct mzqjxq bshd hdv fsfxl (contains eggs, sesame)
tbjnhb dbpr xmd ghfd pgdc bdmmnn xhksx qbxmst tdmqcl dtkdz cnfzz tbbf gxh bsdtlx gnfl rcsrk zhpn qlqqf rqqxrb cpttmnv khtfps nzzxdj hdxpf scxkgk bcc tgqjnp rxdbdq kpvxqt zrjh mzqjxq jvjdqd cmqj tmbtvld zqbhtj cvhn fbtqkzc vnjxjg qjvgh svgrpz mgbcxxg mvskm dhpqh bdlcbg ddpg vhb gcspgn fzbn vzf kkhr hdv zcvzt crznk dgnbsz bffxt qxksrfh zfj qfdh qhlntcc ndjs pchkj plqgqvk jbbsjh slhrk mvtjf blltznj grn lllm vxsjdfl ccrbr hdzxfn bv qrhrmj rnjktbf grpdz svxjl frcxz (contains nuts)
gvpq gjpgp ddpg zjpc gprsvmt bcc kvvzs gfjgh grspss czfhm vnjxjg tgqjnp krv zbxfm cmdfcb hkbzj frcxz lftp gvcrp pchkj tdmqcl fzbn tlbk lllm vbx ccrbr gcspgn hsgzgb mcc tnhcqg gbsr fhbbjj rlxvs qlqqf ppqsg hlxr rxdbdq bdmmnn mgvm slhrk jbbsjh fgdts nlph pqqsx kfqnkld dhhsr gvkcgbb ndjs lvtglg kg gnfl qbxmst hxpc pncz tbjnhb tvxrpmq cxxdh nphhnzj gkntmb qrfpq cbhfjjq zpfs vzjk crznk hdv zcvzt qjvgh cmqj khtfps fmxltts pzsx vxsjdfl cpttmnv jqkc kvhhnx fbtqkzc (contains shellfish)
ccrbr tdmqcl xktgd cbhfjjq plqgqvk gbsr gfcpds scqvnn ddpg vzjk fbtqkzc jbbsjh pncz rzbjx skzkfc jcvrbsv mfdtjx hdxpf hdv ppqsg vnjxjg glpm mzqjxq rqqxrb lllm gkntmb dhhsr hqgc gjpgp bvmld jqkc qbpts mgvm cmdfcb tsc kpvxqt xldmrv xmd xdpjls qsr cjhgj tznx qfdh hkbzj gvcrp zcvzt tvxrpmq rnjktbf pmrf qhlntcc grpdz kdct zfj mvtjf dcdjzd khtfps qxksrfh kbml pzsx cpttmnv vbx (contains shellfish, peanuts, wheat)
scqvnn mzqjxq rbxb tcpjd hdxpf vzjk bcc mnbbg kkhr lftp tp kbml zqrgzc hdv tsgb qjvgh rcsrk xdpjls qsfjh rnjktbf rsjt nlph bdlcbg pchkj kvvzs qxksrfh snksnr cmdfcb fbtqkzc hkbzj ghfd gfjgh lzqfh mgvm tdmqcl zbxfm ccrbr bnjfqpv jqkc tttc kg pqqsx blltznj zrcqxd tsc bvvrkn tmbtvld mvtjf jbbsjh mjmfk dcdjzd gjpgp vnjxjg pncz xktgd (contains dairy)
jvjdqd ccrbr jbbsjh vxsjdfl svgrpz rcsrk xhksx mvtjf rqqxrb gmspg khtfps zbxfm vbx hbrk frcxz nzzxdj cpttmnv zqrgzc tznx zrcqxd lftp bsdtlx tdmqcl qrfpq qlpsq fbtqkzc pmrf jxdk krv crznk vhb xktgd dbpr ghfd tbjnhb kdct bfhkjm bnjfqpv mzqjxq hlxr grpdz hdv kpvxqt snksnr cjhgj rnjktbf xdpjls qxksrfh xldmrv svxjl pchkj tdpgb vnjxjg dgnbsz dhpqh pqkzl gfjgh tmbtvld bdlcbg fgmjgxx (contains eggs, dairy, peanuts)
cpk tp qstnz tdmqcl tnhcqg mnbbg bffxt xktgd kpvxqt grn gxh dcdjzd rcsrk mgbcxxg jtlpb nlph gvcrp bcc mjmfk qtrk ncnzr mcc gprsvmt xmd hbrk mfdtjx tsc qlqqf zqbhtj rnjktbf bvvrkn hdxpf qbpts fsfxl fbtqkzc mzqjxq jvjdqd vnjxjg mvtjf rsjt slhrk lrrkhsq ccrbr hkbzj cmdfcb dgnbsz tcpjd cpttmnv mgvm tcc (contains shellfish)
pmrf lvtglg fmxltts gjgqxt bcc kfqnkld cjhgj fgmjgxx kg gxg fhbbjj tcpjd pchkj cpk hlxr cvhn rsjt cmdfcb tlbk bnjfqpv glpm vhb nlph fghcjm fbtqkzc bffxt hdxpf zjpc blltznj bsdtlx vnjxjg zqbhtj xldmrv tp jbbsjh mgvm ccrbr bv fgdts grn rzbjx dtkdz bvvrkn tdmqcl qtrk hxpc gvpq dhhsr rmmzt hqgc kpvxqt mzqjxq svxjl vgzx jxdk (contains sesame, eggs)
zjpc bsdtlx kvvzs gxg ncnzr cnfzz tcpjd pchkj kdct fghcjm gmspg fgdts rsjt tvxrpmq mcc dcdjzd skzkfc jbbsjh tbjnhb gcspgn hkbzj bdmmnn svxjl fsfxl gvpq xhksx ppqsg gfcpds vnjxjg jvjdqd bshd zrcqxd xlgjn tdmqcl bcc crznk mnbbg mzqjxq bvmld bv gprsvmt nzzxdj gxh qstnz qrhrmj bbsjt qjvgh jxdk grn bnjfqpv qbxmst qfdh rnjktbf hpkznb ndjs cpttmnv pqqsx nlph tznx xktgd crbl tnhcqg jdpl pzsx pzln rlxvs svgrpz fbtqkzc fmxltts mgvm jtlpb hdxpf hdv tdpgb zcvzt rmmzt scqvnn krv (contains soy, nuts, sesame)
jxdk zqrgzc qlqqf fgdts bv mvtjf ghfd pzsx stq kvvzs cxxdh kdct pzln zrcqxd qlpsq zrjh sgtkj pgdc dgnbsz dblp lvtglg kkhr nlph jtlpb gkntmb fghcjm dcdjzd gvcrp mgvm rlxvs jvjdqd mnbbg vnjxjg rbxb bvmld jcvrbsv qrhrmj fmxltts krv bfhkjm ncnzr gxg bbsjt jbbsjh gfjgh cpttmnv mfdtjx vgzx fbtqkzc ccrbr vfrhm mzqjxq glpm zfj (contains eggs, soy)
slhrk cmqj gprsvmt gxg pgdc pqqsx snksnr xktgd hkbzj zqbhtj blltznj gxh mvtjf tdpgb ppqsg grspss bsdtlx fgmjgxx cpk nlph fgdts crbl svgrpz tznx mzqjxq cpttmnv hdv qstnz jxdk mgbcxxg pzsx gtpzt zrjh bvvrkn scqvnn dhpqh qlpsq vnjxjg qhlntcc kkhr ccrbr jbbsjh bshd mvskm rbxb mcc fbtqkzc (contains nuts, shellfish, dairy)
rnjktbf zqbhtj lzqfh cjhgj nlph crbl tcc bvmld hlxr bfhkjm tsgb shb dhhsr gvpq pncz mzqjxq srffnhh stq jqkc zcvzt zqrgzc jbbsjh gbsr mvtjf rqqxrb vnjxjg scxkgk rsjt kvhhnx ddpg tnhcqg tbbf mgbcxxg gxg tbjnhb czfhm qrdqpnd vbx hxpc rbxb gjgqxt qrfpq fbtqkzc plqgqvk tdmqcl jvjdqd pmrf skzkfc zrcqxd cxxdh cpttmnv zrjh snksnr (contains eggs, shellfish, sesame)
pzln grpdz dbpr mzqjxq fbtqkzc bcc kdct zjpc krv rnjktbf zbxfm blltznj qtrk pqkzl pncz jdpl rmmzt tmbtvld frcxz sngvn ndjs shb fzbn kg gfcpds bvvrkn zhpn jqkc gvpq cmdfcb qlqqf tbjnhb ccrbr nzzxdj gnfl cpk nlph fsfxl dblp jvjdqd tvxrpmq hdv lzqfh xktgd tdmqcl cpttmnv kkhr jbbsjh zrjh (contains peanuts)
tp qbxmst mzqjxq qrfpq hdv fzbn bv gvkcgbb dgnbsz rzbjx zjpc svgrpz qhlntcc cjhgj rlxvs fmxltts fbtqkzc nlph tvxrpmq hdzxfn hdxpf ccrbr lrrkhsq zrcqxd grn pqqsx glpm gjgqxt sngvn ppqsg rnjktbf vnjxjg gfcpds hpkznb xldmrv vfrhm cpttmnv tlbk kg mfdtjx hxpc tsc rxdbdq jbbsjh cnfzz zqrgzc qfdh zcvzt tcpjd khtfps vgzx qbpts lzqfh ncnzr tcc qrdqpnd fgmjgxx nphhnzj ltzdz (contains wheat, peanuts)
bv zrcqxd mgvm cpttmnv kvhhnx fmxltts qlpsq gxh ccrbr bffxt tnhcqg gvkcgbb fzbn vfjp nlph zqbhtj jbbsjh xldmrv bfhkjm mnbbg hlxr tcc crbl dhhsr cmqj kkhr tbbf lvtglg tdmqcl qfdh qlqqf xhlgnz crznk bdmmnn rqqxrb qstnz rnjktbf vgzx gkntmb tbjnhb bsdtlx mvtjf kg vnjxjg dtkdz pqkzl khtfps hpkznb bcc fsfxl hbrk pgdc tznx bshd hkbzj pmrf sngvn tsgb hdzxfn slhrk zbxfm lzqfh grn vfrhm tp fhbbjj ghfd tsc zcvzt zfj hsgzgb lrrkhsq qsr qsfjh fbtqkzc stq kdct gvpq hqgc lllm gjgqxt xmd skzkfc hdxpf vzjk rzbjx nzzxdj cpk (contains shellfish)
bshd crznk qsr zqbhtj rnjktbf cjhgj scqvnn qrdqpnd vnjxjg skzkfc jbbsjh sngvn zrjh cpttmnv gvcrp scxkgk pqkzl sgtkj cvhn grspss tbjnhb fhbbjj ncnzr tznx mcc bvmld tdmqcl vbx czfhm jtlpb hsgzgb hpkznb gmspg ccrbr fbtqkzc bvvrkn xlgjn cpk hbrk bfhkjm nlph zrcqxd mgvm mgbcxxg qlpsq fgdts vzjk rqqxrb kpvxqt rlxvs rmmzt tgqjnp xdpjls srffnhh bffxt dtkdz dhpqh cxxdh tmbtvld grpdz tcc pqqsx bdmmnn (contains nuts)
pgdc lllm fbtqkzc fsfxl hkbzj tlbk grn qjvgh xdpjls qstnz jbbsjh gbsr cvhn nlph dtkdz bshd ppqsg vnjxjg rnjktbf kdct lzqfh cbhfjjq zfj qxksrfh srffnhh dblp svgrpz ddpg cpttmnv qsr fgdts plqgqvk pmrf hdzxfn sgtkj cxxdh qhlntcc mjmfk hlxr tdpgb ccrbr khtfps rbxb tdmqcl vhb bvvrkn qfdh tgqjnp zbxfm vjgvx hbrk jqkc (contains sesame)
tcpjd vnjxjg ltzdz bfhkjm qjvgh zrcqxd qbxmst ccrbr hdxpf kfqnkld gnfl xlgjn qlpsq ncnzr bdmmnn ddpg gkntmb fmxltts rsjt rmmzt kvhhnx kbml gxg ppqsg gvkcgbb qrdqpnd ghfd tlbk zqrgzc gtpzt bshd zhpn qtrk shb lvtglg rcsrk gjpgp gvpq tdmqcl fgmjgxx tsgb mzqjxq vgzx vzjk slhrk tnhcqg jxdk qstnz jbbsjh gxh czfhm tttc nzzxdj bvmld gvcrp lrrkhsq gmspg cmdfcb vhb qfdh rxdbdq bdlcbg hpkznb fsfxl gcspgn gjgqxt kpvxqt hbrk snksnr cpttmnv dhpqh nlph tdpgb zjpc kdct rlxvs pchkj qrhrmj cpk svgrpz (contains shellfish, sesame)"""


test1 = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
test2 = """"""
test3 = """"""
test4 = """"""





def solve(data):
    lines = [i for i in data.splitlines()]

    ALL_I = set()
    ALL_A = set()
    see = defaultdict(int)
    foods = []
    for line in lines:
        f, s = line.split("(")
        s = s[:-1]
        s = "".join(s.split()[1:]).split(",")

        #print(s)
        f = f.split()
        ALL_A |= set(s)
        ALL_I |= set(f)
        foods.append((f,s))
    can = {i:set(ALL_A) for i in ALL_I}

    for I, A in foods:
        for j in I:
            see[j] += 1

        for al in A:
            for ing in ALL_I:
                if ing not in I:
                    can[ing].discard(al)
    ans = 0
    for thing in ALL_I:
        if not can[thing]:
            ans += see[thing]
    print(ans)



    MAPPING = {}
    USED = set()
    while len(MAPPING) < len(ALL_A):
        for i in ALL_I:
            pos = [i for i in can[i] if i not in USED]
            if len(pos)==1:
                MAPPING[i] = pos[0]
                USED.add(pos[0])
    print(",".join(sorted(MAPPING, key=lambda x: MAPPING[x])))




solve(test1)
#solve(test2)
#solve(test3)
#solve(test4)

solve(data)






