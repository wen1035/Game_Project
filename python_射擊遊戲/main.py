# sprite
import pygame
import random
import os

FPS = 60
WIDTH = 500
HEIGHT = 600

BLACK =(0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)


# 遊戲初始化 and 創建視窗-----------------------------------------------------------------
pygame.init() # pygame裡的函式全初始化
pygame.mixer.init()#音效初始化
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # 視窗大小
pygame.display.set_caption("太空生存戰") # 頁面名稱

clock = pygame.time.Clock() # 對時間

# 載入圖片
# convert是轉換成pygame比較容易讀取的格式
background_img = pygame.image.load(os.path.join("img/img","background.png")).convert()
bullet_img = pygame.image.load(os.path.join("img/img","bullet.png")).convert()
player_img = pygame.image.load(os.path.join("img/img","player.png")).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
pygame.display.set_icon(player_mini_img) # 頁面圖示
#rock_img = pygame.image.load(os.path.join("img/img","rock.png")).convert()
rock_imgs = []
for i in range(7):
    rock_imgs.append(pygame.image.load(os.path.join("img/img",f"rock{i}.png")).convert())
expl_anim_boo = {}
expl_anim_boo['big'] = []
expl_anim_boo['little'] = []
expl_anim_boo['player'] = []
for i in range(9):
    expl_img = pygame.image.load(os.path.join("img/img",f"expl{i}.png")).convert()
    expl_img.set_colorkey(BLACK)
    expl_anim_boo['big'].append(pygame.transform.scale(expl_img, (75,75)))
    expl_anim_boo['little'].append(pygame.transform.scale(expl_img, (30,30)))
    player_expl_img = pygame.image.load(os.path.join("img/img",f"player_expl{i}.png")).convert()
    player_expl_img.set_colorkey(BLACK)
    expl_anim_boo['player'].append(player_expl_img)
    
power_imgs ={}
power_imgs['shield'] = pygame.image.load(os.path.join("img/img", "shield.png")).convert()
power_imgs['gun'] = pygame.image.load(os.path.join("img/img", "gun.png")).convert()



# 載入音效
shoot_sound = pygame.mixer.Sound(os.path.join("sound/sound","shoot.wav"))
die_sound = pygame.mixer.Sound(os.path.join("sound/sound","rumble.ogg"))
shield_sound = pygame.mixer.Sound(os.path.join("sound/sound","pow0.wav"))
gun_sound = pygame.mixer.Sound(os.path.join("sound/sound","pow1.wav"))

exls_sounds = [
    pygame.mixer.Sound(os.path.join("sound/sound","expl0.wav")),
    pygame.mixer.Sound(os.path.join("sound/sound","expl1.wav"))


]
pygame.mixer.music.load(os.path.join("sound/sound", "background_3.mp3"))
pygame.mixer.music.set_volume(0.1)#背景聲音大小，數字範圍0到1 


font_name = os.path.join("font.ttf")#載入字體
def draw_text(surf, text, size ,x ,y):
    # 寫在什麼平面上，文字，文字大小，座標       
    font = pygame.font.Font(font_name, size)#文字物件
    text_surface = font.render(text, True, WHITE)#1.要渲染的文字物件，2.True是代表讓字滑順，3.顏色
    text_rect = text_surface.get_rect()#文字定位
    text_rect.centerx = x
    text_rect.top = y
    #畫出來blit，1.要畫的東西，2.位子
    surf.blit(text_surface, text_rect)

def new_rock():
    r = Rock()
    all_sprites.add(r)
    rocks.add(r)

def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (hp/100)*BAR_LENGTH# 生命條填多少顏色
    outline_rect =pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)# 矩形
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)#裡面的顏色
    pygame.draw.rect(surf, WHITE, outline_rect, 2)#外框，2是幾像素

def draw_life(surf, life, img, x, y):
    for i in range(life):
        img_rect = img.get_rect()
        img_rect.x = x + 30*i
        img_rect.y = y
        surf.blit(img, img_rect)


def draw_init():
    screen.blit(background_img, (0,0)  )
    draw_text(screen, '太空生存戰', 64, WIDTH/2, HEIGHT/4)
    draw_text(screen, '左右鍵移動飛船，空白鍵發射子彈', 22, WIDTH/2, HEIGHT/2)
    draw_text(screen, '按任意鍵開始', 18, WIDTH/2, HEIGHT*3/4)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)#1秒更新幾次畫面 ex. clock.tick(10) #1秒只能執行10次
        # 取得輸入----------------------------------------------------------------------------
        for event in pygame.event.get():#會回傳所有事件，會回傳列表
            if event.type == pygame.QUIT:  #點到關閉
                pygame.quit()
                return True
            elif event.type == pygame.KEYUP:
                waiting = False
                return False



class Player(pygame.sprite.Sprite): # Player繼承pygame.sprite.Sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # 一定要寫Sprite的初始函式
        # self.image = pygame.Surface((50, 40)) #圖片
        # self.image.fill(GREEN)

        self.image = pygame.transform.scale(player_img, (50,38) ) #圖片,調整大小
        self.image.set_colorkey(BLACK)#把黑色變透明
       
        self.rect = self.image.get_rect() #定位這張圖片，給他一個框框
        self.radius = 20
        #pygame.draw.circle(self.image, RED, self.rect.center,self.radius)
        self.rect.centerx = WIDTH / 2 # 圖片x座標跑到正中央
        self.rect.centery = HEIGHT - 40
        self.speedx = 8
        self.health = 100
        self.life = 3
        self.hidden = False
        self.hid_time = 0
        self.gun = 1
        self.gun_time = 0
    
    def update(self):
        if self.gun > 1 and pygame.time.get_ticks() -self.gun_time > 5000:# 5秒
            self.gun -=1
            self.gun_time = pygame.time.get_ticks()


        # pygame.time.get_ticks()更新時當下的時間
        if self.hidden and pygame.time.get_ticks() - self.hid_time > 1000: 
            self.hidden = False
            self.rect.centerx = WIDTH / 2 # 圖片x座標跑到正中央
            self.rect.centery = HEIGHT - 40

        #判斷有沒有被按按鍵
        key_pressed = pygame.key.get_pressed()#回傳布林值
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left  = 0
    
    def shoot(self):
        if not(self.hidden):
            if self.gun == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            elif self.gun >=2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()

    
    def hide(self):
        self.hidden = True
        self.hid_time = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT+500)
    
    def guns(self):
        self.gun += 1
        self.gun_time = pygame.time.get_ticks()

        


class Rock(pygame.sprite.Sprite): # Rock繼承pygame.sprite.Sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # 一定要寫Sprite的初始函式
        #self.image = pygame.Surface((30, 40)) #圖片
        #self.image.fill(RED)
        self.image_ori = random.choice(rock_imgs)
        self.image_ori.set_colorkey(BLACK)#把黑色變透明
        self.image = self.image_ori.copy()

        self.rect = self.image.get_rect() #定位這張圖片，給他一個框框
        self.radius = int(self.rect.width *0.85  / 2)
        #pygame.draw.circle(self.image, RED, self.rect.center,self.radius)
        
        self.rect.x = random.randrange(0, WIDTH-self.rect.width)
        self.rect.y = random.randrange(-180, -100)
        self.speedy = random.randrange(2, 10)
        self.speedx = random.randrange(-3, 3)
        self.total_degree = 0
        self.rot_degree = random.randrange(-3, 3)
    
    def rotate(self):
        self.total_degree += self.rot_degree
        self.total_degree =self.total_degree % 360
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:#石頭超過視窗
            self.rect.x = random.randrange(0, WIDTH-self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)

class Bullet(pygame.sprite.Sprite): # Bullet繼承pygame.sprite.Sprite
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self) # 一定要寫Sprite的初始函式
        #self.image = pygame.Surface((10, 20)) #圖片
        #self.image.fill(YELLOW)
        self.image =bullet_img
        self.image.set_colorkey(BLACK)#把黑色變透明
        self.rect = self.image.get_rect() #定位這張圖片，給他一個框框
        
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    
    def update(self):
        self.rect.y += self.speedy

        if self.rect.bottom < 0:#石頭超過視窗
            self.kill()


class Explosion(pygame.sprite.Sprite): # Bullet繼承pygame.sprite.Sprite
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self) # 一定要寫Sprite的初始函式
        self.size =size # 存目前是大爆炸還是小
        self.image = expl_anim_boo[self.size][0]
        self.rect = self.image.get_rect() #定位這張圖片，給他一個框框
        self.rect.center = center
        self.frame = 0 # 更新到第幾張圖片
        self.last_update = pygame.time.get_ticks()# 初始化到現在的毫秒數
        self.frame_rate = 50 #計算時間
    
    def update(self):
        now =pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(expl_anim_boo[self.size]):
                self.kill()
            else:
                self.image =expl_anim_boo[self.size][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center

    

class Power(pygame.sprite.Sprite): # Bullet繼承pygame.sprite.Sprite
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self) # 一定要寫Sprite的初始函式
        self.type =random.choice(['shield','gun'])
        self.image =power_imgs[self.type]
        self.image.set_colorkey(BLACK)#把黑色變透明
        self.rect = self.image.get_rect() #定位這張圖片，給他一個框框
        self.rect.center = center
        self.speedy = 3

    
    def update(self):
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT:#石頭超過視窗
            self.kill()




pygame.mixer.music.play(-1)#音樂重複播幾次，-1是無限



#遊戲迴圈--------------------------------------------------------------------------------
show_init = True
running = True
while running:
    if show_init:
        close = draw_init()
        if close:
            break
        show_init = False
        all_sprites = pygame.sprite.Group()
        rocks = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powers = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(20):
            new_rock()
        score = 0
    
    clock.tick(FPS)#1秒更新幾次畫面 ex. clock.tick(10) #1秒只能執行10次


    # 取得輸入----------------------------------------------------------------------------
    for event in pygame.event.get():#會回傳所有事件，會回傳列表
        if event.type == pygame.QUIT:  #點到關閉
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
                player.shoot()


    # 更新遊戲---------------------------------------------------------------------------

    all_sprites.update()#就會執行all_sprites裡每個物件的update()函式
    
    #如果兩個撞擊的話，True是刪掉
    hits = pygame.sprite.groupcollide(rocks, bullets,True,True)
    for hit in hits:#撞到幾顆補給顆
        random.choice(exls_sounds).play()
        score += hit.radius
        expl =Explosion(hit.rect.center, 'big')
        all_sprites.add(expl)
        if random.random() > 0.95: # 0到1
            pow =Power(hit.rect.center)
            all_sprites.add(pow)
            powers.add(pow)
        new_rock()

    #撞到，石頭要不要刪掉
    hits_2 = pygame.sprite.spritecollide(player, rocks, True, pygame.sprite.collide_circle)#圖片圓框，原矩形
    for hit in hits_2:
        new_rock()
        player.health -= hit.radius
        expl =Explosion(hit.rect.center, 'little')
        all_sprites.add(expl)
        if player.health <= 0:
            die = Explosion(player.rect.center, 'player')
            all_sprites.add(die)
            die_sound.play()
            player.life -= 1
            player.health = 100
            player.hide()

    # 判斷寶物，飛機相撞
    hits_3 = pygame.sprite.spritecollide(player, powers, True)
    for hit in hits_3:
        if hit.type == 'shield':
            player.health += 20
            if player.health > 100:
                player.health = 100
            shield_sound.play()
        elif hit.type == 'gun':
            player.guns()
            gun_sound.play()
    
    if player.life == 0 and not(die.alive()): #alive存在
        show_init = True
    # 畫面顯示---------------------------------------------------------------------------
    
    screen.fill(BLACK) #畫面底顏色
    screen.blit(background_img, (0,0)  )
    all_sprites.draw(screen)# 把 all_sprite全部的東西都畫出來，畫到screen上
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    draw_health(screen, player.health, 5, 15) 
    draw_life(screen, player.life, player_mini_img, WIDTH - 100, 15)
    pygame.display.update() #更新畫面


pygame.quit()