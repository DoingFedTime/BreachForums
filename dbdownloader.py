import os
import sys
import requests
from tqdm import tqdm

# List of databases categorized
categories = {
    "Social Media": [
        "8fit_BF.7z", "8tracks_BF.7z", "Facebook_BF.7z", "LinkedIn_BF.7z", "MySpace_BF.7z",
        "VK_BF.7z", "Wishbone_BF.7z", "Zoosk2020_BF.7z", "Zoosk_BF.7z", "Gravatar_BF.7z",
        "Poshmark_BF.7z", "Raychat_BF.7z", "RocketText_BF.7z"
    ],
    "E-commerce": [
        "123RF_BF.7z", "247Hire_BF.7z", "500px_BF.7z", "Canva_BF.7z", "ChqBook_BF.7z",
        "Click_BF.7z", "Epik_BF.7z", "PayHere_BF.7z", "ShopBack_BF.7z", "Tokopedia_BF.7z",
        "Upstox_BF.7z", "Whitepages_BF.7z"
    ],
    "Forums": [
        "8chan_BF.7z", "AbuseWithUs_BF.7z", "AimJunkies_BF.7z", "AlbionOnline_BF.7z",
        "AndroidForums_BF.7z", "BestHack_BF.7z", "BleachAnime_BF.7z", "BellTreeForums_BF.7z",
        "AniLibria_BF.7z", "ArmyForceOnline_BF.7z", "Aspkin_BF.7z", "Autocentrum_BF.7z",
        "Bibione_BF.7z", "Deezer_BF.7z", "ExploitIn_BF.7z", "Aternos_BF.7z"
    ],
    "Gaming": [
        "126_BF.7z", "17Media_BF.7z", "AgeOfWushu_BF.7z", "AlbionOnline_BF.7z",
        "ArmA3Life_BF.7z", "BattleRoyaleForums_BF.7z", "BattlefieldHeroes_BF.7z",
        "MindJolt_BF.7z", "AhoyGame_BF.7z", "AmplitudeStudios_BF.7z", "AnimeGame_BF.7z",
        "AnimePlanet_BF.7z", "Animeify_BF.7z", "ArtNow_BF.7z", "ArtificialAiming_BF.7z"
    ],
    "Miscellaneous": [
        "000webhost_BF.7z", "AGEnergy_BF.7z", "AIType_BF.7z", "APKTW_BF.7z",
        "Dropbox_BF.7z", "Patreon_BF.7z", "Wishbone_BF.7z", "YandexFood_BF.7z",
        "atmeltomo_BF.7z", "17173_BF.7z", "2844Breaches_BF.7z", "2fast4u_BF.7z",
        "4KMILES_BF.7z", "7k7k_BF.7z", "9lives_BF.7z", "ABFRL_BF.7z", "Abandonia_BF.7z",
        "AbbyWinters_BF.7z", "Acne_BF.7z", "ActMobile_BF.7z", "ActionNetwork_BF.7z",
        "Acuity_BF.7z", "Adapt_BF.7z", "Adecco_BF.7z", "Adobe_BF.7z", "AdoptMeTradingValues_BF.7z",
        "AdultFriendFinder2015_BF.7z", "AdultFriendFinder2016_BF.7z", "AerServ_BF.7z",
        "AgusiQTorrents_BF.7z", "AhaShare_BF.7z", "Aipai_BF.7z", "Ajarn_BF.7z",
        "AlexHost_BF.7z", "AllWomensTalk_BF.7z", "Alora_BF.7z", "AlpineReplay_BF.7z",
        "Altenen_BF.7z", "AmartFurniture_BF.7z", "Amigas_BF.7z", "AnabelLee_BF.7z",
        "Ancestry_BF.7z", "AndroidLista_BF.7z", "AnimalJam_BF.7z", "AnimeForum_BF.7z",
        "Animoto_BF.7z", "AntiPublic_BF.7z", "ApexSMS_BF.7z", "Apollo_BF.7z", "Apolyton_BF.7z",
        "Appen_BF.7z", "AtlasQuantum_BF.7z", "AtletasNow_BF.7z", "Avast_BF.7z", "BVD_BF.7z",
        "BabyNames_BF.7z", "Badoo_BF.7z", "Bell2014_BF.7z", "Bestialitysextaboo_BF.7z",
        "BigMoneyJobs_BF.7z", "BioBigBox_BF.7z", "BitTorrent_BF.7z", "Bitmain_BF.7z",
        "Bonobos_BF.7z", "BrandNewTube2022_BF.7z", "CDEK_BF.7z", "COMELEC_BF.7z",
        "Cloud_SQL_Export_2024-04-03 (16;49;50).sql.gz", "Collection1_BF.7z", "DriveSure_BF.7z",
        "Dubsmash_BF.7z", "Dunzo_BF.7z", "Edmodo_BF.7z", "Evite_BF.7z", "ExactisPartial_BF.7z",
        "GateHub_BF.7z", "Houzz_BF.7z", "IHECIraqiVoters_BF.7z", "IIMJobs_BF.7z", "IndiHome_BF.7z",
        "IntelXPasteScrape_BF.7z", "JD_BF.7z", "JukinMedia_BF.7z", "LastFM_BF.7z", "LiveRamp_BF.7z",
        "Luxottica_BF.7z", "MGMGrandHotels_BF.7z", "MMGFusion_BF.7z", "ModernBusinessSolutions_BF.7z",
        "MyFitnessPal_BF.7z", "NetEase_BF.7z", "NitroPDF_BF.7z", "OnlinerSpambot_BF.7z",
        "Pemiblanc_BF.7z", "PeopleDataLabs_BF.7z", "Pipl_BF.7z", "QQ_BF.7z", "START_BF.7z",
        "SevenRooms_BF.7z", "Staminus_BF.7z", "TAPAir_BF.7z", "Thingiverse_BF.7z", "Ticketcounter_BF.7z",
        "TruecallerIndia_BF.7z", "USVoterData_BF.7z", "UniversityofCalifornia_BF.7z", "VNG_BF.7z",
        "VerificationsIO_BF.7z", "Wattpad_BF.7z", "WedMeGood_BF.7z", "Youku_BF.7z",
        "iMesh_BF.7z", "ixigo_BF.7z", "myfitnesspal.com_2018.02.7z", "piZap_BF.7z", "zeeroq.7z",
        "zeeroq_BF.7z"
    ]
}

# Base URL
base_url = "https://bncdn.to/breachnationcdn/"

def download_file(url, dest_folder, total_files, file_index):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    local_filename = os.path.join(dest_folder, url.split('/')[-1])
    resume_header = {}
    file_mode = 'wb'

    if os.path.exists(local_filename):
        file_size = os.path.getsize(local_filename)
        resume_header = {'Range': f'bytes={file_size}-'}
        file_mode = 'ab'
    else:
        file_size = 0

    try:
        with requests.get(url, headers=resume_header, stream=True, timeout=10) as r:
            r.raise_for_status()  # Raise HTTPError for bad responses
            total_size = int(r.headers.get('content-length', 0)) + file_size
            block_size = 1024  # 1 Kibibyte
            file_progress = tqdm(total=total_size, initial=file_size, unit='iB', unit_scale=True, 
                                 desc=f"File {file_index}/{total_files}", ncols=100)
            with open(local_filename, file_mode) as f:
                for data in r.iter_content(block_size):
                    file_progress.update(len(data))
                    f.write(data)
            file_progress.close()
        return local_filename
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None

def print_ascii_art():
    art = """
                                                                                                                                                                                                                                                                        
__/\\\\\\\\\\\\\___________________________________________________________________/\\\___________/\\\\\\\\\\\\\\\___________________________________________________________________                                          
 _\/\\\/////////\\\________________________________________________________________\/\\\__________\/\\\///////////____________________________________________________________________                                         
  _\/\\\_______\/\\\________________________________________________________________\/\\\__________\/\\\_______________________________________________________________________________                                        
   _\/\\\\\\\\\\\\\\____/\\/\\\\\\\_______/\\\\\\\\____/\\\\\\\\\_________/\\\\\\\\__\/\\\__________\/\\\\\\\\\\\__________/\\\\\______/\\/\\\\\\\____/\\\____/\\\_____/\\\\\__/\\\\\___                                       
    _\/\\\/////////\\\__\/\\\/////\\\____/\\\/////\\\__\////////\\\______/\\\//////___\/\\\\\\\\\\___\/\\\///////_________/\\\///\\\___\/\\\/////\\\__\/\\\___\/\\\___/\\\///\\\\\///\\\_                                      
     _\/\\\_______\/\\\__\/\\\___\///____/\\\\\\\\\\\_____/\\\\\\\\\\____/\\\__________\/\\\/////\\\__\/\\\_______________/\\\__\//\\\__\/\\\___\///___\/\\\___\/\\\__\/\\\_\//\\\__\/\\\_                                     
      _\/\\\_______\/\\\__\/\\\__________\//\\///////_____/\\\/////\\\___\//\\\_________\/\\\___\/\\\__\/\\\______________\//\\\__/\\\___\/\\\__________\/\\\___\/\\\__\/\\\__\/\\\__\/\\\_                                    
       _\/\\\\\\\\\\\\\/___\/\\\___________\//\\\\\\\\\\__\//\\\\\\\\/\\___\///\\\\\\\\__\/\\\___\/\\\__\/\\\_______________\///\\\\\/____\/\\\__________\//\\\\\\\\\___\/\\\__\/\\\__\/\\\_                                   
        _\/////////////_____\///_____________\//////////____\////////\//______\////////___\///____\///___\///__________________\/////______\///____________\/////////____\///___\///___\///__                                  
__/\\\\\\\\\\\\______/\\\\\\\\\\\\\________________________/\\\\\\\\\\\\_______________________________________________________/\\\\\\____________________________________________/\\\_________________________________        
 _\/\\\////////\\\___\/\\\/////////\\\_____________________\/\\\////////\\\____________________________________________________\////\\\___________________________________________\/\\\_________________________________       
  _\/\\\______\//\\\__\/\\\_______\/\\\_____________________\/\\\______\//\\\______________________________________________________\/\\\___________________________________________\/\\\_________________________________      
   _\/\\\_______\/\\\__\/\\\\\\\\\\\\\\______________________\/\\\_______\/\\\______/\\\\\______/\\____/\\___/\\___/\\/\\\\\\_______\/\\\_________/\\\\\______/\\\\\\\\\____________\/\\\_______/\\\\\\\\____/\\/\\\\\\\__     
    _\/\\\_______\/\\\__\/\\\/////////\\\_____________________\/\\\_______\/\\\____/\\\///\\\___\/\\\__/\\\\_/\\\__\/\\\////\\\______\/\\\_______/\\\///\\\___\////////\\\______/\\\\\\\\\_____/\\\/////\\\__\/\\\/////\\\_    
     _\/\\\_______\/\\\__\/\\\_______\/\\\_____________________\/\\\_______\/\\\___/\\\__\//\\\__\//\\\/\\\\\/\\\___\/\\\__\//\\\_____\/\\\______/\\\__\//\\\____/\\\\\\\\\\____/\\\////\\\____/\\\\\\\\\\\___\/\\\___\///__   
      _\/\\\_______/\\\___\/\\\_______\/\\\_____________________\/\\\_______/\\\___\//\\\__/\\\____\//\\\\\/\\\\\____\/\\\___\/\\\_____\/\\\_____\//\\\__/\\\____/\\\/////\\\___\/\\\__\/\\\___\//\\///////____\/\\\_________  
       _\/\\\\\\\\\\\\/____\/\\\\\\\\\\\\\/____/\\\\\\\\\\\\\\\__\/\\\\\\\\\\\\/_____\///\\\\\/______\//\\\\//\\\_____\/\\\___\/\\\___/\\\\\\\\\___\///\\\\\/____\//\\\\\\\\/\\__\//\\\\\\\/\\___\//\\\\\\\\\\__\/\\\_________ 
        _\////////////______\/////////////_____\///////////////___\////////////_________\/////_________\///__\///______\///____\///___\/////////______\/////_______\////////\//____\///////\//_____\//////////___\///__________                                                                                                                                                                                            
    """
    print(art)

def menu():
    print_ascii_art()
    print("1. Download All")
    print("2. Download by Category")
    print("3. Download Specific Database")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def download_by_category():
    print("Choose a category to download:")
    for idx, category in enumerate(categories.keys(), start=1):
        print(f"{idx}. {category}")

    category_choice = input("Enter your choice: ")

    try:
        category_idx = int(category_choice) - 1
        chosen_category = list(categories.keys())[category_idx]
        total_files = len(categories[chosen_category])
        print(f"Downloading all databases in the {chosen_category} category...")
        for file_index, db in enumerate(categories[chosen_category], start=1):
            url = base_url + db
            print(f"Downloading {db}...")
            download_file(url, f'downloads/{chosen_category}', total_files, file_index)
        print(f"All downloads in the {chosen_category} category completed.")
    except (IndexError, ValueError):
        print("Invalid category choice. Please try again.")

def download_specific():
    db_name = input("Enter the exact name of the database file to download: ")
    if any(db_name in sublist for sublist in categories.values()):
        print(f"Downloading {db_name}...")
        download_file(base_url + db_name, 'downloads/specific', 1, 1)
        print(f"{db_name} download completed.")
    else:
        print(f"{db_name} not found in the list of databases. Please try again.")

def main():
    try:
        while True:
            choice = menu()
            if choice == '1':
                total_files = sum(len(cat) for cat in categories.values())
                file_index = 1
                print("Downloading all databases...")
                for category in categories.values():
                    for db in category:
                        url = base_url + db
                        print(f"Downloading {db}...")
                        download_file(url, 'downloads', total_files, file_index)
                        file_index += 1
                print("All downloads completed.")
            elif choice == '2':
                download_by_category()
            elif choice == '3':
                download_specific()
            elif choice == '4':
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nDownload interrupted. Exiting...")

if __name__ == "__main__":
    main()
