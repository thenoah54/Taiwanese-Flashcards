import random
import os
import time
import customtkinter
import copy

class Vocabulary(customtkinter.CTk):
    # Main window
    def __init__(self):
        super().__init__()
        self.geometry(CenterWindow.CenterWindowToDisplay(self, 500, 500, self._get_window_scaling()))
        self.title("台灣 Vocabulary")
        customtkinter.set_appearance_mode("dark")
        self.minsize(500, 400)
        # self.maxsize(500, 400)
        
        self.match_answer = ""
        self.selected_vocab = {}
        self.quit_state = False
        self.length = 0

        padding_x_label = 15
        padding_x_button = 5
        padding_y = 5

        fg_pronounce_color = '#1C8900'
        pronounce_hover_color = '#98FF7E'
        fg_english_color = '#890000'
        english_hover_color = '#FF7E7E'

        # TONES
        tones_label = customtkinter.CTkLabel(
            master=self, text="Tones", font=("Arial Bold", 20))
        tones_label.grid(row=0, column=0, padx=padding_x_label, pady=padding_y)
        tones_button = customtkinter.CTkButton(
            master=self, text="Basic Tones",
            font=("Arial Bold", 15), 
            width=110,
            hover_color="#00D4FF",
            command=self.start_quiz_tones)
        tones_button.grid(row=0, column=2, padx=padding_x_button, pady=padding_y)  

        # ALL BUTTON
        all_pronounce_label = customtkinter.CTkLabel(
            master=self, text="All", font=("Arial Bold", 20))
        all_pronounce_label.grid(row=1, column=0, padx=padding_x_label, pady=padding_y)
        all_pronounce_button = customtkinter.CTkButton(
            master=self, text="All Pronunciation",
            font=("Arial Bold", 10), 
            width=110,
            fg_color=fg_pronounce_color,
            hover_color=pronounce_hover_color,
            command=self.start_quiz_all_pronounce)
        all_pronounce_button.grid(row=1, column=1, padx=padding_x_button, pady=padding_y)
        all_character_button = customtkinter.CTkButton(
            master=self, text="All Characters",
            font=("Arial Bold", 10), 
            width=110,
            hover_color="#00D4FF",
            command=self.start_quiz_all_characters)
        all_character_button.grid(row=1, column=2, padx=padding_x_button, pady=padding_y)  
        all_english_button = customtkinter.CTkButton(
            master=self, text="All English",
            font=("Arial Bold", 10), 
            width=110,
            fg_color=fg_english_color,
            hover_color=english_hover_color,
            command=self.start_quiz_all_english)
        all_english_button.grid(row=1, column=3, padx=padding_x_button, pady=padding_y)

        # NUMBERS
        numbers_pronounce_label = customtkinter.CTkLabel(
            master=self, text="Numbers", font=("Arial Bold", 20))
        numbers_pronounce_label.grid(row=2, column=0, padx=padding_x_label, pady=padding_y)
        numbers_pronounce_button = customtkinter.CTkButton(
            master=self, text="Pronunciation",
            font=("Arial Bold", 15), 
            width=110,
            fg_color=fg_pronounce_color,
            hover_color=pronounce_hover_color,
            command=self.start_quiz_numbers_pronounce)
        numbers_pronounce_button.grid(row=2, column=1, padx=padding_x_button, pady=padding_y)
        numbers_character_button = customtkinter.CTkButton(
            master=self, text="Characters",
            font=("Arial Bold", 15), 
            width=110,
            hover_color="#00D4FF",
            command=self.start_quiz_numbers_characters)
        numbers_character_button.grid(row=2, column=2, padx=padding_x_button, pady=padding_y)
        numbers_english_button = customtkinter.CTkButton(
            master=self, text="English",
            font=("Arial Bold", 15), 
            width=110,
            fg_color=fg_english_color,
            hover_color=english_hover_color,
            command=self.start_quiz_numbers_english)
        numbers_english_button.grid(row=2, column=3, padx=padding_x_button, pady=padding_y)
        
        # LESSON 1
        lesson_1_label = customtkinter.CTkLabel(
            master=self, text="Lesson 一", font=("Arial", 20))
        lesson_1_label.grid(row=3, column=0, padx=padding_x_label, pady=padding_y)
        chapter_1_pronounce_button = customtkinter.CTkButton(
            master=self, text="Pronunciation",
            font=("Arial Bold", 15), 
            width=110,
            fg_color=fg_pronounce_color,
            hover_color=pronounce_hover_color,
            command=self.start_quiz_chapter_1_pronounce)
        chapter_1_pronounce_button.grid(row=3, column=1, padx=padding_x_button, pady=padding_y)
        chapter_1_characters_button = customtkinter.CTkButton(
            master=self, text="Characters", 
            font=("Arial Bold", 15),
            width=110,
            hover_color="#00D4FF",
            command=self.start_quiz_chapter_1_characters)
        chapter_1_characters_button.grid(row=3, column=2, padx=padding_x_button, pady=padding_y)
        chapter_1_english_button = customtkinter.CTkButton(
            master=self, text="English", 
            font=("Arial Bold", 15),
            width=110,
            fg_color=fg_english_color,
            hover_color=english_hover_color,
            command=self.start_quiz_chapter_1_english)
        chapter_1_english_button.grid(row=3, column=3, padx=padding_x_button, pady=padding_y)
        
        # LESSON 2
        lesson_2_label = customtkinter.CTkLabel(
            master=self, text="Lesson 二", font=("Arial", 20))
        lesson_2_label.grid(row=4, column=0, padx=padding_x_label, pady=padding_y)
        chapter_2_pronounce_button = customtkinter.CTkButton(
            master=self, text="Pronunciation",
            font=("Arial Bold", 15), 
            width=110,
            fg_color=fg_pronounce_color,
            hover_color=pronounce_hover_color,
            command=self.start_quiz_chapter_2_pronounce)
        chapter_2_pronounce_button.grid(row=4, column=1, padx=padding_x_button, pady=padding_y)
        chapter_2_characters_button = customtkinter.CTkButton(
            master=self, text="Characters",
            font=("Arial Bold", 15), 
            width=110,
            hover_color="#00D4FF",
            command=self.start_quiz_chapter_2_characters)
        chapter_2_characters_button.grid(row=4, column=2, padx=padding_x_button, pady=padding_y)
        chapter_2_english_button = customtkinter.CTkButton(
            master=self, text="English", 
            font=("Arial Bold", 15),
            width=110,
            fg_color=fg_english_color,
            hover_color=english_hover_color,
            command=self.start_quiz_chapter_2_english)
        chapter_2_english_button.grid(row=4, column=3, padx=padding_x_button, pady=padding_y)
        
        # LESSON 3
        lesson_3_label = customtkinter.CTkLabel(
            master=self, text="Lesson 三", font=("Arial", 20))
        lesson_3_label.grid(row=5, column=0, padx=padding_x_label, pady=padding_y)
        chapter_3_pronounce_button = customtkinter.CTkButton(
            master=self, text="Pronunciation",
            font=("Arial Bold", 15), 
            width=110,
            fg_color=fg_pronounce_color,
            hover_color=pronounce_hover_color,
            command=self.start_quiz_chapter_3_pronounce)
        chapter_3_pronounce_button.grid(row=5, column=1, padx=padding_x_button, pady=padding_y)
        chapter_3_characters_button = customtkinter.CTkButton(
            master=self, text="Characters",
            font=("Arial Bold", 15), 
            width=110,
            hover_color="#00D4FF",
            command=self.start_quiz_chapter_3_characters)
        chapter_3_characters_button.grid(row=5, column=2, padx=padding_x_button, pady=padding_y)
        chapter_3_english_button = customtkinter.CTkButton(
            master=self, text="English", 
            font=("Arial Bold", 15),
            width=110,
            fg_color=fg_english_color,
            hover_color=english_hover_color,
            command=self.start_quiz_chapter_3_english)
        chapter_3_english_button.grid(row=5, column=3, padx=padding_x_button, pady=padding_y)
        
        # LESSON 4
        lesson_4_label = customtkinter.CTkLabel(
            master=self, text="Lesson 四", font=("Arial", 20))
        lesson_4_label.grid(row=6, column=0, padx=padding_x_label, pady=padding_y)
        chapter_4_pronounce_button = customtkinter.CTkButton(
            master=self, text="Pronunciation",
            font=("Arial Bold", 15), 
            width=110,
            fg_color=fg_pronounce_color,
            hover_color=pronounce_hover_color,
            command=self.start_quiz_chapter_4_pronounce)
        chapter_4_pronounce_button.grid(row=6, column=1, padx=padding_x_button, pady=padding_y)
        chapter_4_characters_button = customtkinter.CTkButton(
            master=self, text="Characters",
            font=("Arial Bold", 15), 
            width=110,
            hover_color="#00D4FF",
            command=self.start_quiz_chapter_4_characters)
        chapter_4_characters_button.grid(row=6, column=2, padx=padding_x_button, pady=padding_y)
        chapter_4_english_button = customtkinter.CTkButton(
            master=self, text="English", 
            font=("Arial Bold", 15),
            width=110,
            fg_color=fg_english_color,
            hover_color=english_hover_color,
            command=self.start_quiz_chapter_4_english)
        chapter_4_english_button.grid(row=6, column=3, padx=padding_x_button, pady=padding_y)
        
        # LESSON 5
        lesson_5_label = customtkinter.CTkLabel(
            master=self, text="Lesson 五", font=("Arial", 20))
        lesson_5_label.grid(row=7, column=0, padx=padding_x_label, pady=padding_y)
        chapter_5_pronounce_button = customtkinter.CTkButton(
            master=self, text="Pronunciation",
            font=("Arial Bold", 15), 
            width=110,
            fg_color=fg_pronounce_color,
            hover_color=pronounce_hover_color,
            command=self.start_quiz_chapter_5_pronounce)
        chapter_5_pronounce_button.grid(row=7, column=1, padx=padding_x_button, pady=padding_y)
        chapter_5_characters_button = customtkinter.CTkButton(
            master=self, text="Characters",
            font=("Arial Bold", 15), 
            width=110,
            hover_color="#00D4FF",
            command=self.start_quiz_chapter_5_characters)
        chapter_5_characters_button.grid(row=7, column=2, padx=padding_x_button, pady=padding_y)
        chapter_5_english_button = customtkinter.CTkButton(
            master=self, text="English", 
            font=("Arial Bold", 15),
            width=110,
            fg_color=fg_english_color,
            hover_color=english_hover_color,
            command=self.start_quiz_chapter_5_english)
        chapter_5_english_button.grid(row=7, column=3, padx=padding_x_button, pady=padding_y)

        # LESSON 6
        lesson_6_label = customtkinter.CTkLabel(
            master=self, text="Lesson 六", font=("Arial", 20))
        lesson_6_label.grid(row=8, column=0, padx=padding_x_label, pady=padding_y)
        chapter_6_pronounce_button = customtkinter.CTkButton(
            master=self, text="Pronunciation",
            font=("Arial Bold", 15), 
            width=110,
            fg_color=fg_pronounce_color,
            hover_color=pronounce_hover_color,
            command=self.start_quiz_chapter_6_pronounce)
        chapter_6_pronounce_button.grid(row=8, column=1, padx=padding_x_button, pady=padding_y)
        chapter_6_characters_button = customtkinter.CTkButton(
            master=self, text="Characters",
            font=("Arial Bold", 15), 
            width=110,
            hover_color="#00D4FF",
            command=self.start_quiz_chapter_6_characters)
        chapter_6_characters_button.grid(row=8, column=2, padx=padding_x_button, pady=padding_y)
        chapter_6_english_button = customtkinter.CTkButton(
            master=self, text="English", 
            font=("Arial Bold", 15),
            width=110,
            fg_color=fg_english_color,
            hover_color=english_hover_color,
            command=self.start_quiz_chapter_6_english)
        chapter_6_english_button.grid(row=8, column=3, padx=padding_x_button, pady=padding_y)
    
        # LESSON 7
        lesson_7_label = customtkinter.CTkLabel(
            master=self, text="Lesson 七", font=("Arial", 20))
        lesson_7_label.grid(row=9, column=0, padx=padding_x_label, pady=padding_y)
        chapter_7_pronounce_button = customtkinter.CTkButton(
            master=self, text="Pronunciation",
            font=("Arial Bold", 15), 
            width=110,
            fg_color=fg_pronounce_color,
            hover_color=pronounce_hover_color,
            command=self.start_quiz_chapter_7_pronounce)
        chapter_7_pronounce_button.grid(row=9, column=1, padx=padding_x_button, pady=padding_y)
        chapter_7_characters_button = customtkinter.CTkButton(
            master=self, text="Characters",
            font=("Arial Bold", 15), 
            width=110,
            hover_color="#00D4FF",
            command=self.start_quiz_chapter_7_characters)
        chapter_7_characters_button.grid(row=9, column=2, padx=padding_x_button, pady=padding_y)
        chapter_7_english_button = customtkinter.CTkButton(
            master=self, text="English", 
            font=("Arial Bold", 15),
            width=110,
            fg_color=fg_english_color,
            hover_color=english_hover_color,
            command=self.start_quiz_chapter_7_english)
        chapter_7_english_button.grid(row=9, column=3, padx=padding_x_button, pady=padding_y)

        # LESSON 8
        lesson_8_label = customtkinter.CTkLabel(
            master=self, text="Lesson 八", font=("Arial", 20))
        lesson_8_label.grid(row=10, column=0, padx=padding_x_label, pady=padding_y)
        chapter_8_pronounce_button = customtkinter.CTkButton(
            master=self, text="Pronunciation",
            font=("Arial Bold", 15), 
            width=110,
            fg_color=fg_pronounce_color,
            hover_color=pronounce_hover_color,
            command=self.start_quiz_chapter_8_pronounce)
        chapter_8_pronounce_button.grid(row=10, column=1, padx=padding_x_button, pady=padding_y)
        chapter_8_characters_button = customtkinter.CTkButton(
            master=self, text="Characters",
            font=("Arial Bold", 15), 
            width=110,
            hover_color="#00D4FF",
            command=self.start_quiz_chapter_8_characters)
        chapter_8_characters_button.grid(row=10, column=2, padx=padding_x_button, pady=padding_y)
        chapter_8_english_button = customtkinter.CTkButton(
            master=self, text="English", 
            font=("Arial Bold", 15),
            width=110,
            fg_color=fg_english_color,
            hover_color=english_hover_color,
            command=self.start_quiz_chapter_8_english)
        chapter_8_english_button.grid(row=10, column=3, padx=padding_x_button, pady=padding_y)

        self.tones_diacritics = {
            'Tone 1: a': ['high flat'],
            'Tone 2: á': ['high falling'],
            'Tone 3: à': ['mid falling'],
            'Tone 4: a': ['mid stop', 'ends with -p, -t, -k, -h'],
            'Tone 5: â': ['low rising'],
            'Tone 7: ā': ['mid flat'],
            'Tone 8: a̍': ['high stop', 'ends with -p, -t, -k, -h']
        }

        self.numbers_pronounce = {
            'tsi̍t': ['one', '1', '一'],
            'nn̄g': ['two', '2', '二'],
            'sann': ['three', '3', '三'],
            'sì': ['four', '4', '四'],
            'gō/gōo': ['five', '5', '五'],
            'la̍k': ['six', '6', '六'],
            'chit/tshit': ['seven', '7', '七'],
            'poeh/pueh': ['eight', '8', '八'],
            'káu': ['nine', '9', '九'],
            'cha̍p/tsa̍p': ['ten', '10', '十'],
            'tsa̍p-it': ['eleven', '11', '十一'],
            'tsa̍p-jī': ['tweleve', '12', '十二'],
            'jī-tsa̍p': ['twenty', '20', '二十'],
            'jī-tsa̍p-it': ['twenty one', '21', '二十一'],
            'jī-tsa̍p-jī': ['twenty two', '22', '二十二'],
            '_1, greater than 10': ['it', 'tsit becomes it'],
            '_2, greater than 10': ['ji', 'nng becomes ji']    
        }
        self.numbers_characters = {
            '一': ['one', '1', 'tsit'],
            '二': ['two', '2', 'nng'],
            '三': ['three', '3', 'sann'],
            '四': ['four', '4', 'si'],
            '五': ['five', '5', 'go', 'goo'],
            '六': ['six', '6', 'lak'],
            '七': ['seven', '7', 'chit', 'tshit'],
            '八': ['eight', '8', 'poeh', 'pueh'],
            '九': ['nine', '9', 'kau'],
            '十': ['ten', '10', 'chap', 'tsap'],
            '十一': ['eleven', '11', 'tsap-it'],
            '十二': ['twelve', '12', 'tsap-ji'],
            '二十': ['twenty', '20', 'ji-tsap'],
            '二十一': ['twenty one', '21', 'ji-tsap-it'],
            '二十二': ['twenty two', '22', 'ji-tsap-ji']
        }
        self.numbers_english = {
            '1': ['一', 'tsit', 'it when > 10'],
            '2': ['二', 'nng', 'ji when > 10'],
            '3': ['三','sann'],
            '4': ['四', 'si'],
            '5': ['五', 'go', 'goo'],
            '6': ['六', 'lak'],
            '7': ['七', 'chit', 'tshit'],
            '8': ['八', 'poeh', 'pueh'],
            '9': ['九', 'kau'],
            '10': ['十', 'chap', 'tsap'],
            '11': ['十一', 'tsap-it'],
            '12': ['十二', 'tsap-ji'],
            '20': ['二十', 'ji-tsap'],
            '21': ['二十一', 'ji-tsap-it'],
            '22': ['二十二', 'ji-tsap-ji'],    
        }

        self.chapter_1_pronounce = {
            "siû-tsuí": ["to swim", "swimming", "泅水"],
            "tsiok": ["very", "so", "足"],
            "beh": ["to want", 'to be going', "欲"],
            "khī": ["to go", "去"],
            "e-poo": ["this afternoon", "下晡"],
            "káu": ["dog", "狗"],
            "mā": ["also", "too", "嘛"],
            "jua̍h": ["hot", "熱"],
            "kin-á-ji̍t": ["today", "今仔日"],
            "guá": ["I", "me", "我"],
            "kuânn": ["cold", "寒"],
            "thinn": ["day", "sky", "heaven", "天"],
            "tsit-má": ["now", "這馬"],
            "lí/dí": ["you", "你"],
            "guán": ["we", "us", "our", "阮", '(excludes listener)'],
            "ê": ["(possesive)", "的"],
            "lín": ["you (plural)", "恁"],
            "tsái-khí": ["morning", "早起"],
            "àm-sî": ["evening", "暗時"]
        }
        self.chapter_1_characters = {
            "泅水": ["siu-tsui", 'to swim', 'swimming'],
            "足": ["tsiok", 'very', 'so'],
            "欲": ["beh", 'to want', 'to be going'],
            "去": ["khi", 'to go'],
            "下晡": ["e-poo", 'this afternoon'],
            "狗": ["kau", 'dog'],
            "嘛": ["ma", 'also', 'too'],
            "熱": ["juah", 'hot', 'hot (weather)'],
            "今仔日": ["kin-a-jit", 'today'],
            "我": ["gua", 'i', 'me'],
            "寒": ["kuann", 'cold', 'cold (weather)'],
            "天": ["thinn", 'day', 'sky', 'heaven'],
            "這馬": ["tsit-ma", 'now'],
            "你": ["li", "di", 'you'],
            "阮": ["guan", 'we', 'us', '(excludes listener)'],
            "的": ["e", '(possesive)', '(gives possession)'],
            "恁": ["lin", 'you (plural)'],
            "早起": ["tsai-khi", 'morning'],
            "暗時": ["am-si", 'evening']
        }
        self.chapter_1_english = {
            'to swim, swimming': ['siu-tsui', '泅水'],
            'very, so': ['tsiok', '足'],
            'to want/to be going': ['beh', '欲'],
            'to go': ['khi', '去'],
            'this afternoon': ['e-poo', '下晡'],
            'dog': ['kau', '狗'],
            'also, too': ['ma', '嘛'],
            'hot': ['juah', '熱'],
            'today': ['kin-a-jit', '今仔日'],
            'I, me': ['gua', '我'],
            'cold': ['kuann', '寒'],
            'day, sky, heaven': ['thinn', '天'],
            'now': ['tsit-ma', '這馬'],
            'you': ['li', 'di', '你'],
            'we, us, our, (excludes listener)': ['guan', '阮'],
            '(possessive)': ['e', '的'],
            'you (plural)': ['lin', '恁'],
            'morning': ['tsai-khi', '早起'],
            'evening': ['am-si', '暗時']
        }

        self.chapter_2_pronounce = {
            "tuà": ["to live", "蹛"],
            "Bí-kok": ["United States", "美國"],
            "tsi̍t ê": ["one", "一个"],
            "āu lé-pài": ["next week", "後禮拜"],
            "ū": ["to have", 'to exist', "有"],
            "phàu-mī": ["instant ramen", "泡麵"],
            "tsē hui-ki": ["to take a plane", "坐飛機"],
            "tsah": ["to bring", "紮"],
            "tsē": ["many", "濟"],
            "pîng-iú": ["friend", "朋友"],
            'hué-tshia/hé-tshia': ['train', '火車'],
            'kong-tshia/bah-suh': ['bus', '公車'],
            'kè-thîng-tshia/kè-tîng-tshia': ['taxi', '計程車']
        }
        self.chapter_2_characters = {
            "有": ["u", 'to have', 'to exist'],
            "一个": ["tsit e", 'one', 'one (unit)'],
            "朋友": ["ping-iu", 'friend'],
            "蹛": ["tua", 'to live', 'to live (in)'],
            "美國": ["Bi-kok", 'united states', 'america'],
            "後禮拜": ["au le-pai", 'next week'],
            "坐飛機": ["tse hui-ki", 'to take a plane'],
            "紮": ["tsah", 'to bring', 'to carry'],
            "濟": ["tse", 'many', 'much', 'plenty'],
            "泡麵": ["phau-mi", 'instant noodles', 'instant ramen'],
            '火車': ['train', 'hué-tshia', 'hé-tshia'],
            '公車': ['kong-tshia', 'bah-suh', 'bus'],
            '計程車': ['ke-thing-tshia', 'ke-ting-tshia', 'taxi']
        }
        self.chapter_2_english = {
            'to live': ['tua', '蹛'],
            'United States': ['bi-kok', '美國'],
            'one (unit)': ['tsit e', '一个'],
            'next week': ['au le-pai', '後禮拜'],
            'to have/to exist': ['u', '有'],
            'instant ramen': ['phau-mi', '泡麵'],
            'to take a plane': ['tse hui-ki', '坐飛機'],
            'to bring': ['tsah', '紮'],
            'many, much, plenty': ['tse', '濟'],
            'friend': ['ping-iu', '朋友'],
            'train': ['火車', 'hué-tshia', 'hé-tshia'],
            'bus': ['kong-tshia', 'bah-suh', '公車'],
            'taxi': ['kè-thîng-tshia', 'kè-tîng-tshia', '計程車']
        }
        
        self.chapter_3_characters = {
            '伊': ['i', 'he', 'she', 'him', 'her'],
            '會曉': ['e-hiau', 'to know how to do'],
            '講': ['kong', 'to speak', 'to tell'],
            '英語': ['ing-gi', 'english', 'english language'],
            '女朋友': ['lu ping-iu', 'girlfriend'],
            '是': ['si', 'to be', 'yes', 'right', 'correct'],
            '英國人': ['ing-kok-lang', 'british', 'british (people)'],
            '定定': ['tiann-tiann', 'often', 'frequently'],
            '寫批': ['sia phue', 'to write a letter'],
            '予': ['hoo', 'to give'],
            '袂': ['be', 'bue', 'cant', 'wont']
        }
        self.chapter_3_pronounce = {
            'i': ['he', 'she', 'him', 'her', '伊'],
            'ē-hiáu': ['to know how to do', '會曉'],
            'kóng': ['to speak', 'to tell', '講'],
            'Ing-gí': ['english', 'english language', '英語'],
            'lú pîng-iú': ['girlfriend', '女朋友'],
            'sī': ['to be', 'yes', 'right', 'correct', '是'],
            'Ing-kok-lâng': ['british', 'british (people)', '英國人'],
            'tiānn-tiānn': ['often', 'frequently', '定定'],
            'siá phue': ['to write a letter', '寫批'],
            'hōo': ['to give', '予'],
            'bē/buē': ['cant', 'wont', '袂'],
        }
        self.chapter_3_english = {
            'he, she, him, her': ['伊', 'i'],
            'to know how to do': ['會曉', 'e-hiau'],
            'to speak, to tell': ['講', 'kong'],
            'english, english language': ['英語', 'ing-gi'],
            'girlfriend': ['女朋友', 'lu ping-iu'],
            'to be, yes, right, correct': ['是', 'si'],
            'british, british (people)': ['英國人', 'ing-kok-lang'],
            'often, frequently': ['定定', 'tiann-tiann'],
            'to write a letter': ['寫批', 'sia phue'],
            'to give': ['予', 'hoo']
        }

        self.chapter_4_characters = {
            '阿媽': ['grandma', 'a-ma'],
            '阿公': ['grandpa', 'a-kong'],
            '佇': ['at', 'in', 'to be at', 'to be in', 'ti'],
            '台南市': ['Tainan City', 'Tai-lam-tshi'],
            '市': ['city', 'tshi'],
            '厝': ['house', 'tshu'],
            '三': ['three', '3', 'sann'],
            '樓': ['floor', 'multi-story building', 'lau'],
            '棟': ['measure word for;', 'buildings', 'tong'],
            '層': ['measure word for;', 'floors', 'stairs', 'tsan'],
            '飼': ['to feed', 'to raise', 'for (animal, child)', 'tshi'],
            '六': ['six', '6', 'lak'],
            '貓仔': ['cat', 'kitty', 'niau-a'],
            '古錐': ['cute', 'adorable', 'koo-tsui']
        }
        self.chapter_4_pronounce = {
            'a-má': 'grandma',
            'a-kong': 'grandpa',
            'tī': ['at', 'in', 'to be at', 'to be in'],
            'Tâi-lâm-tshī': 'Tainan City',
            'tshī': 'city',
            'tshù': 'house',
            'sann': ['three', '3'],
            'lâu': ['floor', 'multi-story building'],
            'tòng': ['measure word for;', 'buildings'],
            'tsàn': ['measure word for;', 'floors', 'stairs'],
            'tshī': ['to feed', 'to raise', 'for (animal, child)'],
            'la̍k': ['six', '6'],
            'niau-á': ['cat', 'kitty'],
            'kóo-tsui': ['cute', 'adorable']
        }
        self.chapter_4_english = {
            'grandma': ['a-ma', '阿媽'],
            'grandpa': ['a-kong', '阿公'],
            'at, in, to be at/in': ['ti', '佇'],
            'Tainan City': ['Tai-lam-tshi', '台南市'],
            'city': ['tshi', '市'],
            'house': ['tshu', '厝'],
            'three': ['sann', '三'],
            'floor, multi-story building': ['lau', '樓'],
            'measure word for buildings': ['tong', '棟'],
            'measure word for floors and stairs': ['tsan', '層'],
            'to feed, to raise, for (animal, child)': ['tshi', '飼'],
            'six': ['lak', '六'],
            'cat, kitty': ['niau-a', '貓仔'],
            'cute, adorable': ['koo-tsui', '古錐']
        }

        self.chapter_5_pronounce = {
            'lán': ['we', 'us', 'our', '咱', '(includes listener)'],
            'lâì-khì': ['be going', 'get going', 'to leave', '來去'],
            'iā-tshī/iā-tshī-á': ['night market', '夜市', '夜市仔'],
            'tshī-tiûnn': ['market', '市場'],
            'lāu-jia̍t/lāu-lia̍t': ['bustling', 'busy', 'crowded', 'lively', '鬧熱'],
            'hó': ['good', '好'],
            'tsia̍h': ['to eat', 'to take', '食'],
            'tsia̍h-pá': ['to be full', '食䬲'],
            'lóo-bah-pn̄g': ['braised pork rice', '滷肉飯'],
            'bah': ['pork', 'meat', '肉'],
            'pn̄g': ['rice', '飯'],
            'thng': ['soup', '湯'],
            'koh': ['and also', 'moreover', 'yet', 'still', 'again', '閣'],
            'lim': ['to drink', '啉'],
            'tsuí': ['water', '水'],
            'tê': ['tea', '茶'],
            'tsiú': ['alcohol', '酒'],
            'lim-tsiú-tsuì': ['to be drunk', '啉酒醉'],
            'pue': ['cup of', 'glass of', 'cup/glass (of)', '杯'],
            'pue-á': ['cup', 'glass', '杯仔'],
            'uánn': ['bowl of', '碗'],
            'kuàn': ['can', 'jar', 'bottle of', '罐'],
            'tsiap': ['juice', '汁'],
            'kué-tsí/kó': ['fruit', '果子'],
            'tsui-kó': ['fruit', '水果'],
            'si-kue': ['watermelon', '西瓜'],
            'liú-ting': ['orange', '柳丁'],
            'ông-lâi': ['pineapple', '王梨'],
            'phông-kó/lìn-gooh': ['apple', '蘋杲'],
            'pua̍t-á/pa̍t-á': ['guava', '菝仔'],
            'kin-tsio/king-tsio': ['banana', '弓蕉'],
            'suāinn-á': ['mango', '檨仔']
        }
        self.chapter_5_characters = {
            '咱': ['we', 'us', 'our', 'lan', 'lán', '(includes listener)'],
            '來去': ['to be', 'get going', 'to leave', 'lai-khi', 'lâì-khì'],
            '夜市/夜市仔': ['night market', 'ia-tshi', 'ia-tshi-a', 'iā-tshī-á'],
            '市場': ['market', 'tshi-tiunn', 'tshī-tiûnn'],
            '鬧熱': ['bustling', 'busy', 'crowded', 'lively', 'lau-jiat', 'lau-liat', 'lāu-lia̍t'],
            '好': ['good', 'ho', 'hó'],
            '食': ['to eat', 'to take', 'tsiah', 'tsia̍h'],
            '食飽': ['to be full', 'tsiah-pa', 'tsia̍h-pá'],
            '滷肉飯': ['braised pork rice', 'loo-bah-png', 'lóo-bah-pn̄g'],
            '肉': ['pork', 'meat', 'bah'],
            '飯': ['rice', 'png', 'pn̄g'],
            '湯': ['soup', 'thng'],
            '閣': ['and also', 'moreover', 'yet', 'still', 'again', 'koh'],
            '啉': ['to drink', 'lim'],
            '水': ['water', 'tsui', 'tsuí'],
            '茶': ['tea', 'te', 'tê'],
            '酒': ['alcohol', 'tsiu', 'tsiú'],
            '啉酒醉': ['to be drunk', 'lim-tsiu-tsui', 'lim-tsiú-tsuì'],
            '杯': ['cup of', 'glass of', 'cup/glass (of)', 'pue'],
            '杯仔': ['cup', 'glass', 'pue-a', 'pue-á'],
            '碗': ['bowl of', 'uann', 'uánn'],
            '罐': ['can', 'jar', 'bottle of', 'kuan', 'kuàn'],
            '汁': ['juice', 'tsiap'],
            '果子': ['fruit', 'kue-tsi', 'ko-tsi',],
            '水果': ['fruit', 'tsui-kue', 'tsui-ko', 'tsui-kó'],
            '西瓜': ['watermelon', 'si-kue'],
            '柳丁': ['orange', 'liu-ting', 'liú-ting'],
            '王梨': ['pineapple', 'ong-lai', 'ông-lâi'],
            '蘋果': ['apple', 'phong-ko', 'lin-gooh', 'phông-kó/lìn-gooh'],
            '菝仔': ['guava', 'puat-a', 'pat-a', 'pua̍t-á/pa̍t-á'],
            '弓蕉': ['banana', 'kin-tsio', 'king-tsio'],
            '檨仔': ['mango', 'suainn-a', 'suāinn-á']
        }
        self.chapter_5_english = {
            'we, us, our, (includes listener)': ['咱', 'lan'],
            'to be, get going, to leave': ['來去', 'lai-khi'],
            'night market': ['夜市', '夜市仔', 'ia-tshi', 'ia-tshi-a'],
            'market': ['市場', 'tshi-tiunn'],
            'bustling, busy, crowded, lively': ['鬧熱', 'lau-jiat', 'lau-liat'],
            'good': ['好', 'ho'],
            'to eat, to take': ['食', 'tsiah'],
            'to be full': ['食飽', 'tsiah-pa'],
            'braised pork rice': ['滷肉飯', 'loo-bah-png'],
            'pork, meat': ['肉', 'bah'],
            'rice': ['飯', 'png'],
            'soup': ['湯', 'thng'],
            'and also, moreover, yet, still, again': ['閣', 'koh'],
            'to drink': ['啉', 'lim'],
            'water': ['水', 'tsui'],
            'tea': ['茶', 'te'],
            'alcohol': ['酒', 'tsiu'],
            'to be drunk': ['啉酒醉', 'lim-tsiu-tsui'],
            'cup of, glass of, cup/glass (of)': ['杯', 'pue'],
            'cup, glass': ['杯仔', 'pue-a'],
            'bowl of': ['碗', 'uann'],
            'can, jar, bottle of': ['罐', 'kuan'],
            'juice': ['汁', 'tsiap'],
            'fruit': ['果子', 'kue-tsi', 'ko-tsi', '水果', 'tsui-kue', 'tsui-ko'],
            'watermelon': ['西瓜', 'si-kue'],
            'orange': ['柳丁', 'liu-ting'],
            'pineapple': ['王梨', 'ong-lai'],
            'apple': ['蘋果', 'phong-ko', 'lin-gooh'],
            'guava': ['菝仔', 'puat-a', 'pat-a'],
            'banana': ['弓蕉', 'kin-tsio', 'king-tsio'],
            'mango': ['檨仔', 'suainn-a']
        }

        self.chapter_6_pronounce = {
            'ū-îng': ['to be free', 'available', 'to have time', '有閒'],
            'pài-it': ['Monday', '拜一'],
            'pài-jī': ['Tuesday', '拜二'],
            'pài-sann': ['Wednesday', '拜三'],
            'pài-sì': ['Thursday', '拜四'],
            'pài-gōo': ['Friday', '拜五'],
            'pài-la̍k': ['Saturday', '拜六'],
            'le-pài': ['Sunday', 'week', 'church service', '禮拜'],
            'le-pài-ji̍t': ['Sunday', '禮拜日'],
            'tsi̍t le-pài': ['one week', '一禮拜'],
            'bô': ['to not have', 'to not exist', 'not', 'no', '無'],
            'bô?': ['(question marker)', 'u+noun/verb/adj--bo?', '無?'],
            'khuànn tiān-iánn': ['to watch a movie', '看電影'],
            'tshut': ['measure word for movies', 'dramas', 'plays', '齣'],
            'tiān-sī': ['television', '電視'],
            'hó--bô?': ['how about?', 'is it ok?', 'sounds good?', '好無?'],
            'pháinn-sè': ['excuse me', 'sorry', 'to feel embarrassed', '歹勢'],
            'sit-lé': ['sorry', 'my apologies', '失禮'],
            'bô sóng-khuài': ['feeling unwell', 'sick', '無爽快'],
            'lltsué-kīn/tsué-kūn': ['lately', 'recently', '最近'],
            'i-sing': ['doctor', 'physician', 'surgeon', '醫生'],
            'pēnn-īnn': ['hospital', '病院'],
            'hit kang': ['that day', '彼工'],
            'ê': ['(one)', '个'],
            'tsit': ['this', 'this+noun', 'this+measure word+noun', '這'],
        }
        self.chapter_6_characters = {
            '有閒': ['to be free', 'available', 'to have time', 'ū-îng', 'u-ing'],
            '拜一': ['Monday', 'pài-it', 'pai-it'],
            '拜二': ['Tuesday', 'pài-jī', 'pai-ji'],
            '拜三': ['Wednesday', 'pài-sann', 'pai-sann'],
            '拜四': ['Thursday', 'pài-sì', 'pai-si'],
            '拜五': ['Friday', 'pài-gōo', 'pai-goo'],
            '拜六': ['Saturday', 'pài-la̍k', 'pai-lak'],
            '禮拜': ['Sunday', 'week', 'church service', 'le-pài', 'le-pai'],
            '禮拜日': ['Sunday', 'le-pài-ji̍t', 'le-pai-jit'],
            '一禮拜': ['one week', 'tsi̍t le-pài', 'tsit le-pai'],
            '無': ['to not have', 'to not exist', 'not', 'no', 'bô', 'bo'],
            '無?': ['(question marker)', 'u+noun/verb/adj--bo?', 'bô?', 'bo?'],
            '看電影': ['to watch a movie', 'khuànn tiān-iánn', 'khuann tian-iann'],
            '齣': ['measure word for movies', 'dramas', 'plays', 'tshut'],
            '電視': ['television', 'tiān-sī', 'tian-si'],
            '好無?': ['how about?', 'is it ok?', 'sounds good?', 'hó--bô?', 'ho--bo?'],
            '歹勢': ['excuse me', 'sorry', 'to feel embarrassed', 'pháinn-sè', 'phainn-se'],
            '失禮': ['sorry', 'my apologies', 'sit-lé', 'sit-le'],
            '無爽快': ['feeling unwell', 'sick', 'bô sóng-khuài', 'bo song-khuai'],
            '最近': ['lately', 'recently', 'tsué-kīn/tsué-kūn', 'tsue-kin', 'tsue-kun'],
            '醫生': ['doctor', 'physician', 'surgeon', 'i-sing'],
            '病院': ['hospital', 'pēnn-īnn', 'penn-inn'],
            '彼工': ['that day', 'hit kang'],
            '个': ['(one)', 'ê', 'e'],
            '這': ['this', 'this+noun', 'this+measure word+noun', 'tsit']
        }
        self.chapter_6_english = {
            'to be free, available, to have time': ['ū-îng', '有閒'],
            'Monday': ['pài-it', '拜一'],
            'Tuesday': ['pài-jī', '拜二'],
            'Wednesday': ['pài-sann', '拜三'],
            'Thursday': ['pài-sì', '拜四'],
            'Friday': ['pài-gōo', '拜五'],
            'Saturday': ['pài-la̍k', '拜六'],
            'Sunday, week, church service': ['le-pài', '禮拜'],
            'Sunday': ['le-pài-ji̍t', '禮拜日'],
            'one week': ['tsi̍t le-pài', '一禮拜'],
            'to not have, to not exist, not, no': ['bô', '無'],
            '(question marker)': ['u+noun/verb/adj--bo?', 'bô?', '無?'],
            'to watch a movie': ['khuànn tiān-iánn', '看電影'],
            'measure word for movies, dramas, plays': ['tshut', '齣'],
            'television': ['tiān-sī', '電視'],
            'how about?, is it ok?, sounds good?': ['hó--bô?', '好無?'],
            'excuse me, sorry, to feel embarrassed': ['pháinn-sè', '歹勢'],
            'sorry, my apologies': ['sit-lé', '失禮'],
            'feeling unwell, sick': ['bô sóng-khuài', '無爽快'],
            'lately, recently': ['tsué-kīn/tsué-kūn', '最近'],
            'doctor, physician, surgeon': ['i-sing', '醫生'],
            'hospital': ['pēnn-īnn', '病院'],
            'that day': ['hit kang', '彼工'],
            '(one)': ['ê', '个'],
            'this, this+noun, this+measure word+noun': ['tsit', '這']
        }
        self.chapter_7_pronounce = {
            "sió-tsiá": ['lady', 'ms.', '小姐'],
            "sian-sinn/sin-senn": ['gentleman', 'sir', 'mr.', 'teacher', 'doctor', '先生'],
            "thài-thài": ['madam', 'mrs.', 'wife', '太太'],
            "siàu-liân-lâng": ['young man', '少年人'],
            "koo-niû": ['girl', 'lady' '(unmarried)', 'miss', 'nun/sister', '姑娘'],
            "lāi-té/lāi-tué": ['inside', '(noun/adv/prep)', '内底'],
            "guā-kháu": ['outside', '(noun/adv/prep)', '外口'],
            "siòng-phìnn": ['photo', 'picture', '相片'],
            "tiunn": ['measure word for paper', 'papers/letters/photos', '張'],
            "hip-siòng/hip-siōng": ['to take a picture', '翕相'],
            "hip-siòng-ki": ['camera', '翕相機'],
            "suí": ['pretty', 'beautiful', '媠'],
            "bái": ['ugly', 'bad', 'awful', '䆀'],
            "tshiánn-mn̄g": ['may i ask', 'could you please tell me', '(polite)', '請問'],
            "me-me": ['little sister', 'younger sister', '妺妺'],
            "ti-ti": ['little brother', 'younger brother', '弟弟'],
            "ia̍h-sī/ah-sī": ['or', '抑是'],
            "tse-tse": ['older sister', 'big sister', '姊姊'],
            "ko-ko": ['older brother', 'big brother', '哥哥'],
            "ma-ma": ['mother', '媽媽'],
            "pa-pa": ['father', '爸爸'],
            "--lah": ['(slight disagreement)', '(impatience)', '(persuasion)', '啦']
        }
        self.chapter_7_characters = {
            "小姐": ['sió-tsiá', 'sio-tsia', 'lady', 'ms.'],
            "先生": ['sian-sinn', 'sin-senn', 'gentleman', 'sir', 'mr.', 'teacher', 'doctor'],
            "太太": ['thài-thài', 'thai-thai', 'madam', 'mrs.', 'wife'],
            "少年人": ['siàu-liân-lâng', 'siau-lian-lang', 'young man'],
            "姑娘": ['koo-niû', 'koo-niu', 'girl', 'lady (unmarried)', 'miss', 'nun/sister'],
            "内底": ['lāi-té/lāi-tué', 'lai-te', 'lai-tue', 'inside', '(noun/adv/prep)'],
            "外口": ['guā-kháu', 'gua-khau', 'outside (noun/adv/prep)'],
            "相片": ['siòng-phìnn', 'siong-phinn', 'photo', 'picture'],
            "張": ['tiunn', 'measure word for paper', 'papers/letters/photos'],
            "翕相機": ['hip-siòng-ki', 'hip-siong-ki', 'camera'],
            "媠": ['suí', 'sui', 'pretty', 'beautiful'],
            "䆀": ['bái', 'bai', 'ugly', 'bad', 'awful'],
            "請問": ['tshiánn-mn̄g', 'tshiann-mng', 'may I ask', 'could you please tell me', '(polite)'],
            "妺妺": ['me-me', 'little sister', 'younger sister'],
            "弟弟": ['ti-ti', 'little brother', 'younger brother'],
            "抑是": ['ia̍h-sī/ah-sī', 'iah-si', 'ah-si', 'or'],
            "姊姊": ['tse-tse', 'older sister', 'big sister'],
            "哥哥": ['ko-ko', 'older brother', 'big brother'],
            "媽媽": ['ma-ma', 'mother'],
            "爸爸": ['pa-pa', 'father'],
            "啦": ['--lah', 'lah', '(slight disagreement)', '(impatience)', '(persuasion)']
        }
        self.chapter_7_english = {
            "lady/ms.": ['小姐', 'sió-tsiá', 'sio-tsia'],
            "gentleman/sir/mr./teacher/doctor": ['先生', 'sian-sinn', 'sin-senn'],
            "madam/mrs./wife": ['太太', 'thài-thài', 'thai-thai'],
            "young man": ['少年人', 'siàu-liân-lâng', 'siau-lian-lang'],
            "girl/lady (unmarried)/miss/nun/sister": ['姑娘', 'koo-niû', 'koo-niu'],
            "inside (noun/adv/prep)": ['内底', 'lāi-té/lāi-tué', 'lai-te', 'lai-tue'],
            "outside (noun/adv/prep)": ['外口', 'guā-kháu', 'gua-khau'],
            "photo/picture": ['相片', 'siòng-phìnn', 'siong-phinn'],
            "measure word for paper/papers/letters/photos": ['張', 'tiunn'],
            "camera": ['翕相機', 'hip-siòng-ki', 'hip-siong-ki'],
            "pretty/beautiful": ['媠', 'suí', 'sui'],
            "ugly/bad/awful": ['䆀', 'bái', 'bai'],
            "may I ask/could you please tell me/(polite)": ['請問', 'tshiánn-mn̄g', 'tshiann-mng'],
            "little sister/younger sister": ['妺妺', 'me-me'],
            "little brother/younger brother": ['弟弟', 'ti-ti'],
            "or": ['抑是', 'ia̍h-sī/ah-sī', 'iah-si', 'ah-si'],
            "older sister/big sister": ['姊姊', 'tse-tse'],
            "older brother/big brother": ['哥哥', 'ko-ko'],
            "mother": ['媽媽', 'ma-ma'],
            "father": ['爸爸', 'pa-pa'],
            "(slight disagreement)/(impatience)/(persuasion)": ['啦', '--lah', 'lah']
        }
        self.chapter_8_pronounce = {
            'pah-huè kong-si': ['百貨公司', 'department store'],
            'tiàm': ['店', 'shop', 'store'],
            'tsa-hng': ['昨昏', 'yesterday'],
            'miâ-á-tsài': ['明仔載', 'tomorrow'],
            'bé/bué': ['買', 'to buy', 'to purchase'],
            'Sìng-tàn-tsiat': ['聖誕節', 'Christmas'],
            'Kám-un-tsiat': ['感恩節', 'Thanksgiving'],
            'Bān-sìng-tsiat': ['萬聖節', 'Halloween'],
            'Tsîng-jîn-tsiat': ['情人節', "Valentine's Day"],
            'phòng-se-sann': ['膨紗衫', 'sweater', 'knitted', 'garment'],
            'niá': ['領', 'measure word for clothes'],
            'tsı̍t niá sann': ['一領衫', 'a piece of clothing'],
            'tsı̍t niá khòo': ['一領褲', 'a pair of pants'],
            'tsı̍t niá kûn': ['一領裙', 'a skirt'],
            'sann-á-khòo': ['衫仔褲', 'clothes'],
            'sàng': ['送', 'to give', '(as a gift)', 'to send', 'to see somebody off'],
            'bóo': ['某', 'wife'],
            'ang': ['翁', 'husband'],
            'tuā': ['大', 'big', 'large', 'to grow up'],
            'ka-kī': ['家己', 'oneself', "one's own"],
            'tshīng': ['穿', 'to wear', 'to put on']
        }
        self.chapter_8_characters = {
            '百貨公司': ['department store', 'pah-huè kong-si', 'pah-hue kong-si'],
            '店': ['shop', 'store', 'tiàm', 'tiam'],
            '昨昏': ['yesterday', 'tsa-hng', 'tsa-hng'],
            '明仔載': ['tomorrow', 'miâ-á-tsài', 'mia-a-tsai'],
            '買': ['to buy', 'to purchase', 'bé/bué', 'be', 'bue'],
            '聖誕節': ['Christmas', 'Sìng-tàn-tsiat', 'Sing-tan-tsiat'],
            '感恩節': ['Thanksgiving', 'Kám-un-tsiat', 'Kam-un-tsiat'],
            '萬聖節': ['Halloween', 'Bān-sìng-tsiat', 'Ban-sing-tsiat'],
            '情人節': ["Valentine's Day", 'Tsîng-jîn-tsiat', 'Tsing-jin-tsiat'],
            '膨紗衫': ['sweater', 'knitted', 'garment', 'phòng-se-sann', 'phong-se-sann'],
            '領': ['measure word for clothes', 'niá', 'nia'],
            '一領衫': ['a piece of clothing', 'tsı̍t niá sann', 'tsit nia sann'],
            '一領褲': ['a pair of pants', 'tsı̍t niá khòo', 'tsit nia khoo'],
            '一領裙': ['a skirt', 'tsı̍t niá kûn', 'tsit nia kun'],
            '衫仔褲': ['clothes', 'sann-á-khòo', 'sann-a-khoo'],
            '送': ['to give', '(as a gift)', 'to send', 'to see somebody off', 'sàng', 'sang'],
            '某': ['wife', 'bóo', 'boo'],
            '翁': ['husband', 'ang', 'ang'],
            '大': ['big', 'large', 'to grow up', 'tuā', 'tua'],
            '家己': ['oneself', "one's own", 'ka-kī', 'ka-ki'],
            '穿': ['to wear', 'to put on', 'tshīng', 'tshing']
        }
        self.chapter_8_english = {
            'department store': ['百貨公司', 'pah-huè kong-si', 'pah-hue kong-si'],
            'shop/store': ['店', 'tiàm', 'tiam'],
            'yesterday': ['昨昏', 'tsa-hng', 'tsa-hng'],
            'tomorrow': ['明仔載', 'miâ-á-tsài', 'mia-a-tsai'],
            'to buy/to purchase': ['買', 'bé/bué', 'be', 'bue'],
            'Christmas': ['聖誕節', 'Sìng-tàn-tsiat', 'Sing-tan-tsiat'],
            'Thanksgiving': ['感恩節', 'Kám-un-tsiat', 'Kam-un-tsiat'],
            'Halloween': ['萬聖節', 'Bān-sìng-tsiat', 'Ban-sing-tsiat'],
            "Valentine's Day": ['情人節', 'Tsîng-jîn-tsiat', 'Tsing-jin-tsiat'],
            'sweater/knitted/garment': ['膨紗衫', 'phòng-se-sann', 'phong-se-sann'],
            'measure word for clothes': ['領', 'niá', 'nia'],
            'a piece of clothing': ['一領衫', 'tsı̍t niá sann', 'tsit nia sann'],
            'a pair of pants': ['一領褲', 'tsı̍t niá khòo', 'tsit nia khoo'],
            'a skirt': ['一領裙', 'tsı̍t niá kûn', 'tsit nia kun'],
            'clothes': ['衫仔褲', 'sann-á-khòo', 'sann-a-khoo'],
            'to give/(as a gift)/to send/to see somebody off': ['送', 'sàng', 'sang'],
            'wife': ['某', 'bóo', 'boo'],
            'husband': ['翁', 'ang', 'ang'],
            'big/large/to grow up': ['大', 'tuā', 'tua'],
            'oneself/one\'s own': ['家己', 'ka-kī', 'ka-ki'],
            'to wear/to put on': ['穿', 'tshīng', 'tshing']
        }






        self.all_pronounce_dict = {}
        self.all_pronounce_list = [
            self.chapter_1_pronounce, 
            self.chapter_2_pronounce, 
            self.chapter_3_pronounce, 
            self.chapter_4_pronounce, 
            self.chapter_5_pronounce,
            self.chapter_6_pronounce,
            self.chapter_7_pronounce, 
            self.numbers_pronounce
        ]
        for i in self.all_pronounce_list:
            self.all_pronounce_dict.update(i)

        self.all_character_dict = {}
        self.all_character_list = [
            self.chapter_1_characters, 
            self.chapter_2_characters, 
            self.chapter_3_characters, 
            self.chapter_4_characters, 
            self.chapter_5_characters,
            self.chapter_6_characters,
            self.chapter_7_characters,
            self.numbers_characters
        ]
        for i in self.all_character_list:
            self.all_character_dict.update(i)

        self.all_english_dict = {}
        self.all_english_list = [
            self.chapter_1_english, 
            self.chapter_2_english, 
            self.chapter_3_english, 
            self.chapter_4_english, 
            self.chapter_5_english, 
            self.chapter_6_english,
            self.chapter_7_english,
            self.numbers_english
        ]
        for i in self.all_english_list:
            self.all_english_dict.update(i)


    def correct(self, vocab, word):
        # print('是'+'\n')
        del vocab[word]
        # time.sleep(0.5)
    
        return None
    
    def quiz(self, vocab):
        self.quit_state = False

        vocab_copy = copy.deepcopy(vocab)

        out_of = len(vocab_copy)
        remaning = len(vocab_copy)

        while len(vocab_copy) > 0:
            word = random.choice(list(vocab_copy.keys()))

            meanings = vocab_copy[word] 
            self.match_answer = meanings

            top = NewWindow(self, word, meanings, False, out_of, remaning)
            top.wait_window()

            if top.quit_state == True:
                break

            ans = top.get_answer()

            if isinstance(meanings, list):
                meanings = [i.lower()for i in meanings]
                if ans.lower() in meanings:
                    remaning -= 1
                    self.correct(vocab_copy, word)
            else:
                if ans.lower() == meanings.lower():
                    remaning -= 1
                    self.correct(vocab_copy, word)

    def start_quiz_tones(self):
        self.quiz(self.tones_diacritics)

    def start_quiz_all_pronounce(self):
        self.quiz(self.all_pronounce_dict)
    def start_quiz_all_characters(self):
        self.quiz(self.all_character_dict)
    def start_quiz_all_english(self):
        self.quiz(self.all_english_dict)    

    def start_quiz_numbers_pronounce(self):
        self.quiz(self.numbers_pronounce)
    def start_quiz_numbers_characters(self):
        self.quiz(self.numbers_characters)
    def start_quiz_numbers_english(self):
        self.quiz(self.numbers_english)    
        
    def start_quiz_chapter_1_pronounce(self):
        self.quiz(self.chapter_1_pronounce)
    def start_quiz_chapter_1_characters(self):
        self.quiz(self.chapter_1_characters)
    def start_quiz_chapter_1_english(self):
        self.quiz(self.chapter_1_english)
    
    def start_quiz_chapter_2_pronounce(self):
        self.quiz(self.chapter_2_pronounce)
    def start_quiz_chapter_2_characters(self):
        self.quiz(self.chapter_2_characters)
    def start_quiz_chapter_2_english(self):
        self.quiz(self.chapter_2_english)

    def start_quiz_chapter_3_pronounce(self):
        self.quiz(self.chapter_3_pronounce)
    def start_quiz_chapter_3_characters(self):
        self.quiz(self.chapter_3_characters)
    def start_quiz_chapter_3_english(self):
        self.quiz(self.chapter_3_english)

    def start_quiz_chapter_4_pronounce(self):
        self.quiz(self.chapter_4_pronounce)
    def start_quiz_chapter_4_characters(self):
        self.quiz(self.chapter_4_characters)
    def start_quiz_chapter_4_english(self):
        self.quiz(self.chapter_4_english)

    def start_quiz_chapter_5_pronounce(self):
        self.quiz(self.chapter_5_pronounce)
    def start_quiz_chapter_5_characters(self):
        self.quiz(self.chapter_5_characters)
    def start_quiz_chapter_5_english(self):
        self.quiz(self.chapter_5_english)

    def start_quiz_chapter_6_pronounce(self):
        self.quiz(self.chapter_6_pronounce)
    def start_quiz_chapter_6_characters(self):
        self.quiz(self.chapter_6_characters)
    def start_quiz_chapter_6_english(self):
        self.quiz(self.chapter_6_english)

    def start_quiz_chapter_7_pronounce(self):
        self.quiz(self.chapter_7_pronounce)
    def start_quiz_chapter_7_characters(self):
        self.quiz(self.chapter_7_characters)
    def start_quiz_chapter_7_english(self):
        self.quiz(self.chapter_7_english)
    
    def start_quiz_chapter_8_pronounce(self):
        self.quiz(self.chapter_8_pronounce)
    def start_quiz_chapter_8_characters(self):
        self.quiz(self.chapter_8_characters)
    def start_quiz_chapter_8_english(self):
        self.quiz(self.chapter_8_english)

# MAKE ANSWERS SMALLER
# MAKE THE PRONUNCIATION KNOWN???
class NewWindow(customtkinter.CTkToplevel):
    # Top window 
    def __init__(self, master, word, match_answer, quit_state, out_of, remaning):
        super().__init__(master)
        customtkinter.set_appearance_mode("dark")
        self.geometry(CenterWindow.CenterWindowToDisplay(self, 800, 350, self._get_window_scaling()))
        self.title("")
        # self.wm_attributes("-topmost", True)
        self.minsize(650, 350)
        self.maxsize(900, 350)

        self.answer = ""
        self.match_answer = match_answer
        self.quit_state = quit_state
        self.out_of = out_of
        self.remaining = remaning
        
        self.question_label = customtkinter.CTkLabel(self, text=word,
                                                font=("Arial", 35) 
                                                )
        self.question_label.place(relx=0.5, rely=0.2, anchor="center")
        
        self.answer_entry = customtkinter.CTkEntry(self,
                                       placeholder_text="Answer",
                                       width=200, height=40,
                                       font=("Arial", 20)
                                       )
        self.answer_entry.place(relx=0.5, rely=0.4, anchor="center")
        self.after(100, self.set_focus)

        self.feedback_label = customtkinter.CTkLabel(self, text="",
                                                font=("Arial", 20) 
                                                )
        self.feedback_label.place(relx=0.5, rely=0.6, anchor="center")
        # self.feedback_label.configure(text="CHANGED")
        
        self.submit_button = customtkinter.CTkButton(self, 
                                                text="→", 
                                                width=200, height=7, font=("Arial Bold", 20),
                                                command=self.submit_answer
                                                )
        self.submit_button.place(relx=0.5, rely=0.51, anchor="center")
        self.bind('<Return>', self.submit_on_enter_key)

        self.quit_button = customtkinter.CTkButton(self,
                                                   text="Exit",
                                                   width=50, height=10, font=("Arial Bold", 15),
                                                   fg_color="#FE3B3B", hover_color="#8D2828",
                                                   command=self.quit_vocab)
        self.quit_button.place(relx=0.9, rely=0.9, anchor="center")

        self.out_of_label = customtkinter.CTkLabel(self, text=f'{self.remaining }/{self.out_of}',
                                                font=("Arial", 20) 
                                                )
        self.out_of_label.place(relx=0.1, rely=0.9, anchor="center")

        self.next_button = customtkinter.CTkButton(self,
                                                text="Next", 
                                                width=20, height=10, font=("Arial Bold", 15),
                                                command=self.destroy)

    def submit_answer(self):
        self.answer = self.answer_entry.get()
        self.answer_entry.configure(state='disabled')
        self.submit_button.place_forget()
        self.reveal_feedback()

    def set_focus(self):
        self.answer_entry.focus_set()

    def submit_on_enter_key(self, event):
        self.submit_button.invoke()

    def next_on_enter_key(self, event):
        self.next_button.invoke()

    def get_answer(self):
        return self.answer
    
    def get_length(self):
        pass
    
    def quit_vocab(self):
        self.quit_state = True
        self.destroy()
        return self.quit_state
        
    def reveal_feedback(self):
        symbol = ''
        text_color = ''
        if isinstance(self.match_answer, list):
            self.match_answer = [i.lower() for i in self.match_answer]
            if self.answer.lower() in self.match_answer:
                symbol = '是'
                text_color = 'green'
                self.after(1000, self.destroy)
            else: 
                symbol = '不對'
                text_color = 'red'  
                self.next_button.place(relx=0.5, rely=0.8, anchor="center")
        else:
            if self.answer.lower() == self.match_answer.lower():
                symbol = '是'      
                text_color = 'green'      
                self.after(1000, self.destroy)
            else:
                symbol = '不對'
                text_color = 'red'
                self.next_button.place(relx=0.5, rely=0.8, anchor="center")
        self.question_label.configure(text_color=text_color)
        self.feedback_label.configure(text=f"{symbol}\n{self.match_answer}", 
                                      font=("Arial", 26))

class CenterWindow():

    def CenterWindowToDisplay(Screen: customtkinter.CTk, width: int, height: int, scale_factor: float = 1.0):
        """Centers the window to the main display/monitor"""
        screen_width = Screen.winfo_screenwidth()
        screen_height = Screen.winfo_screenheight()
        x = int(((screen_width/2) - (width/2)) * scale_factor)
        y = int(((screen_height/2) - (height/1.5)) * scale_factor)
        return f"{width}x{height}+{x}+{y}"

if __name__ == '__main__':
    
    main_window = Vocabulary()
    main_window.mainloop()
    
    # main_window.mainloop()
