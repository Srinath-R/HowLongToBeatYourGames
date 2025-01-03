from howlongtobeatpy import HowLongToBeat
import info_scraping
from games import game_names


class GamesInfoGetter:
    def get_games_info():
        games_info = []
        i = 0
        for game_name in game_names:
            i += 1
            # just to ensure that too many random matches from HLTB doesn't break this.
            if i == 100:
                break

            results = HowLongToBeat().search(game_name)
            if results is not None and len(results) > 0:
                result = max(results, key=lambda element: element.similarity)
                game_url = "https://howlongtobeat.com/game.php?id=" + str(result.game_id)
                info = info_scraping.scraping(game_url)
                game_info = {
                    'id': result.game_id,
                    'GameName'      : result.game_name, 
                    'Genres'         : info['genres'],
                    'ReleaseDate'  : info['release_date'],
                    'MainStory'     : result.main_story, 
                    'MainExtra'     : result.main_extra, 
                    'Completionist' : result.completionist
                }
                games_info.append(game_info)
        if len(games_info) == 0:
            print("EMPTY GAME LIST!!!")
        return games_info




