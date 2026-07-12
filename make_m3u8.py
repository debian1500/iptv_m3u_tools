#!/usr/bin/python3

print("M3U8 IPTV Playlist Editor")


playlist_name = input("Введите имя плейлиста (можно создать новый): ")
stream_link = input("Введите ссылку на поток: ")
stream_name = input("Введите имя канала/потока: ")
stream_icon = input("Введите ссылку на иконку: ")


# Для всех четырёх переменных:
# Добавить проверку пустого ввода
# Добавить проверку наличия в файле


# Проверяем наличие расширения, если нету - сами добавляем
if not playlist_name.endswith('.m3u8'):
    playlist_name += '.m3u8'

# Строка для добавления
entry = f'#EXTINF:-1 tvg-name="{stream_name}" tvg-logo="{stream_icon}" tvg-country="RU" group-title="Russia",{stream_name}\n{stream_link}\n'


with open (playlist_name, 'a', encoding='utf-8') as f:
   f.write(entry)	
print("Канал добавлен")
