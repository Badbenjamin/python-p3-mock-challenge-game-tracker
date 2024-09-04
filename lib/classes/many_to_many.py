class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title 

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title) > 0 and not hasattr(self, "_title"):
            self._title = new_title
    

    def results(self):
        results = []
        for result in Result.all:
            if result.game is self:
                results.append(result)
        return results
        # thing to append, for loop definition, conditional statement
        return [r for r in Result.all if r.game is self]

    def players(self):
        players_set = set()
        for r in self.results():
            players_set.add(r.player)
        return list(players_set)
        return set([r.player for r in self.results()])

    def average_score(self, player):
        # MY CODE
        # result = 0
        # counter = 0
        # for game in Result.all:
        #     if game.player is player:
        #         result += game.score
        #         counter += 1
        # return result / counter
    
        #  BEN'S CODE
        total = 0
        count = 0
        for r in self.results():
            if r.player is player:
                total += r.score
                count += 1
        if count == 0:
            return None
        
        return total / count

    def __repr__(self):
        return f'<{self.title}>'

class Player:
    def __init__(self, username):
        self.username = username


    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
            self._username = new_username

    def results(self):
        result_objs = []
        for result_obj in Result.all:
            if result_obj.player is self:
                result_objs.append(result_obj)
        return result_objs

    def games_played(self):
        # games = set()
        # for games in Result.all:
        #     if games.player is self:
        #         games.add(games)
        # return games

        # use self.results function to return only player's game
        games = set()
        for r in self.results():
            games.add(r.game)
        return list(games)
        # list comp version
        return [r. game in r in self.results()]


        

    def played_game(self, game):
        # MY CODE
        # result = False
        # for game_played in Result.all:
        #     if game_played.player is self and game_played.game == game:
        #         result = True
        # return result
    
        # BEN'S CODE
        return game in self.games_played()

    def num_times_played(self, game):
        # MY CODE
        # result = 0
        # # print(game.title)
        # for game_played in Result.all:
        #     print(game_played.player)
        #     if game_played.game is game and game_played.player is self:
        #         result += 1
        # return result
            # print(game_played.game)

        #  BEN'S CODE
        count = 0
        for r in self.results():
            if r.game is game:
                count += 1
        return count

        # count the game results for the game (count method)
        return [r.game for r in self.result()].count(game)
    
    @classmethod
    def highest_scored(cls, game):
        # MIN MAX, compare first result to second, if second is higher, replace 
        players = list(game.players())
        # all the players who played the game
        max_player = players[0]
        max_player_average = game.average_score(players[0])
        for player in game.players():
            avg = game.average_score(player)
            if avg > max_player_average:
                max_player_average = avg
                max_player = player
        return max_player
        # avg score for players
        # game.average_score(player)

        return max(players, key=lambda player: game.average_score(player))

    def __repr__(self):
        return f'<{self.username}>'

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if isinstance(new_score, int) and 1 <= new_score <= 5000 and not hasattr(self, "_score"):
            self._score = new_score

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if isinstance(new_player, Player):
            self._player = new_player

    @property 
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if isinstance(new_game, Game):
            self._game = new_game

    def __repr__(self):
        return f'<{self.player.username}, {self.game.title}, {self.score}>'

if __name__ == "__main__":
    g1 = Game("pacman")
    g2 = Game("tetris")
    g3 = Game("pong")

    p1 = Player("ben")
    p2 = Player("ronald")
    # print(p1.username)

    r1 = Result(p1, g1, 4000)
    r2 = Result(p1, g2, 200)
    r3 = Result(p1, g1, 3500)
    r4 = Result(p2, g1, 5000)
    # print(r1.all)

    # print(g1.average_score(p1))
    # print(p1.results())
    print(Player.highest_scored(g2))