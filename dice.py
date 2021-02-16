import importlib
import random

class Dice:
    def __init__(self,val=6): #初期化メソッドの定義で引数valを受け取る
        if val not in [4,6,8,12,20]:
            raise Exception("4,6,8,12,20以外は正多面体ではありません")
        self.face_num = val

    def shoot(self):
        return random.randint(1,self.face_num)

"""val =6の意味は実行するときに引数を指定しない場合は、自動で六面体のサイコロになるということ"""