from sshtunnel import SSHTunnelForwarder
with SSHTunnelForwarder(("10.25.0.251", 22),                # Через какого посредника подключаемся
                        ssh_username="root",
                        ssh_password="2t0p0m3PRIM",
                        remote_bind_address=('172.26.12.2', 18500),        # Настоящий адрес куда нам нужно на самом деле
                        local_bind_address=('127.0.0.1', 18509)):          # Так как у нас нет прямого доступа (это потому что маршрутизаторы в сети не настроенны, по причине либо безопасности либо лени)
    # мы тут должны указать на что мы подминяем тот адрес куда нам надо. 127.0.0.1 - это всегд твой ПК, он в большенстве случиев будет такой, так что можно не трогать.
    # а вот 18509 это порт, главное чтоб две программы в сисетме не использовали один и тот же порт! Тоесть нельзя запустить два таких скрипта на одном компьютере
    # чтобы это цифра была одинаковой, в остальном она может быть любой от 1 до 65535, единственное что первые 10000 используются очень часто теме програмами котрые у тебя работают
    # на ПК в фоне, так что лучше выбирать цифрц между 10000 - 65535.
    # Посчле чего ты сможешь подключится на нужный тебе сервер используюя адрес 127.0.0.1:18509, он будет смаршрутизирован на 172.26.12.2:18500 через 10.25.0.251:22
    print("Ok")
    while True:
        i = input()
        if i.lower() == "e":
            break
        else:
            print("press e + enter for exit")