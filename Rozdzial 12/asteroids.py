from livewires import games


games.init(screen_width = 640, screen_height = 480, fps = 50)
"""
class Ship(games.Sprite):

    def update(self):

        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle +=1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -=1

        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270

        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1
        if games.keyboard.is_pressed(games.K_s):
            self.y += 1
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 1
        if games.keyboard.is_pressed(games.K_d):
            self.x += 1
"""

def main():

    missile_sound = games.load_sound("pocisk.wav")
    games.music.load("temat.mid")

    choice = None
    while choice != "0":

        print(
        """
        Dzwiek i muzyka

        0 - zakoncz
        1 - odwtworz dwiek pocisku
        2 - odtwarzaj cyklicznie dzwiek pocisku
        3 - zatrzymaj odtwarzanie dzwieku pociesku
        4 - odtworz temat muzyczny
        5 - odtwarzaj cyjkuczbue tenat muzyczny
        6 - zatrzymaj odtwarzanie tematu muzycznego
        """
        )

        choice = input("Wybierz: ")
        print()

        if choice == "0":
            print("Zegnaj")
        elif choice == "1":
            missile_sound.play()
            print("Odtworzenie dzwieku pocisku")
        elif choice == "2":
            loop = int(input("Ile razy powtorzyc odtwarzani? -1 jesli bez konca. : "))
            missile_sound.play(loop)
            print("Cykliczne odtwarzanie dzwieku pocisku")
        elif choice == "3":
            missile_sound.stop()
            print("Zatrzymanie odtwarzania dzwieku pocisku")
        elif choice == "4":
            games.music.play()
            print("Odtworzenie tematu muzycznego")
        elif choice == "5":
            loop = int(input("Ile razy odtworzyc muzyke? -1 znaczy bez konca: "))
            games.music.play(loop)
            print("Cykliczne odtwarzanie muzyki")
        elif choice == "6":
            games.music.stop()
            print("Zatrzymanie odtwarzania muzyki")
        else:
            print("\nNiestety, ", choice ," nie jest prawidlowym wyborem")

        input("\nAby zakonczyc nacisniej ENTER.")
        
"""    
    nebula_image = games.load_image("mglawica.jpg", transparent = 0)
    games.screen.background = nebula_image
"""
"""
    ship_image = games.load_image("statek.bmp")
    the_ship = Ship(image = ship_image,
                    x = games.screen.width/2,
                    y = games.screen.height/2)
    games.screen.add(the_ship)


    explosion_files = ["eksplozja1.bmp",
                       "eksplozja2.bmp",
                       "eksplozja3.bmp",
                       "eksplozja4.bmp",
                       "eksplozja5.bmp",
                       "eksplozja6.bmp",
                       "eksplozja7.bmp",
                       "eksplozja8.bmp",
                       "eksplozja9.bmp"]

    explosion = games.Animation(images = explosion_files,
                                x = games.screen.width/2,
                                y = games.screen.height/2,
                                n_repeats = 0,
                                repeat_interval = 5)
    games.screen.add(explosion)
"""
"""
    games.screen.mainloop()
"""

                   

main()
    
