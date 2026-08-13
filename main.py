import random
import json
import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line, Rectangle, RoundedRectangle
from kivy.clock import Clock
from kivy.properties import ListProperty, NumericProperty, StringProperty

SAVE_FILE = "tictactoe_shenoda_save.json"

KV_DESIGN = '''
<MenuButton@Button>:
    font_size: '18sp'
    bold: True
    size_hint_y: None
    height: '52dp'
    background_normal: ''
    background_color: 0, 0, 0, 0

ScreenManager:
    SplashScreen:
    HomeScreen:
    NameScreen:
    DifficultyScreen:
    GameScreen:
    ShopScreen:
    BackgroundShopScreen:
    SkinCategoryScreen:
    XShopScreen:
    OShopScreen:

<SplashScreen>:
    name: 'splash'
    canvas.before:
        Color:
            rgba: 0.05, 0.02, 0.1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(30)
        spacing: dp(15)
        pos_hint: {'center_x': 0.5, 'center_y': 0.65}
        Label:
            text: '[b][color=00FFFF]LEGENDARY ARENA[/color][/b]'
            markup: True
            font_size: '27sp'
            halign: 'center'
            valign: 'middle'
       
<HomeScreen>:
    name: 'home'
    canvas.before:
        Color:
            rgba: app.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(40)
        spacing: dp(18)
        Label:
            text: 'LEGENDARY ARENA\\n[size=14sp]Shenoda Maged Abdo[/size]'
            markup: True
            font_size: '24sp'
            bold: True
            color: 0.3, 1.0, 0.7, 1
            halign: 'center'
        MenuButton:
            text: 'PLAY'
            canvas.before:
                Color:
                    rgba: 0.95, 0.25, 0.45, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.root.current = 'names'
        MenuButton:
            text: 'COMPUTER'
            canvas.before:
                Color:
                    rgba: 0.15, 0.75, 0.95, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.root.current = 'difficulty'
        MenuButton:
            text: 'SHOP'
            canvas.before:
                Color:
                    rgba: 1.0, 0.65, 0.15, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.root.current = 'shop'
        MenuButton:
            text: 'EXIT GAME'
            canvas.before:
                Color:
                    rgba: 0.75, 0.25, 0.95, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.exit_game()

<NameScreen>:
    name: 'names'
    canvas.before:
        Color:
            rgba: app.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(40)
        spacing: dp(20)
        Label:
            text: 'Enter Players Names'
            font_size: '24sp'
            bold: True
            color: 1, 1, 1, 1
        TextInput:
            id: px_name
            hint_text: 'Player X Name'
            font_size: '16sp'
            multiline: False
            size_hint_y: None
            height: dp(45)
        TextInput:
            id: po_name
            hint_text: 'Player O Name'
            font_size: '16sp'
            multiline: False
            size_hint_y: None
            height: dp(45)
        MenuButton:
            text: 'START BATTLE!'
            canvas.before:
                Color:
                    rgba: 0.2, 0.7, 0.5, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.start_pvp(px_name.text, po_name.text)
        MenuButton:
            text: 'BACK'
            canvas.before:
                Color:
                    rgba: 0.8, 0.2, 0.2, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.root.current = 'home'

<DifficultyScreen>:
    name: 'difficulty'
    canvas.before:
        Color:
            rgba: app.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(40)
        spacing: dp(20)
        Label:
            text: 'Select Difficulty'
            font_size: '26sp'
            bold: True
            color: 1, 1, 1, 1
        MenuButton:
            text: 'EASY'
            canvas.before:
                Color:
                    rgba: 0.1, 0.7, 0.8, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.start_pve('easy')
        MenuButton:
            text: 'MEDIUM'
            canvas.before:
                Color:
                    rgba: 0.8, 0.6, 0.1, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.start_pve('medium')
        MenuButton:
            text: 'HARD'
            canvas.before:
                Color:
                    rgba: 0.9, 0.2, 0.4, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.start_pve('hard')
        MenuButton:
            text: 'BACK'
            canvas.before:
                Color:
                    rgba: 0.8, 0.2, 0.2, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.root.current = 'home'

<GameScreen>:
    name: 'game'
    canvas.before:
        Color:
            rgba: app.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)
        
        BoxLayout:
            size_hint_y: 0.15
            Label:
                text: 'Coins: ' + str(app.coins) + ' 🪙'
                color: 1, 0.84, 0, 1
                bold: True
                font_size: '16sp'
            Label:
                id: turn_label
                text: 'Turn: X'
                bold: True
                font_size: '20sp'
            Button:
                text: 'Reset'
                font_size: '12sp'
                size_hint_x: 0.3
                background_normal: ''
                background_color: 0.8, 0.2, 0.2, 1
                on_release: app.reset_scores()

        BoxLayout:
            size_hint_y: 0.1
            Label:
                id: score_x
                text: app.player_x_name + ': 0'
                color: app.current_x_color
                bold: True
                font_size: '14sp'
            Label:
                id: score_o
                text: app.player_o_name + ': 0'
                color: app.current_o_color
                bold: True
                font_size: '14sp'

        AnchorLayout:
            id: board_anchor
            GridLayout:
                id: grid
                cols: 3
                spacing: dp(10)
                size_hint: None, None
                size: min(root.width, root.height) * 0.85, min(root.width, root.height) * 0.85

        BoxLayout:
            size_hint_y: 0.15
            spacing: dp(10)
            MenuButton:
                text: 'AGAIN'
                canvas.before:
                    Color:
                        rgba: 0.2, 0.6, 0.8, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [24,]
                on_release: app.reset_board()
            MenuButton:
                text: 'HOME'
                canvas.before:
                    Color:
                        rgba: 0.7, 0.3, 0.7, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [24,]
                on_release: app.root.current = 'home'

<ShopScreen>:
    name: 'shop'
    canvas.before:
        Color:
            rgba: 0.18, 0.12, 0.28, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(30)
        spacing: dp(20)
        Label:
            text: 'Legendary Shop - Coins: ' + str(app.coins) + ' 🪙'
            font_size: '18sp'
            bold: True
            size_hint_y: 0.2
            color: 1, 0.84, 0, 1
            halign: 'center'
        MenuButton:
            text: 'Backgrounds Studio'
            canvas.before:
                Color:
                    rgba: 0.7, 0.3, 0.9, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.root.current = 'bg_shop'
        MenuButton:
            text: 'Skins Studio (X & O)'
            canvas.before:
                Color:
                    rgba: 0.2, 0.8, 0.6, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.root.current = 'skin_category'
        MenuButton:
            text: 'BACK TO MENU'
            canvas.before:
                Color:
                    rgba: 0.8, 0.2, 0.2, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.root.current = 'home'

<BackgroundShopScreen>:
    name: 'bg_shop'
    canvas.before:
        Color:
            rgba: 0.18, 0.12, 0.28, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)
        Label:
            text: 'Backgrounds Studio - Coins: ' + str(app.coins) + ' 🪙'
            font_size: '14sp'
            bold: True
            size_hint_y: 0.1
            color: 1, 0.84, 0, 1
        ScrollView:
            BoxLayout:
                id: bg_list
                orientation: 'vertical'
                padding: dp(5)
                spacing: dp(12)
                size_hint_y: None
                height: self.minimum_height
        Button:
            text: 'BACK TO SHOP'
            size_hint_y: 0.12
            background_normal: ''
            background_color: 0.8, 0.2, 0.2, 1
            on_release: app.root.current = 'shop'

<SkinCategoryScreen>:
    name: 'skin_category'
    canvas.before:
        Color:
            rgba: 0.18, 0.12, 0.28, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(30)
        spacing: dp(20)
        Label:
            text: 'Select Character Studio'
            font_size: '22sp'
            bold: True
            color: 1, 0.84, 0, 1
            size_hint_y: 0.2
        MenuButton:
            text: 'Customize X Studio'
            canvas.before:
                Color:
                    rgba: 0.95, 0.5, 0.15, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.root.current = 'x_shop'
        MenuButton:
            text: 'Customize O Studio'
            canvas.before:
                Color:
                    rgba: 0.25, 0.6, 0.95, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.root.current = 'o_shop'
        MenuButton:
            text: 'BACK TO SHOP'
            canvas.before:
                Color:
                    rgba: 0.8, 0.2, 0.2, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]
            on_release: app.root.current = 'shop'

<XShopScreen>:
    name: 'x_shop'
    canvas.before:
        Color:
            rgba: 0.18, 0.12, 0.28, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)
        Label:
            text: 'X Characters Studio - Coins: ' + str(app.coins) + ' 🪙'
            font_size: '14sp'
            bold: True
            size_hint_y: 0.1
            color: 1, 0.84, 0, 1
        ScrollView:
            BoxLayout:
                id: x_list
                orientation: 'vertical'
                padding: dp(5)
                spacing: dp(12)
                size_hint_y: None
                height: self.minimum_height
        Button:
            text: 'BACK TO CATEGORIES'
            size_hint_y: 0.12
            background_normal: ''
            background_color: 0.8, 0.2, 0.2, 1
            on_release: app.root.current = 'skin_category'

<OShopScreen>:
    name: 'o_shop'
    canvas.before:
        Color:
            rgba: 0.18, 0.12, 0.28, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)
        Label:
            text: 'O Characters Studio - Coins: ' + str(app.coins) + ' 🪙'
            font_size: '14sp'
            bold: True
            size_hint_y: 0.1
            color: 1, 0.84, 0, 1
        ScrollView:
            BoxLayout:
                id: o_list
                orientation: 'vertical'
                padding: dp(5)
                spacing: dp(12)
                size_hint_y: None
                height: self.minimum_height
        Button:
            text: 'BACK TO CATEGORIES'
            size_hint_y: 0.12
            background_normal: ''
            background_color: 0.8, 0.2, 0.2, 1
            on_release: app.root.current = 'skin_category'
'''

class SplashScreen(Screen): pass
class HomeScreen(Screen): pass
class NameScreen(Screen): pass
class DifficultyScreen(Screen): pass
class GameScreen(Screen): pass
class ShopScreen(Screen): pass
class BackgroundShopScreen(Screen): pass
class SkinCategoryScreen(Screen): pass
class XShopScreen(Screen): pass
class OShopScreen(Screen): pass

class TicTacToeApp(App):
    bg_color = ListProperty([0.14, 0.09, 0.22, 1])  # لون خلفية رئيسية منور ومبهج وغير كاتم
    current_x_color = ListProperty([0.95, 0.35, 0.45, 1])
    current_o_color = ListProperty([0.35, 0.75, 0.95, 1])
    coins = NumericProperty(1000)
    
    player_x_name = StringProperty("Player X")
    player_o_name = StringProperty("Player O")

    def build(self):
        self.load_game_data()
        self.scores = {'X': 0, 'O': 0}
        self.mode = 'player'
        self.difficulty = 'easy'
        self.current_player = 'X'
        self.board = [''] * 9
        self.buttons = []
        self.game_active = True
        self.win_line = None

        bg_bases = ["Midnight", "Obsidian", "Amethyst", "Emerald", "Ruby", "Crimson", "Sapphire", "Topaz", "Galaxy", "Nebula",
                    "Sunset", "Volcano", "Cyberpunk", "Matrix", "Neon", "Void", "Abyss", "Mystic", "Royal", "Titanium"]
        self.shop_bgs = {}
        idx = 0
        used_prices = set()
        used_colors = set()
        for base in bg_bases:
            for mod in ["Alpha", "Beta", "Gamma", "Delta", "Omega"]:
                name = f"{base} {mod}"
                if idx == 0:
                    price = 0
                else:
                    price = 3000 + (idx * 1423)
                    while price in used_prices:
                        price += 13
                used_prices.add(price)
                
                while True:
                    col = [random.uniform(0.12, 0.4), random.uniform(0.1, 0.35), random.uniform(0.2, 0.5), 1]
                    col_key = (round(col[0], 2), round(col[1], 2), round(col[2], 2))
                    if col_key not in used_colors:
                        used_colors.add(col_key)
                        break

                self.shop_bgs[name] = {'price': price, 'color': col}
                idx += 1

        x_bases = ["Flame X", "Neon X", "Plasma X", "Solar X", "Cyber X", "Laser X", "Vortex X", "Pulse X", "Glow X", "Boss X"]
        self.shop_x_skins = {}
        idx = 0
        used_x_prices = set()
        used_x_colors = set()
        for base in x_bases:
            for mod in ["Mk-I", "Mk-II", "Mk-III", "Mk-IV", "Mk-V"]:
                name = f"{base} {mod}"
                if idx == 0:
                    price = 0
                elif idx >= 45:
                    price = 1200000 + (idx * 777)
                else:
                    price = 5000 + (idx * 2551)
                    while price in used_x_prices:
                        price += 19
                used_x_prices.add(price)
                
                while True:
                    col = [random.uniform(0.4, 1.0), random.uniform(0.1, 0.6), random.uniform(0.2, 0.7), 1]
                    col_key = (round(col[0], 2), round(col[1], 2), round(col[2], 2))
                    if col_key not in used_x_colors:
                        used_x_colors.add(col_key)
                        break

                self.shop_x_skins[name] = {'price': price, 'color': col}
                idx += 1

        o_bases = ["Crystal O", "Frost O", "Aqua O", "Electric O", "Zenith O", "Horizon O", "Ocean O", "Stellar O", "Azure O", "God O"]
        self.shop_o_skins = {}
        idx = 0
        used_o_colors = set()
        for base_x, base_o in zip(x_bases, o_bases):
            for mod in ["Mk-I", "Mk-II", "Mk-III", "Mk-IV", "Mk-V"]:
                name = f"{base_o} {mod}"
                x_name = f"{base_x} {mod}"
                price = self.shop_x_skins[x_name]['price']
                
                while True:
                    col = [random.uniform(0.1, 0.5), random.uniform(0.4, 0.9), random.uniform(0.5, 1.0), 1]
                    col_key = (round(col[0], 2), round(col[1], 2), round(col[2], 2))
                    if col_key not in used_o_colors:
                        used_o_colors.add(col_key)
                        break

                self.shop_o_skins[name] = {'price': price, 'color': col}
                idx += 1

        self.root = Builder.load_string(KV_DESIGN)
        self.setup_board()
        self.setup_shop_items()
        
        # 4 ثوانٍ كاملة لشاشة البداية
        Clock.schedule_once(self.goto_home, 15.0)
        return self.root

    def goto_home(self, dt):
        self.root.current = 'home'

    def exit_game(self):
        App.get_running_app().stop()

    def save_game_data(self):
        data = {
            "coins": self.coins,
            "owned_bgs": self.owned_bgs,
            "owned_x_skins": self.owned_x_skins,
            "owned_o_skins": self.owned_o_skins,
            "bg_color": self.bg_color,
            "current_x_color": self.current_x_color,
            "current_o_color": self.current_o_color
        }
        try:
            with open(SAVE_FILE, 'w') as f:
                json.dump(data, f)
        except Exception:
            pass

    def load_game_data(self):
        self.owned_bgs = ['Midnight Alpha']
        self.owned_x_skins = ['Flame X Mk-I']
        self.owned_o_skins = ['Crystal O Mk-I']
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, 'r') as f:
                    data = json.load(f)
                    self.coins = data.get("coins", 1000)
                    self.owned_bgs = data.get("owned_bgs", self.owned_bgs)
                    self.owned_x_skins = data.get("owned_x_skins", self.owned_x_skins)
                    self.owned_o_skins = data.get("owned_o_skins", self.owned_o_skins)
                    if "bg_color" in data:
                        self.bg_color = data["bg_color"]
                    if "current_x_color" in data:
                        self.current_x_color = data["current_x_color"]
                    if "current_o_color" in data:
                        self.current_o_color = data["current_o_color"]
            except Exception:
                pass

    def start_pvp(self, px, po):
        self.player_x_name = px if px.strip() != "" else "Player X"
        self.player_o_name = po if po.strip() != "" else "Player O"
        self.mode = 'player'
        self.reset_scores()
        self.reset_board()
        self.root.current = 'game'

    def start_pve(self, diff):
        self.player_x_name = "You"
        self.player_o_name = "Computer"
        self.mode = 'pc'
        self.difficulty = diff
        self.reset_scores()
        self.reset_board()
        self.root.current = 'game'

    def setup_board(self):
        grid = self.root.get_screen('game').ids.grid
        for i in range(9):
            btn = Button(
                text='', font_size='45sp', bold=True,
                background_normal='', background_color=(0.25, 0.18, 0.35, 1)
            )
            btn.bind(on_release=lambda instance, i=i: self.make_move(i))
            self.buttons.append(btn)
            grid.add_widget(btn)

    def update_ui(self):
        screen = self.root.get_screen('game')
        screen.ids.turn_label.text = f"Turn: {self.current_player}"
        screen.ids.turn_label.color = self.current_x_color if self.current_player == 'X' else self.current_o_color
        screen.ids.score_x.text = f"{self.player_x_name}: {self.scores['X']}"
        screen.ids.score_o.text = f"{self.player_o_name}: {self.scores['O']}"

    def reset_scores(self):
        self.scores = {'X': 0, 'O': 0}
        self.update_ui()

    def make_move(self, index):
        if not self.game_active or self.board[index] != '':
            return
        
        self.execute_move(index, self.current_player)

        if self.check_game_over():
            return

        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.update_ui()

        if self.mode == 'pc' and self.current_player == 'O' and self.game_active:
            Clock.schedule_once(self.pc_move, 0.5)

    def execute_move(self, index, player):
        self.board[index] = player
        btn = self.buttons[index]
        btn.text = player
        btn.color = self.current_x_color if player == 'X' else self.current_o_color

    def pc_move(self, dt):
        if not self.game_active: return
        empty = [i for i in range(9) if self.board[i] == '']
        move = -1

        if self.difficulty == 'easy':
            move = random.choice(empty)
        elif self.difficulty == 'medium':
            move = self.get_best_move(empty, depth_limit=1)
            if move == -1: move = random.choice(empty)
        elif self.difficulty == 'hard':
            move = self.get_best_move(empty, depth_limit=9)
            
        self.make_move(move)

    def get_best_move(self, empty_cells, depth_limit):
        for i in empty_cells:
            self.board[i] = 'O'
            if self.check_win_logic('O'):
                self.board[i] = ''
                return i
            self.board[i] = ''
        for i in empty_cells:
            self.board[i] = 'X'
            if self.check_win_logic('X'):
                self.board[i] = ''
                return i
            self.board[i] = ''
        return random.choice(empty_cells) if empty_cells else -1

    def check_win_logic(self, player):
        win_combos = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        return any(all(self.board[i] == player for i in combo) for combo in win_combos)

    def check_game_over(self):
        win_combos = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        for combo in win_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '':
                self.game_active = False
                winner = self.board[combo[0]]
                self.scores[winner] += 1
                self.draw_winning_line(combo)
                
                winner_name = self.player_x_name if winner == 'X' else self.player_o_name
                msg = f"{winner_name} Wins!"
                
                # التعديل: الفوز يعطي عملات فقط إذا كان النمط هو الكمبيوتر (pc)
                if self.mode == 'pc':
                    reward = {'easy': 50, 'medium': 110, 'hard': 260}[self.difficulty]
                    self.coins += reward
                    msg += f"\n+{reward} Coins 🪙!"
                
                self.save_game_data()
                self.show_popup("Winner!", msg)
                self.update_ui()
                return True
                
        if '' not in self.board:
            self.game_active = False
            # التعديل: التعادل يعطي عملات فقط إذا كان النمط هو الكمبيوتر (pc)
            if self.mode == 'pc':
                self.coins += 25
                self.show_popup("Draw!", "It's a tie!\n+25 Coins 🪙")
            else:
                self.show_popup("Draw!", "It's a tie!")
                
            self.save_game_data()
            return True
            
        return False

    def draw_winning_line(self, combo):
        anchor = self.root.get_screen('game').ids.board_anchor
        b1, b3 = self.buttons[combo[0]], self.buttons[combo[2]]
        with anchor.canvas.after:
            Color(1, 0.84, 0, 1)
            self.win_line = Line(points=[b1.center_x, b1.center_y, b3.center_x, b3.center_y], width=6)

    def reset_board(self):
        self.board = [''] * 9
        self.game_active = True
        self.current_player = 'X'
        for btn in self.buttons:
            btn.text = ''
            
        anchor = self.root.get_screen('game').ids.board_anchor
        if self.win_line in anchor.canvas.after.children:
            anchor.canvas.after.remove(self.win_line)
        self.update_ui()

    def setup_shop_items(self):
        bg_list = self.root.get_screen('bg_shop').ids.bg_list
        bg_list.clear_widgets()
        for name, data in self.shop_bgs.items():
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height='100dp', spacing=10, padding=5)
            preview = Button(size_hint_x=0.45, background_normal='', background_color=data['color'])
            preview.text = f"Studio BG\\n{name}"
            preview.font_size = '11sp'
            preview.bold = True
            
            is_owned = name in self.owned_bgs
            price_str = "FREE" if data['price'] == 0 else f"{data['price']} 🪙"
            action_label = "EQUIPPED" if is_owned else f"BUY:\\n{price_str}"
            
            action_btn = Button(size_hint_x=0.55, background_normal='', background_color=(0.28, 0.22, 0.42, 1))
            action_btn.text = action_label
            action_btn.font_size = '13sp'
            action_btn.bold = True
            action_btn.bind(on_release=lambda instance, n=name, d=data: self.buy_or_equip_item(n, d, 'bg'))
            
            row.add_widget(preview)
            row.add_widget(action_btn)
            bg_list.add_widget(row)

        x_list = self.root.get_screen('x_shop').ids.x_list
        x_list.clear_widgets()
        for name, data in self.shop_x_skins.items():
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height='100dp', spacing=10, padding=5)
            hex_c = f"{int(data['color'][0]*255):02x}{int(data['color'][1]*255):02x}{int(data['color'][2]*255):02x}"
            preview = Button(size_hint_x=0.45, background_normal='', background_color=(0.2, 0.16, 0.3, 1))
            preview.markup = True
            preview.text = f"[color={hex_c}]BIG X Studio\\n{name}[/color]"
            preview.font_size = '11sp'
            preview.bold = True
            
            is_owned = name in self.owned_x_skins
            price_str = "FREE" if data['price'] == 0 else f"{data['price']} 🪙"
            action_label = "EQUIPPED" if is_owned else f"BUY:\\n{price_str}"
            
            action_btn = Button(size_hint_x=0.55, background_normal='', background_color=(0.28, 0.22, 0.42, 1))
            action_btn.text = action_label
            action_btn.font_size = '13sp'
            action_btn.bold = True
            action_btn.bind(on_release=lambda instance, n=name, d=data: self.buy_or_equip_item(n, d, 'x'))
            
            row.add_widget(preview)
            row.add_widget(action_btn)
            x_list.add_widget(row)

        o_list = self.root.get_screen('o_shop').ids.o_list
        o_list.clear_widgets()
        for name, data in self.shop_o_skins.items():
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height='100dp', spacing=10, padding=5)
            hex_c = f"{int(data['color'][0]*255):02x}{int(data['color'][1]*255):02x}{int(data['color'][2]*255):02x}"
            preview = Button(size_hint_x=0.45, background_normal='', background_color=(0.2, 0.16, 0.3, 1))
            preview.markup = True
            preview.text = f"[color={hex_c}]BIG O Studio\\n{name}[/color]"
            preview.font_size = '11sp'
            preview.bold = True
            
            is_owned = name in self.owned_o_skins
            price_str = "FREE" if data['price'] == 0 else f"{data['price']} 🪙"
            action_label = "EQUIPPED" if is_owned else f"BUY:\\n{price_str}"
            
            action_btn = Button(size_hint_x=0.55, background_normal='', background_color=(0.28, 0.22, 0.42, 1))
            action_btn.text = action_label
            action_btn.font_size = '13sp'
            action_btn.bold = True
            action_btn.bind(on_release=lambda instance, n=name, d=data: self.buy_or_equip_item(n, d, 'o'))
            
            row.add_widget(preview)
            row.add_widget(action_btn)
            o_list.add_widget(row)

    def buy_or_equip_item(self, name, data, item_type):
        price = data['price']
        if item_type == 'bg':
            owned_list = self.owned_bgs
        elif item_type == 'x':
            owned_list = self.owned_x_skins
        else:
            owned_list = self.owned_o_skins
        
        icon = name in owned_list
        if icon:
            if item_type == 'bg':
                self.bg_color = data['color']
            elif item_type == 'x':
                self.current_x_color = data['color']
            else:
                self.current_o_color = data['color']
            self.setup_shop_items()
            self.save_game_data()
            self.show_popup("Equipped!", f"Successfully equipped [{name}]!")
        else:
            if self.coins >= price:
                self.coins -= price
                owned_list.append(name)
                self.setup_shop_items()
                self.save_game_data()
                self.show_popup("Purchased! 🎉", f"You bought [{name}]!\nClick it again to equip.")
            else:
                self.show_popup("Not Enough Coins! 😅", f"You need {price - self.coins} more coins!")

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(Label(text=message, font_size='16sp', halign='center'))
        btn = Button(text='Awesome!', size_hint_y=None, height='40dp', background_color=[0.2, 0.6, 0.8, 1])
        content.add_widget(btn)
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.35), title_size='18sp')
        btn.bind(on_release=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    TicTacToeApp().run()
