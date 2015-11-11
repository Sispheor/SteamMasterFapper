from Utils import utils


class Geek:
    def __init__(self, id, mail=None):
        self.id = id
        self.mail = mail
        self.name = self._get_username_from_id(self.id)
        self.played_time_2weeks = self._get_playtime_2weeks(self.id)

    @staticmethod
    def _get_username_from_id(friend_id):
        cfg = utils.get_settings()
        url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="\
              + cfg['API_STEAM_KEY'] + "&steamids="+str(friend_id)
        json_data = utils.get_steam_url(url)
        if json_data:
            try:
                name = json_data['response']['players'][0]['personaname']
                name.encode('utf-8')
                return name
            except IndexError:
                return "Does not exist"
        else:
            return "Does not exist"

    @staticmethod
    def _get_playtime_2weeks(friend_id):
        cfg = utils.get_settings()
        url = "http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key="\
            + cfg['API_STEAM_KEY'] + "&steamid="+str(friend_id)+"&format=json"
        json_data = utils.get_steam_url(url)
        if json_data:
            try:
                minute_played = json_data['response']['games'][0]['playtime_2weeks']
                return minute_played/60
            except KeyError:
                return "0"
        else:
            return "0"
