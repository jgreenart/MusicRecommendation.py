import requests

class MusicRecommendation:
    def __init__(self, api_key):
        self.api_key = api_key

    def recommend_music(self, genre):
        url = f"https://api.spotify.com/v1/recommendations?limit=5&seed_genres={genre}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            if "tracks" in data:
                print(f"Music recommendations for {genre}:")
                for track in data["tracks"]:
                    track_name = track["name"]
                    artist_name = track["artists"][0]["name"]
                    print(f"- {track_name} by {artist_name}")
            else:
                print(f"No music recommendations found for {genre}.")
        else:
            print("Unable to retrieve music recommendations.")

def main():
    api_key = "YOUR_API_KEY"
    genre = "pop"

    recommendation = MusicRecommendation(api_key)
    recommendation.recommend_music(genre)

if __name__ == "__main__":
    main()
