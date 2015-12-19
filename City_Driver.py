import pygame
import sys
import pickle
from pygame.locals import*

#colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
green2 = (0, 153, 0)
green3 = (0,100,0)
gray = (158, 156, 166)
gray2 = (69, 67, 68)

#pictures
cover_img = pygame.image.load("cover.jpg")
logo_img = pygame.image.load("logo.jpg")
#beetle
beetle_up_img = pygame.image.load('beetle_up.png')
beetle_down_img = pygame.image.load('beetle_down.png')
beetle_left_img = pygame.image.load('beetle_left.png')
beetle_right_img = pygame.image.load('beetle_right.png')
#buildings
building1_img = pygame.image.load('building1.jpg')
building2_img = pygame.image.load('building2.jpg')
building3_img = pygame.image.load('building3.jpg')
car_shop_img = pygame.image.load('car_shop.jpg')
fuel_shop_img = pygame.image.load('fuel_store.jpg')
car_fix_shop_img = pygame.image.load('car_fix_shop.jpg')
police_station_img = pygame.image.load('police_station.jpg')
#houses
house1_img = pygame.image.load('house1.jpg')

#needed setup
rendermode = 0
lastbutton = 'up'
car = 'beetle'
speed = 0
money = 1000
fuel = 20
damage = 0
police = 0
police_time = 60
timer = 0
house_info = 0
#building
#building1
building1y = 500
building1x = 1000
#building2
building2y = 1820
building2x = 1000
#building3
building3y = 1131
building3x = 1610
#car shop
car_shop1y = 31
car_shop1x = 1000
#fuel shop
fuel_shop1y = 620
fuel_shop1x = -10
#police station
police_station1y = 969
police_station1x = 1000
#car fix shop
car_fix_shop_1y = -69
car_fix_shop_1x = -10
#roads
#road 1
road1y = 0
road1x = 780
#road 2
road2y = 400
road2x = 0
#road 3
road3y = 1600
road3x = 790

pygame.init()
screen = pygame.display.set_mode((1800, 1000), pygame.RESIZABLE)

#fonts
menu_font = pygame.font.SysFont('Calibri', 40)
hud_font = pygame.font.SysFont('Calibri', 40)
hud_font2 = pygame.font.SysFont('Calibri', 20)

#after init setup
pygame.display.set_icon(cover_img)
pygame.display.set_caption('City Driver (v.d.b.e.1.3)')

screen.fill(white)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)
            
    #needed setup
    mx, my = pygame.mouse.get_pos()
    if lastbutton == 'up':
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                lastbutton = 'up'
            if speed == 0 or speed < 0:
                if event.key == pygame.K_DOWN:
                    lastbutton = 'down'
            if event.key == pygame.K_LEFT:
                lastbutton = 'left'
            if event.key == pygame.K_RIGHT:
                lastbutton = 'right'

    if lastbutton == 'down':
        if event.type == pygame.KEYDOWN:
            if speed == 0 or speed < 0:
                if event.key == pygame.K_UP:
                    lastbutton = 'up'
            if event.key == pygame.K_DOWN:
                    lastbutton = 'down'
            if event.key == pygame.K_LEFT:
                lastbutton = 'left'
            if event.key == pygame.K_RIGHT:
                lastbutton = 'right'

    if lastbutton == 'left':
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                lastbutton = 'up'
            if event.key == pygame.K_DOWN:
                    lastbutton = 'down'
            if event.key == pygame.K_LEFT:
                lastbutton = 'left'
            if speed == 0 or speed < 0:
                if event.key == pygame.K_RIGHT:
                    lastbutton = 'right'

    if lastbutton == 'right':
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                lastbutton = 'up'
            if event.key == pygame.K_DOWN:
                    lastbutton = 'down'
            if speed == 0 or speed < 0:
                if event.key == pygame.K_LEFT:
                    lastbutton = 'left'
            if event.key == pygame.K_RIGHT:
                lastbutton = 'right'
                
    if rendermode == 0:
        screen.fill(white)
        screen.blit(logo_img,(220, 0))
        pygame.draw.rect(screen, black, [0, 0 , 220, 1000])
        #play
        pygame.draw.rect(screen, gray, [10, 10, 200, 40])
        play_text = menu_font.render('PLAY', True, black)
        #load
        pygame.draw.rect(screen, gray, [10, 70, 200, 40])
        load_text = menu_font.render('LOAD', True, black)
        #blit
        screen.blit(play_text,(10, 10))
        screen.blit(load_text,(10, 70))
        #clicked?
        #play
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if my > 10 and my < 50:
                    if mx > 10 and mx < 210:
                        rendermode = 1
        #load
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if my > 70 and my < 110:
                    if mx > 10 and mx < 210:
                        rendermode = 6

    if rendermode == 1:
        screen.fill(green)
        
        if lastbutton == 'up':
            if speed < 20:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if car == 'beetle':
                            speed = (speed + 1) #/ damage
                            pygame.time.wait(50)

            if speed > 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if car == 'beetle':
                            speed = speed - 1
                            pygame.time.wait(20)

            if speed > 0:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        if car == 'beetle':
                            speed = speed - 1
                            pygame.time.wait(45)
            if speed > 0:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        if car == 'beetle':
                            speed = speed - 1
                            pygame.time.wait(45)

        if lastbutton == 'down':
            if speed < 20:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if car == 'beetle':
                            speed = (speed + 1) #/ damage
                            pygame.time.wait(50)

            if speed > 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if car == 'beetle':
                            speed = speed - 1
                            pygame.time.wait(20)

            if speed > 0:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        if car == 'beetle':
                            speed = speed - 1
                            pygame.time.wait(45)
            if speed > 0:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        if car == 'beetle':
                            speed = speed - 1
                            pygame.time.wait(45)

        if lastbutton == 'left':
            if speed < 20:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if car == 'beetle':
                            speed = (speed + 1) #/ damage
                            pygame.time.wait(50)

            if speed > 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if car == 'beetle':
                            speed = speed - 1
                            pygame.time.wait(20)

            if speed > 0:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        if car == 'beetle':
                            speed = speed - 1
                            pygame.time.wait(45)
            if speed > 0:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        if car == 'beetle':
                            speed = speed - 1
                            pygame.time.wait(45)

        if lastbutton == 'right':
            if speed < 20:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if car == 'beetle':
                            speed = (speed + 1) #/ damage
                            pygame.time.wait(50)

            if speed > 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if car == 'beetle':
                            speed = speed - 1
                            pygame.time.wait(20)

            if speed > 0:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        if car == 'beetle':
                            speed = speed - 1
                            pygame.time.wait(45)
            if speed > 0:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        if car == 'beetle':
                            speed = speed - 1
                            pygame.time.wait(45)

        #roads
        pygame.draw.rect(screen, black, [road1x, road1y , 220, 2000])
        pygame.draw.rect(screen, black, [road2x, road2y , 780, 220])
        pygame.draw.rect(screen, black, [road3x, road3y , 2000, 220])
        
        #buildings
        screen.blit(building1_img,(building1x, building1y))
        screen.blit(building2_img,(building2x, building2y))
        screen.blit(building3_img,(building3x, building3y))
        screen.blit(car_shop_img,(car_shop1x, car_shop1y))
        screen.blit(fuel_shop_img,(fuel_shop1x, fuel_shop1y))
        screen.blit(car_fix_shop_img,(car_fix_shop_1x, car_fix_shop_1y))
        screen.blit(police_station_img,(police_station1x, police_station1y))
        
        #road/building eng.
        if lastbutton == 'up':
            road1y = road1y + speed
            road2y = road2y + speed
            road3y = road3y + speed
            building1y = building1y + speed
            building2y = building2y + speed
            building3y = building3y + speed
            car_shop1y = car_shop1y + speed
            fuel_shop1y = fuel_shop1y + speed
            car_fix_shop_1y = car_fix_shop_1y + speed
            police_station1y = police_station1y + speed
            
        if lastbutton == 'down':
            road1y = road1y - speed
            road2y = road2y - speed
            road3y = road3y - speed
            building1y = building1y - speed
            building2y = building2y - speed
            building3y = building3y - speed
            car_shop1y = car_shop1y - speed
            fuel_shop1y = fuel_shop1y - speed
            car_fix_shop_1y = car_fix_shop_1y - speed
            police_station1y = police_station1y - speed
            
        if lastbutton == 'left':
            road1x = road1x + speed
            road2x = road2x + speed
            road3x = road3x + speed
            building1x = building1x + speed
            building2x = building2x + speed
            building3x = building3x + speed
            car_shop1x = car_shop1x + speed
            fuel_shop1x = fuel_shop1x + speed
            car_fix_shop_1x = car_fix_shop_1x + speed
            police_station1x = police_station1x + speed
            
        if lastbutton == 'right':
            road1x = road1x - speed
            road2x = road2x - speed
            road3x = road3x - speed
            building1x = building1x - speed
            building2x = building2x - speed
            building3x = building3x - speed
            car_shop1x = car_shop1x - speed
            fuel_shop1x = fuel_shop1x - speed
            car_fix_shop_1x = car_fix_shop_1x - speed
            police_station1x = police_station1x - speed
            
        #car
        if car == 'beetle':
            if lastbutton == 'up':
                screen.blit(beetle_up_img,(900, 500))
            if lastbutton == 'down':
                screen.blit(beetle_down_img,(900, 500))
            if lastbutton == 'left':
                screen.blit(beetle_left_img,(900, 500))
            if lastbutton == 'right':
                screen.blit(beetle_right_img,(900, 500))

        #hud
        pygame.draw.rect(screen, gray, [0, 900, 1800, 200])
        hud_speed_text = hud_font.render('speed:' +str (speed), True, black)
        hud_money_text = hud_font2.render('money: $' +str (money), True, black)
        hud_fuel_text = hud_font2.render('fuel(g):' +str (fuel), True, black)
        hud_damage_text = hud_font2.render('damage:' +str (damage), True, black)
        hud_police_text = hud_font2.render('police:' +str (police), True, black)
        #hud blit
        screen.blit(hud_speed_text,(800, 950))
        screen.blit(hud_money_text,(970, 960))
        screen.blit(hud_fuel_text,(690, 960))
        screen.blit(hud_damage_text,(1100, 960))
        screen.blit(hud_police_text,(560, 960))

        #fee
        if police > 0:
            pygame.draw.rect(screen, gray, [1400, 100, 400, 30])
            police_time_text = hud_font2.render('your tickets must be paid in ' +str (police_time) +str (' min'), True, black)
            #blit
            screen.blit(police_time_text,(1400, 110))

        #crash eng.
        if building1y > 31 and building1y < 500:
            if building1x > 300 and building1x < 900:
                money = money - 10
                if damage < 100:
                    damage = damage + 1
                if police < 100:
                    police = police + 1

        if building2y > 31 and building2y < 500:
            if building2x > 300 and building2x < 900:
                enter_house_shop_text = hud_font.render('press "space" to enter house shop', True, white)
                #blit
                screen.blit(enter_house_shop_text,(0, 860))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        rendermode = 3

        if building3y > 31 and building3y < 500:
            if building3x > 300 and building3x < 900:
                money = money - 10
                if damage < 100:
                    damage = damage + 1
                if police < 100:
                    police = police + 1

        if car_shop1y > 31 and car_shop1y < 500:
            if car_shop1x > 300 and car_shop1x < 900:
                enter_car_shop_text = hud_font.render('press "space" to enter car shop', True, white)
                #blit
                screen.blit(enter_car_shop_text,(0, 860))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        rendermode = 2

        if fuel_shop1y > 31 and fuel_shop1y < 500:
            if fuel_shop1x > 300 and fuel_shop1x < 900:
                fuel_calc = (20 - fuel) * 2
                enter_car_shop_text = hud_font.render('press "space" to refuel, this will cost: $' +str (fuel_calc), True, white)
                #blit
                screen.blit(enter_car_shop_text,(0, 860))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if money > fuel_calc:
                            fuel = 20
                            money = money - fuel_calc
                        else:
                            not_enough_money_text = hud_font.render('not enough money ', True, red)
                            screen.blit(not_enough_money_text,(0, 700))

        if car_fix_shop_1y > 31 and car_fix_shop_1y < 500:
            if car_fix_shop_1x > 300 and car_fix_shop_1x < 900:
                damage_calc = (damage * 2) * 2
                enter_car_shop_text = hud_font.render('press "space" to fix car, this will cost: $' +str (damage_calc), True, white)
                #blit
                screen.blit(enter_car_shop_text,(0, 860))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if money > damage_calc:
                            damage = 0
                            money = money - damage_calc
                        else:
                            not_enough_money_text = hud_font.render('not enough money ', True, red)
                            screen.blit(not_enough_money_text,(0, 700))

        if police_station1y > 31 and police_station1y < 500:
            if police_station1x > 300 and police_station1x < 900:
                police_calc = (police * 2) * 2
                enter_police_station_text = hud_font.render('press "space" to pay tickets , this will cost: $' +str (police_calc), True, white)
                #blit
                screen.blit(enter_police_station_text,(0, 860))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if money > police_calc:
                            police = 0
                            money = money - police_calc
                        else:
                            not_enough_money_text = hud_font.render('not enough money ', True, red)
                            screen.blit(not_enough_money_text,(0, 700))


    if rendermode == 1:
        timer = timer + 1
        if timer == 500:
            timer = 0
            fuel = fuel - 1
            money = money + 10
            if police > 0:
                police_time = police_time - 1

        if police_time == 0:
            if money == 1000 or money > 1000:
                police = 0
                money = money - 1000
            else:
                rendermode = 0

        if fuel == 0:
            if money > 500:
                money = money - 500
                fuel = 20
            else:
                rendermode = 0

        if damage == 100:
            if money > 1000:
                money = money - 1000
                damage = 0
            else:
                rendermode = 0

        if police == 100:
            if money > 1500:
                money = money - 1500
                damage = 0
            else:
                rendermode = 0

        #pause
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                rendermode = 4

    if rendermode == 2:
        #setup
        speed = 0
        #gui
        screen.fill(gray)
        back_shop_text = menu_font.render('BACK', True, black)
        not_avalable_shop_text = menu_font.render('not avalable yet', True, black)
        #blit
        screen.blit(back_shop_text,(10, 10))
        screen.blit(not_avalable_shop_text,(100, 100))
        pygame.draw.rect(screen, black, [0, 50, 500, 10])
        pygame.draw.rect(screen, black, [500, 0, 10, 1000])
        pygame.draw.rect(screen, black, [500, 400, 1300, 10])
        #clicked?
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if my > 10 and my < 50:
                    if mx > 10 and mx < 210:
                        rendermode = 1

    if rendermode == 3:
        #setup
        speed = 0
        #gui
        screen.fill(gray)
        back_shop_text = menu_font.render('BACK', True, black)
        house_1_text = menu_font.render('basic home', True, black)
        #blit
        pygame.draw.rect(screen, gray2, [90, 90, 200, 50])
        screen.blit(back_shop_text,(10, 10))
        screen.blit(house_1_text,(100, 100))        
        pygame.draw.rect(screen, black, [0, 50, 500, 10])
        pygame.draw.rect(screen, black, [500, 0, 10, 1000])
        pygame.draw.rect(screen, black, [500, 400, 1300, 10])
        #clicked?
        #back
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if my > 10 and my < 50:
                    if mx > 10 and mx < 210:
                        rendermode = 1
        #basic house
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if my > 90 and my < 140:
                    if mx > 90 and mx < 290:
                        house_info = 1
        #house info
        if house_info == 1:
            price_text = menu_font.render('Price = $1500', True, black)
            damage_recover_text = menu_font.render('damage recvovery = 10', True, black)
            house_recover_text = menu_font.render('house recvovery = 60 sec.', True, black)
            buy_text = menu_font.render('BUY', True, black)
            pygame.draw.rect(screen, gray2, [520, 650, 90, 50])
            screen.blit(price_text,(520, 420))    
            screen.blit(damage_recover_text,(520, 500))              
            screen.blit(house_recover_text,(520, 580))
            screen.blit(buy_text,(530, 660))
            #buy click
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if my > 650 and my < 700:
                        if mx > 520 and mx < 610:
                            if money == 1500 or money > 1500:
                                building2_img = house1_img
                                money = money - 1500
                                rendermode = 1
                            else:
                                not_enough_money_text = hud_font.render('not enough money ', True, red)
                                screen.blit(not_enough_money_text,(530, 780))

    if rendermode == 4:
        screen.fill(gray)
        #unpause
        unpause_text = menu_font.render('unpause', True, black)
        pygame.draw.rect(screen, gray2, [700, 200, 400, 60])
        #home screen
        home_text = menu_font.render('home screen', True, black)
        pygame.draw.rect(screen, gray2, [700, 280, 400, 60])
        #save
        save_text = menu_font.render('save', True, black)
        pygame.draw.rect(screen, gray2, [700, 360, 400, 60])
        #blit
        screen.blit(unpause_text,(830, 210))
        screen.blit(home_text,(800, 290))
        screen.blit(save_text,(860, 370)) 
        #clicked?
        #unpause
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if my > 200 and my < 260:
                    if mx > 700 and mx < 1200:
                        rendermode = 1
        #home screen
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if my > 280 and my < 340:
                    if mx > 700 and mx < 1200:
                        rendermode = 0
        #save
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if my > 360 and my < 420:
                    if mx > 700 and mx < 1200:
                        rendermode = 5

    if rendermode == 5:
        saving = 'buildings'
        saving_text = menu_font.render('saving: ' +str (saving), True, black)
        screen.blit(saving_text,(900, 10))
        #buildings
        #building1
        #x
        pickle_out = open('building1x.pickle', 'w')
        pickle.dump(building1x, pickle_out)
        pickle_out.close()
        #y
        pickle_out = open('building1y.pickle', 'w')
        pickle.dump(building1y, pickle_out)
        pickle_out.close()
        #building2
        #x
        pickle_out = open('building2x.pickle', 'w')
        pickle.dump(building2x, pickle_out)
        pickle_out.close()
        #y
        pickle_out = open('building2y.pickle', 'w')
        pickle.dump(building2y, pickle_out)
        pickle_out.close()
        #building3
        #x
        pickle_out = open('building3x.pickle', 'w')
        pickle.dump(building3x, pickle_out)
        pickle_out.close()
        #y
        pickle_out = open('building3y.pickle', 'w')
        pickle.dump(building3y, pickle_out)
        pickle_out.close()
        #car shop
        #x
        pickle_out = open('car_shop1x.pickle', 'w')
        pickle.dump(car_shop1x, pickle_out)
        pickle_out.close()
        #y
        pickle_out = open('car_shop1y.pickle', 'w')
        pickle.dump(car_shop1y, pickle_out)
        pickle_out.close()
        #fuel shop
        #x
        pickle_out = open('fuel_shop1x.pickle', 'w')
        pickle.dump(fuel_shop1x, pickle_out)
        pickle_out.close()
        #y
        pickle_out = open('fuel_shop1y.pickle', 'w')
        pickle.dump(fuel_shop1y, pickle_out)
        pickle_out.close()
        #police station
        #x
        pickle_out = open('police_station1x.pickle', 'w')
        pickle.dump(police_station1x, pickle_out)
        pickle_out.close()
        #y
        pickle_out = open('police_station1y.pickle', 'w')
        pickle.dump(police_station1y, pickle_out)
        pickle_out.close()
        #car fix shop
        #x
        pickle_out = open('car_fix_shop_1x.pickle', 'w')
        pickle.dump(car_fix_shop_1x, pickle_out)
        pickle_out.close()
        #y
        pickle_out = open('car_fix_shop_1y.pickle', 'w')
        pickle.dump(car_fix_shop_1y, pickle_out)
        pickle_out.close()
        #roads
        saving = 'roads'
        #road1
        #x
        pickle_out = open('road1x.pickle', 'w')
        pickle.dump(road1x, pickle_out)
        pickle_out.close()
        #y
        pickle_out = open('road1y.pickle', 'w')
        pickle.dump(road1y, pickle_out)
        pickle_out.close()
        #road2
        #x
        pickle_out = open('road2x.pickle', 'w')
        pickle.dump(road2x, pickle_out)
        pickle_out.close()
        #y
        pickle_out = open('road2y.pickle', 'w')
        pickle.dump(road2y, pickle_out)
        pickle_out.close()
        #road1
        #x
        pickle_out = open('road3x.pickle', 'w')
        pickle.dump(road3x, pickle_out)
        pickle_out.close()
        #y
        pickle_out = open('road3y.pickle', 'w')
        pickle.dump(road3y, pickle_out)
        pickle_out.close()
        #others
        saving = 'others'
        #money
        pickle_out = open('money.pickle', 'w')
        pickle.dump(money, pickle_out)
        pickle_out.close()
        #police
        pickle_out = open('police.pickle', 'w')
        pickle.dump(police, pickle_out)
        pickle_out.close()
        #police timer
        pickle_out = open('police_timer.pickle', 'w')
        pickle.dump(police_time, pickle_out)
        pickle_out.close()
        #damage
        pickle_out = open('damage.pickle', 'w')
        pickle.dump(damage, pickle_out)
        pickle_out.close()
        #fuel
        pickle_out = open('fuel.pickle', 'w')
        pickle.dump(fuel, pickle_out)
        pickle_out.close()
        #timer
        pickle_out = open('timer.pickle', 'w')
        pickle.dump(timer, pickle_out)
        pickle_out.close()
        #done
        rendermode = 1

    if rendermode == 6:
        #building1
        #x
        pickle_in = open('building1x.pickle', 'r')
        building1x = pickle.load(pickle_in)
        #y
        pickle_in = open('building1y.pickle', 'r')
        building1y = pickle.load(pickle_in)
        #building2
        #x
        pickle_in = open('building2x.pickle', 'r')
        building2x = pickle.load(pickle_in)
        #y
        pickle_in = open('building2y.pickle', 'r')
        building2y = pickle.load(pickle_in)
        #building3
        #x
        pickle_in = open('building3x.pickle', 'r')
        building3x = pickle.load(pickle_in)
        #y
        pickle_in = open('building3y.pickle', 'r')
        building3y = pickle.load(pickle_in)
        #car shop
        #x
        pickle_in = open('car_shop1x.pickle', 'r')
        car_shop1x = pickle.load(pickle_in)
        #y
        pickle_in = open('car_shop1y.pickle', 'r')
        car_shop1y = pickle.load(pickle_in)
        #fuel shop
        #x
        pickle_in = open('fuel_shop1x.pickle', 'r')
        fuel_shop1x = pickle.load(pickle_in)
        #y
        pickle_in = open('fuel_shop1y.pickle', 'r')
        fuel_shop1y = pickle.load(pickle_in)
        #police station
        #x
        pickle_in = open('police_station1x.pickle', 'r')
        police_station1x = pickle.load(pickle_in)
        #y
        pickle_in = open('police_station1y.pickle', 'r')
        police_station1y = pickle.load(pickle_in)
        #car fix shop
        #x
        pickle_in = open('car_fix_shop_1x.pickle', 'r')
        car_fix_shop_1x = pickle.load(pickle_in)
        #y
        pickle_in = open('car_fix_shop_1y.pickle', 'r')
        car_fix_shop_1y = pickle.load(pickle_in)
        #roads
        #road1
        #x
        pickle_in = open('road1x.pickle', 'r')
        road1x = pickle.load(pickle_in)
        #y
        pickle_in = open('road1y.pickle', 'r')
        road1y = pickle.load(pickle_in)
        #road2
        #x
        pickle_in = open('road2x.pickle', 'r')
        road2x = pickle.load(pickle_in)
        #y
        pickle_in = open('road2y.pickle', 'r')
        road2y = pickle.load(pickle_in)
        #road3
        #x
        pickle_in = open('road3x.pickle', 'r')
        road3x = pickle.load(pickle_in)
        #y
        pickle_in = open('road3y.pickle', 'r')
        road3y = pickle.load(pickle_in)
        #other
        #money
        pickle_in = open('money.pickle', 'r')
        money = pickle.load(pickle_in)
        #police
        pickle_in = open('police.pickle', 'r')
        police = pickle.load(pickle_in)
        #police timer
        pickle_in = open('police_timer.pickle', 'r')
        police_time = pickle.load(pickle_in)
        #damage
        pickle_in = open('damage.pickle', 'r')
        damage = pickle.load(pickle_in)
        #fuel
        pickle_in = open('fuel.pickle', 'r')
        fuel = pickle.load(pickle_in)
        #timer
        pickle_in = open('timer.pickle', 'r')
        timer = pickle.load(pickle_in) 
        #done
        rendermode = 1
        
    #updater
    pygame.display.update()
