#!/usr/bin/python3

print("M3U/M3U8 IPTV Playlist Editor")

stream_link = input("Введите ссылку на поток: ")
stream_name = input("Введите имя канала/потока: ")
stream_icon = input("Введите ссылку на иконку: ")
playlist_name = input("Введите имя плейлиста (должен лежать в одной папке со скриптом: ")


with open (playlist_name, 'a', encoding='utf-8') as playlist_file:
	print("Here's a playlist: ", playlist_file)
	
