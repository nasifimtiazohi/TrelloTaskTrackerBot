from trello import TrelloClient
trelloToken = 'fafbd8bea1ca07b19f8656b62174b81d7dbed73bdddaf318b61192bce9931ab3'
trelloKey = 'cda12dfc52f6530a3eb17745f1b4e61b'
trelloSecret = '96d037afb64bfb3306bd031bd403b1eeca1836186e0c09109b1a03ad5aec1c11'
list_id = '59d1e50224150f7b3db99037'

client = TrelloClient(
    api_key = trelloKey,
    api_secret=trelloSecret,
    token=trelloToken,
    token_secret=None
)

all_boards = client.list_boards()
last_board = all_boards[-1]
for board in all_boards:
    print board.name

last_board.list_lists()
my_list = last_board.get_list(list_id)
for card in my_list.list_cards():
    print(card.name)