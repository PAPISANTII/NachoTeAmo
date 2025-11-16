from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    room_name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_games')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player2_games', blank=True, null=True)
    board = models.CharField(max_length=9, default="-" * 9)
    active_player = models.IntegerField(default=1)
    winner = models.CharField(max_length=10, blank=True, null=True)
    current_player = models.IntegerField(default=1)
    over = models.BooleanField(default=False)
    
    def __str__(self):
        return self.room_name
    
    def make_move(self, user, position):
        if self.over or self.board[position] != "-": 
            return False
        if self.active_player == 1 and user == self.owner:
            token = 'X'
        elif self.active_player == 2 and user == self.player2:
            token = 'O'
        else:
            return False

        board_list = list(self.board)
        board_list[position] = token
        self.board = "".join(board_list)
        
        self.active_player = 2 if self.active_player == 1 else 1
        self.save()
        return True
    