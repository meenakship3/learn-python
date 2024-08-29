## 🎵 musical-time-machine
Transport yourself back in time with this Spotify playlist. This project scrapes the Billboard top 100 songs for a particular date and uses the Spotify API along with Spotipy to add those songs to a playlist for you.

## 🧰 libraries and APIs used
- BeautifulSoup
- Spotipy
- Spotify API

## ⚙️ installation 
1. Clone this repository
```bash
git clone https://github.com/YOUR-USERNAME/musical-time-machine.git
```
2. Navigate to the project directory
```bash
cd musical-time-machine
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run main.py
5. Enter the date you would like to travel to
6. Grant Billboard access to your Spotify (this tab will be automatically opened)
7. Into your console, copy-paste the URL (http://example.com/?code=...) of the tab that opens

## ‼️ disclaimer
- Songs added may not always be accurate owing to different songs being available in different regions.
- Within the create_playlist function, the market is set to "IN", feel free to change it to the country code of your country.
- The playlist created is by default a public playlist.

## 🖼️ screenshot
<img width="997" alt="Screenshot 2024-08-29 at 1 22 11 PM" src="https://github.com/user-attachments/assets/1a054918-d940-41db-96af-ae0cf99f50ab">
