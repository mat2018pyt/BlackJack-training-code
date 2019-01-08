from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 60)

wall_image = games.load_image("sciana.jpg", transparent = False)
games.screen.background = wall_image

pizza_image = games.load_image("pizza.bmp")
pizza = games.Sprite(image = pizza_image, x = 320, y = 240)


score = games.Text(value = 1756524,
                   size = 60,
                   color = color.black,
                   x = 550,
                   y = 30)


won_message = games.Message(value = "Message!",
                            size = 100,
                            color = color.red,
                            x = games.screen.width/2,
                            y = games.screen.height/2,
                            lifetime = 250,
                            after_death = games.screen.quit
                            )

games.screen.add(won_message)


games.screen.mainloop()

