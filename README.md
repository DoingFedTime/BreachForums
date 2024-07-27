# CDN Down
# USDoD has apparently taken down or disabled his CDN, so the tool no longer works, and as a result, this tool is now archived. 

# 📥 BreachForum DB_Downloader

## Introduction

Welcome to **BreachForum DB_Downloader**, a comprehensive tool designed to simplify the process of downloading databases from the BreachForums CDN. 
This tool was created by **Sam Bent**, aka **DoingFedTime**, to help users easily access the data breaches hosted by USDoD, a major threat actor who hacked BreachForums. 
USDoD has made all the data breaches that were for sale on [BreachForums](https://breachforums.st) and a [onion site](http://breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion) (a site that typically sells breach data) available on his CDN for free, and this tool automates the download process for you.

I made a YouTube video detailing the [X post where USDoD](https://x.com/EquationCorp/status/1814674545787244703) uploaded an XML file, containing all the database links, on his own CDN. Instead of manually searching through the file, this tool handles the download for you, and includes some other features as well.

**Important Note:** It is highly recommended to download these databases using an overlay network like a VPN or other anonymizing medium, as the CDN is owned by a major threat actor.

### ⚠️ Disclaimer
- The availability of the files is up to USDoD, I have no control over that.
- You're downloading the DBs from a TA; act accordingly.
- The breach, sharing of files, etc., I had no part in big or small.
- You agree to do so at your own risk using this tool. I am not responsible for any legal consequences that may arise from its use. You also agree by downloading this to not hold me liable for anything - at all, ever. 
- In all likelihood, I will not be updating this tool because I will be busy editing videos.

### YouTube Video

Here is a video demonstration of the tool's usage on my YouTube channel:

[![BreachForum DB_Downloader Usage](https://i.ibb.co/Yk87Zqn/image.png)](https://www.youtube.com/watch?v=orhbPAIGt9A)



## 📋 Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Unzipping Databases](#unzipping-databases)
6. [Credits](#credits)
7. [Contact](#contact)
8. [Disclaimer](#disclaimer)
9. [Troubleshooting](#troubleshooting)
10. [List of Databases](#list-of-databases)

## ✨ Features

1. **Download All Databases**: Download all available databases at once.
2. **Download by Category**: Choose and download databases by specific categories.
3. **Download Specific Database**: Download a particular database by its name, referring to the `Database.txt` file included with the download. It has all the names of all the breaches. 
4. **Progress Bar**: View real-time progress, including download speed and completion percentage.
5. **Resumption Feature**: Resume interrupted downloads from where they left off.

## 📦 Installation

To use BreachForum DB_Downloader, follow these steps to set up the tool:

1. **Update & Install Git, Python, and Pip** (if not already installed):
    ```sh
    sudo apt update && sudo apt upgrade -y
    sudo apt install git python3 python3-pip p7zip-full -y
    ```
2. **Install Required Python Libraries**:
    ```sh
    pip3 install requests tqdm
    ```

3. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/BreachForum_DB_Downloader.git
    cd BreachForum_DB_Downloader
    ```

## 🛠️ Usage

1. **Open Terminal**:
    ```sh
    Ctrl + Alt + T
    ```

2. **Navigate to the Script Directory**:
    ```sh
    cd /path/to/BreachForum_DB_Downloader
    ```

3. **Run the Script**:
    ```sh
    python3 download_script.py
    ```

The script provides a menu with the following options:

- **Download All**: Downloads all available databases.
- **Download by Category**: Downloads databases by selecting a specific category.
- **Download Specific Database**: Downloads a specific database by its name, referring to the `Database.txt` file for available database names.
- **Exit**: Exits the script.

## 📂 Unzipping Databases

After downloading, you can unzip the `.7z` files using the `7z` command:

1. **Unzip a Specific File**:
    ```sh
    7z x filename.7z
    ```

2. **Unzip All `.7z` Files in a Directory**:
    ```sh
    for file in *.7z; do 7z x "$file"; done
    ```

## 🌟 Credits

This tool was developed by **Sam Bent** (aka **DoingFedTime**).

### Follow Sam Bent (DoingFedTime)

- **YouTube**: [DoingFedTime](https://youtube.com/@doingfedtime)
- **Podcast**: [Darknet Podcast](https://rss.com/podcasts/darknet)
- **Twitter**: [@DoingFedTime](https://twitter.com/DoingFedTime)
- **Amazon Author**: [DoingFedTime on Amazon](https://bit.ly/DoingFedTimeAmazon)
- **My Site**: [DoingFedTime](https://doingfedtime.com)
- **Facebook**: [Doing FedTime on Facebook](https://facebook.com/doing.fedtime)
- **LinkedIn**: [Sam Bent on LinkedIn](https://linkedin.com/in/sam-bent)
- **Gmail**: [ksllc27@gmail.com](mailto:ksllc27@gmail.com)
- **TikTok**: [DoingFedTime on TikTok](https://tiktok.com/@doingfedtime)
- **Rumble**: [DoingFedTime on Rumble](https://rumble.com/c/c-2456184)
- **Dread - Darknet**: [Dread](http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/d/doingfedtime)
- **Pitch - Darknet**: [Pitch](http://pitchprash4aqilfr7sbmuwve3pnkpylqwxjbj2q5o4szcfeea6d27yd.onion/@doingfedtime)
- **BreachForums - Darknet**: [BreachForums Onion](breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion/User-DoingFedTime)
- **KeyBase**: [Keybase](https://keybase.io/doingfedtime)


### Follow USDoD

- **Twitter**: [@EquationCorp](https://twitter.com/EquationCorp) (USDoD)
- **Secret Forum Profile**: [USDoD on Secret Forums](https://secretforums.net/members/usdod.4467/)
- **Leakbase**: [USDoD on Leakbase](https://leakbase.io/usdod/)
- **Dread**: [USDoD on Dread](http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/u/USDoD/)
- **BreachForums**: [USDoD on BreachForums](https://breachforums.st/User-USDoD)
- **Personal Telegram**: [@impacket](https://t.me/impacket)
- **Telegram Group**: [SparrowCorp](https://t.me/SparrowCorp)
- **CDN**: [USDoD's CDN](https://usdod.io)

## 📞 Contact

For further inquiries or support, you can reach out to me through my YouTube channel or other profiles listed above.

## ⚠️ Disclaimer

By using this tool, you agree that you are using it at your own risk. I am not responsible for any legal consequences that may arise from the use of this tool. The availability of the files is up to USDoD. The breach, sharing of files, etc., I had no part in.

Enjoy using the BreachForum DB_Downloader!

## 🔧 Troubleshooting

### 🍏 Mac

Use Linux. 🐧

### 🪟 Windows

Use Linux. 🐧

## 📜 List of Databases

Here is the list of databases/breach data available for download:

1. 000webhost_BF.7z
2. 123RF_BF.7z
3. 126_BF.7z
4. 17173_BF.7z
5. 17Media_BF.7z
6. 247Hire_BF.7z
7. 2844Breaches_BF.7z
8. 2fast4u_BF.7z
9. 4KMILES_BF.7z
10. 500px_BF.7z
11. 7k7k_BF.7z
12. 8chan_BF.7z
13. 8fit_BF.7z
14. 8tracks_BF.7z
15. 9lives_BF.7z
16. ABFRL_BF.7z
17. AGEnergy_BF.7z
18. AIType_BF.7z
19. APKTW_BF.7z
20. Abandonia_BF.7z
21. AbbyWinters_BF.7z
22. AbuseWithUs_BF.7z
23. Acne_BF.7z
24. ActMobile_BF.7z
25. ActionNetwork_BF.7z
26. Acuity_BF.7z
27. Adapt_BF.7z
28. Adecco_BF.7z
29. Adobe_BF.7z
30. AdoptMeTradingValues_BF.7z
31. AdultFriendFinder2015_BF.7z
32. AdultFriendFinder2016_BF.7z
33. AerServ_BF.7z
34. AgeOfWushu_BF.7z
35. AgusiQTorrents_BF.7z
36. AhaShare_BF.7z
37. AhoyGame_BF.7z
38. AimJunkies_BF.7z
39. Aimware_BF.7z
40. Aipai_BF.7z
41. Ajarn_BF.7z
42. AlbionOnline_BF.7z
43. AlexHost_BF.7z
44. AllWomensTalk_BF.7z
45. Alora_BF.7z
46. AlpineReplay_BF.7z
47. Altenen_BF.7z
48. AmartFurniture_BF.7z
49. Amigas_BF.7z
50. AmplitudeStudios_BF.7z
51. AnabelLee_BF.7z
52. Ancestry_BF.7z
53. AndroidForums_BF.7z
54. AndroidLista_BF.7z
55. AniLibria_BF.7z
56. AnimalJam_BF.7z
57. AnimeForum_BF.7z
58. AnimeGame_BF.7z
59. AnimePlanet_BF.7z
60. Animeify_BF.7z
61. Animoto_BF.7z
62. AntiPublic_BF.7z
63. ApexSMS_BF.7z
64. Apollo_BF.7z
65. Apolyton_BF.7z
66. Appen_BF.7z
67. ArmA3Life_BF.7z
68. ArmyForceOnline_BF.7z
69. ArtNow_BF.7z
70. ArtificialAiming_BF.7z
71. Artsy_BF.7z
72. Aspkin_BF.7z
73. AstroPID_BF.7z
74. Aternos_BF.7z
75. AtlasQuantum_BF.7z
76. AtletasNow_BF.7z
77. AuphanOnline_BF.7z
78. Autocentrum_BF.7z
79. Avast_BF.7z
80. BVD_BF.7z
81. BabyNames_BF.7z
82. Badoo_BF.7z
83. BattleRoyaleForums_BF.7z
84. BattlefieldHeroes_BF.7z
85. Battlefy_BF.7z
86. Bell2014_BF.7z
87. BellTreeForums_BF.7z
88. BestHack_BF.7z
89. Bestialitysextaboo_BF.7z
90. Bibione_BF.7z
91. BigMoneyJobs_BF.7z
92. BioBigBox_BF.7z
93. BitTorrent_BF.7z
94. Bitmain_BF.7z
95. BleachAnime_BF.7z
96. Bonobos_BF.7z
97. BrandNewTube2022_BF.7z
98. CDEK_BF.7z
99. COMELEC_BF.7z
100. Canva_BF.7z
101. ChqBook_BF.7z
102. Cit0day_BF.7z
103. Click_BF.7z
104. Cloud_SQL_Export_2024-04-03 (16;49;50).sql.gz
105. Collection1_BF.7z
106. Deezer_BF.7z
107. DriveSure_BF.7z
108. Dropbox_BF.7z
109. Dubsmash_BF.7z
110. Dunzo_BF.7z
111. Edmodo_BF.7z
112. Epik_BF.7z
113. Evite_BF.7z
114. ExactisPartial_BF.7z
115. ExploitIn_BF.7z
116. Facebook_BF.7z
117. Fling_BF.7z
118. GateHub_BF.7z
119. GeckoVPN_BF.7z
120. Gravatar_BF.7z
121. Houzz_BF.7z
122. IHECIraqiVoters_BF.7z
123. IIMJobs_BF.7z
124. IndiHome_BF.7z
125. IntelXPasteScrape_BF.7z
126. JD_BF.7z
127. JukinMedia_BF.7z
128. LastFM_BF.7z
129. LinkedIn_BF.7z
130. LiveRamp_BF.7z
131. Luxottica_BF.7z
132. MGMGrandHotels_BF.7z
133. MMGFusion_BF.7z
134. MindJolt_BF.7z
135. ModernBusinessSolutions_BF.7z
136. MyFitnessPal_BF.7z
137. MySpace_BF.7z
138. NetEase_BF.7z
139. NitroPDF_BF.7z
140. OnlinerSpambot_BF.7z
141. Patreon_BF.7z
142. PayHere_BF.7z
143. Pemiblanc_BF.7z
144. PeopleDataLabs_BF.7z
145. Pipl_BF.7z
146. Poshmark_BF.7z
147. QQ_BF.7z
148. Raychat_BF.7z
149. RocketText_BF.7z
150. START_BF.7z
151. SevenRooms_BF.7z
152. ShopBack_BF.7z
153. Staminus_BF.7z
154. TAPAir_BF.7z
155. Thingiverse_BF.7z
156. Ticketcounter_BF.7z
157. Tokopedia_BF.7z
158. TruecallerIndia_BF.7z
159. USVoterData_BF.7z
160. UniversityofCalifornia_BF.7z
161. Upstox_BF.7z
162. VK_BF.7z
163. VNG_BF.7z
164. VerificationsIO_BF.7z
165. Wattpad_BF.7z
166. WedMeGood_BF.7z
167. Whitepages_BF.7z
168. Wishbone_BF.7z
169. YandexFood_BF.7z
170. Youku_BF.7z
171. Zoosk2020_BF.7z
172. Zoosk_BF.7z
173. Zynga_BF.7z
174. atmeltomo_BF.7z
175. hjedd_BF.7z
176. iMesh_BF.7z
177. ixigo_BF.7z
178. myfitnesspal.com_2018.02.7z
179. piZap_BF.7z
180. zeeroq.7z
181. zeeroq_BF.7z




