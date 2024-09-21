from time import sleep
class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, username, password):
        self.current_user = None
        for i in self.users:
            if username in i.username:
                if hash(password) == i.password:
                    self.current_user = i
                    print(f'Вы успешно зашли, {username}!')
                    return
                else:
                    print('Неправильный пароль')
                    return
        print('Такой пользователь не найден')

    def register(self, username, password, age):
        if len(self.users) != 0:
            for i in self.users:
                if username == i.username:
                    print(f'Пользователь {username} уже существует')
                    return
        self.users.append(User(username, password, age))
        self.current_user = User(username, password, age)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if len(self.users) != 0:
                for i in self.users:
                    if i.title == video:
                        print('Такое видео есть!')
                        return
            self.videos.append(video)

    def get_videos(self, excerpt):
        s = []
        for i in self.videos:
            if excerpt.lower() in i.title.lower():
                s.append(i.title)
        return s

    def watch_video(self, video):
        if self.current_user is not None:
            for i in self.videos:
                if i.title == video:
                    if i.adult_mode:
                        if self.current_user.age >= 18:
                            for j in range(1, i.duration+1):
                                print(j, end=' ')
                                sleep(1)
                            print('Конец видео!')
                        else:
                            print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        s = ''
                        for j in range(0, i.duration):
                            s += str(i)+' '
                        print(s, 'Конец видео')




        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.username

    def __hash__(self):
        return hash(self.password)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)