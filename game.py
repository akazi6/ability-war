import random
from js import document

# ===== ログ出力 =====
def log(text):
    log_div = document.getElementById("log")
    log_div.innerHTML += text + "\n"
    log_div.scrollTop = log_div.scrollHeight

# ===== キャラクター =====
class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 50
        self.guard = False

    def take_damage(self, dmg):
        if self.guard:
            dmg = dmg // 2
            self.guard = False
            log(f"{self.name}は防御してダメージ半減！")
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

# ===== ゲーム初期化 =====
player1 = Character("プレイヤーA")
player2 = Character("プレイヤーB")

# ===== 状態表示 =====
def log_status():
    log(f"{player1.name} HP:{player1.hp} MP:{player1.mp} | {player2.name} HP:{player2.hp} MP:{player2.mp}")

# ===== 能力 =====
def attack(user, target):
    dmg = random.randint(10, 20)
    log(f"{user.name}の攻撃！ {dmg}ダメージ")
    target.take_damage(dmg)

def fireball(user, target):
    if user.mp < 15:
        log("MPが足りない！")
        return
    user.mp -= 15
    dmg = random.randint(20, 35)
    log(f"{user.name}の🔥火球！ {dmg}ダメージ")
    target.take_damage(dmg)

def guard(user, target):
    if user.mp < 5:
        log("MPが足りない！")
        return
    user.mp -= 5
    user.guard = True
    log(f"{user.name}は🛡防御態勢に入った")

def heal(user, target):
    if user.mp < 10:
        log("MPが足りない！")
        return
    user.mp -= 10
    amount = random.randint(15, 25)
    user.hp += amount
    if user.hp > 100:
        user.hp = 100
    log(f"{user.name}は✨回復！ HPが{amount}回復した")

# ===== ターン処理 =====
def turn(player, enemy, choice):
    player.mp += 5
    if player.mp > 50:
        player.mp = 50

    # プレイヤー行動
    if choice == 0: attack(player, enemy)
    elif choice == 1: fireball(player, enemy)
    elif choice == 2: guard(player, enemy)
    elif choice == 3: heal(player, enemy)

    # 状態表示
    log_status()

    # AIターン
    ai_choice = random.randint(0,3)
    if ai_choice == 0: attack(enemy, player)
    elif ai_choice == 1: fireball(enemy, player)
    elif ai_choice == 2: guard(enemy, player)
    elif ai_choice == 3: heal(enemy, player)

    # 状態表示
    log_status()

# ===== ボタンイベント =====
document.getElementById("attackBtn").element.onclick = lambda e: turn(player1, player2, 0)
document.getElementById("fireballBtn").element.onclick = lambda e: turn(player1, player2, 1)
document.getElementById("guardBtn").element.onclick = lambda e: turn(player1, player2, 2)
document.getElementById("healBtn").element.onclick = lambda e: turn(player1, player2, 3)

# ===== 戦闘開始 =====
log("=== PyScriptバトル開始！ ===")
log_status()
