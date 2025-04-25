import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_furia_matches():
    """Busca os próximos jogos da FURIA no HLTV."""
    url = "https://www.hltv.org/matches"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        matches = []
        match_blocks = soup.find_all("div", class_="upcomingMatch")
        
        for match in match_blocks:
            team1 = match.find("div", class_="team1").get_text(strip=True)
            team2 = match.find("div", class_="team2").get_text(strip=True)
            
            if "FURIA" in team1 or "FURIA" in team2:
                event = match.find("div", class_="event").get_text(strip=True)
                time = match.find("div", class_="time").get_text(strip=True)
                match_url = f"https://hltv.org{match['href']}"
                
                matches.append({
                    "team1": team1,
                    "team2": team2,
                    "event": event,
                    "time": time,
                    "url": match_url
                })
        
        return matches[:5]  # Retorna no máximo 5 jogos
        
    except Exception as e:
        print(f"Erro ao acessar HLTV: {e}")
        return None