from trollop import TrelloConnection

# conn = TrelloConnection(<your developer key>, <user's oauth token>)
conn = TrelloConnection('3d282ee48a4cb6018f7b4b1e15ca7cf9', '01812b439967658daad4b79fa5dbdd33039a38401ec1e6956d68c9c3f6ec7d46')

print(conn.me.username)

print(conn.get_board('54819d8633dffb95de497060'))


#all_boards=conn.get_board('54819d8633dffb95de497060')

board = conn.get_board('54819d8633dffb95de497060')

print(board.name)


cards=board.cards.__sizeof__()

print(cards)

conn.me.get






